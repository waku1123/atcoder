def main():
    A = int(input())
    B = int(input())
    C = int(input())
    X = int(input())
    count = 0
    # a_amounts = [500 * i for i in range(1, a+1)] if a else []
    # b_amounts = [100 * j for j in range(1, b+1)] if b else []
    # c_amounts = [50 * k for k in range(1, c+1)] if c else []
    # print(a_amounts)
    # print(b_amounts)
    # print(c_amounts)
    for a in range(A + 1):
        for b in range(B + 1):
            for c in range(C + 1):
                if X == 500 * a + 100 * b + 50 * c:
                    count += 1
    print(count)


if __name__ == "__main__":
    main()
