#include <stdio.h>

int main(){

    int i = 2;

    while (i <= 100){

        int j = 2;
        int isprime = 1;

        while (j * j <= i){

            if (i % j == 0){
                
                isprime = 0;
                break;

            }

            j++;

        }

        if (isprime){

            printf("%d ", i);

        }

        i++;
    }

    return 0;
}