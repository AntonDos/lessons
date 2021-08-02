import random


def get_card_sum(used_cards):
    card_values = {
        "6": 6, "7": 7, "8": 8, "9": 9, "10": 10, "J": 2, "D": 3, "K": 4, "A": 11
    }
    card_sum = 0
    for card in used_cards:
        card_sum += card.split("-")[-1]
        card_sum += card_values[key]

def get_card(used_cards):
    card_suit_list = ["H", "D", "C", "S"]
    card_list = ["6", "7", "8", "9", "10", "J", "D", "K", "A"]
    while True:
        index = random.randint(0, 3)
        card_suit = card_suit_list[index]

    card_list = ["6", "7", "8", "9", "10", "J", "D", "K", "A"]
    index = random.randint(0, len(card_suit) -1)
    card = card_list[index]

    current = f"{card_suit}-{card}"
    if current not in used_cards

    return f"{card_suit}-{card}"

used_cards = []
while True:
    choice = input("Get new card[y/n]: ")
    if choice == "y":
        current = get_card(used_cards)
        used_cards.append(current)
        print(used_cards)

        card_sum = get_card_sum(used_cards)
        if card_sum > 21:
            print("Game over")
        if


print(used_cards)
