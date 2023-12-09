def instruction_mapper(direction):
    if(direction == 'R'):
        return 1
    return 0

def haunted_wasteland(instructions, route_map, queue):
    z_needs = len(queue)

    while(len(queue) != 0):
        print(queue)
        curr_node = queue[0][0]
        ip = queue[0][1]
        step = queue[0][2]
        from_node = queue[0][3]

        queue.pop(0)
        if(ip == len(instructions)):
            ip = 0
        print(curr_node, ip, step, route_map[curr_node], instructions[ip], from_node)

        if(curr_node[-1] == 'Z' and from_node == z_needs):
            return step


        # print(curr_node, ip, step, route_map[curr_node], instructions[ip], from_node)

        next_node = route_map[curr_node][instructions[ip]]

        queue.append((next_node, ip+1, step+1, from_node))

    ip = 0
    steps = 0
    print("****", queue)

    while(True):
        z_count = 0
        if(ip == len(instructions)):
            print("=========================== Done one path iteration =========================")
            ip = 0

        print(queue, ip)

        for i in range(len(queue)):
            curr_node = queue[i]
            if(curr_node[-1] == 'Z'):
                z_count += 1

            next_node = route_map[curr_node][instructions[ip]]
            queue[i] = next_node

        if(z_count == len(queue)):
            return steps

        ip += 1

        steps += 1

if __name__ == "__main__":

    instructions = ""
    route_map = {}
    queue = [] # consists of (node, instruction_position, step_count_so_far, from_node_int)
    from_node = 1

    with open("input.txt", "r") as f:
        line = f.readline()
        line.strip()

        instructions = line

        f.readline()

        while True:
            line = f.readline()
            if not line:
                break

            line = line.strip().split("=")

            line[-1] = line[-1].replace('(', '')
            line[-1] = line[-1].replace(')','')
            line[-1] = line[-1].replace(' ','') 

            node = line[0].strip()
            if(node[-1] == 'A'):
                # queue.append((node, 0, 0, from_node))
                queue.append(node)
                from_node += 1

            route_map[node] = tuple(line[-1].split(','))

    instructions = instructions.strip()
    instructions = list(map(instruction_mapper, instructions))
    # print(route_map)
    # print(queue)


    ans = haunted_wasteland(instructions, route_map, queue)

    print(ans)