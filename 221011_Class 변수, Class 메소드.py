# 클래스 변수 : 객체로 생성하지 않아도 클래스에 하나 존재하는 변수
# 클래스 메소드 : 객체로 생성하지 않아도 클래스에 하나 존재하는 메소드

# 학생
# 속성 : 학번, 이름
class Student:
    def __init__(self, student_number, name):
        self.student_number = student_number
        self.name = name
    def __str__(self):  # {} 안에 변수 넣을 땐 self로 불러오기
        return f'학번 : {self.student_number}\t 이름 : {self.name}'
    def __getitem__(self, key): # 객체[key] 재정의
        if key == '학번':
            return self.student_number
        # 객체['학년'] 했을 때, return 학년
        if key == '학년':
            return int(self.student_number) // 1000
            # return self.student_number[0]

# 동아리
# 속성 : 동아리명, 장소, 멤버들
# 메소드 : 장소 설장하자(), 멤버 추가하자(), 활동하자()
class Club:
    count = 0   # 클래스 변수 : 클래스로 만들어진 객체가 모두 공유하는 변수

    @classmethod    # 어노테이션을 붙였기 때문에 cls가 붙음
    def get_count_club(cls):
        return f'만들어진 클래스 수 : {cls.count}'

    def __init__(self, name):
        self.name = name
        self.location = None
        self.members = []    # 여러 개기 때문에 빈 리스트 넣기
        Club.count += 1 # 클래스 변수 수정
    def __str__(self):
        s = ''
        for member in self.members:
            s += str(member) + "\n"
        return f'동아리명 : {self.name}\t 장소 : {self.location}\n멤버들 : {s}'

    def set_location(self, location):
        self.location = location

    def add_member(self, student):
        self.members.append(student)    # 리스트에 아이템 추가   # 지우는 건 append 대신 remove
    def set_action(self, action):
        self.action = action
    def act(self):  # 동아리 개수 출력
        print(self.action)
    def __len__(self):  # 동아리 멤버 수 리턴
        return len(self.members)
    def __del__(self):  # del 객체 했을 때, 메모리에서 삭제하기 전에 실행
        print(f'{self.name}은/는 간다.')



학생1 = Student('2213', '임채영')
print(학생1)
학생2 = Student('2106', '양다연')
print(학생2)

동아리1 = Club('사진반')
동아리1.set_location('실습 1실')
동아리1.set_action('사진 찍기')
동아리1.add_member(학생2)
동아리1.add_member(학생1)
print(동아리1)
동아리1.act()

동아리2 = Club('보드게임반')
동아리2.set_action('보드게임 하기')
동아리2.add_member(학생1)
print(동아리2)

print(Club.count)
# print(동아리1.count)   # 그렇지만 위 문장으로 출력하는 것이 훨 나음
print(Club.get_count_club())
#print(동아리2.get_count_club())


#사진반 멤버 수 출력
print(len(동아리1.members))

# 특수 메소드 -> 주관식
# __init__(self, ...) : 생성자. 멤버 변수 초기화
# __str__(self) : 클래스의 객체를 string화(문자열화)하여 리턴(주로 객체의 속성을 알아볼 수 있도록 정보 표시) -> str(객체)를 다시 재정의
# __len__(self) : len(객체)할 때 무엇을 리턴할 지 재정의
print('__len__()')
print(len(동아리1))
# __getitem__(self, key) : 객체[key] 재정의
print('__getitem--()')
print(학생1)
print(학생1['학번'])    # print(학생1.student_number)
print(학생1['학년'])
# __del__(self) # 객체를 명시적으로 지울 때 호출되는 메소드
print('__del__()')
print(동아리1)
del(동아리1)
print(동아리1)