import random

def getCard(score):
    score = random.randint(1, 11)
    return score


def displayScore(playerscore, computerscore):
    print("The player's score:", playerscore)
    print("The computer's score:", computerscore)


def checkResults(playerscore, computerscore):
    if playerscore > 21 and computerscore < 21:
        print("The player loses and the computer wins!")
        quit()
    elif playerscore < 21 and computerscore > 21:
        print("The computer loses and the player wins!")
        quit()
    elif playerscore == 21 and computerscore < 21:
        print("Blackjack! Player wins!")
        quit()
    elif computerscore == 21 and playerscore < 21:
        print("Blackjack! Computer wins!")
        quit()


def main():
    playerTotal = computerTotal= 0
    playerTotal += getCard(playerTotal)
    computerTotal += getCard(computerTotal)
    checkResults(playerTotal, computerTotal)
    displayScore(playerTotal,computerTotal)

    while computerTotal < 16 and playerTotal < 21:
        new = input("Want another card? (y/n)")
        if new == 'y':
            playerTotal += getCard(playerTotal)
            while computerTotal < 16:
                computerTotal += getCard(computerTotal)
            displayScore(playerTotal, computerTotal)
            checkResults(playerTotal, computerTotal)
        else:
            while computerTotal < 16:
                computerTotal += getCard(computerTotal)
            checkResults(playerTotal, computerTotal)
            displayScore(playerTotal, computerTotal)
            if playerTotal > computerTotal:
                print('Player wins!')
                quit()
            elif computerTotal > playerTotal:
                print('Computer wins!')
                quit()
            elif computerTotal == playerTotal:
                print('It is a tie.')
                quit()

    while playerTotal < 21 and computerTotal < 21 and computerTotal >= 16:
            new = input("Want another card? (y/n)")
            if new == 'y':
                playerTotal += getCard(playerTotal)
                displayScore(playerTotal, computerTotal)
                checkResults(playerTotal, computerTotal)
            else:
                if playerTotal > computerTotal:
                    print('Player wins!')
                    quit()
                elif computerTotal > playerTotal:
                    print('Computer wins!')
                    quit()
                elif computerTotal == playerTotal:
                    print('It is a tie.')
                    quit()
main()