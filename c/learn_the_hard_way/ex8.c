/* c.learncodethehardway.org ex8 */

#include <stdio.h>

int main(int argc, char *argv[])
{
    int areas[] = {10, 12, 13, 14, 20};
    char name[] = "Zed";
    char full_name[] = {'Z', 'e', 'd', ' ', 'A', '.',
                        ' ', 'S', 'h', 'a', 'w', '\0'};

    printf("size of int: %ld\n", sizeof(int));
    printf("size of areas: %ld\n", sizeof(areas));

    printf("area 1: %d  area 2: %d\n", areas[0], areas[1]);

    printf("size of char: %d\n", sizeof(char));
    printf("size of name (char array): %ld\n", sizeof(name));
    printf("num chars: %ld\n", sizeof(name) / sizeof(char));

    printf("name=\"%s\" and full_name=\"%s\"\n", name, full_name);

    /* Extra Credit Section */
    areas[0] = 100;
    areas[1] = 1000;
    areas[2] = 10000;
    areas[3] = 100000;
    
    printf("areas[0]: %d\n", areas[0]);
    printf("areas[1]: %d\n", areas[1]);
    printf("areas[2]: %d\n", areas[2]);
    printf("areas[3]: %d\n", areas[3]);

    name[0] = 'R';
    printf("New name: %s\n", name);

    return 0;
}
