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