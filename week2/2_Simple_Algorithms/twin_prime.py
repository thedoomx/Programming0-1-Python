p = input("p= ")
p = int(p)

def is_prime(n):
    start = 2
    is_prime = True
    
    while start < n:
        if n % start == 0:
            is_prime = False
            break
        
        start += 1
        
    return is_prime

q_p = p - 2
p_q = p + 2

if is_prime(p) == False:
    print(str(p) + " is not a prime.")
elif is_prime(p) == True and is_prime(q_p) == True and is_prime(p_q) == True:
    print("Twin primes with " + str(p) + ":")
    print(str(q_p) + ", " + str(p))
    print(str(p) + ", " + str(p_q))
elif is_prime(p) == True and is_prime(q_p) == False and is_prime(p_q) == True:
    print("Twin primes with " + str(p) + ":")
    print(str(p) + ", " + str(p_q))
elif is_prime(p) == True and is_prime(q_p) == True and is_prime(p_q) == False:
    print("Twin primes with " + str(p) + ":")
    print(str(q_p) + ", " + str(p))
else:
    print(str(p) + " is prime but:")
    print(str(q_p) + " is not")
    print(str(p_q) + " is not")
    
