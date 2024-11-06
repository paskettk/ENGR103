import matplotlib.pyplot as plt

def read_file(file_path):
    with open(file_path, 'r') as file:
        lines = file.readlines()[1:]
        grades = [list(map(float, line.strip().split(','))) for line in lines if line.strip()]
    return grades

def calculate_grade(grades):
    total = sum([grade[0] for grade in grades])
    possible = sum([grade[1] for grade in grades])
    return total / (possible) * 100

def calculate_current_grade(assignments, labs, midterms, assignment_weight, lab_weight, midterm_weight):
    assignment_grade =  calculate_grade(assignments)
    lab_grade = calculate_grade(labs)
    midterm_grade = calculate_grade(midterms)
    
    current_grade = (((assignment_grade * assignment_weight) + (lab_grade * lab_weight) + (midterm_grade * midterm_weight)) / (assignment_weight + lab_weight + midterm_weight))
    return current_grade

def required_final_score(current_grade, final_weight, letter_grade):
    required_score = (letter_grade - current_grade * (1 - final_weight)) / final_weight
    return required_score

def calcuate_required_scores(current_grade, final_weight):
    letter_grades = ["A", "A-", "B+", "B", "B-", "C+", "C", "C-", "D+", "D", "D-"]
    number_grades = [93, 90, 87, 83, 80, 77, 73, 70, 67, 63, 60]
    required_scores = {}

    for target, letter in zip(number_grades, letter_grades):
        score = required_final_score(current_grade, final_weight, target)
        if score > 100:
            required_scores[letter] = "Not possible"
        elif score < 0:
            required_scores[letter] = "Already achieved"
        else:
            required_scores[letter] = score
    return required_scores

def main():
    while True:

        user_input = input("Do you know your current grade and final weight? Respond with yes or no: ").strip().lower() # MAKES INPUT LOWERCASE AND REMOVES WHITESPACE
        if user_input == "yes":
            current_grade = float(input("Enter your current grade: ").strip())
            final_weight = float(input("Enter the weight for the final as a decimal: ").strip())
            break

        elif user_input == "no":
            assignments = 'assignments.txt'
            labs = 'labs.txt'
            midterms = 'midterms.txt'

            assignments = read_file(assignments)
            labs = read_file(labs)
            midterms = read_file(midterms)

            assignment_weight = .2
            lab_weight = .1
            midterm_weight = .4
            final_weight = .3

            current_grade = calculate_current_grade(assignments, labs, midterms, assignment_weight, lab_weight, midterm_weight)
            break

        else:
            print("Please try again")

    required_scores = calcuate_required_scores(current_grade, final_weight)

    print(f"Current grade: {current_grade:.2f}")
    for grade, score in required_scores.items():
        if score == "Not possible":
            print(f'It is not possible to get a {grade}')
        elif score == "Already achieved":
            print(f'You have already achieved a {grade}')
        else:
            print(f"To get a {grade}, you need a {score:.1f} on the final.")

main()

current_grades = [i for i in range(0, 101, 5)]
final_weight = 0.3

required_final_grades = []
for grade in current_grades:
    required_final_grade = required_final_score(grade, final_weight, 83)
    required_final_grades.append(required_final_grade)