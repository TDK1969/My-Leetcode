class Solution:
    def countCollisions(self, directions: str) -> int:
        blocks = []
        count = 0
        
        for car in directions:
            if not blocks:
                blocks.append([car, 1])
            else:
                if car == blocks[-1][0]:
                    blocks[-1][1] += 1
                else:
                    blocks.append([car, 1])
        n = len(blocks)
        for i, block in enumerate(blocks):
            if block[0] == 'L' and i != 0:
                if blocks[i - 1][0] == 'S':
                    count += block[1]
                if blocks[i - 1][0] == 'R':
                    count += block[1] + blocks[i - 1][1]
            if block[0] == 'R' and i != n - 1:
                if blocks[i + 1][0] == 'S':
                    count += block[1]
        
        return count


