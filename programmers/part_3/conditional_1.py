# 변수 hour에 현재 시간을 저장합니다.
# hour에 저장된 현재 시간이 12보다 작을때 print문이 실행되도록 if문 추가

from datetime import datetime 
hour = datetime.now().hour

#현재 시간이 12시보다 작을때만 print문을 실행하도록 이 아래줄에 if문을 추가.
if hour < 12 :
    print('오전입니다.')
