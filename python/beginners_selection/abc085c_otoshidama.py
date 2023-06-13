def check(N, Y):
    res10000 = -1
    res5000 = -1
    res1000 = -1

    for a in range(N + 1):
        for b in range(N - a + 1):
            c = N - a - b
            total = 10000 * c + 5000 * b + 1000 * a
            if total == Y:
                res10000 = c
                res5000 = b
                res1000 = a
    return f"{res10000} {res5000} {res1000}"


def main():
    N, Y = list(map(int, input().split(" ")))
    print(check(N, Y))


if __name__ == "__main__":
    main()
