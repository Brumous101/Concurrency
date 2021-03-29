# Kyle Johnson
# ETEC3702 – Concurrency 5:00 PM
# Paul Yost
# 3-25-21
# Lab 7 – Inter-Process Communication with Listeners and Clients

#Client Example
import multiprocessing.connection
print("You are now connected please wait...")
address=('127.0.0.1',0x1234)
connection=multiprocessing.connection.Client(address,authkey=b'secret')
sym=connection.recv()
valid = 1
while True:
    while valid != 0:
        newboard=connection.recv()
        if newboard == "P1 Wins!" or newboard == "P2 Wins!" or newboard == 9:
            break
        servermess=connection.recv()
        print(newboard)
        print(servermess)
        mymove = int(input("Enter number to place move: "))
        playerData={'move':mymove,'sym':sym}
        connection.send(playerData)

        waitmess = connection.recv()
        updateboard=connection.recv()
        winstatus = connection.recv()
        if waitmess == "Invalid Entry, try again":
            print(updateboard)
            print(waitmess)
            valid = 1
        else:
            print(updateboard)
            print(waitmess)
            break
    if newboard == "P1 Wins!" or newboard == "P2 Wins!" or newboard == 9:
        break
    if winstatus == "P1 Wins!" or winstatus == "P2 Wins!" or winstatus == 9:
        break
#print(winstatus)
print("Game Over")
if newboard == "P1 Wins!" or newboard == "P2 Wins!":
    print(connection.recv())
    print(newboard)
if winstatus == "P1 Wins!" or winstatus == "P2 Wins!":
    print(connection.recv())
    print(winstatus)
if winstatus == 9 or newboard == 9:
    print(connection.recv())
    print("CAT")
connection.close()