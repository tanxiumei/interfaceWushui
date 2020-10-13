# file1 = open("name.txt",'w')
# file1.write("1 谈秀梅")
# file1.write("2 谈秀梅")
# file1.write("3 谈秀梅")
# file1.write("4 谈秀梅")
#
# file1.close()

# file2 = open("name.txt")
# print(file2.read())
# file2.close()

# file3 = open('name.txt','a')
# file3.write('李亮')
# file3.close()
# file4 = open("name.txt")
# #print(file4.readline())
# for line in file4.readlines():
#     print(line)
#     print("+++++++++++")

file6 = open('name.txt')
print(file6.tell())
file6.read(1)
print(file6.tell())