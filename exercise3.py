import itertools

digits = [1, 1, 2]
combinations = set(itertools.permutations(digits))

for combo in combinations:
    print(combo)

#вариант 2


def generate_combinations(digits, current_combination, used):
    if len(current_combination) == len(digits):
        print(tuple(current_combination))
        return

    for i in range(len(digits)):
        if used[i]:
            continue
        if i > 0 and digits[i] == digits[i - 1] and not used[i - 1]:
            continue

        used[i] = True
        current_combination.append(digits[i])
        generate_combinations(digits, current_combination, used)
        used[i] = False
        current_combination.pop()


digits = [1, 1, 2]
used = [False] * len(digits)
digits.sort()
generate_combinations(digits, [], used)








#вариант 3


def unique_combinations(digits):
    digits.sort()
    result = []
    n = len(digits)

    def backtrack(start, path):
        if len(path) == n:
            result.append(tuple(path))
            return
        for i in range(start, n):
            if i > start and digits[i] == digits[i - 1]:
                continue
            path.append(digits[i])
            backtrack(i + 1, path)
            path.pop()

    backtrack(0, [])
    return set(result)


digits = [1, 1, 2]
combinations = unique_combinations(digits)

for combo in combinations:
    print(combo)