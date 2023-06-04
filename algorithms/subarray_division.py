#  Retornar o número de possibilidades que Lily tem de dividir a barra de chocolate com base nos critérios citados... <= OBJETIVO/PROBLEMA PRINCIPAL
#
#   choco_bar ~> array de inteiros, onde cada quadradinho da barra de chocolate possui um nº de identificação
#   day ~> Refere-se ao dia que Ron nasceu
#   month ~> Refere-se ao mês que Ron nasceu
#
#   Critérios:
#   O somotário de elementos do array que resulte em day, sendo que a qtde. de elementos usadas na soma DEVE SER IGUAL AO VALOR DE month
#  
#   Sub-tarefas:
#
#   Ir somando uma qtde. de elementos(com base em month) e seus resultados, <= month como assistência
#   Incrementar 1 pra cada vez que a soma resultar em day
#  
#   Se é contíguo, eu sei que é da esquerda para a direita, lado a lado
#
#   O que eu preciso fazer/filtrar no choco_bar? 
#
#   retornar +1  toda vez que  s + s + s + s.......(month) == day (SE a soma....)  
# contiguous in this context: side-by-side element
# => choco_bar[i:i+month]
# sample: s=[2,2,1,3,2] | day=4 | month=2
# i=0 => choco_bar[i:i+month] ~> choco_bar[2,2]

# My solution ;)

def isSumTheSameDay(s, d):
    return s == d

def birthday(choco_bar, day, month):
    ways_to_share = int()

    for i, _ in enumerate(choco_bar):
            if (isSumTheSameDay(choco_bar[i:i+month],day)) and(
                len(choco_bar[i:i+month])==month):
                ways_to_share += 1
    
    return ways_to_share