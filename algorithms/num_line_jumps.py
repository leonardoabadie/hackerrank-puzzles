# WEBSITE: HackerRank
#
# Algorithms.....
#
# Description:
#
# You are choreographing a circus show with various animals. For one act, you are given two kangaroos on a number line ready to jump in the positive direction (i.e, toward positive infinity).
#
# The first kangaroo starts at location x1 and moves at a rate of v1 meters per jump.
# The second kangaroo starts at location x2 and moves at a rate of v2 meters per jump.
# # You have to figure out a way to get both kangaroos at the same location at the same time as part of the show. If it is possible, return YES, otherwise return NO.
# The second kangaroo has a starting location that is ahead (further to the right) of the first kangaroo's starting location (i.e., x2 > x1). Because the second kangaroo moves at a faster rate (meaning v2 > v1) and is already ahead of the first kangaroo, the first kangaroo will never be able to catch up. Thus, we print NO.
#
# Minha observação:
#
# Considerando que v1 sempre incrementar *bem*mais a x1 do que v2 a x2, SE em algum momento X1 > X2 então ambos os cangurus nunca 
# alcançaram a mesma posição visto que a cada loop, o valor acrescentado a X1 o deixará muito mais a frente do que a posição do kanguru 2



# My solution ;)

def canCatchUp(x1, x2):
    return True if(x1 == x2) else False

def aheadPosition(position, jump):
    return position + jump

def v1IsTheHighestJump(v1, v2):
    return True if (v1 > v2) else False

def areSamePosition(x1, v1, x2, v2):
    if (v1IsTheHighestJump(v1, v2)):
        while (x1 < x2):
            x1 = aheadPosition(x1, v1)
            x2 = aheadPosition(x2, v2)

            if (canCatchUp(x1, x2)):
                return "YES"

    return "NO"

def kangaroo(x1, v1, x2, v2):
    return areSamePosition(x1, v1, x2, v2)


