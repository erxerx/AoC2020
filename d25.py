# example
# 5764801 loop 8
# 17807724 loop 11
# key 14897079
# input
# 17773298  loop 4347326
# 15530095  loop 14611728
# key 17980581
subject = 1
# i = 1
# while subject != 15530095:
for i in range(4347326):
    subject = (15530095 * subject) % 20201227
    # i += 1
# print(i, subject)
print(subject)
