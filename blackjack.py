import random


users_cards = []
comps_cards = []

def randomize():
    return random.randint(1, 11)

def totalizer(card_list):
    total = sum(card_list)
    if total == 21:
        return 0  
    return total

def final_state():
    print(f"\nYour final hand: {users_cards}, current score: {totalizer(users_cards)}")
    print(f"Computer's final hand: {comps_cards}, computer's score: {totalizer(comps_cards)}")

    if totalizer(users_cards) > 21 and totalizer(comps_cards) > 21:
        print("Explosion! Both you and the computer lose!")
    elif totalizer(users_cards) == 0:
        print("You win with a Blackjack!")
    elif totalizer(comps_cards) == 0:
        print("Computer wins with a Blackjack!")
    elif totalizer(users_cards) > 21:
        print("You went over 21! You lose!")
    elif totalizer(comps_cards) > 21:
        print("Computer went over 21! You win!")
    elif totalizer(users_cards) > totalizer(comps_cards):
        print("You win!")
    elif totalizer(users_cards) < totalizer(comps_cards):
        print("You lose!")
    else:
        print("It's a draw!")

def gameplay():
    global users_cards, comps_cards

    print(logo)

    
    users_cards = [randomize(), randomize()]
    comps_cards = [randomize()]

    while True:
        print(f"\nYour cards: {users_cards}, current score: {totalizer(users_cards)}")
        print(f"Computer's first card: {comps_cards[0]}")

        
        if totalizer(users_cards) == 0 or totalizer(users_cards) > 21:
            break

        
        get_another_card = input("Type 'y' to get another card, or 'n' to pass: ").lower()
        if get_another_card == 'y':
            users_cards.append(randomize())
        else:
            break

    
    while totalizer(comps_cards) < 17:
        comps_cards.append(randomize())

    
    final_state()


def main():
    while True:
        want_to_play = input("Do you want to play a game of Blackjack? Type 'y' or 'n': ").lower()
        if want_to_play == 'y':
            gameplay()
        elif want_to_play == 'n':
            print("Goodbye.")
            break

main()
