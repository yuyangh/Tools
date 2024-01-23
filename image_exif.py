# python3 -m pip install --upgrade exifread
# python3 -m pip install --upgrade Pillow
# python3 -m pip install --upgrade tqdm
import sys

from PIL import Image
from PIL.ExifTags import TAGS
import exifread
import os
import matplotlib
import matplotlib.pyplot as plt
from collections import defaultdict
from collections import Counter
import logging
from tqdm import tqdm
import time

matplotlib.use('TkAgg')
logging.basicConfig(level=logging.INFO)

"""
Date: 2024/01/17
Known limitation
File format: Pillow library right now only supports jpg, but not HEIC and RAW file
Lens information: some camera does not provide lens information, e.g. DJI 2s
"""

focal_lengths = []
lens_type_count_map = defaultdict(lambda: 0)
exif_focal_length_tag = ["Focal length", "FocalLength"]


def get_image_focal_length(path):
    try:
        with Image.open(path) as im:
            exif = im.getexif()
            exif_data = exif.get_ifd(0x8769)
            for tag_id in exif_data:
                tag = TAGS.get(tag_id, tag_id)
                content = exif_data.get(tag_id)
                logging.debug(f'{tag:25}: {content}')
                if tag in exif_focal_length_tag:
                    focal_lengths.append(int(content))
                    return content
    except (AttributeError, KeyError, ValueError, OSError) as e:
        logging.debug(f"Error extracting focal length: {e}")
        return None


def get_image_lens_information(path):
    try:
        with open(path, 'rb') as im:
            tags = exifread.process_file(im)
            lens = tags['EXIF LensModel']
            lens_type_count_map[str(lens)] += 1
            logging.debug('lens', lens)
            return lens
    except (AttributeError, KeyError, ValueError, OSError) as e:
        logging.debug(f"Error extracting lens model: {e}")
        return None


def get_absolute_file_paths(directory):
    """
    Gets a list of absolute file paths for all files under a given directory,
    including files within subfolders.

    Args:
        directory (str): The root directory to start searching from.

    Returns:
        list: A list of absolute file paths as strings.
    """

    file_paths = []
    # Walk through the directory and its subdirectories using os.walk
    for root, _, files in os.walk(directory):
        for filename in files:
            # Construct the full absolute path
            file_path = os.path.join(root, filename)
            file_paths.append(file_path)

    return file_paths


def print_map_as_table(data: dict):
    table = "\n".join([f"{item}: {count}" for item, count in data.items()])

    # Print the table
    print(table)


def main():
    arguments = sys.argv[1:]
    if len(arguments) < 1:
        logging.warning("command line argument is empty, please enter the root directory")
        return
    root_dir = arguments[1]

    print("starting statistics for directory: ", root_dir)
    all_files = get_absolute_file_paths(root_dir)

    for file_path in tqdm(all_files, desc="Processing", unit="item"):
        logging.debug(file_path)
        try:
            get_image_focal_length(file_path)
            get_image_lens_information(file_path)
        except:
            print()

    with open("image_exif_result.txt", "a") as f:
        print("Summary for path: ", root_dir, file=f)
        print("------------------------", file=f)
        print(f'{"focal_lengths":25}: {dict(Counter(focal_lengths))}', file=f)
        print(f'{"lens_type_count_map":25}: {lens_type_count_map}', file=f)
        print(file=f)

    print()
    print("Summary for path: ", root_dir)
    print("------------------------")
    print(f'{"focal_lengths":25}: {dict(Counter(focal_lengths))}')
    print(f'{"lens_type_count_map":25}: {lens_type_count_map}')
    print()

    binwidth = 5
    plt.hist(focal_lengths, edgecolor="black", bins=range(0, max(focal_lengths) + binwidth, binwidth))
    plt.xlabel('Focal Length (mm)')
    plt.xticks(range(0, max(focal_lengths) + binwidth, binwidth))
    plt.ylabel('Count')
    plt.title('Histogram of Focal Lengths')
    plt.show()

    plt.pie(x=lens_type_count_map.values(), labels=lens_type_count_map.keys())
    # plt.xlabel('Focal Length (mm)')
    # plt.ylabel('Count')
    plt.title('Histogram of Focal Lengths')
    plt.show()


if __name__ == '__main__':
    main()
