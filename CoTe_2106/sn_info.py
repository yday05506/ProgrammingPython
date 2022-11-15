def student_number_to_info(student_number):
    #학년의 첫 번째는 학년, 두 번째는 반, 세 번째, 네 번째는 번호
    grade = student_number[0]
    class_ = student_number[1]
    #반이 1,2면 뉴미디어소프트웨어과
    if class_ == '1' or class_ == '2':
        major = '뉴미디어소프트웨어과'
    #반이 3,4면 뉴미디어웹솔루션과
    elif class_ == '3' or class_ == '4':
        major = '뉴미디어웹솔루션과'
    #반이 5,6이면 뉴미디어디자인과
    elif class_ == '5' or class_ == '6':
        major = '뉴미디어디자인과'
    number = student_number[2:4]
    return f'{grade}학년 {class_}반 {number}번 {major}'

print(student_number_to_info("2213"))
