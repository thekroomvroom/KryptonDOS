#include "io.h"

void kputs(const char *s) {
    while (*s) {
        asm volatile (
            "mov ah, 0x0E\n"
            "mov al, %0\n"
            "int 0x10"
            :
            : "r"(*s)
        );
        s++;
    }
}
