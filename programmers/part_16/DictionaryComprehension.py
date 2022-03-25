# 'product_dict' 를 상품의 이름을 키로 가지고, 가격을 값으로 가지는 딕셔너리 생성

product_list = ["풀", "가위", "크래파스"]
price_list = [800, 2500, 5000]
product_dict = { name:value for name, value in zip(product_list,price_list)}

print(product_dict)


'''

students = ["태연", "진우", "정현", "하늘", "성진"]
{"{}번".format(number):name for number, name in enumerate(students)}
    # {'2번': '정현', '0번': '태연', '1번': '진우', '4번': '성진', '3번': '하늘'}
    
students = ["태연", "진우", "정현", "하늘", "성진"]
scores = [85, 92, 78, 90, 100]
result = {x : y for x, y in zip(students, scores)}
    # {'성진': 100, '진우': 92, '하늘': 90, '태연': 85, '정현': 78}

'''
