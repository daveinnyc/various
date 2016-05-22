/* c.learncodethehardway.org ex11 */

/* Extra credit section: 
 *   fix to only allow 1 or 2 
 *   cmd line arguments
 *
 *
 *   TEST SCRIPT (Should be a single bash line)
 *   argArray=(); index=0 ; for args in "" "one " "two " "three " "four "  ; \\
 *   do argArray+=${args}  ; ./executable ${argArray[${index}]} ;  echo "" ; done 
 *
 */

   
#include <stdio.h>

int main(int argc, char *argv[])
{
    int i = 0;

    if(argc == 1) {
        printf("Needs cmd line arguments.\n");
    } else if(argc > 1 && argc < 4) {
        printf("Arguments:\n");

        //Print cmd line arguments, not executable name
        for(i = 1; i < argc; i++) {
            printf("%s ", argv[i]);
        }
        printf("\n");
    } else {
        printf("Too many arguments.\n");
    }

    return 0;
}
