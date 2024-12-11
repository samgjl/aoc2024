def read_file(path: str) -> list[int]:
    with open(path) as f:
        temp = [l.split(" ") for l in f.readlines()]
        return [[int(i) for i in l] for l in temp]      

def part1(path: str) -> int:
    lines = read_file(path)
    
    safe_reports = sum([determine_safety(l) for l in lines])

    return safe_reports
        
def determine_safety(line: list[int]) -> int:
    if len(line) < 2: 
        return 1 # Vacuously
    
    incline = ">" if line[1]>line[0] else "<"

    for i in range(1, len(line)):
        if abs(line[i]-line[i-1]) > 3:
            return 0
        if (incline == ">" and line[i] <= line[i-1]):
            return 0
        elif (incline == "<" and line[i] >= line[i-1]):
            return 0
    return 1
        
def part2(path: str):
    pass
    
if __name__ == "__main__":
    import sys
    path = "input.txt"
    if len(sys.argv) > 1:
        path = sys.argv[1]
    p1 = part1(path)
    p2 = part2(path)
    print("--- Part 1 ---")
    print("Total:", p1)
    print("--------------")
    print("--- Part 2 ---")
    print("Total:", p2)
    print("--------------")