#include <stdio.h>
#include <stdlib.h>
#include <time.h>

void clear() {
    #ifdef _WIN32
    system("cls");
    #else
    system("clear");
    #endif
}

#ifdef _WIN32
int type = 1;
#else
int type = 2;
#endif

#ifdef _WIN32
    #include <windows.h>
    #define delay(ms) Sleep(ms)
#else
    #include <unistd.h>
    #define delay(ms) usleep(ms * 1000)
#endif

void loading() {
    srand(time(NULL));
    
    int lt = rand() % 10 + 1;

    for (int i = 0; i < lt; i++) {
        clear();
        printf("Loading KryptonDOS");
        for (int j = 0; j < i; j++) {
            printf(".");
        }
        fflush(stdout);
        delay(1);
    }
}

int main() {
    char krydir[4096]; char cmd [5000];

    if (type == 1) {
        //char path[MAX_PATH];
        //GetModuleFileNameA(NULL, path, MAX_PATH);
        //char *lastSlash = strrchr(path, '\\');
        //if (lastSlash) {
        //    *(lastSlash + 1) = '\0';
        //} char filePath[MAX_PATH];
        //snprintf(filePath, MAX_PATH, "%sdos\\krypton.py", path);
    } else {realpath("dos/shell.py", krydir);}
    loading();
    clear();
    
    //printf("%s\n", krydir);
    snprintf(cmd, sizeof(cmd), "python3 %s", krydir);
    system(cmd);
    return 0;
}// int main()