import copy

test_cases = int(input())

if 1 <= test_cases <= 5:
    test_dict = {}

    for i in range(test_cases):
        block_size = int(input())
        block_str = input()
        blocks = [int(x) for x in block_str.split()]

        stacked = "Yes"

        if block_size <= 2:
            print(stacked)
            continue

        max = []
        max = [blocks[0], 0] if blocks[0] >= blocks[-1] else [blocks[-1], -1]

        while True:

            if len(blocks) < 1:
                break

            left = [blocks[0], 0]
            right = [blocks[-1], -1]

            temp_max = left if left[0] >= right[0] else right

            if temp_max[0] > max[0]:
                stacked = "No"
                break
            else:
                blocks.pop(temp_max[1])
                max = []
                max = copy.deepcopy(temp_max)

        print(stacked)
