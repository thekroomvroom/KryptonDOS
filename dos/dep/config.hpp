#ifndef CONFIG_HPP
#define CONFIG_HPP

#include <string>
#include <filesystem>

struct CFGcust {
    std::string hostname;
    std::string slash;
};
struct CFGosinfo {
    std::string name;
    std::string id;
    std::string codename;
    std::string build;
};

CFGosinfo fetchOSconfig();
CFGcust fetchCUSTconfig();

#endif