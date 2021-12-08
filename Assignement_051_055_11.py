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
