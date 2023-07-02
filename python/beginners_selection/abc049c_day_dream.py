def main():
    templates = ["eraser", "erase", "dreamer", "dream"]
    S = input()
    for template in templates:
        S = S.replace(template, "")
    print("YES") if S == "" else print("NO")


if __name__ == "__main__":
    main()
