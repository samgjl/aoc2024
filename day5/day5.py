def read_input(path: str) -> list[dict[int,int], list[list[int]]]:
    with open(path) as f:
        rules,sequence = f.read().split("\n\n")
        # turn into lists:
        rules = rules.split("\n")
        rule_dict = {int(r.split("|")[0]):[] for r in rules}
        for rule in rules:
            rule = rule.split("|")
            rule_dict[int(rule[0])] += [int(rule[1])]
        sequence = [
            [int(s) for s in seq.split(",")]
            for seq in sequence.split("\n")
        ]
        return rule_dict,sequence

def part1(path: str) -> int:
    # Given: A sequence P = P(1),P(2),...,P(n)
    # Task: Find each subsequence S, where S is as follows:
    #   * Each S(i) in S has a rule where it comes after S(1)...S(i-1)
    #   * Each S(i) in S has a rule where it comes before S(i+1)...S(n)
    rules,seq = read_input(path)

    valid = [sub for sub in seq if is_valid(rules, sub)]

    # Assume odd length:
    result = [v[int(len(v)/2)] for v in valid]
    return valid,sum(result)

def is_valid(rules:dict[int,list[int]], seq: list[int]) -> bool:
    if (seq == []) or (len(seq) == 1 and seq[0] not in rules.keys()):
        return True
    l = seq[0]
    for r in seq[1:]:
        if l not in rules.keys() or r not in rules[l]:
            return False
    return is_valid(rules,seq[1:])
        
def part2(path: str) -> int:
    rules,seq = read_input(path)
    invalid = [sub for sub in seq if not is_valid(rules, sub)]
    print(invalid)
    '''
    IDEA:
    For each number s in Seq:
        While it's not in a good place:
            Ascertain whether it is too far left or right,
            Then move it to the more ideal direction
    '''


if __name__ == "__main__":
    import sys
    path = sys.argv[1] if len(sys.argv) > 1 else "sample.txt"
    print("---- Part 1 ----")
    _,p1 = part1(path)
    print("Total:", p1)
    print("----------------")
    print("---- Part 2 ----")
    p2 = part2(path)
    print("Total:", p2)
    print("----------------")