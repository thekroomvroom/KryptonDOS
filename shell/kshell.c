#include "parser.h"
#include <string.h>

void shell_loop() {
    char input[128];
    while(1) {
        kputs("KryptonDOS@localhost>");       // prompt
        kgets(input, 128);     // simple input
        parse_command(input);   // call parser (even if stub)
    }
}
