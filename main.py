import numpy as np, time as t, random as r


class Deck:
    def __init__(self) -> None:
        pass

    def buildDeck(self, deck):
        colours = ["Red", "Green", "Yellow", "Blue"]
        values = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, "Draw Two", "Skip", "Reverse"]
        wilds = ["Wild", "Wild Draw Four"]
        deck = []
        for colour in colours:
            for value in values:
                cardVal = "{} {}".format(colour, value)
                deck.append(cardVal)
                if value != 0:
                    deck.append(cardVal)

        for i in range(4):
            deck.append([wilds[0]])
            deck.append(wilds[1])

        np.random.shuffle(deck)
        return deck

    def getCard(self, pickUpAmount, deck):
        for i in range(pickUpAmount):
            sendOff = deck[1:pickUpAmount]
            deck.remove(sendOff)
            return sendOff
        

    def dealSeven(self, deck, numToDeal, getNumOfPlayers, players):
        for i in range(getNumOfPlayers()):
            players[i].addCard(Hand.addCard(7))

    def isEmpty(self, deck):
        if len(deck) == 0:
            return True



class Hand:
    def __init__(self) -> None:
        hand = ["yellow 1"]

    def addCard(self, pickUpAmount, hand):
        self.hand.append(Deck.getCard(pickUpAmount))

        
    def getLength(self, hand):
        if len(self.hand == 1):
            Player.Uno()
        else:
            return len(hand)

    def getHand(self, hand):
        return self.hand
        



class Game:
    def __init__(self) -> None:
        pass

    def startGame(self, players) :
        print("Welcome to Uno.")
        print("To start, you need to choose how many players will be playing.")
        numOfPlayers = int(input("How many players will be playing?  :  (2-4) "))
        if numOfPlayers == [2,3,4]:
            print("You have chosen {} players.".format(numOfPlayers))
            players = [Player() for i in range(numOfPlayers)]
            return players
        else:
            print("Invalid input. Please choose between 2 and 4 players.")
            self.startGame(players)
        

class Player:
    def __init__(self) -> None:
        pass

    def Uno(self):
        print("UNO!")
        saidUno = True
        return saidUno

    def PlayCard(self):
        print("You have chosen to play a card. What card would you like to play")
        print(Hand.getHand())
        cardToPlay = input("Please enter the card you would like to play: 1 - {}".format(Hand.getLength()))
        if cardToPlay <= Hand.getLength():
            card = Hand.getHand()[cardToPlay-1]
            playedCards.setLastCard(card)
            Hand.getHand().remove(card)
            return card


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


