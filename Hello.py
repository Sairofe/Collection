# format 및 문자열 자료형 예제
'''
c = "  I ate {name}, so I'm {condition} now  ".format(name="banana", condition="full")
print(c.replace("banana","apple"))
print(c.strip())
'''

a=["apple","banana","orange","plum","watermelon"]
a[1]="melon"
a[0:2]=[]
print(a[0][0])
a.append("brown")
a.sort()
print(a)