# hundred_after가 지금으로부터 100일 후, 9시 정각을 값으로 가지는 datetime클래스의 인스턴스 생성

import datetime

hundred_after = datetime.datetime.now().replace(hour = 9, minute = 0, second = 0 )+datetime.timedelta(days = 100)

print("{}/{}/{}  {}:{}:{}".format(hundred_after.year,hundred_after.month, hundred_after.day, hundred_after.hour, hundred_after.minute, hundred_after.second))


'''
addtime = datetime.timedelta(days = 10)
datetime.datetime.now() + addtime    # 10일 후
datetime.datetime.now() - addtime    # 10일 전

thedate = datetime.datetime.now().replace(hour = 10, minute=0, second = 0)
          + datetime.timedelta(days = 3)       # 3일 후 10시 정각
'''
