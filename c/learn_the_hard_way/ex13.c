/* c.learncodethehardway.org ex13 */

/* Extra Credit Section 
 *
 * move break inside if y > 2 block:
 *    fixes case where y is the first letter
 *
 * allow multiple arguments on cmd line  
 *
 * Adjust ascii values to make all lowercase
 *
 *
 * TEST STRING:
 * ./executable yaeiouy AEIOUY THJqwrt
 *
 */

   
#include <stdio.h>

int main(int argc, char *argv[])
{
    // Fix check to allow multiple arguments
    if(argc < 2) {
        printf("ERROR: You need at least one argument.\n");
        return 1;

    }
  
    for (int j = 1; j < argc; j++) {
        for(int i = 0; argv[j][i] != '\0'; i++) {
            char letter = argv[j][i];

            //Adjust ascii value to make lowercase
            if ((int)letter < 97){
                letter = (int)letter + 32; 
            }

            switch(letter) {
                case 'a':
                    printf("%d: 'a'\n", i);
                    break;

                case 'e':
                    printf("%d: 'e'\n", i);
                    break;

                case 'i':
                    printf("%d: 'i'\n", i);
                    break;

                case 'o':
                    printf("%d: 'o'\n", i);
                    break;

                case 'u':
                    printf("%d: 'u'\n", i);
                    break;

                case 'y':
                    if(i > 2) {   //e.g. 'by'
                        printf("%d: 'Y'\n", i);
                    break;
                    }

                default:
                    printf("%d: %c is not a vowel\n", i, letter);
            }//End switch(letter)
        }//End for argv[i]
    }//End for j

    return 0;
}//End main

//EOF
