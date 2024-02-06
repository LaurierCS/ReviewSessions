#include<stdio.h>
#include<stdlib.h>
int main(){
    int matrix[3][3]=
    {{1,2,3},
    {4,5,6},
    {7,8,9}};
    for(int i=0;i<3;i++){
        for(int j=0; j<3; j++){
            printf("%2d ", matrix[i][j]); //print value of element in the matrix
        }
        printf("\n"); //print newline character
    }
    return 0;
}