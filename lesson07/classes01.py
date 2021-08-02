import random


def get_card():
    card_suit_list = ["H", "D", "C", "S"]
    index = random.randint(0, 3)
    card_suit = card_suit_list[index]

    card_list = ["6", "7", "8", "9", "10", "J", "D", "K", "A"]
    index = random.randint(0, len(card_suit) -1)
    card = card_list[index]

    return f"{card_suit}-{card}"

print(get_card())
