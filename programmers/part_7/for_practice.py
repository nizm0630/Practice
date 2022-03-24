#각 개월의 날짜 수 나타내기

days = [31,29,31,30,31,30,31,31,30,31,30,31]

for i, a in enumerate(days):
   print('{}월의 날짜수는 {}일 입니다.'.format(i+1 , a))
    
for i in range(len(days)):
  print('{}월의 날짜수는 {}일 입니다.'.format(i+1, days[i]))
