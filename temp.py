num = 0


def cal():
    global num
    print(num)
    num += 1
    print(num)


def main():
    cal()


if __name__ == "__main__":
    main()
