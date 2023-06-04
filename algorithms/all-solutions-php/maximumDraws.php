<?php
/*
Introduction of the challenge: 'If there are n($colors) colors of socks in the drawer, how many socks
need to be removed to be certain of having a matching pair?' i.e.
	=> the minimum number of socks to remove to guarantee a corresponded pair  

My line of reasoning (breaking it down 'step-by-step') :

If there are 'n' colors of socks and each of them got a pair (2), then the total
of socks is n * 2. So if I catch 'n' socks, the next time I get another one,  
it will form a pair with the other one I have took before.

*/

function maximumDraws(int $colors): int {
	return $colors + 1;
}
?>