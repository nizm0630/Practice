# days_until_christmas 함수가 오늘부터 2030년 12월 25일 사이에 몇일이 있는지를 리턴

import datetime

def days_until_christmas():
    christmas_2030 = datetime.datetime(2030, 12, 25)
    days = (christmas_2030-datetime.datetime.now()).days
    return days

print("{}일".format(days_until_christmas()))

#2022/3/25 기준 3196일
