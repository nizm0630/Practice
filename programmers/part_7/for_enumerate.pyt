#enumerate 리스트에서 return 값 2가지 1)리스트 번호 2)리스트 값

rainbow=["빨","주","노","초","파","남","보"]
for i,color in enumerate(rainbow):
    print('{}번째 색은 {}'.format(i+1,color))
