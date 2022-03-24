#튜플로 리턴하기 위해 리스트나 딕셔너리를 이용가능
#딕셔너리의 items()를 이용하여 튜플을 리턴할 때에는 *를 사용

products = {"풀" : 800, "색종이": 1000}

for product_detail in products.items():
    print("{}의 가격: {}원".format(*product_detail))
