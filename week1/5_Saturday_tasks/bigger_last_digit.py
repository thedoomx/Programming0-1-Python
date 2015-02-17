n = input("n= ")
n = int(n)

m = input("m= ")
m = int(m)

n_last_digit = n % 10
m_last_digit = m % 10

if n_last_digit > m_last_digit:
    print("N's last digit is bigger")
elif n_last_digit < m_last_digit:
    print("M's last digit is bigger")
else:
    if n > m:
        print("N's last digit and M's last digit are equal, but N > M")
    else:
        print("N's last digit and M's last digit are equal, but N < M")
