def is_odd_all(target: list) -> bool:
    return all([t % 2 == 0 for t in target])


def main() -> None:
    _ = int(input())
    s_n = list(map(int, input().split(" ")))
    c = 0
    while is_odd_all(s_n):
        s_n = list(map(lambda x: x / 2, s_n))
        c += 1
    print(c)


if __name__ == "__main__":
    main()
