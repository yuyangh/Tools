def main():
    n = int(input())
    m = int(input())

    sum_divisible = 0
    sum_not_divisible = 0

    if (m >= n):
        sum_divisible = (1 + m // n) * m // n / 2 * n
    sum_not_divisible = (1 + m) * m / 2 - sum_divisible
    print(abs(sum_not_divisible - sum_divisible))


if __name__ == '__main__':
    main()
