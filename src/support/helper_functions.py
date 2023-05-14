from settings import LEVELS_FILE_PATH

def level_file_reader():
    """Function to read level files from a text file, has a try except
    structure to deal with levels.txt missing. 

    Returns:
        levels(nested list): Nested list with level data.
    """
    try:
        all_lines, levels, single_level = [], [], []
        with open(LEVELS_FILE_PATH, "r", encoding="utf-8") as file:
            all_lines = [(line.strip("\n")) for line in file.readlines()]
        for line in all_lines:
            if line == "-":
                levels.append(single_level)
                single_level = []
            else:
                single_level.append(line)
        return levels
    except FileNotFoundError:
        return []
