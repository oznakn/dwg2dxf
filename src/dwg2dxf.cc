#include <napi.h>
#include <iostream>
#include <fstream>
#include <sys/stat.h>

#include "dx_iface.h"
#include "dx_data.h"

DRW::Version checkVersion(std::string param) {
    if (param == "R12")
        return DRW::AC1009;
    else if (param == "v2000")
        return DRW::AC1015;
    else if (param == "v2004")
        return DRW::AC1018;
    else if (param == "v2007")
        return DRW::AC1021;
    else if (param == "v2010")
        return DRW::AC1024;
    return DRW::UNKNOWNV;
}

bool dwg2dxfConvert(std::string inName, std::string outName, DRW::Version ver, bool binary, bool overwrite) {
    bool badState = false;
    //verify if input file exist
    std::ifstream ifs;
    ifs.open(inName.c_str(), std::ifstream::in);
    badState = ifs.fail();
    ifs.close();
    if (badState) {
        std::cout << "Error can't open " << inName << std::endl;
        return false;
    }

    //verify if output file exist
    std::ifstream ofs;
    ofs.open (outName.c_str(), std::ifstream::in);
    badState = ofs.fail();
    ofs.close();
    if (!badState) {
        if (!overwrite){
            std::cout << "File " << outName << " already exist, overwrite Y/N ?" << std::endl;
            int c = getchar();
            if (c == 'Y' || c=='y')
                ;
            else {
                std::cout << "Cancelled.";
                return false;
            }
        }
    }
    //All ok proceed whit conversion
    //class to store file read:
    dx_data fData;
    //First read a dwg or dxf file
    dx_iface *input = new dx_iface();
    badState = input->fileImport( inName, &fData );
    if (!badState) {
        std::cout << "Error reading file " << inName << std::endl;
        return false;
    }

    //And write a dxf file
    dx_iface *output = new dx_iface();
    badState = output->fileExport(outName, ver, binary, &fData);
    delete input;
    delete output;

    return badState;
}


Napi::Boolean dwg2dxf(const Napi::CallbackInfo &info) {
    auto env = info.Env();

    if (info.Length() < 2) {
        return Napi::Boolean::New(env, false);;
    }

    DRW::Version ver = DRW::UNKNOWNV;

    if (info.Length() >= 3) {
        ver = checkVersion((std::string) info[1].ToString());

        if (ver == DRW::UNKNOWNV) {
            return Napi::Boolean::New(env, false);
        }
    }

    dwg2dxfConvert(
        (std::string) info[0].ToString(),
        (std::string) info[1].ToString(),
        ver,
        false,
        true
    );

    return Napi::Boolean::New(env, true);
}

Napi::Object Init(Napi::Env env, Napi::Object exports) {
    exports.Set("dwg2dxf", Napi::Function::New(env, dwg2dxf));
    return exports;
}

NODE_API_MODULE(dwg2dxf, Init)
