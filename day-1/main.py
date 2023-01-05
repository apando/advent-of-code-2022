
def get_max_elf_calories(filename: str) -> int:
    """
    Given an input filename, groups number of calories and returns the max number of
    calories held by a single elf.
    """
    max_calories = 0

    curr_elf_cals = 0
    input_file = open(filename, "r")
    for food_calories in input_file.readlines():
        if food_calories == "\n":
            # Empty newline means we're moving on to a new elf.
            if curr_elf_cals > max_calories:
                max_calories = curr_elf_cals
            curr_elf_cals = 0
            continue

        curr_elf_cals += int(food_calories)
    input_file.close()

    # Account for the last elf, since there may not be an explicit newline at the end
    # of the file.
    if curr_elf_cals > max_calories:
        max_calories = curr_elf_cals

    return max_calories


def get_top_three_elf_calories_total(filename: str) -> int:
    """
    Given an input filename, groups number of calories and returns total calories carried
    by the 3 elves with the most calories.
    """
    import bisect

    cals_per_elf = []
    curr_elf_cals = 0
    input_file = open(filename, "r")
    for food_calories in input_file.readlines():
        if food_calories == "\n":
            # Empty newline means we're moving on to a new elf.
            bisect.insort(cals_per_elf, curr_elf_cals)
            curr_elf_cals = 0
            continue

        curr_elf_cals += int(food_calories)
    input_file.close()

    # Account for the last elf, since there may not be an explicit newline at the end
    # of the file.
    bisect.insort(cals_per_elf, curr_elf_cals)

    return sum(cals_per_elf[-3:])


# Sanity check.
test_cals = get_max_elf_calories("test.txt")
print(f"TEST: Max calories held by an elf: {test_cals}")

# Challenge
test_cals = get_max_elf_calories("input.txt")
print(f"CHALLENGE: Max calories held by an elf: {test_cals}")

# Sanity check.
test_cals = get_top_three_elf_calories_total("test.txt")
print(f"TEST: Max calories held by top 3 elves: {test_cals}")

# Challenge
test_cals = get_top_three_elf_calories_total("input.txt")
print(f"CHALLENGE: Max calories held by top 3 elves: {test_cals}")

