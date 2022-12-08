def get_file_sizes(dirs):
    sums = 0
    for size in dirs.values():
        if size <= 100000:
            sums += size
    return sums

def find_samllest_delete_dir(dirs):
    big_dirs = []
    for size in dirs.values():
        if size >= dirs['/'] - 40000000:
            big_dirs.append(size)
    return min(big_dirs)


if __name__ == '__main__':
    active_dir, dir_size = [], {}
    with open('./input/day-07.ipt', 'r') as file:
        commands = file.read().strip().split("\n")
    for line in commands:
        line = line.split(' ')
        if line[1] == 'cd':
            command = line[-1]
            if command != '..':
                if len(active_dir):
                    command = active_dir[-1]+'/'+command
                active_dir.append(command)
                dir_size[command] = 0
            else:
                active_dir.pop()
        elif line[0] != 'dir' and line[0] != '$':
            for a_dir in active_dir:
                dir_size[a_dir] += int(line[0])
    print(get_file_sizes(dir_size))
    print(find_samllest_delete_dir(dir_size))
