import heapq


def elf_carrying_most_calories():
    elifs = dict()
    elif_id = 0
    with open('ds/1.txt', mode='r') as f:
        for line in f:
            if line == '\n':
                elif_id += 1
                continue
            elifs[elif_id] = elifs.get(elif_id, 0) + int(line)
    elif_with_most_calories = max(elifs, key=elifs.get)
    max_calories = elifs[elif_with_most_calories]
    print(f'elif # {elif_with_most_calories};\ncalories: {max_calories}')


# Find top 3 values in dict
def total_top_3_calories():
    elifs = dict()
    id = 0
    with open('ds/1.txt', mode='r') as f:
        for line in f:
            if line == '\n':
                id += 1
                continue
            elifs[id] = elifs.get(id, 0) + int(line)
    top3_calories = heapq.nlargest(3, elifs.items(), key=lambda item: item[1])
    print("top3: calories", top3_calories)
    print("total top3: ", sum(item[1] for item in top3_calories))


elf_carrying_most_calories()
total_top_3_calories()
