class Human():
    
    # 초기화 함수 __init__은 매개변수를 받을 수 있게 정의
    # __init__함수에 매개변수를 넘겨주는 방법은 Human의 인스턴스를 만들때 괄호 안에 매개변수의 값을 넣어주는 것
    def __init__(self, name, weight):
        self.name = name
        self.weight = weight
    
    def __str__(self):
        return "{} (몸무게 {}kg)".format(self.name, self.weight)
    
    def eat(self):
        self.weight += 0.1
        print("{}가 먹어서 {}kg이 되었습니다.".format(self.name, self.weight))
    
    def walk(self):
        self.weight -= 0.1
        print("{}가 걸어서 {}kg이 되었습니다.".format(self.name, self.weight))

person = Human('철수',65.0)
person.walk()
person.walk()
person.eat()


print(person)
