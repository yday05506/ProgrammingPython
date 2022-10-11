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