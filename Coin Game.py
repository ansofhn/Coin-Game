import random
from time import sleep as wait
select=["angka","gambar"]
print("\n","="*14,"\n","GUESS THE COIN","\n","="*14,"\n")
while True:
    result=random.choice(select)
    guess=input("Guess the Coin : ")
    if guess==result:
        wait(1);print("\n",guess,end=" ");wait(0.5);print("====>",end=" ");wait(1);print(result);wait(0.5)
        print("\nWow..!! You're Guessed Right\n")
        print("="*45)
        again=input("Do You want to Continue ? (Y/N): ")
        if again == 'N' or again=='n'or again=='no'or again=='NO':
            print("\nProgram Ends, Thank you for using this program")
            break
    else:
        wait(1);print("\n",guess,end=" ");wait(0.5);print("====>",end=" ");wait(1);print(result);wait(0.5)
        print("\nYou're Guess is Wrong !!\nPlease Try Again\n")