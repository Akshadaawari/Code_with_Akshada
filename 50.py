#50.Implement a python program that will input student details, marks in 5 subjects and calculates the percentage scored by student.
#Requirements:
#1. The program should ask the student for name and roll number.
#Validate if name is a string and roll number is an integer, if not, show an error message saying “Invalid name/roll number” and ask for the value again after that.
#1. Once you have the name and roll number the program should ask for score in 5 subjects in order: English, Hindi, Maths, Science, Social Science
#Score must be within 1-100 otherwise show an error ‘Invalid score’ and ask for the subject score again.
#1. After getting score for all the subjects calculate the percentage of student up to 2 decimal places and show the result in following format:
#Format:
#Name: [Name]
#English: [English score]
#Hindi: [Hindi score] and similarly for other 3 subjects
#Percentage: [Percentage]
#Result: [Pass/Fail]
#If the score is under 36% show the Result as Fail else show Pass.
def get_valid_name():
    while True:
        name = input("Enter student's name: ")
        if name.isalpha(): 
            return name
        else:
            print("Invalid name. Please enter a valid name.")

def get_valid_roll_number():
    while True:
        try:
            roll_number = int(input("Enter student's roll number: "))
            return roll_number
        except ValueError:
            print("Invalid roll number. Please enter an integer value for roll number.")

def get_valid_score(subject):
    while True:
        try:
            score = int(input(f"Enter {subject} score (1-100): "))
            if 1 <= score <= 100:
                return score
            else:
                print("Invalid score. Score must be between 1 and 100.")
        except ValueError:
            print("Invalid input. Please enter an integer between 1 and 100.")

def calculate_percentage(scores):
    total_marks = sum(scores)
    percentage = (total_marks / 500) * 100  
    return round(percentage, 2)

def determine_result(percentage):
    if percentage < 36:
        return "Fail"
    else:
        return "Pass"

def main():
    
    name = get_valid_name()
    roll_number = get_valid_roll_number()
    
    
    english_score = get_valid_score("English")
    hindi_score = get_valid_score("Hindi")
    maths_score = get_valid_score("Maths")
    science_score = get_valid_score("Science")
    social_science_score = get_valid_score("Social Science")
    
   
    scores = [english_score, hindi_score, maths_score, science_score, social_science_score]
   
    percentage = calculate_percentage(scores)
    
   
    result = determine_result(percentage)
    
   
    print("\n--- Student Details ---")
    print(f"Roll no.: {roll_number}")
    print(f"Name: {name}")
    print(f"English: {english_score}")
    print(f"Hindi: {hindi_score}")
    print(f"Maths: {maths_score}")
    print(f"Science: {science_score}")
    print(f"Social Science: {social_science_score}")
    print(f"Percentage: {percentage}%")
    print(f"Result: {result}")


if __name__ == "__main__":
    main()
