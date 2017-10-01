/* 
* Three files to show how to put a typedef struct and 
*   functions into a header file.
*
* Copyright 2017 Dave Cuthbert, MIT license 
*/

#include <stdlib.h>
#include <stdio.h>
#include "typedef_in_header_file.h"


int main(int argc, char *argv[])
{
    Node *root;
    root = new_node();
    root->value = 1;  

    printf("ROOT: %d\n", root->value);
    
    Node *node_ptr = new_node();
    node_ptr = root;
    
    printf("NODE PTR: %d\n", root->value);

     
    /* Add another node */
    node_ptr->next = new_node();

    /* Move forward to new node */
    node_ptr = node_ptr->next;
    node_ptr->next = 0;
    node_ptr->value = 2;
    printf("NEW NODE: %d\n", node_ptr->value);
    
    return 0;
}
