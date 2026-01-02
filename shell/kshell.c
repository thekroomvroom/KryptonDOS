#include "kshell.h"
#include "../kernel/io.h"
#include "parser.h"

#define INPUT_SIZE 128

void shell_loop() {
    char input[INPUT_SIZE];

    while (1) {
        kputs("KryptonDOS@localhost>>");        // Display prompt
        kgets(input, INPUT_SIZE); // Get input from user
        parse_command(input);    // Send it to parser
    }
}
