/* 
* Three files to show how to put a typedef struct and 
*   functions into a header file.
*
* Copyright 2017 Dave Cuthbert, MIT license 
*/

#include <stdio.h>
#include <stdlib.h>
#include "typedef_in_header_file.h"

Node * new_node(void)
{
    Node *n;
    n = (Node*) malloc(sizeof(Node));
    if(n == 0)
    {
        printf("Error creating node\n");
        exit(1);
    }
    n->next = 0;
    n->value = 0;

    return n;
}
