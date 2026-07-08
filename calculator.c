#include <stdio.h>

int subtract(int a, int b)
{
    return a - b;
}

int main()
{
    int result = subtract(20, 10);
    printf("Subtraction = %d\n", result);
    return 0;
}