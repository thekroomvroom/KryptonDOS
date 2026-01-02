#include "parser.h"
#include "../kernel/io.h"
#include "../commands/sys.h"
#include <string.h>

void parse_command(const char* input) {
    if (strcmp(input, "KRVER") == 0) {
        sys_ver();  // call your sys command
    } else if (strcmp(input, "CLEAR") == 0 || strcmp(input, "CLS") == 0) {
        kcls();     // clear screen function from io.c
    } else {
        kputs("Invalid Syntax\n");
    }
}
