def heaviest_loads(path):
    with open(path, 'r') as file:
        max_load, load = 0, 0
        for food in file:
            if food == '\n':
                max_load, load = load if load > max_load else max_load, 0
            else:
                load += int(food)
    return max_load


if __name__ == '__main__':
    print(heaviest_loads('input'))
