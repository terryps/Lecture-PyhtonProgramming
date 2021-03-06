import time
def is_prime(n):
    if n > 1:
        for i in range(2,n):
            if n%i==0:
                return False
        return True
    else:
        return False
    
def all_primes(n):
    lst=[]
    for i in range(1,n+1):
        if is_prime(i):
            lst.append(i)
    return lst

def sieve(n):
    lst = [i for i in range(2,n+1)]
    for k in lst:
        if k>0:
            for i in range(2,n):
                p=k*i
                if p<=n:
                    lst[p-2] = 0
                else:
                    break
    return [x for x in lst if x > 0]

def is_all_prime(lst):
    for i in lst:
        if is_prime(i)==False:
            return False
    return True

lst = sieve(100000)
cur = time.time()
print(is_all_prime(lst))
print(time.time()-cur)

n = input("enter number: ")
n = int(n)

def psum(n):
    lst = sieve(n)
    sum_lst=[0]
    sum = 0
    for i in lst:
        sum+=i
        sum_lst.append(sum)
    for j in range(2,len(sum_lst)):
        for i in range(0, j-1):
            if is_prime(sum_lst[j]-sum_lst[i]):
                print("{0} {1}".format(lst[i:j],sum_lst[j]-sum_lst[i]))
psum(n)
