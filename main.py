# 5 1 2 1 ==> 5 pizzas, 1 team of two, 2 teams of three, and 1 team of four
# 3 onion pepper olive ==> Pizza 0 has the given 3 ingredients
# 3 mushroom tomato basil ==> Pizza 1 has the given 3 ingredients
# 3 chicken mushroom pepper ==> Pizza 2 has the given 3 ingredients
# 3 tomato mushroom basil ==> Pizza 3 has the given 3 ingredients
# 2 chicken basil ==> Pizza 4 has the given 2 ingredients

# [{'pizza_id': 3, 'total_no_of_ing': 3, 'ingredients': {'tomato', 'basil', 'mushroom'}},
# {'pizza_id': 2, 'total_no_of_ing': 3, 'ingredients': {'pepper', 'chicken', 'mushroom'}},
# {'pizza_id': 1, 'total_no_of_ing': 3, 'ingredients': {'tomato', 'basil', 'mushroom'}},
# {'pizza_id': 0, 'total_no_of_ing': 3, 'ingredients': {'onion', 'olive', 'pepper'}},
# {'pizza_id': 4, 'total_no_of_ing': 2, 'ingredients': {'basil', 'chicken'}}]

import random

total_pizza = 0
team_of_2 = 0
team_of_3 = 0
team_of_4 = 0


def logic(total_pizza, count_of_teams, team_type):
    solution_team = {"2": 0, "3": 0, "4": 0}

    for j in range(count_of_teams[0]):
        if total_pizza >= 2:
            total_pizza -= 2
            solution_team['2'] += 1
        else:
            break

    for j in range(count_of_teams[1]):
        if total_pizza >= 3:
            total_pizza -= 3
            solution_team['3'] += 1
        else:
            break

    for j in range(count_of_teams[2]):
        if total_pizza >= 4:
            total_pizza -= 4
            solution_team['4'] += 1
        else:
            break

    # print(solution_team)
    return solution_team


def solution_fun(solution_team, pizzas, f):
    print(solution_team)
    new_data = sorted(pizzas, key=lambda k: len(k['ingredients']))[::-1]

    solution = {"2": [], "3": [], "4": []}
    count_1 = len(new_data[0]['ingredients'])

    random.shuffle(new_data)

    # <-------------------  team_of_4 --------------------->

    for r in range(solution_team['4']):
        # print(r)
        solution["4"].append(new_data[0]['pizza_id'])
        # Take first pizza ing.
        temp = new_data[0]['ingredients']
        # Remove first element
        new_data.pop(0)

        c = 3

        while c > 0:
            dic1 = {}
            flag = False
            for k in range(count_1 + 1):
                dic1[k] = []
            for j in range(0, len(new_data)):
                dic1[len(temp.intersection(
                    new_data[j]['ingredients']))].append(
                        new_data[j]['pizza_id'])
                if len(temp.intersection(new_data[j]['ingredients'])) == 0:
                    solution["4"].append(new_data[j]['pizza_id'])
                    new_data.pop(j)
                    c = c - 1
                    flag = True
                    break
            if not flag:
                for k in range(1, count_1 + 1):
                    if len(dic1[k]) != 0 and c > 0:
                        value = dic1[k].pop(
                            0)  # pop dic1[1] = [2, 3] etc 2 one
                        solution["4"].append(value)
                        new_data = [
                            x for x in new_data
                            if not (value == x.get('pizza_id'))
                        ]
                        c = c - 1
                        break

    print("Team 4 over")

    random.shuffle(new_data)

    # new_data = sorted(new_data, key=lambda k: len(k['ingredients']))[::-1]
    # print("Sort Done")
    # count_1 = len(new_data[0]['ingredients'])

    # <-------------------  team_of_3 --------------------->

    for q in range(solution_team['3']):
        # print(q)
        solution["3"].append(new_data[0]['pizza_id'])
        # Take first pizza ing.
        temp = new_data[0]['ingredients']
        # print(count)
        # Remove first element
        new_data.pop(0)

        c = 2

        while c > 0:
            dic1 = {}
            flag = False
            for k in range(count_1 + 1):
                dic1[k] = []
            for j in range(0, len(new_data)):
                dic1[len(temp.intersection(new_data[j]['ingredients']))].append(new_data[j]['pizza_id'])
                if len(temp.intersection(new_data[j]['ingredients'])) == 0:
                    solution["3"].append(new_data[j]['pizza_id'])
                    new_data.pop(j)
                    c = c - 1
                    flag = True
                    break
            if not flag:
                for k in range(1, count_1 + 1):
                    if len(dic1[k]) != 0 and c > 0:
                        value = dic1[k].pop(
                            0)  # pop dic1[1] = [2, 3] etc 2 one
                        solution["3"].append(value)
                        new_data = [
                            x for x in new_data
                            if not (value == x.get('pizza_id'))
                        ]
                        c = c - 1
                        break

    print("Team 3 over")

    random.shuffle(new_data)
    # new_data = sorted(new_data, key=lambda k: len(k['ingredients']))[::-1]
    # print("Sort Done")
    # count_1 = len(new_data[0]['ingredients'])

    # <-------------------  team_of_2 --------------------->

    for p in range(solution_team['2']):
        # print(p)
        solution["2"].append(new_data[0]['pizza_id'])
        # Take first pizza ing.
        temp = new_data[0]['ingredients']
        # Remove first element
        new_data.pop(0)

        c = 1

        while c > 0:
            dic1 = {}
            flag = False
            for k in range(count_1 + 1):
                dic1[k] = []
            for j in range(0, len(new_data)):
                dic1[len(temp.intersection(
                    new_data[j]['ingredients']))].append(
                        new_data[j]['pizza_id'])
                if len(temp.intersection(new_data[j]['ingredients'])) == 0:
                    solution["2"].append(new_data[j]['pizza_id'])
                    new_data.pop(j)
                    c = c - 1
                    flag = True
                    break
            if not flag:
                for k in range(1, count_1 + 1):
                    if len(dic1[k]) != 0 and c > 0:
                        value = dic1[k].pop(
                            0)  # pop dic1[1] = [2, 3] etc 2 one
                        solution["2"].append(value)
                        new_data = [
                            x for x in new_data
                            if not (value == x.get('pizza_id'))
                        ]
                        c = c - 1
                        break

    print("Team 2 over")

    # print(new_data)
    # print(solution)
    print("2 ----> ", str(len(solution['2'])))
    print("3----> ", str(len(solution['3'])))
    print("4 ----> ", str(len(solution['4'])))

    output = ""
    total_no_of_teams = solution_team['2'] + solution_team[
        '3'] + solution_team['4']
    output += str(total_no_of_teams) + '\n'
    for key, value in solution.items():
        if len(value) > 0 and key == '2':
            s = ""
            for i in range(0, len(value) - 1, 2):
                s = f"{value[i]} {value[i+1]}"
                output += f"{key} {s}\n"

        elif len(value) > 0 and key == '3':
            s = ""
            for i in range(0, len(value) - 2, 3):
                s = f"{value[i]} {value[i+1]} {value[i+2]}"
                output += f"{key} {s}\n"

        elif len(value) > 0 and key == '4':
            s = ""
            for i in range(0, len(value) - 3, 4):
                s = f"{value[i]} {value[i+1]} {value[i+2]} {value[i+3]}"
                output += f"{key} {s}\n"

    with open(f"./outputs/{f}", 'w') as file:
        file.write(output)


file_list = [
    "a_example", "b_little_bit_of_everything.in", "c_many_ingredients.in",
    "d_many_pizzas.in", "e_many_teams.in"
]

# file_list = [
#     "c_many_ingredients.in"
# ]

for f in file_list:
    with open(f"./inputs/{f}") as file:
        data = file.readlines()
        total_pizza = int(data[0].split(" ")[0])
        team_of_2 = int(data[0].split(" ")[1])
        team_of_3 = int(data[0].split(" ")[2])
        team_of_4 = int(data[0].split(" ")[3])
        pizzas = []

        count = 0

        for d in data[1:]:
            total_no_of_ing = int(d[0])
            l = set(d.strip().split(" ")[1:])
            dic = {
                "pizza_id": count,
                "total_no_of_ing": total_no_of_ing,
                "ingredients": l
            }

            pizzas.append(dic)
            count += 1

        count_of_teams = [team_of_2, team_of_3, team_of_4]
        team_type = [2, 3, 4]
        solution_teams = logic(total_pizza, count_of_teams, team_type)
        solution_fun(solution_teams, pizzas, f)
