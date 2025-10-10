#include <stdio.h>

int main() {
    int i; 
    char c;
    float f;
    printf("Enter one integer = ");
    scanf("%d", &i);
    printf("Enter one character = ");
    scanf(" %c", &c);
    printf("Enter one float = ");
    scanf("%f", &f);
    printf("The integer is %d\n",i);
    printf("The character is %c\n",c);
    printf("The float is %.2f\n",f);
    return 0;
}