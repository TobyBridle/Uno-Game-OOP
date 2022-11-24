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

    def isEmpty(self):
        pass



class Hand:
    def __init__(self) -> None:
        hand = []

    def addCard(self, pickUpAmount, hand):
        self.hand.append(Deck.getCard(pickUpAmount))

        
    def getLength(self, hand):
        if len(self.hand == 1):
            Player.Uno()
        else:
            return len(hand)
        



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

    def Uno(self) -> None:
        print("UNO!")
        saidUno = True
        return saidUno

class playedCards:

    def __init__(self) -> None:
        playedCards = []

    def getLastCard(self):
        return playedCards[-1]
        


    def checkColour(self):
        cardSplit = playedCards[-1]
        cardSplit.split()   
        return cardSplit[0]

    def checkNumber(self):
        cardSplit = playedCards[-1]
        cardSplit.split()
        return cardSplit[1]
    
    def changeColour(self):
        pass
