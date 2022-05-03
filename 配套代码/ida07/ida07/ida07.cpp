#include <stdio.h>

int fun_3(int i)
{
    printf("This is fun_3 %d\n", (i + 3));
    return i;
}

int fun_2(int i)
{
    printf("This is fun_2 %d\n", (i + 2));
    return  fun_3(i);
}

int fun_1(int i)
{
    printf("This is fun_1 %d\n", (i + 1));
    return  fun_2(i);
}


int main()
{
    printf("Hello World!\n");
    fun_1(1);
}
