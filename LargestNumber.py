from functools import cmp_to_key
def compare(n1, n2):
    if n1 + n2 > n2 + n1:
        return -1
    else:
        return 1
def LargestNumber(array):
    if sum(array) == 0:
        return '0'
    for i in range(len(array)):
        array[i] = str(array[i])

    array = sorted(array, key=cmp_to_key(compare))
    return "".join(array)

if __name__ == '__main__':
    array=list(map(int,input().split()))
    print(LargestNumber(array))