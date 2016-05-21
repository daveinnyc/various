/* c.learncodethehardway.org ex11 */

#include <stdio.h>

int main(int argc, char *argv[])
{
    //Print out array
    int i = 0;
    while(i < argc){
        printf("arg %d: %s\n", i, argv[i]);
        i++;
    }
    printf("\n");

    //Parse each string in array
    char *states[] = {
        "California", "Oregon",
        "Washington", "Texas"
    };

    int num_states = 4;
    i = 0;
    while(i < num_states){
        printf("State %d: %s\n", i, states[i]);
        i++;
    }
    printf("\n");



    /* Extra Credit */
    i = num_states - 1;
    while(i >= 0){
        printf("State %d: %s\n", i, states[i]);
        i--;
    }
    printf("\n");

    
    char *states2[argc + num_states];
    i = 0;
    while(i < num_states){ 
        states2[i] = states[i];
        i++;
    }

    i = 1;
    while(i <= argc){
        states2[i + num_states - 1] = argv[i];
    i++;
    } 
    
    i = 0;
    while(i < (argc + num_states - 1)){ 
    printf("State %d: %s\n", i, states2[i]);
    i++;
    }

    return 0;
}

