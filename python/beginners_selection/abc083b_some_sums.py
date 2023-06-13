def main():
    N, A, B = tuple(map(int, input().split(" ")))
    total = 0
    for val in [str(i) for i in range(1, N + 1)]:
        total += int(val) if A <= sum([int(digit) for digit in val]) <= B else 0
    print(total)


if __name__ == "__main__":
    main()
