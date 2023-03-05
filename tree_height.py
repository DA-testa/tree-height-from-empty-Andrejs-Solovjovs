# python3 
# 221RDB4442 Andrejs Solovjovs

import sys

def compute_height(n, parents):
    heights = [0] * int(n)
    max_height = 0

    for i in range(int(n)):
        if heights[i] > 0:
            continue
        height = 0
        j = i
        while j != -1:
            if heights[j] > 0:
                height += heights[j]
                break
            else:
                height += 1
                j = int(parents[j])
        heights[i] = height
        if height > max_height:
            max_height = height

    return max_height

def read_input():
    try:
        with open(sys.argv[1]) as f:
            n = f.readline().strip()
            parents = f.readline().strip().split()
    except:
        print("ERROR")
        return None, None

    if not n or not parents:
        print("ERROR")
        return None, None

    return n, parents

def main():
    n, parents = read_input()
    if n and parents:
        height = compute_height(n, parents)
        print(int(height))

if __name__ == "__main__":
    main()
