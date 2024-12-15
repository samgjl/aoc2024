def read_input(path: str) -> tuple[list[list[str]], list[str]]:
    with open(path) as f:
        grid = [list(line.strip("\n")) for line in f.readlines()]
        for i in range(len(grid)):
            if "^" in grid[i]:
                j = grid[i].index("^")
                return grid, (i,j)

def rotateCC(original: list[list[str]]) -> list[list[str]]:
    return list(zip(*original))[::-1]
        
def part1(path: str) -> int:    
    grid,pos = read_input(path)

    visited = []
    # [Up, Right, Down, Left]
    direction = [(-1,0),(0,1),(1,0),(0,-1)]
    current_dir = 0
    visited = {tuple(pos)}
    
    while (0 <= pos[0] < len(grid)) and (0 <= pos[1] < len(grid[0])):
        grid[pos[0]][pos[1]] = "X" # Remove later
        visited.add(tuple(pos)) # Visit
        dir = direction[current_dir]
        next = [pos[0] + dir[0], pos[1] + dir[1]]
        if 0<=next[0]<len(grid) and 0<=next[1]<len(grid[1]) and (grid[next[0]][next[1]] == "#"):
            current_dir = (current_dir + 1) % 4
        else:
            pos = next
         
    print("\n".join(["".join(l) for l in grid]))
    return len(visited)

def part2(path: str) -> int:
    pass

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