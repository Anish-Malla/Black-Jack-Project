# This program will simulate a blackjack game against the dealer
import random
import webbrowser

#Creation of a full deck of cards
#  HEARTS
full_deck= []
for x in range(1,14):
    if x == 1:
        x = "A"
        full_deck.append(f"H{x}")
    elif x == 11:
        x = "J"
        full_deck.append(f"H{x}")
    elif x == 12:
        x = "Q"
        full_deck.append(f"H{x}")
    elif x == 13:
        x = "K"
        full_deck.append(f"H{x}")
    else:
        full_deck.append(f"H{x}")

#  DIAMONDS
diamond_cards = []
for x in range(1,14):
    if x == 1:
        x = "A"
        full_deck.append(f"D{x}")
    elif x == 11:
        x = "J"
        full_deck.append(f"D{x}")
    elif x == 12:
        x = "Q"
        full_deck.append(f"D{x}")
    elif x == 13:
        x = "K"
        full_deck.append(f"D{x}")
    else:
        full_deck.append(f"D{x}")

# SPADES
for x in range(1,14):
    if x == 1:
        x = "A"
        full_deck.append(f"S{x}")
    elif x == 11:
        x = "J"
        full_deck.append(f"S{x}")
    elif x == 12:
        x = "Q"
        full_deck.append(f"S{x}")
    elif x == 13:
        x = "K"
        full_deck.append(f"S{x}")
    else:
        full_deck.append(f"S{x}")

#  CLUBS
for x in range(1,14):
    if x == 1:
        x = "A"
        full_deck.append(f"C{x}")
    elif x == 11:
        x = "J"
        full_deck.append(f"C{x}")
    elif x == 12:
        x = "Q"
        full_deck.append(f"C{x}")
    elif x == 13:
        x = "K"
        full_deck.append(f"C{x}")
    else:
        full_deck.append(f"C{x}")

#Values of cards:
def value_of_cards(card):
    my_list = ["H2","H3","H4","H5","H6","H7","H8","H9",'D2', 'D3', 'D4', 'D5', 'D6', 'D7', 'D8', 'D9', 'D10','S2', 'S3', 'S4', 'S5', 'S6', 'S7', 'S8', 'S9', 'S10', 'C2', 'C3', 'C4', 'C5', 'C6', 'C7', 'C8', 'C9', 'C10']
    ace_list = ["HA","DA","SA","CA"]
    other_list = ["H10","HJ","HQ","HK","D10","DJ","DQ","DK","S10","SJ","SQ","SK","C10","CJ","CQ","CK"]
    if card in my_list:
        x = int(card[1])
    if card in ace_list:
        x = 11
    if card in other_list:
        x = 10
    return x


#Function in order to check if the card has already been selected:
def card_check(playing_card):
    return playing_card not in full_deck

# Function to randomly select a card
def random_card(deck_of_cards):
    selected_card_index = random.randint(0,(len(deck_of_cards)-1))
    selected_card = deck_of_cards[selected_card_index]
    deck_of_cards.remove(selected_card)
    if card_check(selected_card) == True:
        selected_card = deck_of_cards[selected_card_index]
    return selected_card

#the two decks defined below:
def making_dealer_deck():
    dealer_deck = []
    dealer_deck.append(random_card(full_deck))
    dealer_deck.append(random_card(full_deck))
    return dealer_deck

def making_player_deck():
    player_deck = []
    player_deck.append(random_card(full_deck))
    player_deck.append(random_card(full_deck))
    return player_deck

# Amount of chips player has
class Chips:
    def __init__(self):
        self.total = 100
        self.bet = 0
    def win_bet(self):
        self.total += self.bet
    def lose_bet(self):
        self.total -= self.bet

#Taking in the bet
def make_bet(chips):
    while True:
        chips.bet = int(input("How many chips would you like to bet? (Type the number) "))
        if chips.bet > chips.total and chips.bet > -1:
            print(f"The amount can not exceed {chips.total}")
        else:
            break

# adding cards to existing hand
def adding_card(player_deck):
    player_deck.append(random_card(full_deck))

#Sum of cards
def sum_of_cards(deck):
    decks_total = 0
    for cards in deck:
        decks_total += value_of_cards(cards)
    return decks_total

# A is 21 or 1
def ace_value(deck, total_of_deck):
    ace_list = ["HA","DA","SA","CA"]
    for element in deck:
        if element in ace_list and total_of_deck > 21:
            total_of_deck -= 10
    return total_of_deck

#printing decks:
# printing some of the deck
def display_part_of_deck(deck_of_dealer):
    for i in range(0,len(deck_of_dealer)):
       if i > 0:
           print("Card disclosed")
       else:
           print(deck_of_dealer[i])

# Printing full deck
def display_full_deck(deck_of_player):
    for i in range(0,len(deck_of_player)):
       print(deck_of_player[i])

#dealer hit or not
def dealer_hit_or_not(deck_of_dealer):
    if ace_value(deck_of_dealer, sum_of_cards(deck_of_dealer)) <= 16:
        dealer_deck.append(adding_card(deck_of_dealer))
    return dealer_deck

#Player hit or not
playing = True
def player_hit_or_not(player_deck_of_cards):
    global playing

    hit_stay = input("Do you want to hit or stay (enter 'h' or 's') ")
    if hit_stay == "h":
        player_deck_of_cards.append(random_card(full_deck))
    else:
         playing = False
    return player_deck_of_cards

# Player bust
def player_bust(deck_of_player, chips):
    chips.lose_bet()
    print("You have lost the game")

# Player win
def player_win(deck_of_player, chips):
    chips.win_bet()
    print("You have won")

#Dealer bust
def dealer_bust(deck_of_dealer, chips):
    chips.win_bet()
    print("The dealer's deck is a bust you have won the game")

#Dealer win
def dealer_win(deck_of_dealer,chips):
    chips.lose_bet()
    print("You have lost and the dealer has won")

# Main Program
print("WELCOME TO BLACKJACK! \nYou will be playing against the dealer")

tutorial = input("Do you want to watch a tutorial on how to play the game? (yes or no) ")
if tutorial.lower()[0] == "y":
    webbrowser.open("https://www.youtube.com/watch?v=eyoh-Ku9TCI")

print("You will be starting with 100 chips \n")
replay = True

while replay == True:
    # making the bet
    players_chips = Chips()
    make_bet(players_chips)

    # making decks
    player_deck = making_player_deck()
    dealer_deck = making_dealer_deck()

    print("\nDealers Deck:")
    display_part_of_deck(dealer_deck)
    print("\nPlayers deck:")
    display_full_deck(player_deck)

    while playing == True:

        if ace_value(player_deck, sum_of_cards(player_deck)) < 21:
            player_hit_or_not(player_deck)
            print("\nDealers Deck:")
            display_part_of_deck(dealer_deck)
            print("\nPlayers Deck:")
            display_full_deck(player_deck)

        elif ace_value(player_deck, sum_of_cards(player_deck)) > 21:
            player_bust(player_deck,players_chips)
            playing = False

        elif ace_value(player_deck, sum_of_cards(player_deck)) == 21:
            player_win(player_deck,players_chips)
            playing = False

    if ace_value(player_deck, sum_of_cards(player_deck)) <= 21:
        while ace_value(dealer_deck, sum_of_cards(dealer_deck)) < 17:
            dealer_hit_or_not(dealer_deck)
        print("\nDealers Deck:")
        display_full_deck(dealer_deck)
        print("\nPlayers Deck:")
        display_full_deck(player_deck)

        if ace_value(player_deck, sum_of_cards(player_deck)) == ace_value(dealer_deck, sum_of_cards(dealer_deck)):
            print("It is a tie neither of you has won")
        elif ace_value(dealer_deck, sum_of_cards(dealer_deck)) > 21:
            dealer_bust(dealer_deck, players_chips)
        elif ace_value(dealer_deck, sum_of_cards(dealer_deck)) == 32:
            dealer_win(dealer_deck,players_chips)
        elif ace_value(player_deck, sum_of_cards(player_deck)) == 21:
            player_win(player_deck, players_chips)
        elif ace_value(player_deck, sum_of_cards(player_deck)) > ace_value(dealer_deck, sum_of_cards(dealer_deck)) and ace_value(player_deck, sum_of_cards(player_deck)) < 21 and ace_value(dealer_deck, sum_of_cards(dealer_deck)) < 21:
            player_win(player_deck,players_chips)
        elif ace_value(player_deck, sum_of_cards(player_deck)) < ace_value(dealer_deck, sum_of_cards(dealer_deck)) and ace_value(player_deck, sum_of_cards(player_deck)) < 21 and ace_value(dealer_deck, sum_of_cards(
            dealer_deck)) < 21:
            dealer_win(dealer_deck,players_chips)

    print(f"\nYour current earnings are: {players_chips.total}")

    replay = input("Do you want to play again (yes or no): ")
    if replay.lower()[0] == "y":
        replay = True
        playing = True
    else:
        replay = False
        print("Thanks for playing!")