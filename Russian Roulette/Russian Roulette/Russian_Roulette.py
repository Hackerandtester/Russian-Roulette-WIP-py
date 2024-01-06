
import random



def Tutorial():
        print('Welcome to "German Roulette" (For copy right reasons)')
        print("To start, type a number... \nif the number is equaled to the revolver chamber that contains a round.. \nYOU DIE... \nor if it doesnt, you live. (Game is WIP) ")
Tutorial()

def Main():
    while True:
        try:
            
            Bullet = random.randint(1, 8)
            
            Number = float(input("Number:"))
            if (Number > 8):
                print("Invalid Number, Pick a number 1-8 \n------------------------------")
                Main()
            elif Number == Bullet:
                print("you have died")
            else:
                print("You live")

            continue_question = input("Do you wish to continue?: \n Y for Yes \n N for No \n")
            if continue_question == "n" or continue_question == "N":
                print("Good game!")
                break
            elif continue_question == "Y" or continue_question == "y":
                print("------------------------------")
        
        except:
            print("Invalid input try again \n------------------------------")

Main()

    
   




