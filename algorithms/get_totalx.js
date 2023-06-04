// Gloud(user) solution
function getTotalX(a, b) {
    let validCount = 0;
    
    for (let x = 1; x <= 100; x++) {
        if (a.every(int => (x % int == 0))) {
            if (b.every(int => (int % x == 0))) {
                validCount++;
            }
        }
    }

    return validCount;
}


// // zubie7a(user) solution
// Python with comprehension lists, for each number between max(setA) and min(setB), it will create a list that will hold boolean
//values, and 'all' checks that all the boolean values in a list are true. 