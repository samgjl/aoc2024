def read_input(filename: str) -> list[list[int]]:
    with open(filename) as f:
        inp = [l.strip("\n") for l in f.readlines()]
        l = [0]*len(inp)
        r = [0]*len(inp)
        for i in range(len(inp)):
            temp = inp[i].split(" ")
            l[i] = int(temp[0])
            r[i] = int(temp[-1])

        return [l,r]
        
def part1(path: str) -> int:
    lists = read_input(path)
    list1 = lists[0]
    list2 = lists[1]

    list1.sort()
    list2.sort()

    total = 0
    for i in range(len(list1)):
        total += abs(list1[i]-list2[i])
    return total

def part2(path: str) -> int:
    list1,list2 = read_input(path)
    
    total_score = 0
    for id in list1:
        total_score += (id*list2.count(id))
    return total_score

                   
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