from string import ascii_lowercase

def letterAtPosition(index: int):
    alphabet = ascii_lowercase

    if index - 1 > len(alphabet) or index < 1 or isUnRegularNum(index):
        return None
    return alphabet[int(index) - 1] 

def isUnRegularNum(num):
    if not isinstance(num, int):
        if not isinstance(num, float):
            return True
        if num % 1 != 0:
            return True
    return False


if __name__ == "__main__":
    print(letterAtPosition(1))
    print(letterAtPosition(26.0))
    print(letterAtPosition(0))
    print(letterAtPosition(4.5))