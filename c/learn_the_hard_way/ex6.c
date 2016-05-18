/* c.learncodethehardway.org ex6 */

#include <stdio.h>
#include <stdint.h>

int main(int argc, char *argv[])
{
    int  distance = 100;
    float power = 2.345f;
    double super_power = 56789.5432;
    char initial = 'A';
    char fname[] = "Zed";
    char lname[] = "Shaw";

    printf("You are %d miles away\n", distance);
    printf("You have %f levels of power\n", power);
    printf("You have %f super powers\n", super_power);
    printf("Initial %c\n", initial);
    printf("First name %s\n", fname);
    printf("Last name %s\n", lname);
    printf("Whole name %s %c %s\n", fname, initial, lname);

    /* Extra credit -- print formats */
    printf("You are %o miles away\n", distance);          //octal
    printf("You are %x miles away\n", distance);          //hex
    
    return 0;
}
