def count_valleys(steps:int, path:str) -> int:
    sea_level, crossed_valleys, walk, i = 0

    while i < steps:
        if (path[i] == "U"):
            walk += 1
        else:
            walk -= 1

        if (walk == sea_level) and (path[i-1] < sea_level):
            crossed_valleys += 1

        i += 1

    return crossed_valleys

#########################################################
def count_valleys(steps:int, path:str) -> int:
    sea_level, crossed_valleys, count, prev_count = 0

    for step in path:
        if (step == "U"):
            prev_count = count
            count += 1
        else:
            prev_count = count
            count -= 1

        if (count == sea_level) and not(prev_count > sea_level):
            crossed_valleys += 1

    return crossed_valleys
#########################################################
def count_valleys(num_steps:int, steps:str) -> int:
    sea_level = crossed_valleys = walk = prev_walk =  0

    for step in steps:
        prev_walk = walk

        if (step == "U"):
            walk += 1
        else:
            walk -= 1

        if (walk == sea_level) and (prev_walk < sea_level):
            crossed_valleys += 1

    return crossed_valleys
###########################################################
def count_valleys(num_steps:int, steps:str) -> int:
    sea_level = crossed_valleys = walk = 0

    for step in steps:
        walk += 1 if (step == "U") else -1

        if (walk == sea_level) and (step == "U"):
            crossed_valleys += 1

    return crossed_valleys
