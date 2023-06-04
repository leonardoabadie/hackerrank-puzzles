## Read Me
```python
def save_the_prisoner(prisoners, sweets, start):
    rest = start - 1
    if prisoners >= sweets:
        chair = sweets + rest
        if chair > prisoners:
            chair -= prisoners
    else:
        chair = sweets - (prisoners - rest)
        if chair > prisoners:
            chair = chair % prisoners
            if chair == 0:
                chair = prisoners
    return chair
```
<br>

## *Explanation*

<p>
Well, to solve this challenge, I considered two possible situations:
</p>

- ~> The number of prisoners is greater than the number of candies to distribute;
- ~> The number of sweets to distribute is greater than the number of prisoners(someone will receive more than a candy)
<br>

<p>
To this algorithm, the *rest* variable was essential since she represents the number of prisoners that didn't receive sweets in the *"first round"*.
</p>

### Primeiro Caso

<p>
So the first thing I did was check if prisoners were greater than the number of candies available.
</p>

*Suppose we have ten prisoners and eight sweets. We start to distribute the sweets from the first chair(the input would like `prisoners = 10| sweets = 8 | start = 1 `.)*

<p>
As `prisoners >= sweets` is true, we add sweets with rest `chair = sweets + rest` since if `start = 1`, `rest` variable is equal to zero `rest = start - 1` i.e. we start from the first prisoner, therefore isn't nobody missing.
So when we plus sweets with *rest* we would take the chair id that we should warn. However, if `rest` is greater than one, perhaps we would have a value great the number of prisoners. Para ajustar essa margem de erro, poderiamos simplesmente pensar em subtrair de chair o nº de prisioneiros `chair -= prisoners`, já que quando o último prisioneiro receber o doce(representado como prisoners), o restante dos doces deverá ser distribuído a partir do início(1), e daí quando fazemos `chair -= prisoners`(como se estivéssemos voltando do início) teremos um valor justamente menor que `prisoners` que é a pessoa que devemos alertar!
</p>

*Faça um teste, ao invés de começar pela cadeira 1, vamos começar pela cadeira 8. O resultado seria:*

- prisoners = 10 | sweets = 8 | start = 8
- rest = 8 - 1 ~> 7  `rest = start - 1`
- chair = 8 + 7 ~> 15  `chair = sweets + rest`
- 15 > 10 ~> True  `if chair > prisoners`
- chair = 15 - 10 ~> 5  `chair = chair - prisoners`

**Portanto, devemos alertar o prisioneiro da cadeira número 5!**

### Segundo Caso

<p>
Confesso que para achar a solução quando o número de doces era maior que o nº de presidiários foi difícil. Tentei de várias maneiras. Falhava em 10/12 testes 7 vezes seguidas até achar a solução. Mas vamos por partes:
</p>

*Suponha que tenhamos 8 prisioneiros, 10 doces disponíveis e começaremos a distrbuí-los a partir da primeira cadeira, logo a entrada do algoritmo seria => saveThePrisoner(8, 10, 1), ou seja*
*prisoners = 10 | sweets = 8 | start = 1*

A primeira coisa que eu pensei na minha última tentativa ;( foi `sweets - prisoners`. Como resultado eu teria apenas o número de doces que sobraram e então distribuídos aos demais, no entanto, faltava um toque adicional...
Se fizermos `sweets - (prisoners - rest)` estaríamos tirando doces somente considernado a quantidade de prisioneiros que receberam doces na "primeira rodada", e novamente se você pensar, após o último prisioneiro receber o doce, se houver mais doces sobrando eles deverão ser entregues do início(1).

No caso acima `prisoners = 8 | sweets = 10 | start = 1`, deveríamos alertar `2`:

- rest = 1 - 1 ~> 0 `rest = start - 1`
- 8 > 10 ~> False `prisoners > sweets`
 - chair = 10 - (8 - 0) ~> 2 `chair = sweets - (prisoners - rest)`
 - 2 > 8 ~> False `chair > prisoners`
 - return 2

<p>
Por último, vamos considerar o teste básico `prisoners = 3 | sweets = 7 | start = 3`
</p>

<p>
Se começarmos a partir da terceira cadeira, teremos 2 prisidiários sem comer na "primeira rodada". Com o mesmo cálculo acima obtemos:
</p>

- rest = 3 - 1 ~> 2 `start - 1`
- chair = 7 - (3 - 2) ~> 6 `chair = sweets - (prisoners - rest)`
- 6 > 3 ~> True `chair > prisoners`

Opa, não temos 6 cadeiras nem 6 presidiários, portanto não dá para alertar a pessoa da sexta cadeira. Para ajustar essa margem de erro podemos simplesmente extrair o resto entre eles por meio do `%`, visto que agora estaríamos começando do início(1), logo:

- chair = 6 % 3 ~> 0 `chair = chair % prisoners`

Também não há cadeira 0, mas sabemos então que todos os doces foram distribuídos a partir do início, sendo assim o último prisioneiro a receber o doce será o da última cadeira `3`:

- 0 == 0 ~> True `chair == 0`
- chair = 3 `chair = prisoners`

<br>

Bem é isso. Desculpe pelo tamanho do texto, é a minha primeira vez comentando XD e eu quis explicar pra mim mesmo como eu cheguei a solução, mas eu espero que tenha ajudado quem quer que tenha lido isso (embora minha solução não seja tão simples como `print(((S - 1 + M - 1) % N) + 1)` que vi em alguns comentários).

Thanks..!
