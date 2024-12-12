import re

def read_input(path: str) -> list[str]:
    with open(path) as f:
        return f.read()
    

def part1(path: str) -> int:
    text = read_input(path)
    
    regex = r'mul\((\d{1,3})\,(\d{1,3})\)'
    multlist = re.findall(regex, text)
    return sum([int(x[0])*int(x[1]) for x in multlist])
    # return sum(map(lambda x: int(x[0])*int(x[1]), multlist)) # <- Sam moment
    

def part2(path: str) -> int:
    text = read_input(path)
    
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
    