import csv

def read_grades_from_csv(filename):
    grades = []
    with open(filename, 'r', newline='') as csvfile:
        reader = csv.DictReader(csvfile)
        for row in reader:
            grades.append(row)
    return grades

def calculate_average_grades(grades):
    subject_grades = {}
    for grade in grades:
        subject = grade['Subject']
        if subject not in subject_grades:
            subject_grades[subject] = []
        subject_grades[subject].append(float(grade['Grade']))

    average_grades = {}
    for subject, grades in subject_grades.items():
        average_grades[subject] = sum(grades) / len(grades)
    return average_grades

def write_average_grades_to_csv(filename, average_grades):
    with open(filename, 'w', newline='') as csvfile:
        fieldnames = ['Subject', 'Average Grade']
        writer = csv.DictWriter(csvfile, fieldnames=fieldnames)
        writer.writeheader()
        for subject, average_grade in average_grades.items():
            writer.writerow({'Subject': subject, 'Average Grade': average_grade})

if __name__ == "__main__":
    grades_data = read_grades_from_csv('grades.csv')
    average_grades = calculate_average_grades(grades_data)
    write_average_grades_to_csv('average_grades.csv', average_grades)