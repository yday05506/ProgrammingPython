#숫자
student_number = 2106
age = 18
height = 161

#문자
name = '양다연'

print(f'학번 : {student_number}\n이름 : {name}\n나이 : {age}\n키 : {height}')  #학번 : 2106, 이름 : 양다연

#자료형 출력 #ctrl + d : 그 줄 복사
print(type(student_number)) #<class 'int'>
print(type(name))   #<class 'str'>
print(type(age))    #<class 'int>
print(type(height)) #<class 'int>

print(type(10.27))  #<class 'float'>
print(type(1027))   #<class 'int'>
print(type('1027'))   #<class 'str'>
print(10/27)   #java : 0, python : 0.37037037037037035
print(27/10)   #java : 2, python : 2.7
print(27//10)   #python : 나눈 몫 = 2
print(27%10)   #python : 나머지 = 7
print(type(10/27))   #<class 'float'>
print(type(10//27))   #<class 'int'>
print(10/5) #2.0 <class 'float'> -> 나누기를 하면 무조건 float