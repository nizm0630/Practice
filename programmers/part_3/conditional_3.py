# 매 6시간마다 종이 울리는 시계를 구현하기 위해 hour에 저장된 현재 시간이 0,6,12,18시(6의 배수)일때만 print문이 실행되도록 코드7번째줄에 if문을 추가

from datetime import datetime 
hour = datetime.now().hour

#현재 시간이 6의 배수일 때만 print문이 실행되도록 아래줄에 if문을 추가하세요
if hour % 6 == 0 :
    print('종이 울립니다.')#if문을 추가한 이후 이 줄은 들여쓰기 되어야 합니다.
