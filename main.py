# This is a sample Python script.

# Press Shift+F10 to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.

def print_hi(name):
    # Use a breakpoint in the code line below to debug your script.
    print(f'Hi, {name}')  # Press Ctrl+F8 to toggle the breakpoint.


def create_bio(age: int, name: str, is_student: bool):
    bio = name + " is " + str(age) + " and "
    if is_student:
        bio += "is a student."
    else:
        bio += "is not a student."
    print(bio)


def print_variables(age: int, name: str, is_student: bool):
    birth_year = 2023 - age

    print("Name: " + name)
    print("Age: " + str(age))
    print("Student: " + str(is_student))
    print("Birth Year: " + str(birth_year))
    create_bio(age, name, is_student)


shopping_list = ['eggs', 'lettuce', 'toilet paper']


def add_to_shopping_list(item: str):
    print(shopping_list)
    shopping_list.append(item)
    print(shopping_list)


student_info = {
    'name': 'Rafid',
    'age': 21,
    'is_student': True
}


def change_status(student: dict):
    x = student['is_student']
    if x:
        student['is_student'] = False
    else:
        student['is_student'] = True


# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    print_variables(21, "Rafid", True)
    add_to_shopping_list('butter')
    print(student_info)
    change_status(student_info)
    print(student_info)

# See PyCharm help at https://www.jetbrains.com/help/pycharm/
