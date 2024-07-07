def define_levels(state):
    level_1, level_2, level_3, level_4 = [], [], [], []
    for block in state:
        if block != "M":
            if state[block][1] == "M":
                level_1.append(block)

                if state[block][0]:
                    level_2.append(state[block][0])

                    if state[state[block][0]][0]:
                        level_3.append(state[state[block][0]][0])

                        if state[state[state[block][0]][0]][0]:
                            level_4.append(state[state[state[block][0]][0]][0])
                        else:
                          level_4.append(" ")
                    else:
                        level_3.append(" ")
                else:
                    level_2.append(" ")
    return level_1, level_2, level_3, level_4

def print_state(state):
    level_1, level_2, level_3, level_4 = define_levels(state)
    if any(i != " " for i in level_4):
      print(*level_4)

    if any(i != " " for i in level_3):
      print(*level_3)

    if any(i != " " for i in level_2):
      print(*level_2)

    print(*level_1)

def print_path(path):
    print("Estado Inicial\n")
    print_state(eval(path[0]))
    print("--------")
    print("\n  ↓\n")

    for state in path[1:-1]:
        print_state(eval(state))
        print("--------")
        print("\n  ↓\n")

    print("Estado Final\n")
    print_state(eval(path[-1]))
    print("--------")
