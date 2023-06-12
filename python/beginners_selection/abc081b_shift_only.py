def is_odd_all(target: list):
    return all([t % 2 == 0 for t in target])


def main():
    _ = int(input())
    s_n = list(map(int, input().split(" ")))
    c = 0
    while is_odd_all(s_n):
        s_n = list(map(lambda x: x / 2, s_n))
        c += 1
    print(c)


if __name__ == "__main__":
    main()
