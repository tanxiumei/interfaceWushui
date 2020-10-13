# #读取人物名称
f = open("name.txt",encoding="UTF8")
datalines = f.read()
data1 = datalines.split("|")
print(data1)

#读取兵器名称
f2 = open("weapon.txt",encoding="UTF8")
data2 = f2.readlines()
i=1
for dataline in data2:
    if(i%2!=0):
        print(dataline.strip('\n'))
    i+=1

#读取三国
f3 = open('sanguo2.txt', encoding='utf-8')
print(f3.read().replace('\n',''))