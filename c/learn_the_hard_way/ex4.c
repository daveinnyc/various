//c.lerncodethehardway.org ex4

#include <stdio.h>
#include <stdint.h>

/* Code with problems for valgrind */

int8_t main()
{
    int8_t age = 10;
    //int8_t height;                             //Original line
    int8_t height = 72;

    //printf("I am %d years old\n");             //Original line
    printf("I am %d years old\n", age);
    printf("I am %d inches tall\n", height);

    return 0;
}
