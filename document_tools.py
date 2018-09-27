# -*- coding: utf-8 -*-
import sys


def clearBlankLine(documentHasEmptyLine, newDocumentWithoutEmptyLine):
    '''
    delete all empty lines in a document file 删除文件中所有空行
    :param documentHasEmptyLine: file address
    :param newDocumentWithoutEmptyLine: file address
    :return: none
    '''
    file1 = open(documentHasEmptyLine, 'r', encoding='utf-8')  # 要去掉空行的文件
    file2 = open(newDocumentWithoutEmptyLine, 'w', encoding='utf-8')  # 生成没有空行的文件
    try:
        for line in file1.readlines():
            if line == '\n':
                line = line.strip("\n")
            file2.write(line)
    finally:
        file1.close()
        file2.close()



def is_ustr(in_str, chinese=True, ASCII=True, numbers=True,
            special_characters=True, blanks=True,
            ASCII_punctuation=True, chinese_punctuation=True):
    '''
    keep only characters allowed in the is_uchar() method
    :param in_str: string
    :return: string with only allowed characters
    '''
    out_str = ''
    for i in range(len(in_str)):
        if is_uchar(in_str[i], chinese, ASCII, numbers,
                    special_characters, blanks,
                    ASCII_punctuation, chinese_punctuation):
            out_str = out_str + in_str[i]
        else:
            out_str = out_str + ''
    return out_str


def is_uchar(uchar, chinese=True, ASCII=True, numbers=True,
             special_characters=True, blanks=True,
             ASCII_punctuation=True, chinese_punctuation=True):
    '''
    判断字符是否符合规则
    :param uchar: a character
    :return: passing the rules or not
    '''
    """判断一个unicode是否是汉字"""
    if uchar >= u'\u4e00' and uchar <= u'\u9fa5':
        return chinese
    """判断一个unicode是否是数字"""
    if uchar >= u'\u0030' and uchar <= u'\u0039':
        return numbers
    """判断一个unicode是否是英文字母"""
    if (uchar >= u'\u0041' and uchar <= u'\u005a') or (uchar >= u'\u0061' and uchar <= u'\u007a'):
        return ASCII
    if uchar in ('-', ',', '.', '>', '<', '?'):
        return ASCII_punctuation
    if uchar in ('，', '。', '《', '》'):
        return chinese_punctuation
    '''判断空格 " "   '''
    if uchar == " ":
        return blanks
    if uchar in ('\n', '\t', "\"", "\'"):
        return special_characters
    return False


def delete_empty_line(contents):
    '''
    find adjacent new line characters and delete one of them
    :param contents: file contents
    :return: contents in string
    '''
    str = ""
    count = 0
    for char in contents:
        if char == "\n":
            count += 1
            if count == 2:
                count = 0
                continue
        str += char
    return str


if __name__ == "__main__":
    str = ""

    with open("paris_lyrics.txt", mode="r") as r:
        lines = r.readlines()
        for line in lines:
            str += is_ustr(line, chinese=False, chinese_punctuation=False)

    # with open("temp.txt", mode="r") as r:
    #     lines = r.read()
    #     str = delete_empty_line(lines)

    print(str)

