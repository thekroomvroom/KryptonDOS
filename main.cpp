#define _HAS_STD_BYTE 0
#include <iostream>
#include <cstdlib>
#include <string>
#include <filesystem>

using namespace std;
namespace fs = filesystem;

#if defined(_WIN32)
    #include <windows.h>

    void clear() {system("cls");}

    string getorigin() {
        char buffer[MAX_PATH];
        GetModuleFileNameA(NULL, buffer, MAX_PATH);
        return string(buffer);
    }
#elif defined(__APPLE__)
    #include <mac-o/dyld.h>
    #include <vector>
    #include <unistd.h>

    void clear() {system("clear");}

    string getorigin() {
        uint32_t size = 0;
        _NSGetExecutablePath(nullptr, &size);
        vector<char> buffer(size);
        _NSGetExecutablePath(buffer.data(), &size);
        return string(buffer.data());
    }
#elif defined(__linux__)
    #include <unistd.h>
    #include <limits.h>

    void clear() {system("clear");}

    string getorigin() {
        char buffer[PATH_MAX];
        ssize_t len = readlink("/proc/self/exe", buffer, sizeof(buffer) - 1);
        if (len != -1) buffer[len] = '\0';
        return string(buffer);
    }
#else
    #error "Program Incompatible with Host System"
#endif

string sub(string str, const string& from, const string& to) {
    size_t pos = 0;
    while ((pos = str.find(from, pos)) != string::npos) {
        str.replace(pos, from.length(), to);
        pos += to.length();
    }
    return str;
}

int main() {
    string owd = getorigin();

    fs::path opath = owd;
    fs::path odir = opath.parent_path();
    fs::path shellpath = odir / "dos" / "shell.py";

    #if defined(_WIN32)
        string lcmd = string("py \"") + shellpath.string() + "\"";
    #else
        string lcmd = string("python3 \"") + shellpath.string() + "\"";
    #endif

    clear();
    system(lcmd.c_str());

    return 0;
}