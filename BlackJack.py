'''
SIMPLE BLACKJACK GAME
'''

from random import shuffle

class Card:

    '''
    CREATE THE DECK OF CARDS
    '''

    def __init__(self):
        self.values = ['A', '2', '3', '4', '5', '6', '7', '8', '9', '10', 'J', 'Q', 'K']
        self.suits = ['CLUBS', 'DIAMONDS', 'HEARTS', 'SPADES']
        self.deck = []

        for i in self.suits:
            for j in self.values:
                new_card = j + ' ' + i
                self.deck.append(new_card)

    def __str__(self):
        return self.deck

    def shuffle(self):
        return shuffle(self.deck)

    def pop_first(self):
        return self.deck.pop(0)


class Bank:
    '''
    CREATE A BANK ACCOUNT OF PLAYER
    '''

    def __init__(self, amount):
        self.amount = amount

    def deposit(self, deposit_amount):
        self.amount += deposit_amount
        print("Your money at bank has reached {}$\n".format(self.amount))

    def withdrawal(self, withdrawal_amount):
        if withdrawal_amount > self.amount:
            print("Sorry! You don't have enough money :(\n")
            print("The current amount is {}$\n".format(self.amount))
        else:
            self.amount -= withdrawal_amount
            print("Your money at bank has fallen to {}$\n".format(self.amount))


class Player(Card):
    '''
    CREATE A PLAYER WITH NO CARDS AT HAND
    '''

    def __init__(self, name):
        self.name = name
        self.player_hand = []

    def __str__(self):
        return self.player_hand

    def hit(self, deck_list):
        self.player_hand.append(deck_list.pop_first())
        print("Cards of {} : {} \n".format(self.name, Player.__str__(self)))
        return self.player_hand


class Computer(Card):
    '''
    CREATE THE COMPUTER WITH NO CARD AT HAND, EITHER
    '''

    def __init__(self):
        self.computer_hand = []

    def __str__(self):
        return self.computer_hand[1:]

    def hit(self, deck_list):
        self.computer_hand.append(deck_list.pop_first())
        print("Cards of Computer : {}".format(self.__str__()))
        return self.computer_hand

def is_sum_twentyone(hand):
    val_list = []

    for i in hand:
        value = i.split(" ")[0]
        if value == 'K' or value == 'Q' or value == 'J':
            val_list.append(10)
        elif value != 'A':
            val_list.append(int(value))
        else:
            val_list.append(11)

    sum_hand = sum(val_list)
    count_A = val_list.count(11)

    i = 0

    while i < count_A:
        if sum_hand > 21:
            sum_hand -= 10
        i += 1

    return sum_hand


if __name__ == '__main__':

    #CREATE A GAME WITH A BANK ACCOUNT OF 500$
    bank_account = Bank(500)

    #THE GAME STARTS :)
    print("WELCOME TO THE BLACKJACK GAME!!!")
    print("WE HAVE JUST GIVEN YOU 500$ TO PLAY YOUR GAME")
    print("HAVE FUN :)\n")

    #GETTING NAME AND CREATING PLAYER AND COMPUTER OBJECTS..
    name = input("Your name : ")

    player1 = Player(name)
    my_computer = Computer()

    while True:

        #THE BEGINNING OF EACH ROUND, THE DECK WILL BE UPDATED..
        my_deck = Card()

        while True:
            try:
                #PLAYER IS WANTED TO GIVE SOME MONEY TO START.
                player_bet = int(input("Your Bet : "))

            #IF THE INPUT IS NOT INT OR NOT IN THE RANGE OF THE USER'S ACCOUNT, THE PLAYER WILL ASKED AGAIN
            except ValueError:
                print("Please provide a number with base 10..\n")
            else:
                if 0 < player_bet <= bank_account.amount:
                    break

        print()

        #THE DECK WILL BE SHUFFLED
        my_deck.shuffle()

        #THE BET WILL BE WITHDRAWED
        bank_account.withdrawal(player_bet)

        #THE DECKS ARE EMPTY
        my_computer.computer_hand = []
        player1.player_hand = []

        #THE PLAYER AND THE COMPUTER GET TWO CARDS OF EACH
        my_computer.hit(my_deck)
        player1.hit(my_deck)

        my_computer.hit(my_deck)
        player1.hit(my_deck)

        while True:
            #IF PLAYER HAS MORE THAN 20, CAN'T HIT CARDS ANYMORE
            if is_sum_twentyone(player1.player_hand) >= 21:
                break
            else:
                while True:
                    answer = input("Print 'H' to hit or 'S' to stand.\nYour move : ")

                    #IF PLAYER HAS LESS THAN 21, CHOOSE THE MOVE HIT/STAND
                    if answer.upper()[0] == 'H':
                        player1.hit(my_deck)
                        break
                    if answer.upper()[0] == 'S':
                        break
                if answer.upper()[0] == 'S':
                    break

        #AFTER THE PLAYER, IT'S COMPUTER'S TURN :)
        sum_player = is_sum_twentyone(player1.player_hand)

        while True:
            #IF PLAYER IS LESS THAN OR EQUAL TO 21, COMPUTER SHOULD GET MORE SCORE THAN THE PLAYER
            if sum_player <= 21:
                if is_sum_twentyone(my_computer.computer_hand) < sum_player:
                    my_computer.hit(my_deck)
                    print()
                else:
                    break
            #IF PLAYER LOST, COMPUTER DID NOT NEED TO HIT
            else:
                break

        #AT THE END OF THE TOUR, COMPUTER SHOWS ALL THE CARDS IT HAS
        print("\nAll cards of Computer : " , my_computer.computer_hand)

        sum_comp = is_sum_twentyone(my_computer.computer_hand)

        #IF PLAYER HAS MORE SCORES THAN COMPUTER AND ALSO LESS THAN 22, PLAYER WINS
        if sum_comp < sum_player <= 21 or sum_comp > 21:
            print("\nYou have won !!")
            bank_account.deposit(player_bet * 2)
        #IF PLAYER'S SCORE IS EQUAL TO COMPUTER'S SCORE, IT'S TIE
        elif sum_comp == sum_player:
            print("\nIt's Tie..")
            bank_account.deposit(player_bet)
        #IF PLAYER GETS MORE THAN 21 OR COMPUTER GETS BETTER SCORE, PLAYER LOSES
        else:
            print("\nYou have lost :(")

        #THE END OF THE TOUR
        cont = input("Play again [y/n] : ")

        #IF THE GAME ENDS, SHOWS HOW MUCH MONEY IN ACCOUNT IS
        if cont.upper()[0] == 'N':
            print("\nYour current bank account : {}$".format(bank_account.amount))
            break