def restack_container_9000(containers_9000, instructions):
    containers_9000 = containers_9000
    for instruction in instructions:
        for i in range(instruction[0]):
            moving_container = containers_9000[instruction[1]-1][-1]
            containers_9000[instruction[1]-1].pop()
            containers_9000[instruction[2]-1].append(moving_container)
    last_containers = [container[-1] for container in containers_9000]
    return ''.join(last_containers)


def restack_container_9001(containers, instructions):
    for instruction in instructions:
        moving_container = containers[instruction[1]-1][-1*instruction[0]:]
        del containers[instruction[1]-1][-1*instruction[0]:]
        containers[instruction[2]-1].extend(moving_container)
    last_containers = [container[-1] for container in containers]
    return ''.join(last_containers)

if __name__ == '__main__':
    containers_str = []
    instructions = []
    containers = []
    with open('./input/day-05.ipt', 'r') as file:
        instruction_lines = False
        for line in file:
            if not instruction_lines:
                if line == '\n':
                    instruction_lines = True
                else:
                    if len(line) % 4 == 0:
                        containers_str.append(line)
            else:
                instructions.append(list(map(int, line.split(' ')[1::2])))

    containers_str = containers_str[::-1]
    for i in range(int(len(containers_str[0])/4)):
        containers.append([])

    for container in containers_str:
        for i in range(int(len(container)/4)):
            if container[4*i + 1] != ' ':
                containers[i].append(container[4*i + 1])
    print(restack_container_9000(containers.copy(), instructions))

    containers_str = []
    instructions = []
    containers = []
    with open('./input/day-05.ipt', 'r') as file:
        instruction_lines = False
        for line in file:
            if not instruction_lines:
                if line == '\n':
                    instruction_lines = True
                else:
                    if len(line) % 4 == 0:
                        containers_str.append(line)
            else:
                instructions.append(list(map(int, line.split(' ')[1::2])))

    containers_str = containers_str[::-1]
    for i in range(int(len(containers_str[0])/4)):
        containers.append([])

    for container in containers_str:
        for i in range(int(len(container)/4)):
            if container[4*i+1] != ' ':
                containers[i].append(container[4*i+1])
    print(restack_container_9001(containers.copy(), instructions))
