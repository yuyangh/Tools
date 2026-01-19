#!/bin/bash

# ==============================================================================
# 脚本名称: macOS 屏保图片库优化工具 (AvIF/HEIC -> JPG 替换)
# 
# 功能描述:
#   该脚本用于解决 macOS 锁屏/屏保使用高压缩率图片 (AvIF/HEIC) 时可能出现的
#   "先模糊后变清晰" (延迟加载) 问题。
#   它会自动扫描指定的屏保文件夹，查找非 JPG 格式的图片。
#
# 工作原理 (更新版):
#   1. [预筛选索引] 扫描源照片库，**逐一检查分辨率**，仅将符合 4K 标准的 JPG 
#      写入临时索引文件。
#   2. [扫描屏保] 遍历屏保文件夹中的目标文件。
#   3. [快速匹配] 在纯净的 4K 索引中查找同名文件。
#   4. [执行替换] 找到即替换，无需二次检查。
#
# ==============================================================================

# ================= 配置区域 =================
# 1. 你的屏保文件夹路径 (需要被替换的文件夹)
SCREENSAVER_DIR=''

# 2. 你的源照片库路径 (存放已有 4K JPG 的地方)
SOURCE_LIB_DIR=''

# 3. 是否强制更新已有的 JPG 文件? (true/false)
FORCE_UPDATE_JPG="true"

# 4. 定义 "4K" 的长边像素范围 (单位: px)
#    只有源图片的长边在这个范围内，才会被录入索引并用于替换。
MIN_4K_SIZE=3600
MAX_4K_SIZE=4600
# ===========================================

echo "========================================"
echo "开始优化屏保图片库 (预筛选 4K 索引版)"
echo "扫描目录: $SCREENSAVER_DIR"
echo "源图库:   $SOURCE_LIB_DIR"
echo "4K判定:   长边 ${MIN_4K_SIZE}px - ${MAX_4K_SIZE}px"
echo "========================================"

# 启用 nullglob
shopt -s nullglob

# 创建临时文件
JPG_INDEX_FILE=$(mktemp /tmp/screensaver_4k_index.XXXXXX)
RAW_LIST_FILE=$(mktemp /tmp/screensaver_raw_list.XXXXXX)

# 清理函数
cleanup() {
    rm -f "$JPG_INDEX_FILE" "$RAW_LIST_FILE"
}
trap cleanup EXIT

echo "正在扫描源图库所有 JPG 文件..."
find "$SOURCE_LIB_DIR" -type f -iname "*.jpg" > "$RAW_LIST_FILE"
total_files=$(wc -l < "$RAW_LIST_FILE" | xargs)

echo "找到 $total_files 个 JPG 文件，开始检查分辨率建立 4K 索引..."
echo "注意: 如果源文件在网络驱动器上，这可能需要几分钟。"

count_scanned=0
count_valid_4k=0

# --- 核心改动：在构建索引时筛选分辨率 ---
while IFS= read -r file_path; do
    ((count_scanned++))
    
    # 简单的进度显示 (每处理 50 个文件刷新一次，避免刷屏太快)
    if (( count_scanned % 50 == 0 )); then
        echo -ne "  进度: [$count_scanned / $total_files] 已录入 4K: $count_valid_4k\r"
    fi

    # 检查分辨率
    dims=$(sips -g pixelWidth -g pixelHeight "$file_path" 2>/dev/null)
    # 提取长边
    long_edge=$(echo "$dims" | awk '/pixel/ {if ($2 > max) max = $2} END {print max}')

    # 验证是否为数字且在范围内
    if [[ "$long_edge" =~ ^[0-9]+$ ]]; then
        if (( long_edge >= MIN_4K_SIZE && long_edge <= MAX_4K_SIZE )); then
            echo "$file_path" >> "$JPG_INDEX_FILE"
            ((count_valid_4k++))
        fi
    fi
done < "$RAW_LIST_FILE"

echo -e "\n----------------------------------------"
echo "索引构建完成！有效 4K 图片数: $count_valid_4k"
echo "----------------------------------------"

# 统计计数器
count_processed=0
count_skipped=0

# --- 构建待处理的文件列表 ---
files_to_process=( "$SCREENSAVER_DIR"/*.{heic,HEIC,avif,AVIF,webp,png} )
if [ "$FORCE_UPDATE_JPG" == "true" ]; then
    files_to_process+=( "$SCREENSAVER_DIR"/*.{jpg,JPG} )
fi

# 遍历屏保文件
for file in "${files_to_process[@]}"; do
    [ -e "$file" ] || continue

    filename=$(basename "$file")
    basename="${filename%.*}"
    target_jpg="$SCREENSAVER_DIR/$basename.jpg"

    echo "正在检查: $filename"

    # 在已经筛选好的 4K 索引中查找
    found_src=$(grep -m 1 -i "/${basename}.jpg$" "$JPG_INDEX_FILE")

    if [ -n "$found_src" ]; then
        echo "  [✅ 匹配成功] 找到对应的 4K 源文件: $found_src"
        
        # 执行替换 (无需再检查分辨率，索引里肯定是对的)
        cp "$found_src" "$target_jpg"
        
        if [ $? -eq 0 ]; then
            if [ "$file" != "$target_jpg" ]; then
                echo "  -> 替换成功，删除旧格式原图。"
                rm "$file"
            else
                echo "  -> 强制更新成功。"
            fi
            ((count_processed++))
        else
            echo "  [❌ 错误] 复制失败。"
        fi
        
    else
        echo "  [⚠️ 跳过] 未找到 $filename 同名 4K JPG 源文件。"
        ((count_skipped++))
    fi
    echo "----------------------------------------"
done

echo "任务完成！"
echo "成功替换: $count_processed"
echo "未找到匹配: $count_skipped"
