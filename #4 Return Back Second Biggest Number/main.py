

def secondLargestNumber(arr):
    arr.sort()
    return arr[-2]


if __name__ == "__main__":
    print(secondLargestNumber([10, 40, 30, 20, 50]))
    print(secondLargestNumber([25, 143, 89, 13, 105]))
    print(secondLargestNumber([54, 23, 11, 17, 10]))