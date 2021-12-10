
import random
from random import seed

wins = 0

class Player:

    def __init__(self, total, soft, hand, bj):
        self.total = total
        self.soft = soft
        self.hand = hand
        self.bj = bj

def getTotal(self):
    return self.total

def outputVals(self):
    vals = (self.total, self.soft)
    return vals



class BlackJack:

    def __init__(self, players, numDecks, numGames): #initializing blackjack game
        self.players = players
        self.numDecks = numDecks
        self.numGames = numGames


#returns a hand
def deal():
    h1 = random.randint(0, len(curDeck)-1)
    card1 = curDeck.pop(h1)
    h2 = random.randint(0, len(curDeck)-1)
    card2 = curDeck.pop(h2)
    hand = [card1, card2]
    return hand

def playHand(player):
    if 1 in player.hand:
        return softTotal(player.total)
    return hardTotal(player.total)

def hitMe():
    h1 = random.randint(0, len(curDeck)-1)
    card = curDeck.pop(h1)
    return card


def softTotal(total):
    total = total + 10 #treating ace as an 11 until total is over 21 then treating ace as a 1
    hit = True
    if total >= 19:
        return total
    if total >= 18 and upcard < 9 and upcard != 1:
        return total

    #everything above accounts for totals above 18
    #supposed to hit on all soft totals 17 and below
    newCard = hitMe()
    #print("New Card: " + str(newCard))
    newTotal = total + newCard

    #print("New total: " + str(newTotal))
    if newCard == 1:
        return softTotal(total - 9) #reseting the total then adding another ace



    if newTotal > 21:
        return hardTotal(newTotal - 10) # shifting total to a hardTotal with the ace changed to a 1 instead of 11
    else:
        return softTotal(newTotal - 10)




    return total

def hardTotal(total):
    hit = False
    if upcard > 1 and upcard <= 6 and total > 12: # if dealer has bust card and player has bust card stand
        return total
    elif total >= 17: # everything over 17 stand
        return total
    elif total <= 11:
        hit = True
    elif upcard >=7 and total > 11 or upcard == 1:
        hit = True
    elif upcard >=4 and upcard <= 6 and total == 12:
        return total
    elif (upcard == 3 or upcard == 2) and total == 12:
        hit = True
    else:
        return total

    if hit == True:
        newCard = hitMe()
        newTotal = total + newCard
        if newCard == 1:
            return softTotal(newTotal)
        else:
            return hardTotal(newTotal)
    else:
        return total


def dealerSoft(total):
    total = total + 10
    if total >= 17: #hitting until above 17
        return total
    else:
        newCard = hitMe()

    if newCard == 1: # accounting for another ace drawn
        return dealerSoft(total-9)

    newTotal = newCard + total

    if newTotal > 21: # if gone over 21 then ace becomes a 1 and total becomes hard
        return dealerHard(newTotal-10)



    return dealerSoft(newTotal - 10)

def dealerHard(total):
    if total >= 17:
        return total
    else:
        newCard = hitMe()

    if newCard == 1:
        return softTotal(total)
    else:
        newTotal = total + newCard
        return dealerHard(newTotal)



    return total



def runGame(blackj): #will return a percentage of games won
    global deck
    global curDeck
    global dealerHand
    global numGames
    global wins
    global upcard
    global pushes
    global pbusts
    global dbusts
    global numBJs

    dbusts = 0
    pbusts = 0
    numBJs = 0
    wins = 0
    pushes = 0


    deck = [1,2,3,4,5,6,7,8,9,10,10,10,10]
    deck = deck*4 #full deck
    # creating universal deck
    if blackj.numDecks == 0 or blackj.numDecks > 6:
        return 0
    if blackj.numGames == 0:
        return 0
    if blackj.players == 0 or blackj.numDecks > 6:
        return 0


    #add for loop here eventually to run through numGames


    for x in range(blackj.numGames):


        curDeck = []
        dealerHand = []
        playerlist = []
        dealerBJ = False




        curDeck = blackj.numDecks * deck



        for i in range(blackj.players): #adding players into player list
            playerBJ = False
            newHand = deal()
            total = newHand[0] + newHand[1]
            if total == 11 and 1 in newHand:
                playerBJ = True
            soft = False
            if newHand[0] == 1 or newHand[1] == 1:
                soft = True
            playerlist = playerlist + [Player(total, soft, newHand, playerBJ)]


        dealerHand = deal()
        dealerTotal = dealerHand[0] + dealerHand[1]
        if dealerTotal == 21:
            dealerBJ = True
        upcard = dealerHand[0]

        #print("Dealer upcard: " + str(upcard))

        for i in playerlist: # playing all player hands
            i.total = playHand(i)
            #print("Player hand total: " + str(i.total))

        if 1 in dealerHand: #playing ace hand for dealer
            dealerTotal = dealerSoft(dealerTotal)
        else:
            dealerTotal = dealerHard(dealerTotal)

        #print("Dealer final total: " + str(dealerTotal))

        #evaluate wins and losses here

        for i in playerlist:
            if dealerBJ == True and i.bj == True:
                #print("Push")
                pushes = pushes + 1
                numBJs = numBJs + 1
            elif dealerBJ == True and i.bj == False:
                #print("Dealer Wins")
                xxy = 0
            elif dealerBJ == False and i.bj == True:
                #print("Player Wins")
                numBJs = numBJs + 1
                wins = wins + 1
            elif i.total > 21:
                #print("Dealer Wins")
                pbusts = pbusts + 1
            elif dealerTotal > 21:
                #print("Player Wins")
                dbusts = dbusts + 1
                wins = wins + 1
            elif dealerTotal > i.total and dealerTotal <= 21:
                #print("Dealer Wins")
                xxy = 1
            elif dealerTotal < i.total and i.total <= 21:
                #print("Player Wins")
                wins = wins + 1
            elif dealerTotal == i.total and dealerTotal <= 21 and i.total <= 21:
                #print("Push")
                pushes = pushes + 1
            else:
                print("This should not be reached")
                print("Dealer Total was: " + str(dealerTotal))
                print("Player Total was: " + str(i.total))



    games = blackj.numGames * blackj.players
    pw = 1.0*wins / games
    dw = 1.0*(games-wins-pushes)/games
    p = 1.0*pushes/games
    bjs = 1.0*numBJs/games
    pb = 1.0*pbusts/games
    db = 1.0*dbusts/games

    print("Percentage of Player Wins: " + str(100*pw) + "%")
    print("Percentage of Dealer Wins: " + str(100*dw) + "%")
    print("Percentage of Pushes: " + str(100*p) + "%")
    print("Percentage of BlackJacks: " + str(100*bjs) + "%")
    print("Percentage of Player Busts: " + str(100*pb) + "%")
    print("Percentage of Dealer Busts: " + str(100*db) + "%")

    return(1)




if __name__ == '__main__':

    #LINE BELOW IS ONE TO CHANGE TO LOOK AT GAMES PLAYERS AND DECKS ETC

    bj = BlackJack(5, 6, 1000000) #runs blackjack game (players, numDecks, numGames)
    game = runGame(bj)







