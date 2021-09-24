import sys
wishing = int(sys.stdin.readline())
broken_n = int(sys.stdin.readline())
my_button = {str(i) for i in range(10)}
if broken_n > 0:
    my_button -= set(map(str, sys.stdin.readline().split()))

current_channel = 100

count = abs(current_channel - wishing)

for channel in range(1000001):
    channel = str(channel)
    for j in range(len(channel)):
        if channel[j] not in my_button:
            break
        elif j == len(channel) - 1:
            count = min(count, abs(int(channel)-wishing) + len(str(channel)))

print(count)