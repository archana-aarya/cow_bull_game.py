import random

digit=5

name=input("PLEASE ENTER YOUR NAME🖋️🖊️_ _ _ _ _")

print(name,"ji WELCOME TO COW AND BULL GAME 💃💃💃💃💃")

def Secret_number():
    number=list(range(10))
    random.shuffle(number)
    return number
print(Secret_number())

    # test_list = [1, 4, 5, 6, 3]
#     res = random.sample(number, len(number))
#     return res
# print (Secret_number())

def clues():
    numbers=Secret_number()
    secret_num=[]
    for i in range(digit):
        secret_num.append(numbers[i])
    return(secret_num)

def check_guess():
    bull=[]
    cow=[]
    num=clues()
    print(num)
    i=0
    chances=10
    while chances>0:
        guess=int(input("enter your guess="))
        position=int(input("enter the position of your number="))

        if guess in num:
            index=num.index(guess)

            if index==position:
                if guess not in bull:
                    bull.insert(index,guess)
                    print("BULL__🐂🐂",bull)
                else:
                    print("you alreday used this number PLEASE TRY AGAIN🧐🧐🧐")
            else:
                cow.append(guess)
                print("cow__🐄🐄 __possition is not matching you can reuse it",cow)

        if bull==num:
            print(name,"CONGRAGULATION DEAR you win the game🥳🥳🥳🥳🥳🥳🥳..................")
            break
        chances-=1
        print("only",chances,"chances you have now so please play carefully👍🏻👍🏻👍🏻...........")

    else:
        print("you run outyour tries,You losse the game")
    return bull   
check_guess()

def play_again():
    while True:
        again=input("Enter yes if you want play again else no\n yes👍🏻👍🏻\n no👎👎")

        if again=="yes":
            print("Welcom",name,"for playing again👍🏻👍🏻👍🏻")
            check_guess()

        else:
            print("Thanks for playing🙏🏻🙏🏻🙏🏻🙏🏻" )
            break

play_again()