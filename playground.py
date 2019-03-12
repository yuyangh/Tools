def calculate_purchase():
    purchase = {'盛一洲': 10.5,
                '周金程': 14.5,
                '朱昶宇': 13,
                '李杨': 14,
                '黄郁旸': 14,
                '于天易': 17 / 2,
                'Kitty': 17 / 2,
                '张宇伦': 13}
    sum = 0
    tip = 12
    tax = 0.08
    for item in purchase:
        value = purchase[item] * (1 + tax)
        sum += value
        print(str(item), str(value + tip / len(purchase)))
    print(sum + tip)


if __name__ == '__main__':
    calculate_purchase()
