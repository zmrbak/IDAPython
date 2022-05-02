// ida03.cpp : 此文件包含 "main" 函数。程序执行将在此处开始并结束。
//

#include <stdio.h>

//int fun_1(int i);
//int fun_2(int i);
//int fun_3(int i);

int fun_3(int i)
{
    printf("This is Func 1 %d\n" ,(i + 3));
    return i;
}

int fun_2(int i)
{
    printf("This is Func 1 %d\n", (i + 2));
    return  fun_3(i);
}

int fun_1(int i) 
{
    printf("This is Func 1 %d\n", (i + 1));
    return  fun_2(i);
}


int main()
{
    printf("Hello World!\n");
    fun_1(1);
}
