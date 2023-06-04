def squares(a:int, b:int):
    numbers = [n for n in range(a, b + 1)]

    for n in range(a, b + 1):
        base = 2
        while abs(base - (n * base)) > 0.00001:
            p = (base + (n / base)) / 2
            base = p

        print(p, end=" ")

n = float(input("Digite um número para encontrar a sua raiz quadrada: "))
p = n
b = 2
while abs(n - (b * b)) > 0.00001:
    p = (b + (n / b)) / 2
    b = p
print(f"A raiz quadrada de {n} é aproximadamente {p:8.4f}")

