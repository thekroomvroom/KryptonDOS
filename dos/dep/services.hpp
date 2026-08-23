#ifndef SERVICES_HPP
#define SERVICES_HPP

#include <string>
#include <vector>
#include <filesystem>
#if defined(_WIN32)
#include <windows.h>
#elif defined(__APPLE__)
#include <mach-o/dyld.h>
#include <unistd.h>
#elif defined(__linux__)
#include <unistd.h>
#include <limits.h>
#endif

std::string sub(std::string str, const std::string& from, const std::string& to);
void cls();
std::string fod();
std::string opcwd();
void nl();

#endif