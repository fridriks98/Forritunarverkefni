sum = 0

for chess in range(0, 64):
    grain = 2**chess
    sum += grain

print(sum)