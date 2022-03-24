list1 = [1, 2, 3, 4]

# list1의 1번째 자리에 8을 넣고 원래 있던 값은 오른쪽으로 밀기
list1.insert(0,8)
print("첫 번째 자리에 8을 넣은 결과 : {}".format(list1))

# list1을 작은 수부터 큰 수로 정렬
list1.sort()
print("list1을 작은 수부터 큰 수로 정렬한 결과 : {}".format(list1))

# list1을 거꾸로 만들어 보세요
list1.reverse()

print("list1을 거꾸로 정렬한 결과 : {}".format(list1))
