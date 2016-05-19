/* c.learncodethehardway.org ex10 */

#include <stdio.h>

int main(int argc, char *argv[])
{
    int i = 0;

    for(i = 1; i < argc; i++){
        printf("arg %d: %s\n", i, argv[i]);
    }

    printf("argv[0]: %s\n", argv[0]);

    //An array of strings
    char *states[] = { 
        "California", "Oregon", "Texas",
        "Washington", "New York"
    };

    int num_states = 5;

    for(i = 0; i < num_states; i++){
        printf("ST: %d: %s\n", i, states[i]);
    }


    //Demonstrate 2x2 array
    for(i = 0; i < num_states; i++){
        printf("ST: %d: %c\n", i, states[i][0]);
    }

    /* Break it */
    //This segfaults -- index is unallocated memory
    /*
    for(i = 0; i < num_states + 1; i++){
        printf("ST: %d: %c\n", i, states[i][0]);
    }
    */

    /* Extra Credit 
     * Note: under valgrind argv[3] adds a shell variable
     * adds different shell variables depending on the
     * number of arguments given
     */
    states[2] = NULL;
    states[3] = argv[3];
    for(i = 0; i < num_states; i++){
        printf("ST-null: %d: %s\n", i, states[i]);
    }

    return 0;
}
