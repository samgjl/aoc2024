from tqdm import tqdm

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

def optimize(fs: list[int|str]) -> list[int|str]:
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

def checksum(fs: list[int|str]) -> int:
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
    original = read_input(path)
    fs = filesystem(original)
    opt = optimize2(fs)
    return checksum(opt)
    
def optimize2(fs: list[int|str]):
    fs = fs[::]
    id = max(
        fs,
        key = lambda x: x if x!="." else -1
    )
    
    left = 0
    for id in tqdm(range(id, -1, -1)):
        # Find leftmost pointer and length of rightmost id
        right = fs.index(id)
        length = fs.count(id)
        # try to find leftmost position of a block that fits
        left = fs.index(".")
        if left > right:
            continue
        
        while left < right:
            temp_len = 0
            # Period found, build chunk
            if fs[left] == ".":
                temp_len = 0
                # build chunk until problem
                while fs[left+temp_len] == ".":
                    temp_len += 1
                # Check for valid chunk. If valid, swap
                if temp_len >= length:
                    fs[left:left + length] = [id]*length
                    fs[right:right+length] = ["."]*length
                    right = -1
                else: # no match, skip by length
                    left += temp_len
            else: # No period, skip this index
                left += 1
    return fs

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