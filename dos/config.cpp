#include <iostream>
#include <cstdlib>
#include <fstream>
#include "dep/config.hpp"
#include "dep/services.hpp"

using namespace std;
namespace fs = filesystem;

fs::path owd = fod();
fs::path cfg = owd.parent_path() / "dos" / "cfg";

CFGosinfo fetchOSconfig() {
    CFGosinfo osinf;
    string str1;
    fs::path oscfg = cfg / "os-info.krc";

    ifstream osinfo(oscfg);

    if (!osinfo.is_open()) {
        cerr << "Error: Unable to Load Configuration File";
        return osinf;
    }

    while (getline(osinfo, str1)) {
        
    }

}

CFGcust fetchCUSTconfig() {
    fs::path custcfg = cfg / "cust.krc";
}