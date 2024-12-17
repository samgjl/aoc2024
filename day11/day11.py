from tqdm import tqdm

def read_input(path: str) -> list[int]:
    with open(path) as f:
        return [int(x) for x in f.read().split(" ")]

def part1(path: str):
    stones = read_input(path)

    for _ in range(25):
        stones = step(stones)
        
    return len(stones)

def step(stones: list[int]) -> list[int]:
    new_stones = []
    for i in range(len(stones)):
        if stones[i] == 0:
            new_stones.append(1)
        elif len(str(stones[i])) % 2 == 0:
            mid = int(len(str(stones[i]))/2)
            left = int(str(stones[i])[:mid])
            right = int(str(stones[i])[mid:])
            new_stones.append(left)
            new_stones.append(right)
        else:
            new_stones.append(stones[i]*2024)
    return new_stones


def part2(path: str):
    stones = read_input(path)
    steps = 75
    total = recurse(steps, stones)
        
    return total

memo = dict()
def recurse(steps, stones):
    total = 0
    for stone in stones:
        total += recurse_helper(steps, stone)
    return total 

def recurse_helper(steps, stone):
    if (steps,stone) in memo.keys():
        return memo[(steps,stone)]

    total = 0
    stones = []
    # Base Case
    if steps == 0:
        return 1
    
    # Recursive Case: Apply rules, recurse down, memoize
    if stone == 0:
        stones = [1]
    elif len(str(stone)) % 2 == 0:
        mid = int(len(str(stone))/2)
        left = int(str(stone)[:mid])
        right = int(str(stone)[mid:])
        stones = [left, right]
    else:
        stones = [stone * 2024] 
    
    for s in stones:
        total += recurse_helper(steps-1,s)
    memo[(steps,stone)] = total
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