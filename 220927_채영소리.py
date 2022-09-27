#옆친구와 클래스 구조 만들고
#객체화 하고
#상속하고
#출력

'''
사람 - 이름, 나이, 성별
선생님 - 과목, 담임반
'''

class People:
    def __init__(self, name):
        self.name = name
        self.age = None
        self.gender = None

    def set_age(self, age):#매개변수와 함수이름을 같게하지말것
        self.age = age

    def set_gender(self, gender):
        genders = ['여자','남자']
        if gender in genders:
            self.gender = gender
    def __str__(self):
        return f'{self.name}\t{self.age}\t{self.gender}'

# people에 값넣기
고나근샘 = People('고낙은')
고나근샘.set_age('34')
고나근샘.set_gender('남자')
print(고나근샘)

class Teacher(People):
    def subject(self, sub):
        self.sub = sub
    def HRT(self, hrt):
        self.hrt = hrt
    def __str__(self):
        return f'{super().__str__()}\t담당과목: {self.sub}\t담임반: {self.hrt}'


#Teacher에 값넣기
고낙은샘 = Teacher('고낙은')

고낙은샘.subject('체육')
고낙은샘.HRT('2-2')
print(고낙은샘)