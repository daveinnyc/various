/* c.learncodethehardway.org ex14 */


/* Extra Credit Section 
 *
 * Inline the can_print_it test
 *
 * Add output for isdigit 
 *
 */

#include <stdio.h>
#include <ctype.h>
#include <string.h>



//Function Declarations
void print_arguments(int argc, char *argv[]);
void print_letters(char arg[], int s_len);



void print_arguments(int argc, char *argv[])
{
    int i = 0;
    int s_length = 0;

    for(i = 0; i < argc; i++) {
        s_length = strlen(argv[i]);
        print_letters(argv[i], s_length);
    }
}

void print_letters(char arg[], int s_len)
{
    int i = 0;

    for(i = 0; i < s_len; i++) {
        char ch = arg[i];

        if(isalpha(ch) || isblank(ch)) {
            printf("'%c' == %d ", ch, ch);
        }

        if(isdigit(ch)) {
            printf("'#' == %d ", ch);
        }
    }

    printf("\n");
}


/* ############
   ##  MAIN  ##  
   ############ */
int main(int argc, char *argv[])
{
    print_arguments(argc, argv);
    return 0;
}

//EOF
