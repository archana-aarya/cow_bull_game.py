print("I will generate a number, and you have to guess the numbers four digit at a time.🗒️🗒️🗒️")
print("For every number in the wrong place, you get a cow🐄🐄🐄.\nFor every one in the right place, you get a bull🐂🐂🐂.")

import random
def get_Digits(num):
    return [int(i) for i in str(num)]   
def no_Duplicates(num):
    num_list = get_Digits(num)
    if len(num_list) == len(set(num_list)):
        return True
    else:
        return False

def generate_Num():
    while True:
        num = random.randint(1000,9999)
        if no_Duplicates(num):
            print(num)
            return num
def num_Of_Bulls_Cows(num,guess):
    bull_cow = [0,0]
    num_list = get_Digits(num)
    guess_list = get_Digits(guess)
    for i,j in zip(num_list,guess_list):
        if j in num_list:
            if j == i:
                bull_cow[0] += 1
            else:
                bull_cow[1] += 1
    return bull_cow
      
num = generate_Num()
tries =int(input('Enter number of tries: '))
while tries > 0:
    guess = int(input("Enter your guess: "))
      
    if not no_Duplicates(guess):
        print("Number should not have repeated digits. TRY AGAIN 👎.")
        continue
    if guess < 1000 or guess > 9999:
        print("Enter 4 digit number only. TRY AGAIN 👎.")
        continue
      
    bull_cow = num_Of_Bulls_Cows(num,guess)
    print(f"{bull_cow[0]} bulls, {bull_cow[1]} cows")
    tries -=1 
      
    if bull_cow[0] == 4:
        print("You guessed right!🥳🥳🥳🥳🥳")
        break
else:
    print(f"You ran out of tries. Number was👉🏻👉🏻👉🏻👉🏻 {num}")