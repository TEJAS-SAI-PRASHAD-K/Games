def winning(m,n):

    # numbering {1:"ROCK",2:"PAPER",3:"SCISSORS"}

    while (m==1 and n==2) and (m==2 and n==1):
        if m==1 and n==2:
            print("USER : ROCK VS COMPUTER : PAPER")
            print("COMPUTER WINS USING PAPER")
            # return comp+=1
        elif m==2 and n==1:
            print("USER : PAPER VS COMPUTER : ROCK")
            print("USER WINS USING PAPER")
            # return user+=1
    while (m==1 and n==3) and (m==3 and n==1):
        if m==1 and n==3:
            print("USER : ROCK VS COMPUTER : SCISSORS")
            print(" USER WINS USING ROCK")
            # return user+=1
        elif m==3 and n==1:
            print("USER : SCISSORS VS COMPUTER : ROCK")
            print("COMPUTER WINS USING ROCK")
            # return comp+=1
    while (m==2 and n==3) and (m==3 and n==2):
        if m==2 and n==3:
            print("USER : PAPER VS COMPUTER : SCISSORS")
            print("COMPUTER WINS USING SCISSORS")
            # return comp+=1
        elif m==3 and n==2:
            print("USER : SCISSORS VS COMPUTER : PAPER")
            print("USER WINS USING SCISSORS")
            # return user+=1
            

import random

brk=False

y=3
for i in range(y):
    if brk:
        break
    else:
        x=int(input("Enter the choice:"))
        print("1 -- ROCK")
        print("2 -- PAPER")
        print("3 -- SCISSORS")

        rd=random.randint(1,3)

        comp=1
        user=2

        if x==rd:
            print("DRAW")
            break
        else:
            x=winning(x,rd)
            if user==2 or comp==2:
                brk=True
                break
        

