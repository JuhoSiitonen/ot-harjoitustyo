
def level_file_reader():
    """Function to read level files from a text file. 

    Returns:
        levels(nested list): Nested list with level data.
    """
    
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
