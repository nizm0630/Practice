# 'OR' 연산의 결과는 앞의 값이 True이면 앞의 값을, 앞의 값이 False이면 뒤의 값을 따릅

a = 10 or 110    # 1의 bool 값은 True입니다.
b = 0 or 10    # 0의 bool 값은 False입니다.

print("a:{}, b:{}".format(a, b))
