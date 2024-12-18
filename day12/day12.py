# from dataclasses import dataclass

# @dataclass
class Region:
    perimeter: int
    area: int
    letter: str
    grid: list[list[str]]
    
    def __init__(self, letter):
        self.letter = letter

    def perimeter(self):
        if self.perimeter:
            return self.perimeter
        
    def area(self):
        if self.area:
            return self.area
        


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