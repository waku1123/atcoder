def main():
    _ = int(input())
    cards = sorted(list(map(int, input().split(" "))), reverse=True)
    a = []
    b = []
    for idx, card in enumerate(cards, start=1):
        b.append(card) if idx % 2 == 0 else a.append(card)
    print(sum(a) - sum(b))

if __name__ == "__main__":
    main()
