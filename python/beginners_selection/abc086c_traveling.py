def main():
    N = int(input())
    plans = []
    for i in range(N):
        plans.append(map(int, input().split(" ")))

    st = sx = sy = 0
    for t, x, y in plans:
        dt, dx, dy = t - st, abs(x - sx), abs(y - sy)  # 各時点のマンハッタン距離
        if t % 2 != (x + y) % 2 or dx + dy > dt:
            print("No")
            return
        st, sx, sy = t, x, y
    print("Yes")

if __name__ == "__main__":
    main()
