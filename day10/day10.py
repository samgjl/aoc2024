def read_input(path: str):
    with open(path) as f:
        grid = []
        for line in f.read().split("\n"):
            grid.append([int(x) for x in line])
        return grid
            
def find_trailheads(grid):
    heads = []
    for i in range(len(grid)):
        for j in range(len(grid[0])):
            if grid[i][j] == 0:
                heads.append((i,j))
    return heads

def score(grid,start, unique=False):
    #BFS!!
    nines = list()

    queue = [start]
    directions = [(0,1), (1,0), (0,-1), (-1,0)]
    
    while len(queue) > 0:
        curr = queue.pop(0)
        val = grid[curr[0]][curr[1]]
        if val == 9:
            # nines.add(curr)
            nines.append(curr)
            # continue

        for d in directions:
            adj = (curr[0] + d[0], curr[1] + d[1])
            in_bounds = (0<=adj[0]<len(grid)) and (0<=adj[1]<len(grid[0]))
            valid_trail = in_bounds and grid[adj[0]][adj[1]] == val+1
            if valid_trail:
                queue.append(adj)
    if unique:
        return len(set(nines))
    return len(nines)

def part1(path: str):
    grid = read_input(path)
    heads = find_trailheads(grid)
    
    total = 0
    for zero in heads:
        total += score(grid,zero,unique=True)
    
    return total

def part2(path: str):
    grid = read_input(path)
    heads = find_trailheads(grid)
    
    total = 0
    for zero in heads:
        total += score(grid,zero,unique=False)
    
    return total


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