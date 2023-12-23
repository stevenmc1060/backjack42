import random
    
playerHandCard1 = random.randrange(2,11)
playerHandCard2 = random.randrange (2,11)
dealerHandCard1 = random.randrange(2,11)
dealerHandCard2 = random.randrange(2,11)

def showPlayerhand():
    global playerHand
    playerHand = playerHandCard1 + playerHandCard2
    print (f"Your hand is a: {playerHand}")

def showDealerHand():
    global dealerHand
    dealerHand = dealerHandCard1 + dealerHandCard2
    print(f"The Dealer has a: {dealerHandCard2} showing:")

def hit_me():
    hitMe = input("Do you want to hit?")
    if hitMe == ("yes"):
        hitCard1 = random.randrange(2,11)
        global newplayerHand
        newplayerHand = newplayerHand + hitCard1
        print(f"You now have a: {newplayerHand}")
    elif hitMe ==("no"):
        newplayerHand = playerHand
        return
    hitmeAgain = input("Do you want to hit again?")    
    if hitmeAgain == ("yes"):
        hitcard2 = random.randrange(2,11)
        newplayerHand = newplayerHand + hitcard2
        print(f"You now have a: {newplayerHand}")
    elif hitmeAgain == ("no"):
        return
    
showPlayerhand()
showDealerHand()
hit_me()

def who_wins():
    if newplayerHand > dealerHand:
        print(f"You win! You had a: {newplayerHand}")
        print(f"The dealer had a: {dealerHand}")
    if dealerHand > newplayerHand:
        print(f"The dealer won! The dealer had a:{dealerHand}")
        print(f"You had a: {newplayerHand}")
        return
    


def playAgain():
    doPlayAgain = input("Would you like to play again?")
    if doPlayAgain == ("yes"):
        showDealerHand ()
        showPlayerhand ()
        hit_me ()


who_wins ()

playAgain()
