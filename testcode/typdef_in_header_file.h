/* 
* Three files to show how to put a typedef struct and 
*   functions into a header file.
*
* Copyright 2017 Dave Cuthbert, MIT license 
*/

/* Linked list helpers */
#include <stdio.h>

typedef struct Node 
{
    int value;
    struct Node *next;
} Node;

Node * new_node();
