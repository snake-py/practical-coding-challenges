


def strMatchBy2Char(str1: str, str2: str)-> int: 
    if (len(str1) == 0 or len(str2) == 0): 
        return 0
    count = 0
    for i in range(len(str1)-1): 
        if (str1[i:i+2] == str2[i:i+2]): 
            count += 1
    return count


if __name__ == "__main__": 
    print(strMatchBy2Char("yytaazz", "yyjaaz"))
    print(strMatchBy2Char("edabit", "ed"))
    print(strMatchBy2Char("xxxx", "xx"))
    print(strMatchBy2Char("", ""))