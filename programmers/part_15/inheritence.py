class Car():
    
    def run(self):
        print("차가 달립니다.")

# Car를 상속받는 Truck클래스
class Truck(Car):
    
    def load(self):
        print("짐을 실었습니다.")
