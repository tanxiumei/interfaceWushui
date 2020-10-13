

# print(chinese_zodiac[year%12])
# if(chinese_zodiac[year%12]) =="狗":
#     print("狗年的运势。。。。")

chinese_zodiac = '猴鸡狗猪鼠牛虎兔龙蛇马羊'
zodiac_name = (
    u'摩羯座',
    u'水瓶座',
    u'双鱼座',
    u'白羊座',
    u'金牛座',
    u'双子座',
    u'巨蟹座',
    u'狮子座',
    u'处女座',
    u'天秤座',
    u'天蝎座',
    u'射手座')
zodiac_days = ((1, 20), (2, 19), (3, 24), (4, 21), (5, 21), (6, 22),
               (7, 23), (8, 23), (9, 23), (10, 23), (11, 23), (12, 23))

cz_num = {}
for i in chinese_zodiac:
    cz_num[i] = 0
z_num = {}
for i in zodiac_name:
    z_num[i] = 0
while True:
    year = int(input("请用户输入出生年份："))
    int_month = int(input("请输入您的月份："))
    int_day = int(input("请输入您的日期："))

    n = 0
    while zodiac_days[n] < (int_month, int_day):
        if int_month == 12 and int_day > 23:
            break
        n += 1
    print(n)
    print("星座是：" + zodiac_name[n])
    print('%s 年的生肖是 %s' % (year, chinese_zodiac[year % 12]))

    cz_num[chinese_zodiac[year % 12]] += 1
    z_num[zodiac_name[n]] += 1

    for each_key in cz_num.keys():
        print('生肖%s 有 %d 个' % (each_key, cz_num[each_key]))
    for each_key1 in z_num.keys():
        print('星座 %s 有 %d 个' % (each_key1, z_num[each_key1]))
