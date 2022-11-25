import numpy as np, time as t, random as r


class Deck:
    def __init__(self) -> None:
        self.cards = []

    def buildDeck(self, deck):
        colours = ["Red", "Green", "Yellow", "Blue"]
        values = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, "Draw Two", "Skip", "Reverse"]
        wilds = ["Wild", "Wild Draw Four"]
        for colour in colours:
            for value in values:
                cardVal = "{} {}".format(colour, value)
                self.cards.append(cardVal)
                if value != 0:
                    self.cards.append(cardVal)

        for _ in range(4):
            deck.append([wilds[0]])
            deck.append(wilds[1])

        np.random.shuffle(deck)
        return deck

    def getCard(self, pickUpAmount, hand):
        for _ in range(pickUpAmount):
            sendOff = self.cards[1:pickUpAmount]
            hand.remove(sendOff)
            return sendOff
        

    def dealSeven(self, hand, numToDeal, getNumOfPlayers, players):
        for i in range(getNumOfPlayers()):
            players[i].addCard(hand.addCard(7))

    def isEmpty(self, deck):
        return bool(len(deck) == 0) # Will return True if deck is empty



class Hand:
    def __init__(self) -> None:
        self.hand = ["yellow 1"]

    def addCard(self, pickUpAmount):
        # FIX: Make it so that it picks up the amount of cards specified
        self.hand.append(Deck.getCard(pickUpAmount, self.hand))


    def getHand(self):
        return self.hand
        



class Game:
    def __init__(self) -> None:
        self.players = []

    def startGame(self) :
        print("Welcomle to Uno.")
        print("To start, you need to choose how many players will be playing.")
        numOfPlayers = int(input("How many players will be playing?  :  (2-4) "))
        if numOfPlayers in [2,3,4]:
            print("You have chosen {} players.".format(numOfPlayers))
            self.players = [Player() for _ in range(numOfPlayers)]
            return self.players
        else:
            print("Invalid input. Please choose between 2 and 4 players.")
            self.startGame()
        

class Player:
    def __init__(self) -> None:
        self.hand = Hand()

    def Uno(self):
        print("UNO!")
        saidUno = True
        return saidUno


    def PlayCard(self):
        print("You have chosen to play a card. What card would you like to play")
        print(self.hand.getHand())
        _cardToPlay = ""
        # Card must be an integer and within the bounds 1 - self.hand.getLength()
        handLength = len(self.hand.getHand())
        while _cardToPlay not in range(1, handLength):
            _cardToPlay = input("Please enter the card you would like to play: 1 - {}".format(handLength))
        # Try to convert to integer
        cardToPlay = int(_cardToPlay)
        
        if cardToPlay <= handLength:
            card = self.hand.getHand()[int(cardToPlay)-1]
            # FIX: What is playedCards??
            playedCards.setLastCard(card)
            self.hand.getHand().remove(card)
            return card
        if handLength == 1:
            self.Uno()


class playedCards:

    def __init__(self) -> None:
        PlayedCards = []

    def getLastCard(self, PlayedCards):
        return PlayedCards[-1]

    def setLastCard(self, card, PlayedCards):
        PlayedCards.append(card)
        return PlayedCards

    def checkColour(self, PlayedCards):
        card = PlayedCards[-1]
        cardSplit = card.split(" ")
        colour = str(cardSplit[0])  
        return colour

    def checkNumber(self, PlayedCards):
        card = PlayedCards[-1]
        cardSplit = card.split(" ")
        number = int(cardSplit[1])  
        return number
    
    def changeColour(self):
        colourChoice = input("""What colour would you like to change the play to?:
        R - Red
        B - Blue
        Y - Yellow
        G - Green
        
        - """)
        colour = ""
        if colourChoice in ["R", "B", "Y", "G"]:
            if colourChoice == "R":
                colour = "Red"
                print("You have chosen to change the colour to Red.")
            elif colourChoice == "B":
                colour = "Blue"
                print("You have chosen to change the colour to Blue.")
            elif colourChoice == "Y":
                colour = "Yellow"
                print("You have chosen to change the colour to Yellow.")
            elif colourChoice == "G":
                colour = "Green"
                print("You have chosen to change the colour to Green.")
            else:
                print("Invalid input. Please try again.")
                self.changeColour()
            return colour
        else:
            print("Invalid input. Please try again.")
            self.changeColour()


while True:
    deck = Deck()
    deck.buildDeck(deck)
    game = Game()
    game.startGame()
    print()

