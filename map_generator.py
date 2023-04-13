"""
    input shape:
    <map_width> <map_height> <obstacle_count> <bomber_count>
    <obstacle1_location_x> <obstacle1_location_y> <obstacle1_durability>
    <obstacle2_location_x> <obstacle2_location_y> <obstacle2_durability>
    ....
    <obstacleN_location_x> <obstacleN_location_y> <obstacleN_durability>

    <bomber1_x> <bomber1_y> <bomber1_total_argument_count>

    <bomber1_executable_path> <bomber1_arg1> <bomber1_arg2> ... <bomber1_argM>
    ....
    <bomberK_x> <bomberK_y> <bomberK_total_argument_count>
    <bomberK_executable_path> <bomberK_arg1> <bomber1_arg2> ... <bomberK_argL>
"""

import random
import sys
import os

class ANSI():
    def background(code):
        return "\33[{code}m".format(code=code)
 
    def style_text(code):
        return "\33[{code}m".format(code=code)
 
    def color_text(code):
        return "\33[{code}m".format(code=code)
 

def generate_input(map_width, map_height, obstacle_count, bomber_count):
    # Generate obstacle locations and durabilities
    locs = set()
    obstacles = list()
    while len(obstacles) < obstacle_count:
        x = random.randint(0, map_width - 1)
        y = random.randint(0, map_height - 1)
        durability = random.randint(1, 5)
        if (x, y) not in locs:
            obstacles.append((x, y, durability))
            locs.add((x, y))
    obstacles = sorted(obstacles)

    # Generate bomber locations, argument counts, and arguments
    bombers = list()
    while len(bombers) < bomber_count:
        x = random.randint(0, map_width - 1)
        y = random.randint(0, map_height - 1)
        arg_count = 3
        args = ["10", map_width, map_height]
        if (x, y) not in locs:
            bombers.append((x, y, arg_count, "./bomber", args ))
            locs.add((x, y))
    bombers = sorted(bombers)

    # Visualize the map
    map = [[ANSI.background(90) + ANSI.color_text(49) + ANSI.style_text(1) +"[ ]" for i in range(map_width)] for j in range(map_height)]
    for obs in obstacles:
        map[obs[1]][obs[0]] = ANSI.background(91) + ANSI.color_text(49) + ANSI.style_text(1) + "[X]"
    for bomber in bombers:
        map[bomber[1]][bomber[0]] = ANSI.background(92) + ANSI.color_text(49) + ANSI.style_text(1) + "[B]"
    for row in map:
        print("".join(row))

    response = input("Is this map okay? (y/n):")
    if response == "n":
        os.system("clear")
        return generate_input(map_width, map_height, obstacle_count, bomber_count)
    elif response == "y":

        # Generate input string
        input_string = "{map_width} {map_height} {obstacle_count} {bomber_count}\n".format(map_width=map_width, map_height=map_height, obstacle_count=obstacle_count, bomber_count=bomber_count)
        for obs in obstacles:
            input_string += "{x} {y} {durability}\n".format(x=obs[0], y=obs[1], durability=obs[2])
        for bomber in bombers:
            input_string += "{x} {y} {arg_count}\n".format(x=bomber[0], y=bomber[1], arg_count=bomber[2]+1)
            input_string += "{executable_path} ".format(executable_path=bomber[3])
            for arg in bomber[4]:
                input_string += "{arg} ".format(arg=arg)
            input_string += "\n"
        return input_string
    else:
        exit(0)



if __name__ == "__main__":
    if len(sys.argv) != 5:
        print("Usage: python input_generator.py <map_width> <map_height> <obstacle_count> <bomber_count>")
        exit(1)

    map_width = int(sys.argv[1])
    map_height = int(sys.argv[2])
    obstacle_count = int(sys.argv[3])
    bomber_count = int(sys.argv[4])

with open("input_{map_width}_{map_height}_{obstacle_count}_{bomber_count}.txt".format(map_width=map_width, map_height=map_height, obstacle_count=obstacle_count, bomber_count=bomber_count) , "w") as f:
    f.write(generate_input(map_width, map_height, obstacle_count, bomber_count))
    f.close()
    


