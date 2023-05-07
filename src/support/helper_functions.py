def level_file_reader():
    all_lines, levels, single_level = [], [], []
    with open("src/data/levels.txt") as f:
        [all_lines.append(line.strip("\n")) for line in f.readlines()]
    for line in all_lines:
        if line == "-":
            levels.append(single_level)
            single_level = []
        else:
            single_level.append(line)
    return levels

def highscore_list_reader():
    all_lines = []
    with open("src/data/highscores.txt", "w+") as f:
        [all_lines.append(line.strip("\n")) for line in f.readlines()]
    return all_lines