#include <stdio.h>

int main() {
    int a;
    printf("Enter a number: ");
    scanf("%d", &a);

    if(a > 0) {
        printf("The number %d is positive\n", a);
    }
    else if(a < 0) {
        printf("The number %d is negative\n", a);
    }
    else {
        printf("The number is 0\n");
    }

    return 0;
}
