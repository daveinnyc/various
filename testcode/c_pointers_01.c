/* 
* Demonstrate relationship between pointers and arrays 
*
* Copyright 2017 Dave Cuthbert, MIT license 
*/

#include <stdio.h>

int main(int argc, char **argv)
{
    char c[10] = {0};
    char *pc;

    c[2] = 'a';
    pc = c;

    /* array c[] */
    printf("c[]: %u\n", c); 

    /* address at ptr to c is the same */
    printf("pc:  %u\n", pc);

    /* value at the ptr to c is the same as c[0] */
    printf("*pc:  %u\n", *pc);
    printf("&c[0]: %u\n", &c[0]);

    /* increment the pointer twice to move along the 
     * c[] array.
     */
    pc++;
    pc++;
        
    /* Check the value at c[2] equals value at ptr pc */
    printf("*pc:  %c\n", *pc);
    printf("c[2]:  %c\n", c[2]);

    return 0;
}
