//c.lerncodethehardway.org ex2

#include <stdio.h>

int main(int argc, char *argv[])
{
    int age = 10;
    int age2;
    int height = 72;

    printf("I am %d years old.\n", age);       //Original
    printf("I am %d years old.\n" );           //Extra -- No age variable for %d
    printf("I am %d years old.\n", age2);      //Extra -- Age variable for %d uninitialized
    printf("I am %d inches tall.\n", height);

    return 0;
}

//Output:
//  I am 10 years old.
//  I am 1542676480 years old.
//  I am 32765 years old.
//  I am 72 inches tall.
//
//EOF
