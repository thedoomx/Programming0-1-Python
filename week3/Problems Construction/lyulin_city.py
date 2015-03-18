block_list = [1, 5, 3, 2, 1, 8, 3, 4, 5]

blocks_seen = []
counter = 0
max_height = 0

for block in block_list:
    if block > max_height:
        counter += 1
        max_height = block
        blocks_seen += [block]

print("We can see " + str(counter) + " blocks.")
print(blocks_seen)
