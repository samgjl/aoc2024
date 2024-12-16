import math

def read_input(path: str) -> tuple[list[list[str]],dict[str:list]]:
    with open(path) as f:
        grid = [[l for l in line.strip("\n")] for line in f.readlines()]
        nodes: dict[str,list] = {}
        for i in range(len(grid)):
            for j in range(len(grid)):
                val = grid[i][j]
                if val != ".":
                    if val not in nodes:
                        nodes[val] = []
                    nodes[val].append((i,j))
        return grid,nodes

def part1(path: str):
    grid,nodes = read_input(path)
    
    locations: set[tuple[int,int]] = set()

    for n in nodes.keys():
        nodeset = nodes[n]
        for i in range(len(nodeset)):
            pos1 = nodeset[i]
            for j in range(len(nodeset)):
                pos2 = nodeset[j]
                if pos1 == pos2:
                    continue

                vec = vector(pos1,pos2)
                loc1 = (pos1[0] + 2*vec[0], pos1[1] + 2*vec[1])
                loc2 = (pos1[0] - vec[0], pos1[1] - vec[1])
                if 0<=loc1[0]<len(grid) and 0<=loc1[1]<len(grid[0]):
                    locations.add(loc1)
                if 0<=loc2[0]<len(grid) and 0<=loc2[1]<len(grid[0]):
                    locations.add(loc2)
    return len(locations)

def vector(p1,p2):
    return [(p2[0]-p1[0]),(p2[1]-p1[1])]
def distance(p1,p2):
    return ((p1[0]-p2[0])**2+(p1[1]-p2[1])**2)**(1/2)
def normal(p1,p2):
    v = vector(p1,p2)
    d = distance(p1,p2)
    d = float("inf") if d==0 else d
    return (v[0]/d,v[1]/d)
def minimal_vector(p1,p2):
    vec = vector(p1,p2)
    denom = math.gcd(*vec)
    return list(map(lambda v: v/denom, vec))


def part2(path:str):
    grid,nodes = read_input(path)
    locations = set()

    for n in nodes.keys():
        nodeset = nodes[n]

        for i in range(len(nodeset)):
            pos1 = nodeset[i]
            for j in range(i+1,len(nodeset)):
                pos2 = nodeset[j]
                vec = minimal_vector(pos1,pos2)

                loc = pos1 # Current location
                s = 0 # Scale
                while 0<=loc[0]<len(grid) and 0<=loc[1]<len(grid[0]):
                    locations.add(loc)
                    loc = (pos1[0]+s*vec[0], pos1[1]+s*vec[1])
                    s += 1
                loc = pos1
                s = 0
                while 0<=loc[0]<len(grid) and 0<=loc[1]<len(grid[0]):
                    locations.add(loc)
                    loc = (pos1[0]+s*vec[0], pos1[1]+s*vec[1])
                    s -= 1
    return len(locations)
                        




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