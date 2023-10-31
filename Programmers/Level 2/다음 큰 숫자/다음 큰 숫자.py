def solution(n):
    key = bin(n).count("1")
    while True:
        n+=1
        if bin(n).count("1") == key:
            return n