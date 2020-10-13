import time
# x = "123"
# if x == 'abc':
#     print("x的值和abc相等")
# elif x == '123':
#     print("x和123相等")
# else:
#     print("x和abc不相等")

chinese_zodiac = '猴鸡狗猪鼠牛虎兔龙蛇马羊'
# year = int(input("请用户输入出生年份："))
# print(chinese_zodiac[year%12])
# if(chinese_zodiac[year%12]) =="狗":
#     print("狗年的运势。。。。")
# for cz in chinese_zodiac:
#     print(cz)
# for i in range(1,13):
#     print(i)
# for year in range(2000,2019):
#     print('%s 年的生肖是 %s' %(year,chinese_zodiac[year%12]))

zodiac_name = (u'摩羯座',u'水瓶座',u'双鱼座',u'白羊座',u'金牛座',u'双子座'u'巨蟹座',u'狮子座',u'处女座',u'天秤座',u'天蝎座',u'射手座')
zodiac_days =((1,20),(2,19),(3,24),(4,21),(5,21),(6,22),(7,23),(8,23),(9,23),(10,23),(11,23),(12,23))
int_month = int(input("请输入您的月份："))
int_day = int(input("请输入您的日期："))
# for num in range(len(zodiac_days)):
#     if zodiac_days[num] >=(int_month,int_day):
#         print(zodiac_name[num])
#         break
#     elif int_month==12 and int_day>23:
#         print(zodiac_name[0])
#         break
n=0
while zodiac_days[n]< (int_month,int_day):
    if int_month==12 and int_day>23:
        break
    n+=1
print(zodiac_name[n])