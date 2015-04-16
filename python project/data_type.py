__author__ = '绍文'

bag = ["hello", 78, 1.56, 2+3j]
print(bag[2:3])
print(bag * 2)

dictionary = {}
dictionary['first name'] = "han"
dictionary['last name'] = 'shaowen'
字典 = {"姓名": "韩绍文", "年龄": 24}
print("---------------------------------\n")
print(dictionary)
print(dictionary['first name'])
print(字典["年龄"])
print(dictionary.keys())
print(字典.values())

floatnum = 0xe
interger = int(floatnum)
print("--------------------------------\n")
print(interger)

iNum = 4
lList = [5, 4, 3]
print("--------------------------------\n")
if iNum in lList:
    print("iNum is in lList")
else:
    print("iNum is not in lList")
print("--------------------------------\n")

lList2 = [5, 4, 3]
if lList is lList2:
    print("both of them are same")
elif type(lList) == type(lList2):
    print("both of them have same type")
print("lList id = " + str(id(lList)))
print("iList2 id = " + str(id(lList2)))

print("--------------------------------\n")
for i in range(3, 9, 4):
    print(i)

for letter in "中文真的没问题吗？":
    print(letter)

名字 = ["韩绍文", "acezio", "weilor"]
for name in 名字:
    print(name)
for new_name in range(len(名字)):
    print("我的名字:",名字[new_name])
else:
    print("for else")

print("--------------------------------\n")
learntodel = [0, "1", 2 ,"3", 4, "5"]
print(learntodel)
print("--------------------------------\n")
del learntodel[1:3]
print(learntodel)
print("--------------------------------\n")
print(learntodel[2])
print("\a")

print("--------------------------------\n")
print("我的名字叫%s,我今年%d岁." % ("acezio", 25))
