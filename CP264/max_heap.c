#include <stdio.h>

int size = 0;

void swap(int *a, int *b) {
  int temp = *b;
  *b = *a;
  *a = temp;
}

void heapify(int array[], int size, int i) {
  int largest = i;
  int left_node = 2 * i + 1;
  int right_node = 2 * i + 2;

  if (left_node < size && array[left_node] > array[largest])
    largest = left_node;
  if (right_node < size && array[right_node] > array[largest])
    largest = right_node;
  if (largest != i) {
    swap(&array[i], &array[largest]);
    heapify(array, size, largest);
  }
}

void insert(int array[], int value) {
  if (size == 0) {
    array[0] = value;
    size += 1;
  } else {
    array[size] = value;
    size += 1;
    for (int i = size / 2 - 1; i >= 0; i--) {
      heapify(array, size, i);
    }
  }
}

void pop(int array[]) {
  swap(&array[0], &array[size - 1]);
  size -= 1;
  for (int i = size / 2 - 1; i >= 0; i--) {
    heapify(array, size, i);
  }
}

void print_heap(int array[], int size) {
  for (int i = 0; i < size; i++) {
    printf("%d ", array[i]);
  }
  printf("\n");
}

int main() {
  int array[10];

  insert(array, 12);
  insert(array, 7);
  insert(array, 2);
  insert(array, 78);
  insert(array, 2);
  insert(array, 32);
  insert(array, 22);
  insert(array, 1);
  insert(array, 99);

  print_heap(array, size);

  pop(array);
  print_heap(array, size);
  pop(array);
  print_heap(array, size);
  pop(array);
  print_heap(array, size);
}
