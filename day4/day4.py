from itertools import combinations_with_replacement
class Solution:
    def __init__(self, path: str):
        self.graph = self.read_input(path)
        
    def read_input(self, path: str) -> list[str]:
        with open(path) as f:
            return [[c for c in l] for l in f.readlines()]            
        
    def part1(self) -> int:
        total = 0
        for i in range(len(self.graph)):
            for j in range(len(self.graph[i])):
                if self.graph[i][j] == 'X':
                    total += self.raycast([i,j])
        return total
    # Raycast in a given direction for "XMAS" from a given coordinate
    # PARAM: coords -> [int, int] coordinates
    def raycast(self, coords) -> int:
        perms = self.gen_dirs()
        total = 0
        for dir in perms:
            total += self.ray_helper(coords,dir)
        return total

    def ray_helper(self, coords: tuple[int,int], dir: tuple[int,int]):
        q = ["M","A","S"]
        x,y = coords
        dx,dy = dir
        while len(q) > 0:
            x,y = (x+dx, y+dy)
            if 0<=x<len(self.graph) and 0<=y<len(self.graph[x]) and self.graph[x][y]==q[0]:
                q = q[1:]
            else:
                return 0
        return 1
    
    def gen_dirs(self) -> list[tuple[int]]:
        l = []
        for i in range(-1,2):
            for j in range(-1,2):
                if (i,j) != (0,0): l.append((i,j))
        return l

    def part2(path: str) -> int:
        pass

if __name__ == "__main__":
    import sys
    path = sys.argv[1] if len(sys.argv) > 1 else "sample.txt"
    print("---- Part 1 ----")
    p1 = Solution(path).part1()
    print("Total:", p1)
    print("----------------")
    print("---- Part 2 ----")
    p2 = Solution(path).part2()
    print("Total:", p2)
    print("----------------")