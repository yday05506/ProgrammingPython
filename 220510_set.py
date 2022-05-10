games= {"LOL", "Overwatch", "Tetris", 1942, 2048}
print(games)    #{2048, 'Overwatch', 'Tetris', 'LOL', 1942}
                #{2048, 'Tetris', 'LOL', 'Overwatch', 1942}
empty_set = {}  #빈 dictionary
empty_set = set()   #빈 set
print(set({'google' : 'google.com', 18 : 'unesco.org'}))    #{18, 'google'} #key만 들어옴

#요소 추가
games.add("테일즈러너")
print(games)
games.update(("카트라이더", "지렁이"))
print(games)

#set 연산
#교집합
s3 = {3, 6, 9, 12}
s4 = {4, 8, 12, 16}
s3 & s4
print(s3.intersection(s4))

#합집합
s3 | s4
print(s3.union(s4))

#차집합
s3 - s4
print(s3.difference(s4))

#대칭 차집합
s3 ^ s4
print(s3.symmetric_difference(s4))

idol = ['세븐틴', '스트레이키즈', '악뮤', 'DKZ', 'DKZ']
print(idol)
print(list(set(idol)))  #중복 제거 : set() -> list()