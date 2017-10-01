/* 
* Start a process that will keep running for a long, but variable, time. 
*
* Copyright 2017 Dave Cuthbert, MIT license 
*/

#include <stdio.h>
#include <unistd.h>

int main(int argc, char *argv[]) 
{
    int count = 0;
    int sleep_time;

    printf("Enter sleep time: ");
    scanf("%d", &sleep_time);


    while(count < 10000) 
    {
	sleep(sleep_time);
	printf("%d ", count);
	fflush(stdout);
        count++;
    }
    printf("\n");
    printf("DONE\n");

    return 0;
}
