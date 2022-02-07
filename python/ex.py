a = 80
b = 75
c = 55
d = ((a+b+c)/3)
print(f"1) 평균은 {d}점 입니다.")
a=13 % 2
if a == 1 :
    print('2) 홀수입니다.')
else:
    print('2) 짝수입니다.')
        
a=("881120-1068234")
year = a[:2]
month = a[2:4]
day = a[4:6]
print(f"3) Year : {year}, Month : {month}, Day : {day}")

if a[7] == '1':
    print('4) M')
else:
    print('4) F')
    
a = "a:b:c:d"
b = '5) '
print(b + a.replace(":", "#"))

a = [1,3,5,4,2]
b = '6) '
a.sort()
a.reverse()
print(a)

a = ['Life','is','too','short']
result = " ".join(a)
print(a)

a = (1, 2, 3)
a = a + (4,)
print(a)

## 9
a = dict()

##10
a = {'A':90, 'B':80, 'C':70}
result = a.pop('B')
print(a)
print(result)

##11
a = [1, 1, 1, 2, 2, 3, 3, 3, 4, 4, 5]
aSet = set(a)
b = list(aSet)
print(b)
