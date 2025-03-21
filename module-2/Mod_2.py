#William Stearns
#CH2_Prg1.py
#This program will calculate remaing credits for the program of study.


#input
def get_input(studName, degree, creditComp):
    
    studName = input("Enter the student name: ")
    degree = input("Enter the name of the degree program: ")
    creditComp =  int(input("Enter the number of credits completed: "))
    return studName, degree, creditComp
#process
def calculate_remaining_credits(creditComp):
    DEGREE_CREDITS = 64
    return DEGREE_CREDITS - creditComp

def main():
    #input
    studName, degree, creditComp = get_input("Enter the student name: ", "Enter the name of the degree program: ", "Enter the number of credits completed: ")

    #process
    credLeft = calculate_remaining_credits(creditComp)

    #output
    print("Pass'em State College")
    print(f"{studName} is in the {degree} program and has {credLeft:.1f} credits left to graduate.")
if __name__ == "__main__":
    main()