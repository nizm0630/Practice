class Car():
    
    def __init__(self, name):
        self.name = name
    
    def run(self):
        print("차가 달립니다.")


class Truck(Car):
  
    # __init__ 메소드 오버라이드
    def __init__(self, name, capacity):
        super().__init__(name)
        self.capacity = capacity
    
    def load(self):
        print("짐을 실었습니다.")
        
Truck1 = Truck("소렌토", 50)
