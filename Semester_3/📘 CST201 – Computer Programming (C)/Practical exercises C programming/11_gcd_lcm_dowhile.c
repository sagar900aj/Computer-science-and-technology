#include <stdio.h>

int main(){
    int a, b;
    
    printf("Enter the first number : ");
    scanf("%d", &a);
    printf("Enter the second number : ");
    scanf("%d", &b);
    
    int x = a, y = b;
    int rem;
    
    do{
        rem = x % y;
        x = y;
        y = rem;
    } while (rem != 0);
    
    int gcd = x;
    int lcm = (a * b) / gcd;
    
    printf("GCD = %d\n", gcd);
    printf("LCM = %d\n", lcm);

    return 0;
}