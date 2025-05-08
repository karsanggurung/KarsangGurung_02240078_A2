import random 
# import re
# Guess_The_Number_Game
x = 1
y = 100

# Rock_Paper_Scissors_game
options = ('rock', 'paper', 'scissor')

# Trivia_Quize_game
a = 3
b = 4
number_player_in_a_team = 11 
king_of_football = "pele"
most_popular_bhutnese_channel = "bbs"
award = 2022

# Pokemon_Binder_Game
least_pokedex = 0
Highest_pokedex = 1025
pokedex_binder = []
#view placement of pokemon binder
def position(num):
    num=num-1
    page=(num//64)+1
    row=((num%64)//8)+1
    column= ((num%64)%8)+1
    return (page, row, column)

while True:
    print("welcome to the game!")
    print("menu")
    print("1. guess_number_game.")
    print("2. rock_paper_scissor_game.")
    print("3. Trivia Quize")
    print("4. Pokemon binder")
    print("6. Exit program.")
    
    choice = int(input("select the game u want to play: "))
    if choice == 1:
        Your_Score = 0
        user_input = input("enter the number (1-100) : ")
        computer = random.randint(x, y)
        if user_input == computer:
         Your_Score = Your_Score + 10
        else:
            print("try again")
            print(f"your score is : {Your_Score}")
            continue
    elif choice == 2:
        Score2 = 0
        while(True):
            user_choice = input("enter your choice [Rock, Paper,Scissor, Quit] : ").lower()
            computer = random.choices(options)[0]
            youWin="You Win"
            
            if user_choice[0]=="q":break
            
            if user_choice[0] == computer[0]:
                youWin="Tie"
                
            elif (user_choice[0]=="p" and computer=="scissor") or (user_choice[0]=="s" and computer=="rock") or (user_choice[0]=="r" and computer=="paper"):
                youWin="You Lose"
            else:
                Score2 = Score2+5
            print(f"bot: {computer}")
            print(f"user: {user_choice}")
            print(youWin)
        print(f"Thanyou for playing game2\nYour Score: {Score2}")
    elif choice == 3:
        Your_Score = 0
        while True:
            print("categories")
            print("1. maths")
            print("2. soccer")
            print("3. Media")
            print("4. quit")
            interest = int(input("enter your choice: "))  
            if interest == 1:
                print("what is a + b if a = 3 and b = 4?")
                print("a.3  b.4  c.5  d.7 ")
                ans = int(input("enter your ans: "))
                result = (a + b)
                if ans == result :
                    Your_Score = Your_Score + 5
                    print("correct answer")
                else:
                    print("incorrect")
                print("what is a*b (a = 3, b = 4)")
                print("a.4 b.3 c.5 d.12")
                ans = int(input("enter your ans: "))
                correct_ans = (a * b)
                if ans == correct_ans:
                    Your_Score = Your_Score + 5
                    print("correct answer")
                    print("you have completed this you can try playing other games")
                else:
                    print("incorrect")
                    
                
            elif interest == 2:
                print("how many player should be there in a soccer team?")
                print("a.8 b.9 c.10 d.11")
                ans = int(input("enter ur ans: "))
                if ans == number_player_in_a_team :
                    Your_Score = Your_Score + 6
                    print("you are good at this")
                elif ans != number_player_in_a_team:
                    print("wrong ans")
                else:
                    print("invalid response")
                print("who is known as the king of football")
                print("a.Cristiano Ronaldo")
                print("b.lionel Messi")
                print("c.Pele")
                print("d.Maradona")
                ans = input("enter his name : ")
                if ans == king_of_football :
                    Your_Score = Your_Score + 6
                    print("you are good at this")
                elif ans != king_of_football:
                    print("wrong ans")
                else:
                    print("invalid response")
            elif interest == 3:
                print("most popular bhutnese channel.")
                print("a.bbc b.NDTV c.Samuah d.bbs")
                ans = str(input("enter your ans: "))
                if ans == most_popular_bhutnese_channel:
                    Your_Score = Your_Score + 5
                    print("great")
                elif ans != most_popular_bhutnese_channel:
                    print("wrong ans")
                else:
                    print("invalid response")
                print("when did Samuh got its Award")
                print("a.2021 b.2022 c.2023 d.2020")
                ans = int(input("enter your answer : "))
                if ans == award:
                    Your_Score = Your_Score + 5
                    print("great")
                elif ans != most_popular_bhutnese_channel:
                    print("wrong ans")
                else:
                    print("invalid response")
            print(f"your score: {Your_Score}")
            print("hooray! you have completed this level")
            break
        
    elif choice == 4:   
        while True:
            print("Main Menu: ") 
            print("1. Add pokemon card") 
            print("2. Reset binder") 
            print("3. view placement")
            
            option = int(input("what are you looking for: "))
        
            if option == 1:
                pokedex = int(input("which podex would you like to add?: "))
                pokedex_binder.append(pokedex)
                pokedex_binder= bubble_sort(pokedex_binder.copy())#rearranging the pokedwx in accending order of pokedex number
                
            elif option == 2:
                your_confirmation = input("confirm the command to proceed (yes/no) : ")
                if your_confirmation == "yes":
                    pokedex_binder.clear() 
                    print(pokedex_binder)
                    
            elif option == 3:
                feature=int(input("1. all\n 2. Selective:  "))
                
                if feature==1:
                    for i in pokedex_binder:
                        page,row,column= position(i)
                        print(f"pokedex number: {i}")
                        print(f"Page: {page}")
                        print(f"row: {row}")
                        print(f"Column: {column}")
                elif feature==2:
                    pokedex = int(input("enter the pokedex you want to view the placement"))
                    if pokedex in pokedex_binder:
                        page,row,column= position(pokedex)
                        print(f"pokedex number: {i}")
                        print(f"Page: {page}")
                        print(f"row: {row}")
                        print(f"Column: {column}")
            else:
                exit 
    elif choice == 5:
        print("thank you for playing!")
        break
    else:
        print("try again")
        
