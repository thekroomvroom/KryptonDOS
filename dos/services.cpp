#include "dep/services.hpp"
#include <cstdlib>
#include <iostream>
#include <filesystem>

using namespace std;

void cls() {
    std::cout << "\033[2J\033[H";
} std::string fod() {
    #if defined(_WIN32)
    char buffer[MAX_PATH];
    GetModuleFileNameA(NULL, buffer, MAX_PATH);
    return std::string(buffer);

    #elif defined(__APPLE__)
    uint32_t size = 0;
    _NSGetExecutablePath(nullptr, &size);
    vector<char> buffer(size);
    _NSGetExecutablePath(buffer.data(), &size);
    return std::string(buffer.data());

    #elif defined(__linux__)
    char buffer[PATH_MAX];
    ssize_t len = readlink("/proc/self/exe", buffer, sizeof(buffer) - 1);
    if (len != -1) buffer[len] = '\0';
    return std::string(buffer);

    #endif
} std::string sub(string str, const string& from, const string& to) {
    size_t pos = 0;
    while ((pos = str.find(from, pos)) != string::npos) {
        str.replace(pos, from.length(), to);
        pos += to.length();
    }
    return str;
} std::string opcwd() {
    filesystem::path rcwd = filesystem::current_path();
    std::string cwd = rcwd.string();
    return cwd;
} void nl() {
    cout << "\n";
}