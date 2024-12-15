
# RETURNS:
# [
#   [<target>, [<components>]]
# ]
def read_input(path: str) -> list[list]:
    with open(path) as f:
        lines = f.readlines()
        out = []
        for line in lines:
            line = line.strip("\n").split(": ")
            out.append([
                int(line[0]), 
                [int(i) for i in line[1].split(" ")]
                ])
        return out

def part1(path: str) -> int:
    equations = read_input(path)
    
    total = 0
    for e in equations:
        tar,comp = e
        if check_valid(tar,comp):
            total += tar
        
    return total

# Recursive function to check if there are any combos that would work
def check_valid(tar: int, comp: list[int], curr: int = 0,):
    if len(comp) == 0:
        return tar == curr
    else:
        plus = check_valid(tar,comp[1:],curr+comp[0]) if curr+comp[0]<=tar else False
        times = check_valid(tar,comp[1:], curr*comp[0]) if curr*comp[0]<=tar else False
        return plus or times

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