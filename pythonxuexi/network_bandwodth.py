# 网络带宽计算
"""
print(100 / 8)
bandwidth = 100
ratio = 8
print(bandwidth/ratio)


#记录十二生肖，根据年份来判断生肖
chinese_zodiac = '猴鸡狗猪鼠牛虎兔龙蛇马羊'
print(chinese_zodiac[0:5])
print(chinese_zodiac[-1])
year = 2016
print(chinese_zodiac[year%12])

print('龙' in chinese_zodiac)
print(chinese_zodiac+chinese_zodiac)
print(chinese_zodiac*3)
print(chinese_zodiac+"十二生肖")
"""
# 根据月份和日期，判断星座
zodiac_name = (
    u'摩羯座',
    u'水瓶座',
    u'双鱼座',
    u'白羊座',
    u'金牛座',
    u'双子座'
    u'巨蟹座',
    u'狮子座',
    u'处女座',
    u'天秤座',
    u'天蝎座',
    u'射手座')
zodiac_days = ((1, 20), (2, 19), (3, 24), (4, 21), (5, 21), (6, 22),
               (7, 23), (8, 23), (9, 23), (10, 23), (11, 23), (12, 23))
(month, day) = (3, 18)
zadiac_day = list(filter(lambda x: x <= (month, day), zodiac_days))
zadiac_len = len(zadiac_day) % 12
print(zodiac_name[zadiac_len])
