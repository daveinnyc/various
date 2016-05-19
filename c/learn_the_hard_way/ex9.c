/* c.learncodethehardway.org ex9 */

#include <stdio.h>

int main(int argc, char *argv[])
{
    int numbers[4] = {0};
    char name[4] = {'a'};

    //Print them as is
    printf("nums: %d %d %d %d\n",
            numbers[0], numbers[1],
            numbers[2], numbers[3]);

    printf("chars: %c %c %c %c\n",
            name[0], name[1], 
            name[2], name[3]); 

    printf("name: %s\n", name);

    //Set up numbers
    numbers[0] = 1;
    numbers[1] = 2;
    numbers[2] = 3;
    numbers[3] = 4;

    //Setup name
    name[0] = 'Z';
    name[1] = 'e';
    name[2] = 'd';
    name[3] = '\0';

    //Print out intitialized
    printf("nums: %d %d %d %d\n",
            numbers[0], numbers[1],
            numbers[2], numbers[3]);

    printf("chars: %c %c %c %c\n",
            name[0], name[1], 
            name[2], name[3]); 
         
    printf("name: %s\n", name);

    char *another = "Zed";

    printf("another: %s\n", another);

    printf("anothereach : %c %c %c %c\n",
            another[0], another[1], 
            another[2], another[3]); 


    //Break it
    char name2[4];
    
    //Print un0'd storage
    printf("un 0d: %c %c %c %c\n",
            name2[0], name2[1], 
            name2[2], name2[3]); 



    //Initialize
    name2[0] = 'Z';
    name2[1] = 'e';
    name2[2] = 'd';
    name2[3] = 'A';

    printf("name2: %s\n", name2);

    char name3[4] = {'a', 'a', 'a', 'a'};

    printf("name3: %s\n", name3);


    return 0;

/*  OUTPUT
   
nums: 0 0 0 0
chars: a   
name: a
nums: 1 2 3 4
chars: Z e d 
name: Zed
another: Zed
anothereach : Z e d 
name2: ZedA
name3: aaaa

 */  
}
