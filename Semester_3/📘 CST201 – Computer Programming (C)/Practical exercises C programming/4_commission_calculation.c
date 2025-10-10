#include <stdio.h>

int main() {
    float sales, commission;
    printf("Enter the total sales amount : ");
    scanf("%f", &sales);
    commission=(0.25*sales)+1200;
    printf("Your total earning is = %.2f\n", commission);

    return 0;
}