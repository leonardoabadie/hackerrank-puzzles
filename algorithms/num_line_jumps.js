/*
* Autor: Matias
* Data: 05/07/22
*
* WEBSITE: HackerRank
* Algorithms.....
* Description(Ensligh obvious):
* You are choreographing a circus show with various animals. For one act, you are given two kangaroos on a number line ready to jump in * the positive direction (i.e, toward positive infinity).
* The first kangaroo starts at location x1 and moves at a rate of v1 meters per jump.
* The second kangaroo starts at location x2 and moves at a rate of v2 meters per jump.
* You have to figure out a way to get both kangaroos at the same location at the same time as part of the show. If it is possible,
* return YES, otherwise return NO.
* The second kangaroo has a starting location that is ahead (further to the right) of the first kangaroo's starting location (i.e., x2 > * x1). Because the second kangaroo moves at a faster rate (meaning v2 > v1) and is already ahead of the first kangaroo, the first
* kangaroo will never be able to catch up. Thus, we print NO.
*
* Minha observação:
* Considerando que v1 sempre vai incrementar mais a x1 do que v2 a x2, SE em algum momento X1 > X2, como consequência => 
* ambos os cangurus nunca alcançaram a mesma posição visto que a cada loop, o valor acrescentado a X1 o deixará "muito" 
* mais a frente do que a posição do kanguru 2
*/

// My solution



function canCatchUp(x1, x2) {
    if (x1 == x2) {
        return true;
    }
    return false;
}

function aheadPosition(position, jump) {
    return position + jump;
}


function v1IsTheHighestJump(v1, v2) {
    if (v1 > v2) {
        return true;
    }
    return false;
}

function areSamePosition(x1, v1, x2, v2) {
    if (v1IsTheHighestJump(v1, v2)) {
        while (x1 < x2) {
            x1 = aheadPosition(x1, v1);
            x2 = aheadPosition(x2, v2);

            if (canCatchUp(x1, x2)) {
                return "YES";
            }
        }
    }

    return "NO";
}

function kangaroo() {
    var x1, v1, x2, v2;
    
    let same_position = areSamePosition(x1, v1, x2, v2);    
    return same_position;
}

function main() {
    console.log(kangaroo);
}

