from random import randint
from IPython.display import clear_output

# 21 points game
# cerate the balckjack class, which will hold all game methods and attributes
class BlackJack():
    def __init__(self):
        self.deck = []
        self.suits = ('Spades', 'Hearts', 'Diamonds', 'Clubs')
        self.values = ('2', '3', '4', '5', '6', '7', '8', '9', '10', 'J', 'Q', 'K', 'A')

    def makeDeck(self):
        for suit in self.suits:
            for value in self.values:
                self.deck.append((value, suit))
    
    def pullCard(self):
        card = self.deck.pop(randint(0, len(self.deck)-1))
        return card

class Player():
    def __init__(self,name):
        self.name = name
        self.hand = []

    def addCard(self, card):
        self.hand.append(card)

    def showHand(self, dealer_start = True):
        print(f'{self.name}:')
        print('======================')
        for i in range(len(self.hand)):
            if self.name == 'Dealer' and i == 0 and dealer_start:
                print('- of -')
            else:
                card = self.hand[i]
                print(f'{card[0]} of {card[1]}')
        print(f'Total = {self.calcHand(dealer_start)}')
    
    def calcHand(self, dealer_start = True):
        total = 0
        aces = 0
        card_values = {'2':2, '3':3, '4':4, '5':5, '6':6, '7':7, '8':8, '9':9, '10':10, 'J':10, 'Q':10, 'K':10, 'A':11}
        if self.name == 'Dealer' and dealer_start:
            card = self.hand[1]
            return card_values[card[0]]
        for card in self.hand:
            if card[0] == 'A':
                aces += 1
            else:
                total += card_values[card[0]]
        for i in range(aces):
            if total + 11 > 21:
                total += 1
            else:
                total += 11
        return total


game = BlackJack()
game.makeDeck()
name = input("What is your name?")
player = Player(name)
dealer = Player("Dealer")
# print(player.name, dealer.name)
for i in range(2):
    player.addCard(game.pullCard())
    dealer.addCard(game.pullCard())
    print(f'Player:{player.hand}\nDealer:{dealer.hand}')
player.showHand()
dealer.showHand()
player_bust = False
while input('Would you like to stay or hit?').lower() != 'stay':
    clear_output()
    # pull card and  put into player's hand
    player.addCard(game.pullCard())
    # show both hands using mthods
    player.showHand()
    dealer.showHand()
    # check if player busts
    if player.calcHand() > 21:
        player_bust = True
        print('You lose!')
        break
dealer_bust = False
if not player_bust:
    while dealer.calcHand() < 17:
        # pull card and put into dealer's hand
        dealer.addCard(game.pullCard())
        # check if dealer over 21
        if dealer.calcHand() > 21:
            dealer_bust = True
            print('You win!')
            break

clear_output()
# show both hands using methods
player.showHand()
dealer.showHand()
if player_bust:
    print('You busted, better luck next time!')
elif dealer_bust:
    print('Dealer busted, you win!')
elif player.calcHand() > dealer.calcHand():
    print('You win!')
elif player.calcHand() < dealer.calcHand():
    print('You lose!')
else:
    print('It\'s a tie!')
