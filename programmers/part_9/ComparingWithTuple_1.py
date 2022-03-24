# [check_and_clear]는 딕셔너리 타입의 box를 매개변수로 받음
# box에 "불량품"이라는 이름표가 있으면 box 전체를 빈 딕셔너리로 만들어 버리고, 불량품이 없으면 box를 그대로 두는 함수

def check_and_clear(box):
    if "불량품" in box:
        box.clear()
        
box1 = {"불량품" : 10}
check_and_clear(box1)
# {}가 출력되어야합니다.
print(box1)

box2 = {"정상품": 10}
check_and_clear(box2)
# {"정상품": 10}가 출력되어야합니다.
print(box2)
