import random

digit=5

name=input("PLEASE ENTER YOUR NAMEποΈποΈ_ _ _ _ _")

print(name,"ji WELCOME TO COW AND BULL GAME πππππ")

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
                    print("BULL__ππ",bull)
                else:
                    print("you alreday used this number PLEASE TRY AGAINπ§π§π§")
            else:
                cow.append(guess)
                print("cow__ππ __possition is not matching you can reuse it",cow)

        if bull==num:
            print(name,"CONGRAGULATION DEAR you win the gameπ₯³π₯³π₯³π₯³π₯³π₯³π₯³..................")
            break
        chances-=1
        print("only",chances,"chances you have now so please play carefullyππ»ππ»ππ»...........")

    else:
        print("you run outyour tries,You losse the game")
    return bull   
check_guess()

def play_again():
    while True:
        again=input("Enter yes if you want play again else no\n yesππ»ππ»\n noππ")

        if again=="yes":
            print("Welcom",name,"for playing againππ»ππ»ππ»")
            check_guess()

        else:
            print("Thanks for playingππ»ππ»ππ»ππ»" )
            break

play_again()