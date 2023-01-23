import random
import hangmanArt
import hangman_words
import time
# import os
# import sys,subprocess


print(hangmanArt.logo)

chosen_word=random.choice(hangman_words.word_list)

display=[]
for i in range(len(chosen_word)):
    display.append("_")
print(display)

# clear=lambda : os.system("clear") ---> to clear screen

k=7
store=[]
while k>0:
    
    print("\nremaining lives: ",k)
    if k>7:
        print("your current situation is: ")
        print(hangmanArt.stages[k])

    print("\naphabets you already used: ")
    print(store)
    guess=input("\nenter your alphabet: ").lower()

    if guess in chosen_word:
        if guess in store:
            print(f"you already used {guess}")
        else:
            print("correct !!")
            for i in range(len(chosen_word)):
                if guess==chosen_word[i]:
                    display[i]=guess
                    

        # print("\033c\033[3J") #---> to clear screen in mac
        # subprocess.call('clear',shell=True) ----> to clear screen in linux or mac ; for window use 'cls' instead of clear
        # clear()
    else:
        if guess in store:
            print(f"you already used {guess}")
        else:
            k-=1
            print(hangmanArt.stages[k])
            print("remaining lives: ",k)

            # print("\033c\033[3J")
            # subprocess.call('clear',shell=True)
            # clear()
    if guess not in store:
        store.append(guess)
        print("\nclearing screen in 1 second")
        time.sleep(1)
        
        print("\033c\033[3J") #---> to clear screen in mac

    print()
    print(display)
    if "_" not in display:
        print("CONGRATULATION !!!!")
        break

if k==0:
    print(hangmanArt.stages[0])
    print("===============================")
    print("\nANSWER :",chosen_word)
    print("\n===============================")


