import random
def cow_bull():
    print("WELCOME TO THE GAME")
    print("ENTER exit to exit and number to continue")
    s=random.randint(1000,9999)
    s1=str(s)
    guesses=0
    cow=0
    bull=0
    while cow!=4:
        cow=0
        bull=0
        guesses+=1
        s2=str((input("Enter: ")))
        if s2=="exit":
            print("You chose to exit")
            break
        else:
            for i in range(len(s1)):
                if s1[i]==s2[i]:
                    cow+=1
                elif s1[i] in s2:
                    bull+=1
            print(f"Cows:{cow} & Bulls:{bull}")
            if cow!=4:
                 print("Please try again")
        
        if s2=="exit":
            pass
        else:
            print(f"Congratulations! You found the number {s2} with {guesses} guesses.")
    
    
        

cow_bull()


