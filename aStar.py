def binary_search(list, value, start, end):
    if start > end: return start

    middle = (start + end) // 2
    if (list[middle]['cost'] + list[middle]['heuristic']) == value:
        return middle
    elif (list[middle]['cost'] + list[middle]['heuristic']) < value:
        return binary_search(list, value, middle + 1, end)
    else:
        return binary_search(list, value, start, middle - 1)

def add_new_state(states_avaliations, open_states, state, cost, heuristic):
    position = binary_search(states_avaliations, cost+heuristic, 0, len(open_states)-1)
    open_states.insert(position, state)
    states_avaliations.insert(position, {"cost": cost, "heuristic": heuristic})

def get_path(course, last_state):
    path = []
    while last_state:
        path.insert(0, last_state)
        last_state = course.get(last_state)
    return path

def get_blocks_misplaced(current_state, goal_state):
    return len(list(filter(lambda block: current_state[block] != goal_state[block], current_state)))

def get_possible_movements(current_state):
    free_blocks = list(filter(lambda chave: isinstance(current_state[chave], (list, tuple))
                              and current_state[chave][0] == False, current_state))
    
    movements = []
    for block in free_blocks: # Blocks to move
        if block != "M":
            for destination in free_blocks: # Places where to move
                if destination != block:
                    movements.append((block, destination))

    return movements

def move_block(current_state, movement):
    # Atualizar as informações do bloco sob o bloco movido
    if current_state[movement[0]][1] != "M":
        current_state[current_state[movement[0]][1]] = (False, current_state[current_state[movement[0]][1]][1])

    # Atualizar as informações do block movido
    current_state[movement[0]] = (False, movement[1])

    # Atualizar as informações do bloco destino
    if movement[1] != "M":
        current_state[movement[1]] = (movement[0], current_state[movement[1]][1])

    return current_state

def a_star(starting_state, goal_state, moves_costs):
    closed_states, open_states, states_avaliations= [], [], []
    
    open_states.append(starting_state)
    states_avaliations.append({"cost": 0, "heuristic": get_blocks_misplaced(starting_state, goal_state)})

    course = {}
    while open_states:
        current_state, current_state_avaliation = open_states.pop(0), states_avaliations.pop(0)
        
        if current_state == goal_state:
            return get_path(course, str(current_state))
        
        closed_states.append(current_state)

        for movement in get_possible_movements(current_state):
            next_state = move_block(current_state.copy(), movement)

            if next_state not in closed_states and next_state not in open_states:
                course[str(next_state)] = str(current_state)
                add_new_state(
                    states_avaliations,
                    open_states,
                    next_state,
                    current_state_avaliation['cost'] + moves_costs[movement[0]], # Cost
                    get_blocks_misplaced(next_state, goal_state) # Heuristic
                )

    return "NO POSSIBLE SOLUTION"