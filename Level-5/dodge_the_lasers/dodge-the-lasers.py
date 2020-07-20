# sqrt2 decimals up to 100 digits
sqrt2_minus_one = 4142135623730950488016887242096980785696718753769480731766797379907324784621070388503875343276415727

# making use of Beatty sequences =>  a(n) = floor(n*sqrt(2))
# calculate the sum recursively
# S(n) = [(n * (n + 1)) - (n' * (n' + 1))] / 2 - [n * n'] where n' = floor(n * (sqrt(2) - 1))
def solution(str_n):
    return str(recurse(int(str_n)));

def recurse(n):
    if(n <= 1):
        return n;
    n_prime = (sqrt2_minus_one * n) // 10**100
    return (n * (n + 1)  - n_prime * (n_prime + 1)) // 2 + (n * n_prime) - recurse(n_prime);

n = '5'
print(
solution(n)
)

