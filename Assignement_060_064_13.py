# First
def get_score(**skills):
    print(type(skills))
    for skill, value in skills.items():
        print(f'\"{skill} => {value}\"')


get_score(Math=90, Science=80, Language=70)
get_score(Logic=70, Problems=60)

# Second


def get_people_scores(name='', **skills):
    if len(name) == 0:
        for skill, value in skills.items():
            print(f'\"{skill} => {value}\"')
    elif len(skills) == 0:

        print(f'Hello {name} you have no score ')
    else:
        print(f'Hello {name} this your score: ')
        for skill, value in skills.items():
            print(f'\"{skill} => {value}\"')


get_people_scores("Osama", Math=90, Science=80, Language=70)
print('#' * 50)
get_people_scores("Mahmoud", Logic=70, Problems=60)
print('#' * 50)
get_people_scores('Sidna')
print('#' * 50)
get_people_scores(Logic=70, Problems=60)

# Third
scores_list = {
    'Matth': 90,
    'Science': 80,
    'Language': 70

}


def get_the_scores(*name, **scores_list):
    if len(name) == 0:
        for skill, value in scores_list.items():
            print(f'\"{skill} => {value}\"')
    elif len(scores_list) == 0:
        print(f'Hello {name} you have no Score to show ')
    else:
        print(f'Hello {name} this is your Score')
        for skill, value in scores_list.items():
            print(f'\"{skill} => {value}\"')


get_the_scores("Sidna", **scores_list)
print('#' * 50)
get_the_scores("Sidna")
print('#' * 50)
get_the_scores(**scores_list)
