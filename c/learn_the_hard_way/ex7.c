/* c.learncodethehardway.org ex7 */

#include <stdio.h>
#include <stdint.h>

int8_t main(int8_t argc, int8_t *argv[])
{
    int8_t bugs = 100;
    double bug_rate = 1.2;

    printf("%d bugs at rate of %f\n\n", bugs, bug_rate);

    int64_t univ_of_defects = 1L * 1024L * 1024L * 1024L;
    printf("Universe has %ld bugs\n\n", univ_of_defects);

    double expected_bugs = bugs * bug_rate;
    printf("Expected %f\n\n", expected_bugs);

    double part_of_universe = expected_bugs / univ_of_defects;
    printf("Only %e portion of universe\n\n", part_of_universe);

    //For demo purposes
    int8_t nul_byte = '\0';
    int8_t care_percentage = bugs * nul_byte;
    printf("Should care: %d%%\n\n", care_percentage);


    /* Extra credit */
    printf("percent s **%s**\n", nul_byte);
    printf("percent c **%c**\n", nul_byte);


    return 0;
}
