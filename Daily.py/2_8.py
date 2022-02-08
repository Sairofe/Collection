# format 및 문자열 자료형 예제
'''
c = "  I ate {name}, so I'm {condition} now  ".format(name="banana", condition="full")
print(c.replace("banana","apple"))
print(c.strip())
'''
# format 축약형
'''
name = "Kal"
a = f"My name is {name}"
print(a)
'''
#list 활용
'''
a=["apple","banana","orange","plum","watermelon"]
a[1]="melon"
a[0:2]=[]
print(a[0])
a.append("brown")
a.sort()
print(a)
'''

'''
a = [1,2,5,7,1,1,1]
a.reverse()
a.insert(0,4)
a.remove(1)
print(a)
print(a.count(1))

'''

# 02장 연습문제



'''
# 평균 점수 구하기
a = 80
b = 75
c = 55
print((a+b+c)/3)

#자연수 13이 홀수인지 짝수인지 판별
a=13%2
if(a==1):
    print("13은 홀수입니다.")
else:
    print("13은 짝수 입니다.")
    

#문자열 슬라이싱
a = "881120-1068234"
b = a[:6]
c = a[7:]
print(b)
print(c)


#문자열 인덱싱
pin = "881120-1068234"
print(pin[7])
if (pin[7]==1):
    print("이 사람은 남자입니다.")
elif(pin[7]==2):
    print("이 사람은 여자입니다.")
else:
    print('성별을 알 수 없습니다.')


#replace 함수 사용하기
a = "a:b:c:d"
b = a.replace(":","#")
print(b)


#숫자 정렬하기
a = [1, 3, 5, 4, 2]
a.sort()
a.reverse()
print(a)
'''

#
a = ['Life','is','too','short']
b = " ".join(a)
print(b)