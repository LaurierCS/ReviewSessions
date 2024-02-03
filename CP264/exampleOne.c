#include<stdio.h>
int main() {
    int x = 1890259661;
    int *ptr = &x;
    printf("Value of x is %d\n", x);
    printf("Runtime memory address of x is %lu\n", (unsigned long int) &x);
    printf("Value of pointer ptr is %lu\n", (unsigned long int) ptr);
    printf("Size of pointer ptr is %d\n", sizeof(ptr));
    printf("Runtime memory address of pointer ptr is %lu\n", (unsigned long int) &ptr);
    printf("Value of *ptr is %d\n", *ptr);

    *ptr = 10;
    printf("Value of *ptr is %d\n", *ptr);
    printf("Value of x is %d\n", x);
    return 0;
}