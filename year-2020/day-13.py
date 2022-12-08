def next_bus(arrival_time, buses):
    next_arrivals = {}
    for bus in buses:
        next_arrivals[bus] = arrival_time + (bus - arrival_time % bus)
    return min(next_arrivals, key=next_arrivals.get) * min(next_arrivals.values())


def restack_container_9001(containers, instructions):
    pass

if __name__ == '__main__':
    values = []
    with open('./input/day-13.ipt', 'r') as file:
        line = int(file.readline())
        uf_values = file.readline().split(',')
        for value in uf_values:
            if value != 'x':
                values.append(int(value))
    print(next_bus(line, values))
