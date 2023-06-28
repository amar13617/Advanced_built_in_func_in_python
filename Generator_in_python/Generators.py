#def first_hundred():
#    for number in range(1, 101):
#        print(number)
    
#first_hundred()

#def first_hundreds():
#    print("First value requested\n")

#    for number in range(1, 101):
#        print("Starting new iteration")
#        yield number
#        print("Ending this iteration\n")

#g = (first_hundreds())
#print(next(g))
#print(next(g))

#Exercise

def gen_primes(limit):
    
    for dividend in range(2, limit+1):
        for divisor in range(2,dividend):
            if dividend % divisor == 0:
                break
        else:
            yield dividend
            
primes = gen_primes(10)
print(next(primes))
print(next(primes))


names = [" rick", " MORTY  ", "beth ", "Summer", "jerRy    "]

names = (name.strip().split() for name in names)


ranks = (2, 3, 4, 5, 6, 7, 8, 9, 10, "jack", "queen", "king", "ace")
suits = ("clubs", "diamonds", "hearts", "spades")

cards = [(rank, suit) for suit in suits for rank in ranks]

#4
import itertools
import random

def deal(cards, number_of_players):
    deck = shuffle_deck(cards)

    deal_to_players(deck, number_of_players)
    deal_to_table(deck)

def deal_to_players(deck, number_of_players):
    first_cards = [next(deck)  for _ in  range(number_of_players)]
    second_cards = [next(deck)  for _ in  range(number_of_players)]

    hands = zip(first_cards, second_cards)

    print()

    for i,  (first_card, second_card)  in  enumerate(hands, start=1):
        print(f"Player {i} was dealt: {first_card}, {second_card}")

    print()

def deal_to_table(deck):
    next(deck)  # burn
    flop = ', '.join(str(next(deck))  for _ in  range(3))
    print(f"The flop: {flop}")

    next(deck)  # burn
    print(f"The turn: {next(deck)}")

    next(deck)  # burn
    print(f"The river: {next(deck)}")
    print()

def get_players():
    while True:
        number_of_players = input("How many players are there? ").strip()

        try:
            number_of_players = int(number_of_players)
        except ValueError:
            print("You must enter an integer.")
        else:
            if number_of_players in range(2, 11):
                return number_of_players
            elif number_of_players < 2:
                print("You must have at least 2 players.")
            else:
                print("You can have a maximum of 10 players.")

def shuffle_deck(cards):
    deck = list(cards)
    random.shuffle(deck)

    return iter(deck)

ranks = (2, 3, 4, 5, 6, 7, 8, 9, 10, "jack", "queen", "king", "ace")
suits = ("clubs", "diamonds", "hearts", "spades")

cards = list(itertools.product(ranks, suits))

deal(cards, get_players())

