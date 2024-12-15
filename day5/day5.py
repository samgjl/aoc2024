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
    return sum(result)

# re-wrote this code following the theorem derived in part 2
def is_valid(rules:dict[int,list[int]], seq: list[int]) -> bool:
    rules = minimize_rules(rules,seq)
    for i in range(1, len(seq)):
        if len(rules[seq[i-1]]) < len(rules[seq[i]]):
            return False
    return True
    # # Original approach:
    # if (seq == []) or (len(seq) == 1 and seq[0] not in rules.keys()):
    #     return True
    # l = seq[0]
    # for r in seq[1:]:
    #     if l not in rules.keys() or r not in rules[l]:
    #         return False
    # return is_valid(rules,seq[1:])
        
def part2(path: str) -> int:
    rules,seq = read_input(path)
    invalid: list[list[int]] = [sub for sub in seq if not is_valid(rules, sub)]
    for inv in invalid:
        # Let S(1),S(2),...,S(n) be a valid subsequence.
        # By design,the ruleset for what S(i) contains be AT LEAST [S(i+1),...,S(n)]
        #   * EX: If [1,2,3,4] is valid, {then 1:[2,3,4], 2:[3,4], 3:[4] | 4->[]} at minimum.
        # We can simply create this minimal ruleset via intersection between the original ruleset and the current sequence
        # Finally, we are left with a ruleset where S(1)'s value is a list of length (n-1), S(2)->[n-2],...,S(n)->[]
        # From here, we don't even need to look at their rulesets' contents. We can simply sort by ruleset length
        new_rules = minimize_rules(rules,inv)
        inv.sort(
            # Invert the length because more rules implies earlier in the sequence
            key = lambda x: -len(new_rules[x])
        )
    result = [i[int(len(i)/2)] for i in invalid]

    return sum(result)

def minimize_rules(rules: dict[int,list[int]], seq: list[int]) -> dict[int,list[int]]:
    new_rules = {}
    for s in seq:
        if s not in rules.keys():
            new_rules[s] = []
        else:
            new_rules[s] = list(set(rules[s]) & set(seq))
    return new_rules


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