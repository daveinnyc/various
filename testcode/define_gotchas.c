/* 
* Demonstrate why TWO * TWO doens't equal 4
*
* Copyright 2017 Dave Cuthbert, MIT license 
*/

#include <stdio.h>
#define TWO 1 + 1
#define WHAT TWO * (TWO + TWO)
#define HMM 1 + 1 * (1 + 1 + 1 + 1)

int main(int argc, char **argv)
{

    printf("T %d\n", TWO);
    // Preprocessor substitutes then evaluates, so 5 instead of 8
    printf("W %d\n", WHAT);
    printf("H %d\n", HMM);

	return 0;
}

/* 
OUTPUT

T 2
W 5
H 5

*/
