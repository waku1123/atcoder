def main():
    N = int(input())
    d = []
    d = [int(input()) for _ in range(N)]
    d = list(set(d))
    print(len(d))


if __name__ == "__main__":
    main()
