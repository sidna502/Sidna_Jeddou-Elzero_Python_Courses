# First
my_numbers = [15, 81, 5, 17, 20, 21, 13]
num2 = []
a = 0
for number in my_numbers:

    if number % 5 == 0:
        num2.append(number)
    num2.sort(reverse=True)

for number in num2:

    a += 1
    print(f'{a} => {number}')

print('All numbers printed')
print('#' * 50)

# Second

for num in range(1, 21):
    if num == 6:
        continue
    elif num == 8:
        continue
    elif num == 12:
        continue
    else:
        print(f'{str(num).zfill(2)}')
# Third
total_marks = 0
my_rank = {
    'Math': 'A',
    'Science': 'B',
    'Drawing': 'A',
    'Sport': 'C'
}
A = 100
B = 80
C = 40
for rank_key, rank_value in my_rank.items():
    if my_rank[rank_key] == "A":
        print(
            f'My rank in {rank_key} is {rank_value} and this equal {A} points')
        total_marks += A
    elif my_rank[rank_key] == 'B':
        print(
            f'My rank in {rank_key} is {rank_value} and this equal {B} points')
        total_marks += B
    elif my_rank[rank_key] == 'C':
        print(
            f'My rank in {rank_key} is {rank_value} and this equal {C} points')
        total_marks += C
print(f'Total points is {total_marks}')
# Third
students = {
    "Ahmed": {
        "Math": "A",
        "Science": "D",
        "Draw": "B",
        "Sports": "C",
        "Thinking": "A"
    },
    "Sayed": {
        "Math": "B",
        "Science": "B",
        "Draw": "B",
        "Sports": "D",
        "Thinking": "A"
    },
    "Mahmoud": {
        "Math": "D",
        "Science": "A",
        "Draw": "A",
        "Sports": "B",
        "Thinking": "B"
    }
}

A = 100
B = 80
C = 40
D = 20
total_marks = 0

# Fourth 1
for student_name in students:
    print('-' * 50)
    print(f'\"-- Student name => {student_name}\"')
    print('-' * 50)
    for student_rank in students[student_name]:
        if students[student_name][student_rank] == 'A':
            print(f'\"- {student_rank} => {A} points\"')
            total_marks += A

        elif students[student_name][student_rank] == 'B':
            print(f'\"- {student_rank} => {B} points\"')
            total_marks += B

        elif students[student_name][student_rank] == 'C':
            print(f'\"- {student_rank} => {C} points\"')
            total_marks += C
        elif students[student_name][student_rank] == 'D':
            print(f'\"- {student_rank} => {D} points\"')
            total_marks += D
    print(f'Total point for {student_name} is {total_marks}')
    total_marks = 0

# Fourth 2
for student_key, student_value in students.items():
    print('-' * 50)
    print(f'\"-- Student name => {student_key}\"')
    print('-' * 50)
    for child_student_key, child_student_value in student_value.items():
        if students[student_key][child_student_key] == 'A':
            print(f'\"- {child_student_key} => {A} points\"')
            total_marks += A

        elif students[student_key][child_student_key] == 'B':
            print(f'\"- {child_student_key} => {B} points\"')
            total_marks += B

        elif students[student_key][child_student_key] == 'C':
            print(f'\"- {child_student_key} => {C} points\"')
            total_marks += C

        elif students[student_key][child_student_key] == 'D':
            print(f'\"- {child_student_key} => {D} points\"')
            total_marks += D

    print(f'Total point for {student_key} is {total_marks}')
    total_marks = 0
