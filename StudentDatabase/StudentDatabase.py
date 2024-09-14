import random

# Generate a list of 50 students and save it to a txt file
def generate_students():
    first_names = ["John", "Jane", "Bob", "Alice", "Mike", "Emily", "Tom", "Lily", "James", "Sophia"]
    last_names = ["Doe", "Smith", "Johnson", "Williams", "Jones", "Brown", "Davis", "Miller", "Wilson", "Moore"]
    majors = ["Business", "Computer Science", "Engineering", "Math", "Physics", "Biology", "Economics", "Finance", "Marketing", "Accounting"]

    with open("students.txt", "w") as f:
        for i in range(50):
            student_id = 1000 + i
            first_name = random.choice(first_names)
            last_name = random.choice(last_names)
            date_of_birth = f"{random.randint(1990, 2005)}-{random.randint(1, 12):02}-{random.randint(1, 28):02}"
            major = random.choice(majors)
            f.write(f"{student_id}, \"{first_name}\", \"{last_name}\", \"{date_of_birth}\", \"{major}\"\n")

# Read the data from the txt file
def read_students():
    students = []
    with open("students.txt", "r") as f:
        for line in f.readlines():
            student_id, first_name, last_name, date_of_birth, major = line.strip().split(", ")
            student_id = int(student_id)
            first_name = first_name.strip("\"")
            last_name = last_name.strip("\"")
            date_of_birth = date_of_birth.strip("\"")
            major = major.strip("\"")
            students.append((student_id, first_name, last_name, date_of_birth, major))
    return students

class Student:
    def __init__(self, student_id, first_name, last_name, date_of_birth, major):
        self.student_id = student_id
        self.first_name = first_name
        self.last_name = last_name
        self.date_of_birth = date_of_birth
        self.major = major

class Node:
    def __init__(self, student):
        self.student = student
        self.left = None
        self.right = None

class BinarySearchTree:
    def __init__(self):
        self.root = None

    def insert(self, student):
        if self.root is None:
            self.root = Node(student)
        else:
            self._insert(self.root, student)

    def _insert(self, node, student):
        if student.student_id < node.student.student_id:
            if node.left is None:
                node.left = Node(student)
            else:
                self._insert(node.left, student)
        else:
            if node.right is None:
                node.right = Node(student)
            else:
                self._insert(node.right, student)

    def search(self, student_id):
        return self._search(self.root, student_id)

    def _search(self, node, student_id):
        if node is None or node.student.student_id == student_id:
            return node
        if student_id < node.student.student_id:
            return self._search(node.left, student_id)
        return self._search(node.right, student_id)

# Generate a list of 50 students and save it to a txt file
generate_students()

# Read the data from the txt file
students = read_students()

# Create a binary search tree
tree = BinarySearchTree()
for student in students:
    tree.insert(Student(*student))

while True:
    try:
        student_id = int(input("Enter a student ID (4 digits, starts with 10): "))
        if len(str(student_id)) == 4 and str(student_id).startswith("10"):
            break
        else:
            print("Please enter a 4 digit number that starts with 10.")
    except ValueError:
        print("Invalid input. Please enter a number.")

# Search for a student
result = tree.search(student_id)
if result:
    print("Student ID:", result.student.student_id)
    print("First Name:", result.student.first_name)
    print("Last Name:", result.student.last_name)
    print("Date of Birth:", result.student.date_of_birth)
    print("Major:", result.student.major)
else:
    print("Student not found")

