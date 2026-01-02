#include "io.h"

void kputs(const char* s) {
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

void kcls() {
    asm volatile (
        "mov ah, 0x0\n"
        "mov al, 0x3\n"  // simple clear screen via BIOS (mode 3)
        "int 0x10"
    );
}

void kgets(char* buffer, int max) {
    int i = 0;
    char c;
    while (i < max - 1) {
        asm volatile (
            "mov ah, 0x00\n"
            "int 0x16\n"
            "mov %0, al"
            : "=r"(c)
        );

        if (c == 0x0D) break; // Enter key
        buffer[i++] = c;

        // echo
        asm volatile (
            "mov ah, 0x0E\n"
            "mov al, %0\n"
            "int 0x10"
            :
            : "r"(c)
        );
    }
    buffer[i] = 0;
}
