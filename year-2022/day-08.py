import numpy as np

def get_visible_trees(trees):
    row, col = (trees.shape)
    count = 0
    for i in range(row):
        for j in range(col):
            if is_visible(i,j,trees):
                count += 1
    return count

def is_visible(y,x, forest):
    row, col = (forest.shape)
    if x == 0 or y == 0 or x == col-1 or y == row -1:
        return True
    invisible_site = 0
    for i in range(x+1, row):
        if forest[i, y] >= forest[x, y]:
            invisible_site += 1
            break
    for i in range(x-1, -1, -1):
        if forest[i, y] >= forest[x, y]:
            invisible_site += 1
            break
    for i in range(y+1, col):
        if forest[x, i] >= forest[x, y]:
            invisible_site += 1
            break
    for i in range(y-1, -1, -1):
        if forest[x, i] >= forest[x, y]:
            invisible_site += 1
            break
    if invisible_site < 4:
        return True
    return False

def get_site(forest, start, end, interval,row, col, vertical):
    for i in range(start, end, interval):
        if vertical:
            if forest[i, col] >= forest[row, col]:
                return False
        else:
            if forest[row, i] >= forest[row, col]:
                return False
def highest_viewing_distance(trees):
    row, col = (trees.shape)
    max_viewing_distance = 0
    for i in range(row):
        for j in range(col):
            viewing_distance = get_viewing_distance(i, j, trees)
            if viewing_distance > max_viewing_distance:
                max_viewing_distance = viewing_distance
    return max_viewing_distance



def get_viewing_distance(x, y, forest):
    row, col = (forest.shape)
    if x == 0 or y == 0 or x == col-1 or y == row-1:
        return 0
    x1, x2, y1, y2 = 0,0,0,0
    for i in range(x+1, row):
        x1 += 1
        if forest[i, y] >= forest[x, y]:
            break
    for i in range(x-1, -1, -1):
        x2 += 1
        if forest[i, y] >= forest[x, y]:
            break
    for i in range(y+1, col):
        y1 += 1
        if forest[x, i] >= forest[x, y]:
            break
    for i in range(y-1, -1, -1):
        y2 += 1
        if forest[x, i] >= forest[x, y]:
            break
    return x1*x2*y1*y2
if __name__ == '__main__':
    with open('./input/day-08.ipt', 'r') as file:
        grid = []
        for line in file:
            rows = []
            for digit in line[:-1]:
                rows.append(int(digit))
            grid.append(rows)
    values = np.array(grid, dtype=int)
    print(get_visible_trees(values))
    print(highest_viewing_distance(values))
