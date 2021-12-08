# First
# my_numbers = [15, 81, 5, 17, 20, 21, 13]
# num2 = []
# a = 0
# for number in my_numbers:

#     if number % 5 == 0:
#         num2.append(number)
#     num2.sort(reverse=True)

# for number in num2:

#     a += 1
#     print(f'{a} => {number}')

# print('All numbers printed')
# print('#' * 50)

# Second

# for num in range(1, 21):
#     if num == 6:
#         continue
#     elif num == 8:
#         continue
#     elif num == 12:
#         continue
#     else:
#         print(f'{str(num).zfill(2)}')
# Third
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
    elif my_rank[rank_key] == 'B':
        print(
            f'My rank in {rank_key} is {rank_value} and this equal {B} points')

    elif my_rank[rank_key] == 'C':
        print(
            f'My rank in {rank_key} is {rank_value} and this equal {C} points')
# print(my_rank['Math'])
