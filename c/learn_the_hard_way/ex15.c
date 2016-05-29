/* c.learncodethehardway.org ex15
 *
 * Extra credit exercises
 * 
 *
 */

#include <stdio.h>

int main(int argc, char *argv[])
{
    int ages[] = {23, 43, 12, 89, 2};
    char *names[] = {"Alan", "Frank", "Mary",
                     "Johnny", "Lisa"};

    /* Get size safely */
    int count = sizeof(ages) / sizeof(int);
    int i = 0;

    /* Use indexing */
    for( i = 0; i < count; i++){
        printf("I: %s has %d years\n", names[i], ages[i]);
    }

    printf("----\n");

    /* Set pointers to array start */
    int *cur_age = ages;
    char **cur_name = names;

    /* Use pointers  */
    for( i = 0; i < count; i++){
        printf("P: %s is %d years old\n", *(cur_name + i), 
                *(cur_age + i ));
    }

    printf("----\n");
   
    /* Pointers as arrays */
    for( i = 0; i < count; i++){
        printf("PaA: %s is %d years old\n", cur_name[i],
                    cur_age[i]);
    } 

    printf("----\n");

    /* Overly complex pointers */
    for(cur_name = names, cur_age = ages; (cur_age - ages) < count;
        cur_name++, cur_age++){
        printf("OCP: %s is %d years old\n", *cur_name, *cur_age);
    } 


    printf("----\n");

    /* Print out Addresses */
    i = 0;
    while(i < count){
        printf("Addr: %p\n", &ages[i]);
        i++;
    } 

    return 0;
}

//EOF
