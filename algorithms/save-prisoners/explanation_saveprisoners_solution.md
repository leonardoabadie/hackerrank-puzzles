# Abordagem

Para resolver esse desafio, eu considerei duas possiveis situacoes:

- O numero de prisioneiros e` maior do que o numero de doces para distribuir
- O numero de doces para distribuir e` maior do que o numero de prisioneiros (alguem vai receber maiis de um doce)

Para esse algoritmo, a variavel *rest* foi essencial ja que ela representa o numero de prisioneiros que nao receberam doce na primeira rodada

## Primeiro Caso

A primeira coisa que fiz foi checar se os prisioneiros estavam em maior quantidade do que o numero de doces disponiveis

*Suponha que tenhamos 10 prisioneiros e 8 doces. Comecamos a distribuir os doces a partir da primeira cadeira (a entrada seria `priosoners = 10 / sweets = 8 / start = 1`)*

Como `prisoners >= sweets` True, entao adicionamos doces com `chair = sweets = rest` desde que `start = 1`, variavel `rest` igual a zero `rest = start - 1`, portanto, comecamos do primeiro prisioneiro, e dai ninguem ficara sem doce.

Entao quando adicionamos `sweets` com `rest` nos pegariamos a posicao da cadeira que avisariamos. No entanto, se `rest` for maior que um, entao talvez teriamos um numero maior de prisioneiros. Para ajustar essa margem de erro, poderiamos simplesmente pensar em subtrair de chair o nº de prisioneiros `chair -= prisoners`, já que quando o último prisioneiro receber o doce(representado como prisoners), o restante dos doces deverá ser distribuído a partir do início(1), e daí quando fazemos `chair -= prisoners`(como se estivéssemos voltando do início) teremos um valor justamente menor que `prisoners` que é a pessoa que devemos alertar! 

*Faça um teste, ao invés de começar pela cadeira 1, vamos começar pela cadeira 8. O resultado seria:*

- `prisoners = 10 | sweets = 8 | start = 8`
- rest = 8 - 1 ~> 7  `rest = start - 1`
- chair = 8 + 7 ~> 15  `chair = sweets + rest`
- 15 > 10 ~> True  `if chair > prisoners`
- chair = 15 - 10 ~> 5  `chair = chair - prisoners`

**Portanto, devemos alertar o prisioneiro da cadeira número 5!**

## Segundo Caso

Confesso que para achar a solução quando o número de doces era maior que o nº de presidiários foi difícil. Tentei de várias maneiras. Falhava em 10/12 testes 7 vezes seguidas até achar a solução. Mas vamos por partes:

*Suponha que tenhamos 8 prisioneiros, 10 doces disponíveis e começaremos a distrbuí-los a partir da primeira cadeira, logo a entrada do algoritmo seria => `saveThePrisoner(8, 10, 1)`, ou seja `prisoners = 10 | sweets = 8 | start = 1`

A primeira coisa que eu pensei na minha última tentativa foi `sweets - prisoners`. Como resultado eu teria apenas o número de doces que sobraram e então distribuídos aos demais, no entanto, faltava um toque adicional...

Se fizermos `sweets - (prisoners - rest)` estaríamos tirando doces somente considernado a quantidade de prisioneiros que receberam doces na "primeira rodada", e novamente se você pensar, após o último prisioneiro receber o doce, se houver mais doces sobrando eles deverão ser entregues do início(1).

No caso acima `prisoners = 8 | sweets = 10 | start = 1`, deveríamos alertar `2`:

- rest = 1 - 1 ~> 0 `rest = start - 1`
- 8 > 10 ~> False `prisoners > sweets`
- chair = 10 - (8 - 0) ~> 2 `chair = sweets - (prisoners - rest)`
- 2 > 8 ~> False `chair > prisoners`
- `return 2`

Por último, vamos considerar o teste básico `prisoners = 3 | sweets = 7 | start = 3`

Se começarmos a partir da terceira cadeira, teremos 2 prisidiários sem comer na "primeira rodada". Com o mesmo cálculo acima obtemos:

- rest = 3 - 1 ~> 2 `start - 1`
- chair = 7 - (3 - 2) ~> 6 `chair = sweets - (prisoners - rest)`
- 6 > 3 ~> True `chair > prisoners`

Opa, não temos 6 cadeiras nem 6 presidiários, portanto não dá para alertar a pessoa da sexta cadeira. Para ajustar essa margem de erro podemos simplesmente extrair o resto entre eles por meio do `%`, visto que agora estaríamos começando do início(1), logo:

- chair = 6 % 3 ~> 0 `chair = chair % prisoners`

Também não há cadeira 0, mas sabemos então que todos os doces foram distribuídos a partir do início, sendo assim o último prisioneiro a receber o doce será o da última cadeira `3`:

- 0 == 0 ~> True `chair == 0`
- chair = 3 `chair = prisoners`