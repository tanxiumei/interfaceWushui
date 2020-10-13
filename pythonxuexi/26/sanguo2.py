# import re
# def find_item(hero):
#     with open("sanguo2.txt",encoding="UTF8") as f:
#         data =f.read().replace('\n','')
#         name_num = re.findall(hero,data)
#         print("主角 %s 出现 %s 次" %(hero,len(name_num)))
#     return len(name_num)
#
# #读取任务信息：
# name_dic = {}
# with open("name.txt",encoding="UTF8") as f:
#     for line in f.readlines():
#         names = line.split('|')
#         for n in names:
#             #             print(n)
#             name_num = find_item(n)
#             name_dic[n] = name_num
#
# name_sorted = sorted(name_dic.items(), key=lambda item: item[1], reverse=True)
# print(name_sorted[0:10])
# print("abc",end="111\n")
# print("edf")
# def tan1(a,b,c):
#     print("a=",a)
#     print("b=", b)
#     print("c=", c)
# def howlong(first,*kw):
#     print(1)
# tan1(c=1,a=2,b=3)
# list1 = [1,2,3]
# it =iter(list1)
# print(next(it))
# print(next(it))
# print(next(it))
# print(next(it))#except
# for i in range(10,20,2):
#     print(i)
def frange(start,stop,step):
    x=start
    while x <stop:
        yield x
        x+=step
for i in frange(10,20,0.5):
    print(i)
