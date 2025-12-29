#include <stdio.h>

int main() {
    int n = 5;
    int arr[n];
    for (int i = 0 ; i<n; i++){
        printf("Enter the value of index %d = ", i);
        scanf("%d", &arr[i]);
    }
    for (int i = 0 ; i<n; i++){
        printf("%d, ", arr[i]);
    }
    return 0;
}