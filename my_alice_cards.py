from random import randint
from time import sleep

def find_card(total_cards, challenge_card):    
    cards = []
    for _ in range(total_cards):
        cards.append(randint(1,total_cards))
    
    if challenge_card in cards:
        return f'{challenge_card} is at {cards.index(challenge_card)}th position in the collection of cards'
    else:
        return f'{challenge_card} is not present in the collection.'
    
print(find_card(5,1))