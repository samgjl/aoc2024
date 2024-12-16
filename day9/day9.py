def read_input(path: str):
    with open(path) as f:
        return f.read()

def filesystem(og: str) -> list[int|str]:
    fs = []
    id = 0
    block = True
    for char in og:
        if block:
            fs += ([id]*int(char))
            id += 1
        else:
            fs += (["."]*int(char))
        block = not block
    return fs

def optimize(fs: list[str]):
    fs = fs[::]
    left = 0
    right = len(fs)-1

    while True:
        while fs[left] != ".":
            left += 1
        while fs[right] == ".":
            right -= 1
        if left >= right:
            return fs
        fs[left] = fs[right]
        fs[right] = "."

def checksum(fs: list[str]) -> int:
    total = 0
    for i in range(len(fs)):
        if fs[i] != ".":
            total += int(fs[i]) * i
    return total


def part1(path: str):
    original = read_input(path)
    fs = filesystem(original)
    opt = optimize(fs)
    return checksum(opt)
    
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