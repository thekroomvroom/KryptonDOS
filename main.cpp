#define _HAS_STD_BYTE 0
#include <iostream>
#include <cstdlib>
#include "dos/dep/shell.hpp"
#include "dos/dep/services.hpp"
#include <stdio.h>
#include <format>
#include <filesystem>

using namespace std;
namespace fs = filesystem;

int main(int argc, char *argv[]) {
    if (argc > 1) {
        string str1 = argv[1];

        for (int i = 2; i < argc; i++) {
            str1 += " ";
            str1 += argv[i];
        }
        cerr << "Error: Unexpected Argument '" << str1 << "'\n";
        return 1;
    }
    string owd = fod();

    /*Cpp Op*/
    shell(owd);
    
    /**/
    /* Python Op
    fs::path opath = owd;
    fs::path odir = opath.parent_path();
    fs::path shellpath = odir / "dos" / "shell.py";

    #if defined(_WIN32)
        string lcmd = string("py \"") + shellpath.string() + "\"";
    #else
        string lcmd = string("python3 \"") + shellpath.string() + "\"";
    #endif

    cls();
    system(lcmd.c_str());
    */

    return 0;
}