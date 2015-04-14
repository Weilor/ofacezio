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
while 1 :
    print("loop!")
else:
    print("exit")
print("exit from loop!")