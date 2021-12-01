import fileinput

# challenge 1
def basic_sonar():
    count = 0
    prev = 1000000000000000000
    for line in fileinput.input():
        if (int(line) > prev):
            count = count + 1
        prev = int(line)
    print(count)

# challenge 2
def adv_sonar():
    count = 0
    x = 2
    prev_sum = 10000000000000
    vals = [10000, 10000]
    for line in fileinput.input():
        vals.append(int(line))
        curr_sum = vals[x] + vals[x-1] + vals[x-2]
        if (curr_sum > prev_sum):
            count = count + 1
        prev_sum = curr_sum
        x = x + 1
    print(count)

adv_sonar()
