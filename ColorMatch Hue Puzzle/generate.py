from collections import Counter
from itertools import cycle
import random
correct_grid = [
                #Level 8
                ["#f4f3bd", "#f3dbab", "#f1c49a", "#f2ae89", "#ef987a", "#ec806b", "#ee6a5b"],
                ["#e1e4b7", "#ded0ab", "#dbbd9b", "#d8a98f", "#d39580", "#d08075", "#cd6c66"],
                ["#ced8b5", "#c8c7a8", "#c4b49b", "#bda193", "#b88f89", "#b27e80", "#ae6d75"],
                ["#becbaf", "#b5bda8", "#acad9f", "#a69d98", "#9d8d90", "#977d89", "#8e6e83"],
                ["#a9beab", "#9fb1a5", "#98a4a2", "#8d989e", "#808a99", "#767c94", "#6e6f8e"],
                ["#96b2a4", "#8aa7a3", "#809ba2", "#7491a3", "#6786a2", "#5a7b9e", "#4e709d"],
                ["#85a79f", "#779ca2", "#6795a3", "#588ba6", "#4c82a8", "#3c7aa9", "#2f71ab"]
            ]

game_puzzle = [
                [{'movable': 0, 'color': ''}, {'movable': 0, 'color': ''}, {'movable': 0, 'color': ''}, {'movable': 0, 'color': ''}, {'movable': 0, 'color': ''}, {'movable': 0, 'color': ''}, {'movable': 0, 'color': ''}],
                [{'movable': 0, 'color': ''}, {'movable': 1, 'color': ''}, {'movable': 1, 'color': ''}, {'movable': 0, 'color': ''}, {'movable': 1, 'color': ''}, {'movable': 1, 'color': ''}, {'movable': 0, 'color': ''}],
                [{'movable': 0, 'color': ''}, {'movable': 1, 'color': ''}, {'movable': 1, 'color': ''}, {'movable': 0, 'color': ''}, {'movable': 1, 'color': ''}, {'movable': 1, 'color': ''}, {'movable': 0, 'color': ''}],
                [{'movable': 0, 'color': ''}, {'movable': 0, 'color': ''}, {'movable': 0, 'color': ''}, {'movable': 0, 'color': ''}, {'movable': 0, 'color': ''}, {'movable': 0, 'color': ''}, {'movable': 0, 'color': ''}],
                [{'movable': 0, 'color': ''}, {'movable': 1, 'color': ''}, {'movable': 1, 'color': ''}, {'movable': 0, 'color': ''}, {'movable': 1, 'color': ''}, {'movable': 1, 'color': ''}, {'movable': 0, 'color': ''}],
                [{'movable': 0, 'color': ''}, {'movable': 1, 'color': ''}, {'movable': 1, 'color': ''}, {'movable': 0, 'color': ''}, {'movable': 1, 'color': ''}, {'movable': 1, 'color': ''}, {'movable': 0, 'color': ''}],
                [{'movable': 0, 'color': ''}, {'movable': 0, 'color': ''}, {'movable': 0, 'color': ''}, {'movable': 0, 'color': ''}, {'movable': 0, 'color': ''}, {'movable': 0, 'color': ''}, {'movable': 0, 'color': ''}],
            ]
# Reset and shuffle all colors from the correct grid
all_colors = [color for row in correct_grid for color in row]
random.shuffle(all_colors)

# Separate immovable and movable color pools
immovable_colors = set([correct_grid[row_idx][col_idx]
                        for row_idx, row in enumerate(game_puzzle)
                        for col_idx, cell in enumerate(row) if cell["movable"] == 0])

movable_colors = [color for color in all_colors if color not in immovable_colors]

# Shuffle the movable colors to ensure randomness
random.shuffle(movable_colors)

# Assign colors uniquely to the grid
movable_color_iterator = iter(movable_colors)  # Iterator for unique color assignment

for row_index, row in enumerate(game_puzzle):
    for col_index, cell in enumerate(row):
        if cell["movable"] == 0:
            # Assign correct color to immovable tiles
            cell["color"] = correct_grid[row_index][col_index]
        elif cell["movable"] == 1:
            # Assign unique color to movable tiles
            cell["color"] = next(movable_color_iterator)

# Validate the result
used_colors = [cell["color"] for row in game_puzzle for cell in row]
color_counts = Counter(used_colors)
duplicates = {color: count for color, count in color_counts.items() if count > 1}
all_colors_used = set(used_colors) == set([color for row in correct_grid for color in row])

print(game_puzzle, duplicates, all_colors_used)