from library get_card, get_card_sum


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
