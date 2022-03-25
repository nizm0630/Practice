#자동차

class Car():
    def run(self):
        print("{}가 달립니다.".format(self.name))
        
taxi = Car()
taxi.name = "택시"
taxi.run()
