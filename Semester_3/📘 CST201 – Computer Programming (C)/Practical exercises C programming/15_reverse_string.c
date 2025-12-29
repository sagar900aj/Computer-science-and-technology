#include <stdio.h>
#include <string.h>

int main() {
    char name[10];
    printf("Enter the string : ");
    scanf("%s", name );
    int n =strlen(name);
    for(int i = n ; i>=0; i--){
        printf("%c", name[i]);
    }
    return 0;
}