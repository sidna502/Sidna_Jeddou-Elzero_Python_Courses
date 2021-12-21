# First
# def calculate(A, B, op='unknown'):
#     if op.lower() == 'add' or op.lower() == 'a':
#         print(A+B)
#     elif op.lower == 'substrct' or op.lower() == 's':
#         print(A-B)
#     elif op.lower() == 'multiply' or op.lower() == 'm':
#         print(A*B)
#     elif op.lower() == 'unknown' or op.lower() == 'u':
#         print(A+B)

#     else:
#         print('Wrong operation')


# calculate(10, 20, 'aDD')
# calculate(10, 20, 's')
# calculate(10, 20, 'm')
# calculate(10, 20, 'n')
# calculate(10, 20)
# Second


# def addition(*numbers):
#     n = 0
#     for num in numbers:
#         if num == 10:
#             continue
#         elif num == 5:
#             n -= 5

#         n += num

#     print(n)


# addition(10, 50, 50, 5, 15)

# # Third

def show_skills(name, *skills):
    if len(skills) == 0:
        print(f'Hello {name} you have no skill')
    else:
        print(f'Hello {name} your skill is: ')
        for skill in skills:
            print(f'\"- {skill}\"')


show_skills('Sidna', 'Html', 'Css', 'Python')
show_skills('Sidna')

# Fourth
# def say_hello(name='unknown', age='unknown', country='unknown'):
#     print(
#         f'Hello {name.capitalize().strip()} your age is {age} years old and your country is {country.capitalize()}')


# say_hello('sidna', 30, 'mauritania')
