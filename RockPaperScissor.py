def winning(m,n):

    # numbering {1:"ROCK",2:"PAPER",3:"SCISSORS"}
        if m==1 and n==2:
            print("USER : ROCK VS COMPUTER : PAPER")
            print("COMPUTER WINS USING PAPER \n")
            return "comp"
        elif m==2 and n==1:
            print("USER : PAPER VS COMPUTER : ROCK")
            print("USER WINS USING PAPER \n")
            return "user"
        elif m==1 and n==3:
            print("USER : ROCK VS COMPUTER : SCISSORS")
            print(" USER WINS USING ROCK \n")
            return "user"
        elif m==3 and n==1:
            print("USER : SCISSORS VS COMPUTER : ROCK")
            print("COMPUTER WINS USING ROCK \n")
            return "comp"
        elif m==2 and n==3:
            print("USER : PAPER VS COMPUTER : SCISSORS")
            print("COMPUTER WINS USING SCISSORS \n")
            return "comp"
        elif m==3 and n==2:
            print("USER : SCISSORS VS COMPUTER : PAPER")
            print("USER WINS USING SCISSORS \n")
            return "user"
            

import random

brk=True
comp=0
user=0

while brk:    
        print("1 -- ROCK")
        print("2 -- PAPER")
        print("3 -- SCISSORS")
        x=int(input("Enter the choice:"))
        print("\n")
        
        rd=random.randint(1,3)

        if x==rd:
            print("-----DRAW----- \n")
            print("-----PLAY AGAIN----- \n")
        else:
            y=winning(x,rd)
            if y=="comp":
                 comp+=1
            else:
                 user+=1
            if user==2 or comp==2:
                brk=True
                break
        

