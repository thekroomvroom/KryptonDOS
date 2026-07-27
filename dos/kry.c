#include <stdio.h>
#include <stdlib.h>

#ifdef _WIN32
int sys = 1;
#else
int sys = 2;
#endif

void clear() {
    if (sys == 1){system("cls");}
    else if (sys == 2){system("clear");}
    else {
        printf("System Configuration Error")
        return 1;
    }
}//void clear()

int main() {}//int main()