#include <stdio.h>
#include <string.h>

int main() {
    char name[20]= "Sagar ", title[10]= "Maity";
    strcat(name, title);
    printf("%s", name);
    return 0;
}