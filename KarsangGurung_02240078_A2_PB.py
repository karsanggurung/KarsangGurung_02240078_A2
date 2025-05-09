# Pokemon_Binder_Game
least_pokedex = 1
Highest_pokedex = 1025
pokedex_binder = []

def bubble_sort(pokedex_binder):
    n = len(pokedex_binder)
    for i in range(n):
        for j in range(0, n - i - 1):
            if pokedex_binder[j] > pokedex_binder[j + 1]:
                pokedex_binder[j], pokedex_binder[j + 1] = pokedex_binder[j + 1], pokedex_binder[j]
    return pokedex_binder
def position(num):
    num=num-1
    page=(num//64)+1
    row=((num%64)//8)+1
    column= ((num%64)%8)+1
    return (page, row, column)
while True:
    print("Main Menu: ") 
    print("1. Add pokemon card") 
    print("2. Reset binder") 
    print("3. view placement")
            
    option = int(input("what are you looking for: "))
        
    if option == 1:
        pokedex = int(input("which podex would you like to add?: "))
        if pokedex < least_pokedex and pokedex > Highest_pokedex :
            print("does not exist")
        else:
            pokedex_binder.append(pokedex)
            pokedex_binder= bubble_sort(pokedex_binder.copy())#rearranging the pokedwx in accending order of pokedex number
        print(pokedex_binder)        
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
            pokedex = int(input("enter the pokedex you want to view the placement: "))
            for pokedex in pokedex_binder:
                page,row,column= position(pokedex)
                print(f"pokedex number: {i}")
                print(f"Page: {page}")
                print(f"row: {row}")
                print(f"Column: {column}")