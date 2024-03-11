from string import Template

def solution(phone_book):
    phone_book.sort()
    # 문자열 정렬을 하게 되면 비슷한 문자열끼리 인접하게 됨
    for i in range(len(phone_book)-1):
        if (phone_book[i+1].startswith(phone_book[i])):
            return False

    return True