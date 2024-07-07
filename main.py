import aStar, format

initial_state = { "A": (False, "B"), "B": ("A", "M"), "C": ("D", "M"), "D": (False, "C"), "M": (False,) }
final_state = { "A": ("B", "M"), "B": ("C", "A"), "C": ("D", "B"), "D": (False, "C"), "M": (False,) }

block_costs = {"A": 1, "B": 2, "C": 2, "D": 3}


path = aStar.a_star(initial_state, final_state, block_costs)
format.print_path(path)
print(*path)