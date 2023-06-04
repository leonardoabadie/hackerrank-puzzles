"""
    1º passo: regitrar todas as ocorrências de cada tipo de pássaro(identificado pelo ID);
    2º passo: descobrir o(s) elemento(s) de maior ocorrência no array id_birds;
    3º passo: verificar se há mais de um elemento com maior ocorrência. Se houver, retornar
    o menor entre eles;
"""


def migratoryBirds(id_birds):
    occurrences = dict()

    for type_bird in id_birds :
        if not occurrences.get(type_bird, 0):
            occurrences[type_bird] = id_birds.count(type_bird)

    max_occurence = max(occurrences.values())
    type_birds = list()
    
    for type_bird, occurence in occurrences.items():
        if occurence == max_occurence:
            type_birds.append(type_bird)

    return min(type_birds)