import subprocess
import os
class ANSI():
    def background(code):
        return "\33[{code}m".format(code=code)
 
    def style_text(code):
        return "\33[{code}m".format(code=code)
 
    def color_text(code):
        return "\33[{code}m".format(code=code)
        
 
def update_map(map, bombers, bombs, obstacles):
    # Update the map with obstacles
    for obs in obstacles:
        map[obs[2]][obs[1]] = ANSI.background(91) + ANSI.color_text(49) + ANSI.style_text(1) + "[X]"#"[X{}]".format(obs[0])
    
    # Update the map with bombs
    for i in range(len(bombs)):
        b = bombs[i]
        map[b[2]][b[1]] = ANSI.background(93) + ANSI.color_text(49) + ANSI.style_text(1) + "[*]"#"[*{}]".format(b[0])
    # Update the map with bombers
    for i in range(len(bombers)):
        b = bombers[i]
        if map[b[2]][b[1]] == ANSI.background(93) + ANSI.color_text(49) + ANSI.style_text(1) + "[*]":
            map[b[2]][b[1]] = ANSI.background(93) + ANSI.color_text(49) + ANSI.style_text(1) + "[B*]"
        map[b[2]][b[1]] = ANSI.background(92) + ANSI.color_text(49) + ANSI.style_text(1) + "[B]"#"[B{}]".format(b[0])

    

def main():
    # Initialize the map
    map_width = 10  # Change to the actual map width
    map_height = 10  # Change to the actual map height
    map = [[ANSI.background(90) + ANSI.color_text(49) + ANSI.style_text(1) +"[ ]" for i in range(map_width)] for j in range(map_height)]
    
    # Run the controller and capture its output
    #proc = subprocess.Popen(["./controller"], stdout=subprocess.PIPE)
    obstacles = []
    bombers = []
    bombs = []
    while True:
        # Read one line at a time from the controller's output
        line = input().strip() #proc.stdout.readline().decode().strip()
        if line == "":
            break
        
        # Parse the line and update the map
        tokens = line.split()
        #print(tokens)
        if tokens[0] == "map":
            # Update the map with new information
            obj_type = tokens[1]
            if obj_type == "obstacle":
                obstacles.append((int(tokens[2]), int(tokens[3]), int(tokens[4]), int(tokens[5])))
            elif obj_type == "bomber":
                bombers.append((int(tokens[2]), int(tokens[3]), int(tokens[4])))
            elif obj_type == "bomb":
                bombs.append((int(tokens[2]), int(tokens[3]), int(tokens[4])))
        elif tokens[0] == "initial":
        # Print the updated map
            os.system("clear")
            update_map(map, bombers, bombs, obstacles)
            for row in map:
                print("".join(row))
            print()
            map = [["[ ]" for i in range(map_width)] for j in range(map_height)]
            obstacles = []
            bombers = []
            bombs = []

        

if __name__ == "__main__":
    main()
