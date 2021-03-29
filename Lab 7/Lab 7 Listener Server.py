# Kyle Johnson
# ETEC3702 – Concurrency 5:00 PM
# Paul Yost
# 3-25-21
# Lab 7 – Inter-Process Communication with Listeners and Clients

#Listener Example
import multiprocessing.connection
import random
def checkwin(sym, moves):
    # Fail fast
    if(moveCounter < 5):
        return False
    # Check Rows
    if(sym == boardlist[0] and sym == boardlist[1] and sym == boardlist[2]):
        return True
    elif(sym == boardlist[3] and sym == boardlist[4] and sym == boardlist[5]):
        return True
    elif(sym == boardlist[6] and sym == boardlist[7] and sym == boardlist[8]):
        return True
    #Check Cols
    elif(sym == boardlist[0] and sym == boardlist[3] and sym == boardlist[6]):
        return True
    elif(sym == boardlist[1] and sym == boardlist[4] and sym == boardlist[7]):
        return True
    elif(sym == boardlist[2] and sym == boardlist[5] and sym == boardlist[8]):
        return True
    #Check diags
    elif(sym == boardlist[0] and sym == boardlist[4] and sym == boardlist[8]):
        return True
    elif(sym == boardlist[2] and sym == boardlist[4] and sym == boardlist[6]):
        return True
    # Failed
    else:
        return False
num = random.randint(1, 2)
if num == 1:
    p1sym = 'X'
    p2sym = 'O'
else:
    p1sym = 'O'
    p2sym = 'X'

address=('127.0.0.1',0x1234)
listener=multiprocessing.connection.Listener(address,authkey=b'secret')
boardlist = [1,2,3,4,5,6,7,8,9]
board = "\n " + str(boardlist[0]) + " | " + str(boardlist[1]) + " | " + str(boardlist[2]) + "\n" + "---+---+---\n" + " " + str(boardlist[3]) + " | " + str(boardlist[4]) + " | " + str(boardlist[5]) + "\n" + "---+---+---\n" + " " + str(boardlist[6]) + " | " + str(boardlist[7]) + " | " + str(boardlist[8]) + "\n"
p1turndone = False
p2turndone = False
moveCounter = 0

print("waiting for connection.")
player1 = listener.accept()
player1id = listener.last_accepted
player2 = listener.accept()
player2id = listener.last_accepted
player1.send(p1sym)
player2.send(p2sym)

while True:
    p1turndone = False
    p2turndone = False
    while p1turndone != True:
        if(moveCounter == 9):
            player2.send(moveCounter)
            player1.send(moveCounter)
            break
        player1.send(board)
        player1.send("You are "+ p1sym + ". Input a number to send it to board.")
        input = player1.recv()

        if input['move'] in boardlist:
            player1.send("Waiting for other player...")
            boardlist[input['move'] - 1] = input['sym']
            board = "\n " + str(boardlist[0]) + " | " + str(boardlist[1]) + " | " + str(boardlist[2]) + "\n" + "---+---+---\n" + " " + str(boardlist[3]) + " | " + str(boardlist[4]) + " | " + str(boardlist[5]) + "\n" + "---+---+---\n" + " " + str(boardlist[6]) + " | " + str(boardlist[7]) + " | " + str(boardlist[8]) + "\n"
            player1.send(board)
            moveCounter = moveCounter + 1

            if(moveCounter == 9):
                player2.send(moveCounter)
                player1.send(moveCounter)
                player2.send(board)
                player1.send(board)
                break
            else:
                player1.send(moveCounter)
            if(checkwin(p1sym, moveCounter) == True):
                player1.send("P1 Wins!")
                player2.send("P1 Wins!")
                player2.send(board)
                player1.send(board)
                break
            if(checkwin(p2sym, moveCounter) == True):
                player1.send("P2 Wins!")
                player2.send("P2 Wins!")
                player2.send(board)
                player1.send(board)
                break

            p1turndone = True
        else:
            player1.send("Invalid Entry, try again")
            player1.send(board)
            player1.send(moveCounter)
            print("Invalid input need to retry")
            
    print(board)
    

    while p2turndone != True:
        player2.send(board)
        player2.send("You are "+ p2sym+ ". Input a number to send it to board.")
        input = player2.recv()
        if input['move'] in boardlist:
            player2.send("Waiting for other player...")
            boardlist[input['move'] - 1] = input['sym']
            board = "\n " + str(boardlist[0]) + " | " + str(boardlist[1]) + " | " + str(boardlist[2]) + "\n" + "---+---+---\n" + " " + str(boardlist[3]) + " | " + str(boardlist[4]) + " | " + str(boardlist[5]) + "\n" + "---+---+---\n" + " " + str(boardlist[6]) + " | " + str(boardlist[7]) + " | " + str(boardlist[8]) + "\n"
            player2.send(board)
            moveCounter = moveCounter + 1

            if(moveCounter == 9):
                player2.send(moveCounter)
                player1.send(moveCounter)
                player2.send(board)
                player1.send(board)
                break
            else:
                player2.send(moveCounter)
            if(checkwin(p2sym, moveCounter) == True):
                player2.send("P2 Wins!")
                player1.send("P2 Wins!")
                player2.send(board)
                player1.send(board)
                break
            if(checkwin(p1sym, moveCounter) == True):
                player2.send("P1 Wins!")
                player1.send("P1 Wins!")
                player2.send(board)
                player1.send(board)
                break

            p2turndone = True
        else:
            player2.send("Invalid Entry, try again")
            player2.send(board)
            player2.send(moveCounter)
            print("Invalid input need to retry")

    print(board)
    
print("Game Over")
player1.close()
player2.close()
