#include "dep/shell.hpp"
#include "dep/services.hpp"
#include "dep/config.hpp"
#include <iostream>
#include <cstdlib>
#include <filesystem>

using namespace std;
namespace fs = filesystem;

void shell(string dir) {
    cout << "Initializing KryptonDOS...\n";

    string cmd, rawcwd = opcwd(), awd;
    int loop = 1;
    #if defined(_WIN32)
    string cwd = sub(rawcwd, "C:", "K:");
    #else
    string cwd = "K:" + rawcwd;
    #endif

    fs::path opth = dir;
    fs::path odir = opth.parent_path();
    fs::path dosdir = odir / "dos";

    // Configuration
    



    while (loop == 1){
    cout << cwd << "> ";
    getline(cin, cmd);
    nl();
    cout << cmd;
    }
}
void exec(string dir, string exec) {
    cerr << "Function not developed yet";
}