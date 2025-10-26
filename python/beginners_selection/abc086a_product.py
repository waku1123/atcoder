import math


def main() -> None:
    # product = math.prod(list(map(int, input().split(" "))))
    print("Even") if math.prod(list(map(int, input().split(" ")))) % 2 == 0 else print("Odd")


if __name__ == "__main__":
    main()
