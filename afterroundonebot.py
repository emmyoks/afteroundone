def player():
    __name__ = '__main__'
    import random

    global name
    name = input("Enter you name:")

    def playern():

        try:
            global num

            num = int(input("Enter your lucky number(from 1-10):"))
        except ValueError:
            print("You need to enter a valid whole number.", name.capitalize())
            playern()
        else:
            if num > 11:
                print("you need to enter a value less than or equal to '10'")
                playern()
                return

            def gnumc():
                global cnum
                cnum = random.choice(range(1, 11))
                if cnum != num:
                    return cnum
                else:
                    gnumc()
            gnumc()
            print("Computer's lucky number is:", cnum)
            print("welcome ", name.capitalize(), "your lucky number is ", num, " \n START GAME:")

            def aro():
                try:
                    x = int(input("After round one,Original panadol extra ,Otun gbede:"))
                except ValueError:
                    print("You need to enter a valid whole number.")
                    aro()
                else:
                    if x > 5:
                        print("you need to enter a value less than or equal to '5'")
                        aro()

                cx = random.choice(range(0, 6))
                sx = cx+x
                print("Computer played: ", cx, "\nSum : ", sx)
                if sx == num:
                    print("you won,hurray!!!")
                elif sx == cnum:
                    print("Computer wins,ha ha ha")
                else:
                    aro()
            aro()
    playern()


player()
