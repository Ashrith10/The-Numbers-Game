#Copyright Ashrith Kanakanala 2018
import random
import getpass as gp

print("Would You Like To Read the Rules")
print("Type 'yes' or 'no'")
ruleans = str(input(""))
while ruleans == "yes":
    print("THE GAME IS SIMPLE!")
    print("all you have to do is pick a number between 1-10")
    print("and who ever crosses the final number 50 is the loser!")
    print("press ENTER start")
    ruleans = str(input(""))

print("Would You like to play with a friend or with a computer? Type 'friend' or 'computer'")
oppo = str(input(" "))


gameend = False

oppoans = False

while oppoans == False:
    if oppo == "computer":
        while gameend == False:
            p1 = str(input("Please Enter Your Name: "))
            print(" ")
            print("Hello",p1,"You Are Player 1!")
            print(" ")

            p2 = "Computer"

            players = [p1,p2]

            pt1 = 0
            pt2 = 0

            x = 0

            pturn = random.choice(players)

            if pturn == p1:
              pt1 += 1
            else:
              pt2 += 1

            while x < 51:
              if pt1 == 1:
                print("Its",p1 + "'s","Turn")
                numcor = "no"
                while numcor == "no":
                    xadd = gp.getpass("Please enter a number: ")
                    if not isinstance(xadd, int):
                        try:
                            int(xadd)
                            numcor = "yes"
                        except:
                            print("Please only enter a Number")
                    elif int(xadd) <= 10 and int(xadd) >= 1:
                        numcor = "yes"
                    else:
                        print("Please enter a number between 1-10")
                x = x + int(xadd)
                pt1 -= 1
                pt2 += 1
              elif pt2 == 1:
                print("Its",p2 + "'s","Turn")
                xadd = random.randint(1,10)
                x = x + xadd
                pt2 -= 1
                pt1 += 1

            if pt1 == 1:
                print(" ")
                print(" ")
                print(" ")
                print(" ")
                print(" ")
                print(p1,"WINS!!!!!!")
            elif pt2 == 1:
                print(" ")
                print(" ")
                print(" ")
                print(" ")
                print(" ")
                print(p2, "WINS!!!!!!")

            print(" ")
            print(" ")
            print(" ")
            print(" ")
            print(" ")
            print("Would You like to play again")
            playagainloop = True
            while playagainloop:
                print("type 'y' or 'n'")
                playagain = str(input(""))
                if playagain == "y" or playagain == "n":
                    if playagain == "n":
                        playagainloop = False
                        gameend = True
                    elif playagain == "y":
                        playagainloop = False
                else:
                    print("Please answer properly")
        oppoans = True
    elif oppo == "friend":
        while gameend == False:
            p1 = str(input("Please Enter Player 1s Name: "))
            print(" ")
            print("Hello",p1,"You Are Player 1!")
            print(" ")
            p2 = str(input("Please Enter Player 2s Name: "))
            print(" ")
            print("Hello",p2,"You Are Player 2!")
            print(" ")

            players = [p1,p2]

            pt1 = 0
            pt2 = 0

            x = 0

            pturn = random.choice(players)

            if pturn == p1:
              pt1 += 1
            else:
              pt2 += 1

            while x < 51:
              if pt1 == 1:
                print("Its",p1 + "'s","Turn")
                numcor = "no"
                while numcor == "no":
                    xadd = gp.getpass("Please enter a number: ")
                    if not isinstance(xadd, int):
                        try:
                            int(xadd)
                            numcor = "yes"
                        except:
                            print("Please only enter a Number")
                    elif int(xadd) <= 10 and int(xadd) >= 1:
                        numcor = "yes"
                    else:
                        print("Please enter a number between 1-10")
                x = x + int(xadd)
                pt1 -= 1
                pt2 += 1
              elif pt2 == 1:
                print("Its",p2 + "'s","Turn")
                numcor = "no"
                while numcor == "no":
                    xadd = gp.getpass("Please enter a number: ")
                    if not isinstance(xadd, int):
                        try:
                            int(xadd)
                            numcor = "yes"
                        except:
                            print("Please only enter a Number")
                    elif int(xadd) <= 10 and int(xadd) >= 1:
                        numcor = "yes"
                    else:
                        print("Please enter a number between 1-10")
                x = x + int(xadd)
                pt2 -= 1
                pt1 += 1

            if pt1 == 1:
                print(" ")
                print(" ")
                print(" ")
                print(" ")
                print(" ")
                print(p1,"WINS!!!!!!")
            elif pt2 == 1:
                print(" ")
                print(" ")
                print(" ")
                print(" ")
                print(" ")
                print(p2, "WINS!!!!!!")

            print(" ")
            print(" ")
            print(" ")
            print(" ")
            print(" ")
            print("Would You like to play again")
            playagainloop = True
            while playagainloop:
                print("type 'y' or 'n'")
                playagain = str(input(""))
                if playagain == "y" or playagain == "n":
                    if playagain == "n":
                        playagainloop = False
                        gameend = True
                    elif playagain == "y":
                        playagainloop = False
                else:
                    print("Please answer properly")
        oppoans = True
    else:
        print("Please answer properly")
