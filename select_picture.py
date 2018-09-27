import random

NUM_SELECTED_PICTURE = 100000

# shopfront has 1,557,288 lines of data
with open("/Users/yuyanghuang/Downloads/Data/shopfront_list.txt", mode="r") as file:
    data = file.readlines()
    random.seed(0)
    indices = random.sample(range(0, len(data)), NUM_SELECTED_PICTURE)
    # print(indices)
    with open("/Users/yuyanghuang/Downloads/Data/shopfront_selected_list.txt", mode="w") as shopfront_selected_list:
        shopfront_selected_list.write("Selected index in shopfront file:\n")
        for index in indices:
            shopfront_selected_list.write(str(index) + "\n")
