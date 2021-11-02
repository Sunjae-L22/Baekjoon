import random
music = random.randrange(0, 101)
art = random.randrange(0, 101)
cheyook = random.randrange(0, 101)
gajung = random.randrange(0, 101)

mean = (music + art + cheyook + gajung) / 4

print("음악 : ", music)
print("미술 : ", art)
print("체육 : ", cheyook)
print("가정 : ", gajung)
print("평균 : ", mean)