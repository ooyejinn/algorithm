def solution(phone_book):
    N = len(phone_book)
    phone_book.sort()
    
    for i in range(N-1):
        if phone_book[i+1].startswith(phone_book[i]):
            return False
                
    return True