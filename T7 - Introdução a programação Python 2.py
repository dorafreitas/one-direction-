def func1(a):
    return sum(a), sum(a)/len(a)


def func2(a,b,c):
    for i in range(len(a)):
        if a[i] == b:
            a[i] = c
        return a

def func3(num_linhas):
    for i in range(1, num_linhas + 1):
        print('*' * i)
