# ARRAY INTEIRO: a
# ARRAY INTEIRO: b
# ** os arrays recebidos como parâmetro não necessariamente possuem o mesmo tamanho **
# todos os elementos de a são fatores(divisores) de X(número em si) -- e
# X é um fator(divisor) de todos os elementos de b(multiplos)
# portanto ---> X precisa:     a[i] <= X <= b[j]   |||||   em que ~>   X % a[i]==0 && b[j] %X == 0 (todos)

# primeiro passo: verificar se a soma dos elementos de do array a é maior que a soma dos elementos de b
# se SIM, então não existe um número entre os dois arrays que atende aos critérios acima
# caso contrário, haverá pelo menos um elemento 

# segundo passo: ordenar tanto o array a quanto o array b para que:
# possamos listar todos os elementos maiores que o maior elemento de a e todos os elementos que são menores que o menor elemento de b
# interval_between_em = [x for x in range(a[-1], (b[-1]+1))]



# My solution ;)
def isFactor(a,b,x):
    div_result_a = []
    div_result_b = []

    for num_a in a:
        # True if an element a is a factor
        div_result_a.append(x%num_a==0)
    for num_b in b:
        # True if x is a factor
        div_result_b.append(num_b%x==0)

    return True if((False not in div_result_a) and (False not in div_result_b)) else False

def getTotalX(a,b):
    between_them = int()

    if (sum(a) <= sum(b)):
        # max(a) -- (min(b)+1) ~> range of numbers between two sets
        for x in range(max(a), (min(b)+1)):
            if isFactor(a,b,x):
                between_them +=1

    return between_them



# zubie7a(user) solution
# Python with comprehension lists, for each number between max(setA) and min(setB), it will create a list that will hold boolean
# values, and 'all' checks that all the boolean values in a list are true. 

lenA, lenB = map(int, raw_input().split())
setA = map(int, raw_input().split())
setB = map(int, raw_input().split())

maxA = max(setA)
minB = min(setB)
count = 0
for num in range(maxA, minB + 1):
    left = all([num % numA == 0 for numA in setA])
    right = all([numB % num == 0 for numB in setB])
    count += left*right

print(count)


# comments about above code // tradutor: comments on the code above
#
# wolfahoward user
# Was unaware of the all function. I was trying something similar to this with list comprehensions nested in a for loop, but I was
# removing options from a list within the range. I understood the question, but had no concept of the methods I should use to compare
# every element returning True. Appreciate the knowledge. I agree with the commenter below, found this pretty difficult.
#
# # luboyswag user
# Here is a documentation defintion from Python that defines the all and any function. Pretty useful.
# https://docs.python.org/3/library/functions.html#all
# https://docs.python.org/3/library/functions.html#any
#


