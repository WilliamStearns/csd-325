#William Stearns
#3-20-25
#module 1.3
#User will input a number and the program will count down the bottles of beer on the wall.


#Diplay a countdown from the number inputted by the user, changing when only one is left.
def song(bottles):
    for i in range(bottles, 1, -1):
        print(f"{i} bottles of beer on the wall, {i} bottles of beer.\nTake one down and pass it around, {i-1} bottle(s) of beer on the wall.\n")
    print("1 bottle of beer on the wall, 1 bottle of beer.\nTake one down and pass it around, 0 bottles of beer on the wall\n")
        
def main():
    while True:
        try:
            bottles = int(input("Enter number of bottles: "))
            break              
        except ValueError:
            print("Please enter a valid number.\n")
            
    if bottles > 0:
        song(bottles)

    print("Time to buy more bottles of beer.")

if __name__ == '__main__':
    main()