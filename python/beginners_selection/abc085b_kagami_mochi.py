def main():
    N = int(input())
    d = []
    for _ in range(N):
        d.append(int(input()))
    d = list(set(d))
    print(len(d))


if __name__ == "__main__":
    main()
