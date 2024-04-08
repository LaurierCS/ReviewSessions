#include <stdio.h>

// we define our union here, which we will be able to use in the rest of our
// code
union myunion {
  int i;
  float f;
  char c;
};

int main() {
  printf("This is an example for a union type\n");

  union myunion u;

  u.i = 0x34333234;

  printf("int: %d\n", u.i);
  printf("float: %.2f\n", u.f);
  printf("char: %c\n", u.c);

  return 0;
}
