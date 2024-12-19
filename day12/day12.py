def read_input(path: str) -> list[list[str]]:
    with open(path) as f:
        grid = []
        for line in f.read().split("\n"):
            grid.append(list(line))
        return grid
        # return [[str(x) for x in l.split()] for l in f.read().split("\n")]

def part1(path: str) -> int:
    grid = read_input(path)
    
    total = 0
    chunk_start = (0,0)

    while chunk_start != (len(grid),len(grid[0])):
        # print("-----")
        # print("\n".join(["".join([x for x in l]) for l in grid]))
        # Infect whole chunk (BFS), replacing chnunk with space as we go
        perimeter,area = chunk(grid,chunk_start)        
        total += perimeter*area
        # Find next letter
        chunk_start = find_next(grid,chunk_start)

        
    return total

# Remove the chunk from the grid
# NOTE: This is done in-place!! <grid> is PERMANENTLY modified.
def chunk(grid: list[list[str]], start: tuple[int,int]) -> tuple[int,int]:
    # print("Start:",start)
    letter = grid[start[0]][start[1]]
    directions = [(1,0), (0,1), (-1,0), (0,-1)]
    # BFS:
    queue = [start]
    perim = 0
    area = 0
    visited = set()
    while len(queue) > 0:
        curr = queue.pop(0)
        visited.add(curr)
        area += 1
        # grid[curr[0]][curr[1]] = " "
        
        for d in directions:
            next = (curr[0]+d[0], curr[1]+d[1])
            in_bounds = 0<=next[0]<len(grid) and 0<=next[1]<len(grid[0])
            if in_bounds and (grid[next[0]][next[1]]) == letter and (next not in visited):
                visited.add(next)
                queue.append(next)
            elif (not in_bounds) or (in_bounds and grid[next[0]][next[1]] != letter):
                perim += 1
    
    for v in visited:
        grid[v[0]][v[1]] = " " 
        
    # print("Letter:",letter,"|","Perim:",perim,"|","Area:",area,"|","Visited:",visited)
    return perim,area


def find_next(grid: list[list[str]], pos: tuple[int,int]):
    row,col = pos
    while 0<=row<len(grid) and 0<=col<len(grid[0]):
        if grid[row][col] != " ":
            return (row,col)
        col = (col+1) % len(grid[0])
        if col == 0:
            row += 1
    return (len(grid), len(grid[0])) # Not found

def part2(path: str):
    grid = read_input(path)
    
    total = 0
    chunk_start = (0,0)

    while chunk_start != (len(grid),len(grid[0])):
        print("-----")
        # Infect whole chunk (BFS), replacing chnunk with space as we go
        num_sides = turtle(grid, chunk_start)
        print(f"Letter: {grid[chunk_start[0]][chunk_start[1]]} | Sides: {num_sides}", end=" | ")
        _,area = chunk(grid, chunk_start)   
        print(f"Area: {area}")     
        total += num_sides*area
        # Find next letter
        chunk_start = find_next(grid,chunk_start)

    return total

def turtle(grid: list[list[str]], start_pos: tuple[int,int]):
    sides = 0
    letter = grid[start_pos[0]][start_pos[1]]
    pos = start_pos
    start_dir = (0,1)
    dir = start_dir
    
    grid = [g[::] for g in grid]
    for i in range(len(grid)):
        for j in range(len(grid)):
            grid[i][j] = letter if grid[i][j] == letter else " "

    emergency = 0
    while True:
        if emergency == 5:
            exit()
        # temp = [["#"] + g[::] + ["#"] for g in grid]
        # print(pos)
        # if 0<=pos[0]<len(grid) and 0<=pos[1]<len(grid[0]):
        #     temp[pos[0]][pos[1]+1] = "X"
        #     print("\n".join(["".join(t) for t in temp]))
            

        # boundary is either != our letter or out of bounds
        left = move(pos, turn("L",dir))
        left_closed = 0<=left[0]<len(grid) and 0<=left[1]<len(grid[0]) and grid[left[0]][left[1]] == letter
        front = move(pos, dir)
        front_closed = 0<=front[0]<len(grid) and 0<=front[1]<len(grid[0]) and grid[front[0]][front[1]] == letter
        # If front AND left are not letter: Take one right, add one to the sides
        if not (left_closed or front_closed):
            emergency += 1
            # print("Front and left OOB, turn RIGHT")
            dir = turn("R",dir)
            sides += 1
        # If front and left ARE letter: take a left, move forward one, add one side
        elif left_closed:
            # print("CLAUSTROPHOBIC! Turning LEFT & MOVING 1")
            dir = turn("L",dir)
            pos = move(pos, dir)
            sides += 1
        # else move 1 forward
        else:
            emergency = 0
            # print("Good to go! Forward it is.")
            pos = move(pos,dir)

        # print("Direction:", dir)

        if pos == start_pos and dir == start_dir:
            break
    
    return sides

def move(a,b):
    return (a[0]+b[0], a[1]+b[1])
    
def turn(lr: str, dir: tuple[int,int]):
    directions = {
        (0,-1): [(1,0),(-1,0)],     # Left
        (0,1):  [(-1,0),(1,0)],     # Right
        (-1,0): [(0,-1),(0,1)],     # Up
        (1,0):  [(0,1),(0,-1)]      # Down
    }
    # directions = [(-1,0),(0,1),(1,0),(0,-1)]
    # index = -1 + (2 * "LR".index(lr))
    return directions[dir]["LR".index(lr)]

if __name__ == "__main__":
    import sys
    path = sys.argv[1] if len(sys.argv) > 1 else "sample.txt"
    print("---- Part 1 ----")
    p1 = part1(path)
    print("Total:", p1)
    print("----------------")
    print("---- Part 2 ----")
    p2 = part2(path)
    print("Total:", p2)
    print("----------------")