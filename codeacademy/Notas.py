lloyd = {
    "name": "Lloyd",
    "homework": [90.0, 97.0, 75.0, 92.0],
    "quizzes": [88.0, 40.0, 94.0],
    "tests": [75.0, 90.0]
}
alice = {"name": "Alice", "homework": [100.0, 92.0, 98.0, 100.0], "quizzes": [82.0, 83.0, 91.0], "tests": [89.0, 97.0]}
tyler = {"name": "Tyler", "homework": [0.0, 87.0, 75.0, 22.0], "quizzes": [0.0, 75.0, 78.0], "tests": [100.0, 100.0]}

students = [lloyd, alice, tyler]


def average(numbers):
    total = float(sum(numbers) / len(numbers))
    return total


def get_average(student):
    homework = average(student["homework"])
    quizzes = average(student["quizzes"])
    tests = average(student["tests"])

    grade = 0.1 * homework + 0.3 * quizzes + 0.6 * tests
    return grade


def get_letter_grade(score):
    if score >= 90:
        return "A"
    elif score >= 80:
        return "B"
    elif score >= 70:
        return "C"
    elif score >= 60:
        return "D"
    else:
        return "F"


def get_class_average(class_list):
    results = []
    for student in class_list:
        a = get_average(student)
        results.append(a)
    return average(results)


for student in students:
    score = get_letter_grade(get_average(student))
    print("\n", student["name"])
    print("homework: ", student["homework"])
    print("quizzes: ", student["quizzes"])
    print("tests: ", student["tests"])
    print("Score: ", score, "\n")

class_average = get_class_average(students)
class_grade = get_letter_grade(class_average)
print("Class Average: ", class_average, "\nClass Grade: ", class_grade)
