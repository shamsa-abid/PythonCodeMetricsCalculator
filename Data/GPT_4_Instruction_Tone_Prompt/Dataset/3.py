def below_zero(operations: List[int]) -> bool:
    balance = 0
    for i in operations:
        balance += i
        if balance < 0:
            return True
    return False
