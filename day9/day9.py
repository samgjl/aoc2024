def read_input(path: str):
    with open(path) as f:
        return f.read()

def filesystem(og: str):
    fs = ""
    id = 0
    block = True
    for char in og:
        if block:
            fs += (f"{id}"*int(char))
            id += 1
        else:
            fs += ("."*int(char))
        block = not block
    return fs
        



def part1(path: str):
    original = read_input(path)
    fs = filesystem(original)
    
    print(fs)

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