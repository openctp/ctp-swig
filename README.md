# ctp-swig

## 环境准备

### Windows

- Windows 10
- CMake 3.30.4
- VisualStudio 2022

### Linux

- Debian 12

## Swig 转换说明

### Linux

### Windows

<details>
    <summary>Windows 编译示例</summary>

    PS E:\projects\ctp-swig\6.3.15> .\auto_compile.bat
    ################## Swig generate cpp/py files ##################
    Could Not Find E:\projects\ctp-swig\6.3.15\*_wrap.*
    win64\ThostFtdcTraderApi.h(30) : Warning 514: Director base class CThostFtdcTraderSpi has no virtual destructor.
    win64\ThostFtdcMdApi.h(30) : Warning 514: Director base class CThostFtdcMdSpi has no virtual destructor.
    ########################## Compile 37 ##########################
    -- Building for: Visual Studio 17 2022
    CMake Deprecation Warning at CMakeLists.txt:1 (cmake_minimum_required):
    Compatibility with CMake < 3.5 will be removed from a future version of
    CMake.

    Update the VERSION argument <min> value or use a ...<max> suffix to tell
    CMake that the project does not need compatibility with older versions.


    -- Selecting Windows SDK version 10.0.22621.0 to target Windows 10.0.19045.
    -- The C compiler identification is MSVC 19.37.32822.0
    -- The CXX compiler identification is MSVC 19.37.32822.0
    -- Detecting C compiler ABI info
    -- Detecting C compiler ABI info - done
    -- Check for working C compiler: D:/Microsoft Visual Studio/2022/Community/VC/Tools/MSVC/14.37.32822/bin/Hostx64/x64/cl.exe - skipped
    -- Detecting C compile features
    -- Detecting C compile features - done
    -- Detecting CXX compiler ABI info
    -- Detecting CXX compiler ABI info - done
    -- Check for working CXX compiler: D:/Microsoft Visual Studio/2022/Community/VC/Tools/MSVC/14.37.32822/bin/Hostx64/x64/cl.exe - skipped
    -- Detecting CXX compile features
    -- Detecting CXX compile features - done
    -- Configuring done (2.9s)
    -- Generating done (0.0s)
    -- Build files have been written to: E:/projects/ctp-swig/6.3.15/build
    MSBuild version 17.7.2+d6990bcfa for .NET Framework

    MSBuild version 17.7.2+d6990bcfa for .NET Framework

    1>Checking Build System
    Building Custom Rule E:/projects/ctp-swig/6.3.15/CMakeLists.txt
    thostmduserapi_wrap.cxx
    E:\projects\ctp-swig\6.3.15\win64\ThostFtdcUserApiStruct.h(1,1): warning C4819: 该文件包含不能在当前代码页(936)中表示的字符。请将该文件保存为 Unicode 格式以防止数据丢失
    [E:\projects\ctp-swig\6.3.15\build\_thostmduserapi.vcxproj]
    E:\projects\ctp-swig\6.3.15\win64\ThostFtdcUserApiStruct.h(1153,1): warning C4819: 该文件包含不能在当前代码页(936)中表示的字符。请将 该文件保存为 Unicode 格式以防止数据
    丢失 [E:\projects\ctp-swig\6.3.15\build\_thostmduserapi.vcxproj]
    E:\projects\ctp-swig\6.3.15\win64\ThostFtdcUserApiStruct.h(6943,1): warning C4819: 该文件包含不能在当前代码页(936)中表示的字符。请将 该文件保存为 Unicode 格式以防止数据
    丢失 [E:\projects\ctp-swig\6.3.15\build\_thostmduserapi.vcxproj]
    E:\projects\ctp-swig\6.3.15\win64\ThostFtdcUserApiStruct.h(8014,1): warning C4819: 该文件包含不能在当前代码页(936)中表示的字符。请将 该文件保存为 Unicode 格式以防止数据
    丢失 [E:\projects\ctp-swig\6.3.15\build\_thostmduserapi.vcxproj]
    E:\projects\ctp-swig\6.3.15\thostmduserapi_wrap.cxx(316364,16): warning C4244: “初始化”: 从“Py_ssize_t”转换到“int”，可能丢失数据 [E:\projects\ctp-
    swig\6.3.15\build\_thostmduserapi.vcxproj]
    E:\projects\ctp-swig\6.3.15\thostmduserapi_wrap.cxx(316421,16): warning C4244: “初始化”: 从“Py_ssize_t”转换到“int”，可能丢失数据 [E:\projects\ctp-
    swig\6.3.15\build\_thostmduserapi.vcxproj]
    E:\projects\ctp-swig\6.3.15\thostmduserapi_wrap.cxx(316478,16): warning C4244: “初始化”: 从“Py_ssize_t”转换到“int”，可能丢失数据 [E:\projects\ctp-
    swig\6.3.15\build\_thostmduserapi.vcxproj]
    E:\projects\ctp-swig\6.3.15\thostmduserapi_wrap.cxx(316535,16): warning C4244: “初始化”: 从“Py_ssize_t”转换到“int”，可能丢失数据 [E:\projects\ctp-
    swig\6.3.15\build\_thostmduserapi.vcxproj]
    正在创建库 E:/projects/ctp-swig/6.3.15/build/Release/_thostmduserapi.lib 和对象 E:/projects/ctp-swig/6.3.15/build/Release/_thostmduserap
    i.exp
    _thostmduserapi.vcxproj -> E:\projects\ctp-swig\6.3.15\build\Release\_thostmduserapi.dll
    Building Custom Rule E:/projects/ctp-swig/6.3.15/CMakeLists.txt
    thosttraderapi_wrap.cxx
    E:\projects\ctp-swig\6.3.15\win64\ThostFtdcUserApiStruct.h(1,1): warning C4819: 该文件包含不能在当前代码页(936)中表示的字符。请将该文件保存为 Unicode 格式以防止数据丢失
    [E:\projects\ctp-swig\6.3.15\build\_thosttraderapi.vcxproj]
    E:\projects\ctp-swig\6.3.15\win64\ThostFtdcUserApiStruct.h(1153,1): warning C4819: 该文件包含不能在当前代码页(936)中表示的字符。请将 该文件保存为 Unicode 格式以防止数据
    丢失 [E:\projects\ctp-swig\6.3.15\build\_thosttraderapi.vcxproj]
    E:\projects\ctp-swig\6.3.15\win64\ThostFtdcUserApiStruct.h(6943,1): warning C4819: 该文件包含不能在当前代码页(936)中表示的字符。请将 该文件保存为 Unicode 格式以防止数据
    丢失 [E:\projects\ctp-swig\6.3.15\build\_thosttraderapi.vcxproj]
    E:\projects\ctp-swig\6.3.15\win64\ThostFtdcUserApiStruct.h(8014,1): warning C4819: 该文件包含不能在当前代码页(936)中表示的字符。请将 该文件保存为 Unicode 格式以防止数据
    丢失 [E:\projects\ctp-swig\6.3.15\build\_thosttraderapi.vcxproj]
    正在创建库 E:/projects/ctp-swig/6.3.15/build/Release/_thosttraderapi.lib 和对象 E:/projects/ctp-swig/6.3.15/build/Release/_thosttraderap
    i.exp
    _thosttraderapi.vcxproj -> E:\projects\ctp-swig\6.3.15\build\Release\_thosttraderapi.dll
    Building Custom Rule E:/projects/ctp-swig/6.3.15/CMakeLists.txt
    1 file(s) copied.
    1 file(s) copied.
    ########################## Compile 38 ##########################
    -- Building for: Visual Studio 17 2022
    CMake Deprecation Warning at CMakeLists.txt:1 (cmake_minimum_required):
    Compatibility with CMake < 3.5 will be removed from a future version of
    CMake.

    Update the VERSION argument <min> value or use a ...<max> suffix to tell
    CMake that the project does not need compatibility with older versions.


    -- Selecting Windows SDK version 10.0.22621.0 to target Windows 10.0.19045.
    -- The C compiler identification is MSVC 19.37.32822.0
    -- The CXX compiler identification is MSVC 19.37.32822.0
    -- Detecting C compiler ABI info
    -- Detecting C compiler ABI info - done
    -- Check for working C compiler: D:/Microsoft Visual Studio/2022/Community/VC/Tools/MSVC/14.37.32822/bin/Hostx64/x64/cl.exe - skipped
    -- Detecting C compile features
    -- Detecting C compile features - done
    -- Detecting CXX compiler ABI info
    -- Detecting CXX compiler ABI info - done
    -- Check for working CXX compiler: D:/Microsoft Visual Studio/2022/Community/VC/Tools/MSVC/14.37.32822/bin/Hostx64/x64/cl.exe - skipped
    -- Detecting CXX compile features
    -- Detecting CXX compile features - done
    -- Configuring done (2.8s)
    -- Generating done (0.0s)
    -- Build files have been written to: E:/projects/ctp-swig/6.3.15/build
    MSBuild version 17.7.2+d6990bcfa for .NET Framework

    MSBuild version 17.7.2+d6990bcfa for .NET Framework

    1>Checking Build System
    Building Custom Rule E:/projects/ctp-swig/6.3.15/CMakeLists.txt
    thostmduserapi_wrap.cxx
    E:\projects\ctp-swig\6.3.15\win64\ThostFtdcUserApiStruct.h(1,1): warning C4819: 该文件包含不能在当前代码页(936)中表示的字符。请将该文件保存为 Unicode 格式以防止数据丢失
    [E:\projects\ctp-swig\6.3.15\build\_thostmduserapi.vcxproj]
    E:\projects\ctp-swig\6.3.15\win64\ThostFtdcUserApiStruct.h(1153,1): warning C4819: 该文件包含不能在当前代码页(936)中表示的字符。请将 该文件保存为 Unicode 格式以防止数据
    丢失 [E:\projects\ctp-swig\6.3.15\build\_thostmduserapi.vcxproj]
    E:\projects\ctp-swig\6.3.15\win64\ThostFtdcUserApiStruct.h(6943,1): warning C4819: 该文件包含不能在当前代码页(936)中表示的字符。请将 该文件保存为 Unicode 格式以防止数据
    丢失 [E:\projects\ctp-swig\6.3.15\build\_thostmduserapi.vcxproj]
    E:\projects\ctp-swig\6.3.15\win64\ThostFtdcUserApiStruct.h(8014,1): warning C4819: 该文件包含不能在当前代码页(936)中表示的字符。请将 该文件保存为 Unicode 格式以防止数据
    丢失 [E:\projects\ctp-swig\6.3.15\build\_thostmduserapi.vcxproj]
    E:\projects\ctp-swig\6.3.15\thostmduserapi_wrap.cxx(316364,16): warning C4244: “初始化”: 从“Py_ssize_t”转换到“int”，可能丢失数据 [E:\projects\ctp-
    swig\6.3.15\build\_thostmduserapi.vcxproj]
    E:\projects\ctp-swig\6.3.15\thostmduserapi_wrap.cxx(316421,16): warning C4244: “初始化”: 从“Py_ssize_t”转换到“int”，可能丢失数据 [E:\projects\ctp-
    swig\6.3.15\build\_thostmduserapi.vcxproj]
    E:\projects\ctp-swig\6.3.15\thostmduserapi_wrap.cxx(316478,16): warning C4244: “初始化”: 从“Py_ssize_t”转换到“int”，可能丢失数据 [E:\projects\ctp-
    swig\6.3.15\build\_thostmduserapi.vcxproj]
    E:\projects\ctp-swig\6.3.15\thostmduserapi_wrap.cxx(316535,16): warning C4244: “初始化”: 从“Py_ssize_t”转换到“int”，可能丢失数据 [E:\projects\ctp-
    swig\6.3.15\build\_thostmduserapi.vcxproj]
    正在创建库 E:/projects/ctp-swig/6.3.15/build/Release/_thostmduserapi.lib 和对象 E:/projects/ctp-swig/6.3.15/build/Release/_thostmduserap
    i.exp
    _thostmduserapi.vcxproj -> E:\projects\ctp-swig\6.3.15\build\Release\_thostmduserapi.dll
    Building Custom Rule E:/projects/ctp-swig/6.3.15/CMakeLists.txt
    thosttraderapi_wrap.cxx
    E:\projects\ctp-swig\6.3.15\win64\ThostFtdcUserApiStruct.h(1,1): warning C4819: 该文件包含不能在当前代码页(936)中表示的字符。请将该文件保存为 Unicode 格式以防止数据丢失
    [E:\projects\ctp-swig\6.3.15\build\_thosttraderapi.vcxproj]
    E:\projects\ctp-swig\6.3.15\win64\ThostFtdcUserApiStruct.h(1153,1): warning C4819: 该文件包含不能在当前代码页(936)中表示的字符。请将 该文件保存为 Unicode 格式以防止数据
    丢失 [E:\projects\ctp-swig\6.3.15\build\_thosttraderapi.vcxproj]
    E:\projects\ctp-swig\6.3.15\win64\ThostFtdcUserApiStruct.h(6943,1): warning C4819: 该文件包含不能在当前代码页(936)中表示的字符。请将 该文件保存为 Unicode 格式以防止数据
    丢失 [E:\projects\ctp-swig\6.3.15\build\_thosttraderapi.vcxproj]
    E:\projects\ctp-swig\6.3.15\win64\ThostFtdcUserApiStruct.h(8014,1): warning C4819: 该文件包含不能在当前代码页(936)中表示的字符。请将 该文件保存为 Unicode 格式以防止数据
    丢失 [E:\projects\ctp-swig\6.3.15\build\_thosttraderapi.vcxproj]
    正在创建库 E:/projects/ctp-swig/6.3.15/build/Release/_thosttraderapi.lib 和对象 E:/projects/ctp-swig/6.3.15/build/Release/_thosttraderap
    i.exp
    _thosttraderapi.vcxproj -> E:\projects\ctp-swig\6.3.15\build\Release\_thosttraderapi.dll
    Building Custom Rule E:/projects/ctp-swig/6.3.15/CMakeLists.txt
    1 file(s) copied.
    1 file(s) copied.
    ########################## Compile 39 ##########################
    -- Building for: Visual Studio 17 2022
    CMake Deprecation Warning at CMakeLists.txt:1 (cmake_minimum_required):
    Compatibility with CMake < 3.5 will be removed from a future version of
    CMake.

    Update the VERSION argument <min> value or use a ...<max> suffix to tell
    CMake that the project does not need compatibility with older versions.


    -- Selecting Windows SDK version 10.0.22621.0 to target Windows 10.0.19045.
    -- The C compiler identification is MSVC 19.37.32822.0
    -- The CXX compiler identification is MSVC 19.37.32822.0
    -- Detecting C compiler ABI info
    -- Detecting C compiler ABI info - done
    -- Check for working C compiler: D:/Microsoft Visual Studio/2022/Community/VC/Tools/MSVC/14.37.32822/bin/Hostx64/x64/cl.exe - skipped
    -- Detecting C compile features
    -- Detecting C compile features - done
    -- Detecting CXX compiler ABI info
    -- Detecting CXX compiler ABI info - done
    -- Check for working CXX compiler: D:/Microsoft Visual Studio/2022/Community/VC/Tools/MSVC/14.37.32822/bin/Hostx64/x64/cl.exe - skipped
    -- Detecting CXX compile features
    -- Detecting CXX compile features - done
    -- Configuring done (2.8s)
    -- Generating done (0.0s)
    -- Build files have been written to: E:/projects/ctp-swig/6.3.15/build
    MSBuild version 17.7.2+d6990bcfa for .NET Framework

    MSBuild version 17.7.2+d6990bcfa for .NET Framework

    1>Checking Build System
    Building Custom Rule E:/projects/ctp-swig/6.3.15/CMakeLists.txt
    thostmduserapi_wrap.cxx
    E:\projects\ctp-swig\6.3.15\win64\ThostFtdcUserApiStruct.h(1,1): warning C4819: 该文件包含不能在当前代码页(936)中表示的字符。请将该文件保存为 Unicode 格式以防止数据丢失
    [E:\projects\ctp-swig\6.3.15\build\_thostmduserapi.vcxproj]
    E:\projects\ctp-swig\6.3.15\win64\ThostFtdcUserApiStruct.h(1153,1): warning C4819: 该文件包含不能在当前代码页(936)中表示的字符。请将 该文件保存为 Unicode 格式以防止数据
    丢失 [E:\projects\ctp-swig\6.3.15\build\_thostmduserapi.vcxproj]
    E:\projects\ctp-swig\6.3.15\win64\ThostFtdcUserApiStruct.h(6943,1): warning C4819: 该文件包含不能在当前代码页(936)中表示的字符。请将 该文件保存为 Unicode 格式以防止数据
    丢失 [E:\projects\ctp-swig\6.3.15\build\_thostmduserapi.vcxproj]
    E:\projects\ctp-swig\6.3.15\win64\ThostFtdcUserApiStruct.h(8014,1): warning C4819: 该文件包含不能在当前代码页(936)中表示的字符。请将 该文件保存为 Unicode 格式以防止数据
    丢失 [E:\projects\ctp-swig\6.3.15\build\_thostmduserapi.vcxproj]
    E:\projects\ctp-swig\6.3.15\thostmduserapi_wrap.cxx(316364,16): warning C4244: “初始化”: 从“Py_ssize_t”转换到“int”，可能丢失数据 [E:\projects\ctp-
    swig\6.3.15\build\_thostmduserapi.vcxproj]
    E:\projects\ctp-swig\6.3.15\thostmduserapi_wrap.cxx(316421,16): warning C4244: “初始化”: 从“Py_ssize_t”转换到“int”，可能丢失数据 [E:\projects\ctp-
    swig\6.3.15\build\_thostmduserapi.vcxproj]
    E:\projects\ctp-swig\6.3.15\thostmduserapi_wrap.cxx(316478,16): warning C4244: “初始化”: 从“Py_ssize_t”转换到“int”，可能丢失数据 [E:\projects\ctp-
    swig\6.3.15\build\_thostmduserapi.vcxproj]
    E:\projects\ctp-swig\6.3.15\thostmduserapi_wrap.cxx(316535,16): warning C4244: “初始化”: 从“Py_ssize_t”转换到“int”，可能丢失数据 [E:\projects\ctp-
    swig\6.3.15\build\_thostmduserapi.vcxproj]
    正在创建库 E:/projects/ctp-swig/6.3.15/build/Release/_thostmduserapi.lib 和对象 E:/projects/ctp-swig/6.3.15/build/Release/_thostmduserap
    i.exp
    _thostmduserapi.vcxproj -> E:\projects\ctp-swig\6.3.15\build\Release\_thostmduserapi.dll
    Building Custom Rule E:/projects/ctp-swig/6.3.15/CMakeLists.txt
    thosttraderapi_wrap.cxx
    E:\projects\ctp-swig\6.3.15\win64\ThostFtdcUserApiStruct.h(1,1): warning C4819: 该文件包含不能在当前代码页(936)中表示的字符。请将该文件保存为 Unicode 格式以防止数据丢失
    [E:\projects\ctp-swig\6.3.15\build\_thosttraderapi.vcxproj]
    E:\projects\ctp-swig\6.3.15\win64\ThostFtdcUserApiStruct.h(1153,1): warning C4819: 该文件包含不能在当前代码页(936)中表示的字符。请将 该文件保存为 Unicode 格式以防止数据
    丢失 [E:\projects\ctp-swig\6.3.15\build\_thosttraderapi.vcxproj]
    E:\projects\ctp-swig\6.3.15\win64\ThostFtdcUserApiStruct.h(6943,1): warning C4819: 该文件包含不能在当前代码页(936)中表示的字符。请将 该文件保存为 Unicode 格式以防止数据
    丢失 [E:\projects\ctp-swig\6.3.15\build\_thosttraderapi.vcxproj]
    E:\projects\ctp-swig\6.3.15\win64\ThostFtdcUserApiStruct.h(8014,1): warning C4819: 该文件包含不能在当前代码页(936)中表示的字符。请将 该文件保存为 Unicode 格式以防止数据
    丢失 [E:\projects\ctp-swig\6.3.15\build\_thosttraderapi.vcxproj]
    正在创建库 E:/projects/ctp-swig/6.3.15/build/Release/_thosttraderapi.lib 和对象 E:/projects/ctp-swig/6.3.15/build/Release/_thosttraderap
    i.exp
    _thosttraderapi.vcxproj -> E:\projects\ctp-swig\6.3.15\build\Release\_thosttraderapi.dll
    Building Custom Rule E:/projects/ctp-swig/6.3.15/CMakeLists.txt
    1 file(s) copied.
    1 file(s) copied.
    ########################## Compile 310 ##########################
    -- Building for: Visual Studio 17 2022
    CMake Deprecation Warning at CMakeLists.txt:1 (cmake_minimum_required):
    Compatibility with CMake < 3.5 will be removed from a future version of
    CMake.

    Update the VERSION argument <min> value or use a ...<max> suffix to tell
    CMake that the project does not need compatibility with older versions.


    -- Selecting Windows SDK version 10.0.22621.0 to target Windows 10.0.19045.
    -- The C compiler identification is MSVC 19.37.32822.0
    -- The CXX compiler identification is MSVC 19.37.32822.0
    -- Detecting C compiler ABI info
    -- Detecting C compiler ABI info - done
    -- Check for working C compiler: D:/Microsoft Visual Studio/2022/Community/VC/Tools/MSVC/14.37.32822/bin/Hostx64/x64/cl.exe - skipped
    -- Detecting C compile features
    -- Detecting C compile features - done
    -- Detecting CXX compiler ABI info
    -- Detecting CXX compiler ABI info - done
    -- Check for working CXX compiler: D:/Microsoft Visual Studio/2022/Community/VC/Tools/MSVC/14.37.32822/bin/Hostx64/x64/cl.exe - skipped
    -- Detecting CXX compile features
    -- Detecting CXX compile features - done
    -- Configuring done (2.8s)
    -- Generating done (0.0s)
    -- Build files have been written to: E:/projects/ctp-swig/6.3.15/build
    MSBuild version 17.7.2+d6990bcfa for .NET Framework

    MSBuild version 17.7.2+d6990bcfa for .NET Framework

    1>Checking Build System
    Building Custom Rule E:/projects/ctp-swig/6.3.15/CMakeLists.txt
    thostmduserapi_wrap.cxx
    E:\projects\ctp-swig\6.3.15\win64\ThostFtdcUserApiStruct.h(1,1): warning C4819: 该文件包含不能在当前代码页(936)中表示的字符。请将该文件保存为 Unicode 格式以防止数据丢失
    [E:\projects\ctp-swig\6.3.15\build\_thostmduserapi.vcxproj]
    E:\projects\ctp-swig\6.3.15\win64\ThostFtdcUserApiStruct.h(1153,1): warning C4819: 该文件包含不能在当前代码页(936)中表示的字符。请将 该文件保存为 Unicode 格式以防止数据
    丢失 [E:\projects\ctp-swig\6.3.15\build\_thostmduserapi.vcxproj]
    E:\projects\ctp-swig\6.3.15\win64\ThostFtdcUserApiStruct.h(6943,1): warning C4819: 该文件包含不能在当前代码页(936)中表示的字符。请将 该文件保存为 Unicode 格式以防止数据
    丢失 [E:\projects\ctp-swig\6.3.15\build\_thostmduserapi.vcxproj]
    E:\projects\ctp-swig\6.3.15\win64\ThostFtdcUserApiStruct.h(8014,1): warning C4819: 该文件包含不能在当前代码页(936)中表示的字符。请将 该文件保存为 Unicode 格式以防止数据
    丢失 [E:\projects\ctp-swig\6.3.15\build\_thostmduserapi.vcxproj]
    E:\projects\ctp-swig\6.3.15\thostmduserapi_wrap.cxx(316364,16): warning C4244: “初始化”: 从“Py_ssize_t”转换到“int”，可能丢失数据 [E:\projects\ctp-
    swig\6.3.15\build\_thostmduserapi.vcxproj]
    E:\projects\ctp-swig\6.3.15\thostmduserapi_wrap.cxx(316421,16): warning C4244: “初始化”: 从“Py_ssize_t”转换到“int”，可能丢失数据 [E:\projects\ctp-
    swig\6.3.15\build\_thostmduserapi.vcxproj]
    E:\projects\ctp-swig\6.3.15\thostmduserapi_wrap.cxx(316478,16): warning C4244: “初始化”: 从“Py_ssize_t”转换到“int”，可能丢失数据 [E:\projects\ctp-
    swig\6.3.15\build\_thostmduserapi.vcxproj]
    E:\projects\ctp-swig\6.3.15\thostmduserapi_wrap.cxx(316535,16): warning C4244: “初始化”: 从“Py_ssize_t”转换到“int”，可能丢失数据 [E:\projects\ctp-
    swig\6.3.15\build\_thostmduserapi.vcxproj]
    正在创建库 E:/projects/ctp-swig/6.3.15/build/Release/_thostmduserapi.lib 和对象 E:/projects/ctp-swig/6.3.15/build/Release/_thostmduserap
    i.exp
    _thostmduserapi.vcxproj -> E:\projects\ctp-swig\6.3.15\build\Release\_thostmduserapi.dll
    Building Custom Rule E:/projects/ctp-swig/6.3.15/CMakeLists.txt
    thosttraderapi_wrap.cxx
    E:\projects\ctp-swig\6.3.15\win64\ThostFtdcUserApiStruct.h(1,1): warning C4819: 该文件包含不能在当前代码页(936)中表示的字符。请将该文件保存为 Unicode 格式以防止数据丢失
    [E:\projects\ctp-swig\6.3.15\build\_thosttraderapi.vcxproj]
    E:\projects\ctp-swig\6.3.15\win64\ThostFtdcUserApiStruct.h(1153,1): warning C4819: 该文件包含不能在当前代码页(936)中表示的字符。请将 该文件保存为 Unicode 格式以防止数据
    丢失 [E:\projects\ctp-swig\6.3.15\build\_thosttraderapi.vcxproj]
    E:\projects\ctp-swig\6.3.15\win64\ThostFtdcUserApiStruct.h(6943,1): warning C4819: 该文件包含不能在当前代码页(936)中表示的字符。请将 该文件保存为 Unicode 格式以防止数据
    丢失 [E:\projects\ctp-swig\6.3.15\build\_thosttraderapi.vcxproj]
    E:\projects\ctp-swig\6.3.15\win64\ThostFtdcUserApiStruct.h(8014,1): warning C4819: 该文件包含不能在当前代码页(936)中表示的字符。请将 该文件保存为 Unicode 格式以防止数据
    丢失 [E:\projects\ctp-swig\6.3.15\build\_thosttraderapi.vcxproj]
    正在创建库 E:/projects/ctp-swig/6.3.15/build/Release/_thosttraderapi.lib 和对象 E:/projects/ctp-swig/6.3.15/build/Release/_thosttraderap
    i.exp
    _thosttraderapi.vcxproj -> E:\projects\ctp-swig\6.3.15\build\Release\_thosttraderapi.dll
    Building Custom Rule E:/projects/ctp-swig/6.3.15/CMakeLists.txt
    1 file(s) copied.
    1 file(s) copied.
    ########################## Compile 311 ##########################
    -- Building for: Visual Studio 17 2022
    CMake Deprecation Warning at CMakeLists.txt:1 (cmake_minimum_required):
    Compatibility with CMake < 3.5 will be removed from a future version of
    CMake.

    Update the VERSION argument <min> value or use a ...<max> suffix to tell
    CMake that the project does not need compatibility with older versions.


    -- Selecting Windows SDK version 10.0.22621.0 to target Windows 10.0.19045.
    -- The C compiler identification is MSVC 19.37.32822.0
    -- The CXX compiler identification is MSVC 19.37.32822.0
    -- Detecting C compiler ABI info
    -- Detecting C compiler ABI info - done
    -- Check for working C compiler: D:/Microsoft Visual Studio/2022/Community/VC/Tools/MSVC/14.37.32822/bin/Hostx64/x64/cl.exe - skipped
    -- Detecting C compile features
    -- Detecting C compile features - done
    -- Detecting CXX compiler ABI info
    -- Detecting CXX compiler ABI info - done
    -- Check for working CXX compiler: D:/Microsoft Visual Studio/2022/Community/VC/Tools/MSVC/14.37.32822/bin/Hostx64/x64/cl.exe - skipped
    -- Detecting CXX compile features
    -- Detecting CXX compile features - done
    -- Configuring done (2.7s)
    -- Generating done (0.0s)
    -- Build files have been written to: E:/projects/ctp-swig/6.3.15/build
    MSBuild version 17.7.2+d6990bcfa for .NET Framework

    MSBuild version 17.7.2+d6990bcfa for .NET Framework

    1>Checking Build System
    Building Custom Rule E:/projects/ctp-swig/6.3.15/CMakeLists.txt
    thostmduserapi_wrap.cxx
    E:\projects\ctp-swig\6.3.15\win64\ThostFtdcUserApiStruct.h(1,1): warning C4819: 该文件包含不能在当前代码页(936)中表示的字符。请将该文件保存为 Unicode 格式以防止数据丢失
    [E:\projects\ctp-swig\6.3.15\build\_thostmduserapi.vcxproj]
    E:\projects\ctp-swig\6.3.15\win64\ThostFtdcUserApiStruct.h(1153,1): warning C4819: 该文件包含不能在当前代码页(936)中表示的字符。请将 该文件保存为 Unicode 格式以防止数据
    丢失 [E:\projects\ctp-swig\6.3.15\build\_thostmduserapi.vcxproj]
    E:\projects\ctp-swig\6.3.15\win64\ThostFtdcUserApiStruct.h(6943,1): warning C4819: 该文件包含不能在当前代码页(936)中表示的字符。请将 该文件保存为 Unicode 格式以防止数据
    丢失 [E:\projects\ctp-swig\6.3.15\build\_thostmduserapi.vcxproj]
    E:\projects\ctp-swig\6.3.15\win64\ThostFtdcUserApiStruct.h(8014,1): warning C4819: 该文件包含不能在当前代码页(936)中表示的字符。请将 该文件保存为 Unicode 格式以防止数据
    丢失 [E:\projects\ctp-swig\6.3.15\build\_thostmduserapi.vcxproj]
    E:\projects\ctp-swig\6.3.15\thostmduserapi_wrap.cxx(316364,16): warning C4244: “初始化”: 从“Py_ssize_t”转换到“int”，可能丢失数据 [E:\projects\ctp-
    swig\6.3.15\build\_thostmduserapi.vcxproj]
    E:\projects\ctp-swig\6.3.15\thostmduserapi_wrap.cxx(316421,16): warning C4244: “初始化”: 从“Py_ssize_t”转换到“int”，可能丢失数据 [E:\projects\ctp-
    swig\6.3.15\build\_thostmduserapi.vcxproj]
    E:\projects\ctp-swig\6.3.15\thostmduserapi_wrap.cxx(316478,16): warning C4244: “初始化”: 从“Py_ssize_t”转换到“int”，可能丢失数据 [E:\projects\ctp-
    swig\6.3.15\build\_thostmduserapi.vcxproj]
    E:\projects\ctp-swig\6.3.15\thostmduserapi_wrap.cxx(316535,16): warning C4244: “初始化”: 从“Py_ssize_t”转换到“int”，可能丢失数据 [E:\projects\ctp-
    swig\6.3.15\build\_thostmduserapi.vcxproj]
    正在创建库 E:/projects/ctp-swig/6.3.15/build/Release/_thostmduserapi.lib 和对象 E:/projects/ctp-swig/6.3.15/build/Release/_thostmduserap
    i.exp
    _thostmduserapi.vcxproj -> E:\projects\ctp-swig\6.3.15\build\Release\_thostmduserapi.dll
    Building Custom Rule E:/projects/ctp-swig/6.3.15/CMakeLists.txt
    thosttraderapi_wrap.cxx
    E:\projects\ctp-swig\6.3.15\win64\ThostFtdcUserApiStruct.h(1,1): warning C4819: 该文件包含不能在当前代码页(936)中表示的字符。请将该文件保存为 Unicode 格式以防止数据丢失
    [E:\projects\ctp-swig\6.3.15\build\_thosttraderapi.vcxproj]
    E:\projects\ctp-swig\6.3.15\win64\ThostFtdcUserApiStruct.h(1153,1): warning C4819: 该文件包含不能在当前代码页(936)中表示的字符。请将 该文件保存为 Unicode 格式以防止数据
    丢失 [E:\projects\ctp-swig\6.3.15\build\_thosttraderapi.vcxproj]
    E:\projects\ctp-swig\6.3.15\win64\ThostFtdcUserApiStruct.h(6943,1): warning C4819: 该文件包含不能在当前代码页(936)中表示的字符。请将 该文件保存为 Unicode 格式以防止数据
    丢失 [E:\projects\ctp-swig\6.3.15\build\_thosttraderapi.vcxproj]
    E:\projects\ctp-swig\6.3.15\win64\ThostFtdcUserApiStruct.h(8014,1): warning C4819: 该文件包含不能在当前代码页(936)中表示的字符。请将 该文件保存为 Unicode 格式以防止数据
    丢失 [E:\projects\ctp-swig\6.3.15\build\_thosttraderapi.vcxproj]
    正在创建库 E:/projects/ctp-swig/6.3.15/build/Release/_thosttraderapi.lib 和对象 E:/projects/ctp-swig/6.3.15/build/Release/_thosttraderap
    i.exp
    _thosttraderapi.vcxproj -> E:\projects\ctp-swig\6.3.15\build\Release\_thosttraderapi.dll
    Building Custom Rule E:/projects/ctp-swig/6.3.15/CMakeLists.txt
    1 file(s) copied.
    1 file(s) copied.
    ########################## Compile 312 ##########################
    -- Building for: Visual Studio 17 2022
    CMake Deprecation Warning at CMakeLists.txt:1 (cmake_minimum_required):
    Compatibility with CMake < 3.5 will be removed from a future version of
    CMake.

    Update the VERSION argument <min> value or use a ...<max> suffix to tell
    CMake that the project does not need compatibility with older versions.


    -- Selecting Windows SDK version 10.0.22621.0 to target Windows 10.0.19045.
    -- The C compiler identification is MSVC 19.37.32822.0
    -- The CXX compiler identification is MSVC 19.37.32822.0
    -- Detecting C compiler ABI info
    -- Detecting C compiler ABI info - done
    -- Check for working C compiler: D:/Microsoft Visual Studio/2022/Community/VC/Tools/MSVC/14.37.32822/bin/Hostx64/x64/cl.exe - skipped
    -- Detecting C compile features
    -- Detecting C compile features - done
    -- Detecting CXX compiler ABI info
    -- Detecting CXX compiler ABI info - done
    -- Check for working CXX compiler: D:/Microsoft Visual Studio/2022/Community/VC/Tools/MSVC/14.37.32822/bin/Hostx64/x64/cl.exe - skipped
    -- Detecting CXX compile features
    -- Detecting CXX compile features - done
    -- Configuring done (2.8s)
    -- Generating done (0.0s)
    -- Build files have been written to: E:/projects/ctp-swig/6.3.15/build
    MSBuild version 17.7.2+d6990bcfa for .NET Framework

    MSBuild version 17.7.2+d6990bcfa for .NET Framework

    1>Checking Build System
    Building Custom Rule E:/projects/ctp-swig/6.3.15/CMakeLists.txt
    thostmduserapi_wrap.cxx
    E:\projects\ctp-swig\6.3.15\win64\ThostFtdcUserApiStruct.h(1,1): warning C4819: 该文件包含不能在当前代码页(936)中表示的字符。请将该文件保存为 Unicode 格式以防止数据丢失
    [E:\projects\ctp-swig\6.3.15\build\_thostmduserapi.vcxproj]
    E:\projects\ctp-swig\6.3.15\win64\ThostFtdcUserApiStruct.h(1153,1): warning C4819: 该文件包含不能在当前代码页(936)中表示的字符。请将 该文件保存为 Unicode 格式以防止数据
    丢失 [E:\projects\ctp-swig\6.3.15\build\_thostmduserapi.vcxproj]
    E:\projects\ctp-swig\6.3.15\win64\ThostFtdcUserApiStruct.h(6943,1): warning C4819: 该文件包含不能在当前代码页(936)中表示的字符。请将 该文件保存为 Unicode 格式以防止数据
    丢失 [E:\projects\ctp-swig\6.3.15\build\_thostmduserapi.vcxproj]
    E:\projects\ctp-swig\6.3.15\win64\ThostFtdcUserApiStruct.h(8014,1): warning C4819: 该文件包含不能在当前代码页(936)中表示的字符。请将 该文件保存为 Unicode 格式以防止数据
    丢失 [E:\projects\ctp-swig\6.3.15\build\_thostmduserapi.vcxproj]
    E:\projects\ctp-swig\6.3.15\thostmduserapi_wrap.cxx(316364,16): warning C4244: “初始化”: 从“Py_ssize_t”转换到“int”，可能丢失数据 [E:\projects\ctp-
    swig\6.3.15\build\_thostmduserapi.vcxproj]
    E:\projects\ctp-swig\6.3.15\thostmduserapi_wrap.cxx(316421,16): warning C4244: “初始化”: 从“Py_ssize_t”转换到“int”，可能丢失数据 [E:\projects\ctp-
    swig\6.3.15\build\_thostmduserapi.vcxproj]
    E:\projects\ctp-swig\6.3.15\thostmduserapi_wrap.cxx(316478,16): warning C4244: “初始化”: 从“Py_ssize_t”转换到“int”，可能丢失数据 [E:\projects\ctp-
    swig\6.3.15\build\_thostmduserapi.vcxproj]
    E:\projects\ctp-swig\6.3.15\thostmduserapi_wrap.cxx(316535,16): warning C4244: “初始化”: 从“Py_ssize_t”转换到“int”，可能丢失数据 [E:\projects\ctp-
    swig\6.3.15\build\_thostmduserapi.vcxproj]
    正在创建库 E:/projects/ctp-swig/6.3.15/build/Release/_thostmduserapi.lib 和对象 E:/projects/ctp-swig/6.3.15/build/Release/_thostmduserap
    i.exp
    _thostmduserapi.vcxproj -> E:\projects\ctp-swig\6.3.15\build\Release\_thostmduserapi.dll
    Building Custom Rule E:/projects/ctp-swig/6.3.15/CMakeLists.txt
    thosttraderapi_wrap.cxx
    E:\projects\ctp-swig\6.3.15\win64\ThostFtdcUserApiStruct.h(1,1): warning C4819: 该文件包含不能在当前代码页(936)中表示的字符。请将该文件保存为 Unicode 格式以防止数据丢失
    [E:\projects\ctp-swig\6.3.15\build\_thosttraderapi.vcxproj]
    E:\projects\ctp-swig\6.3.15\win64\ThostFtdcUserApiStruct.h(1153,1): warning C4819: 该文件包含不能在当前代码页(936)中表示的字符。请将 该文件保存为 Unicode 格式以防止数据
    丢失 [E:\projects\ctp-swig\6.3.15\build\_thosttraderapi.vcxproj]
    E:\projects\ctp-swig\6.3.15\win64\ThostFtdcUserApiStruct.h(6943,1): warning C4819: 该文件包含不能在当前代码页(936)中表示的字符。请将 该文件保存为 Unicode 格式以防止数据
    丢失 [E:\projects\ctp-swig\6.3.15\build\_thosttraderapi.vcxproj]
    E:\projects\ctp-swig\6.3.15\win64\ThostFtdcUserApiStruct.h(8014,1): warning C4819: 该文件包含不能在当前代码页(936)中表示的字符。请将 该文件保存为 Unicode 格式以防止数据
    丢失 [E:\projects\ctp-swig\6.3.15\build\_thosttraderapi.vcxproj]
    正在创建库 E:/projects/ctp-swig/6.3.15/build/Release/_thosttraderapi.lib 和对象 E:/projects/ctp-swig/6.3.15/build/Release/_thosttraderap
    i.exp
    _thosttraderapi.vcxproj -> E:\projects\ctp-swig\6.3.15\build\Release\_thosttraderapi.dll
    Building Custom Rule E:/projects/ctp-swig/6.3.15/CMakeLists.txt
    1 file(s) copied.
    1 file(s) copied.
    ########################## Compile 313 ##########################
    -- Building for: Visual Studio 17 2022
    CMake Deprecation Warning at CMakeLists.txt:1 (cmake_minimum_required):
    Compatibility with CMake < 3.5 will be removed from a future version of
    CMake.

    Update the VERSION argument <min> value or use a ...<max> suffix to tell
    CMake that the project does not need compatibility with older versions.


    -- Selecting Windows SDK version 10.0.22621.0 to target Windows 10.0.19045.
    -- The C compiler identification is MSVC 19.37.32822.0
    -- The CXX compiler identification is MSVC 19.37.32822.0
    -- Detecting C compiler ABI info
    -- Detecting C compiler ABI info - done
    -- Check for working C compiler: D:/Microsoft Visual Studio/2022/Community/VC/Tools/MSVC/14.37.32822/bin/Hostx64/x64/cl.exe - skipped
    -- Detecting C compile features
    -- Detecting C compile features - done
    -- Detecting CXX compiler ABI info
    -- Detecting CXX compiler ABI info - done
    -- Check for working CXX compiler: D:/Microsoft Visual Studio/2022/Community/VC/Tools/MSVC/14.37.32822/bin/Hostx64/x64/cl.exe - skipped
    -- Detecting CXX compile features
    -- Detecting CXX compile features - done
    -- Configuring done (2.7s)
    -- Generating done (0.0s)
    -- Build files have been written to: E:/projects/ctp-swig/6.3.15/build
    MSBuild version 17.7.2+d6990bcfa for .NET Framework

    MSBuild version 17.7.2+d6990bcfa for .NET Framework

    1>Checking Build System
    Building Custom Rule E:/projects/ctp-swig/6.3.15/CMakeLists.txt
    thostmduserapi_wrap.cxx
    E:\projects\ctp-swig\6.3.15\win64\ThostFtdcUserApiStruct.h(1,1): warning C4819: 该文件包含不能在当前代码页(936)中表示的字符。请将该文件保存为 Unicode 格式以防止数据丢失
    [E:\projects\ctp-swig\6.3.15\build\_thostmduserapi.vcxproj]
    E:\projects\ctp-swig\6.3.15\win64\ThostFtdcUserApiStruct.h(1153,1): warning C4819: 该文件包含不能在当前代码页(936)中表示的字符。请将 该文件保存为 Unicode 格式以防止数据
    丢失 [E:\projects\ctp-swig\6.3.15\build\_thostmduserapi.vcxproj]
    E:\projects\ctp-swig\6.3.15\win64\ThostFtdcUserApiStruct.h(6943,1): warning C4819: 该文件包含不能在当前代码页(936)中表示的字符。请将 该文件保存为 Unicode 格式以防止数据
    丢失 [E:\projects\ctp-swig\6.3.15\build\_thostmduserapi.vcxproj]
    E:\projects\ctp-swig\6.3.15\win64\ThostFtdcUserApiStruct.h(8014,1): warning C4819: 该文件包含不能在当前代码页(936)中表示的字符。请将 该文件保存为 Unicode 格式以防止数据
    丢失 [E:\projects\ctp-swig\6.3.15\build\_thostmduserapi.vcxproj]
    E:\projects\ctp-swig\6.3.15\thostmduserapi_wrap.cxx(316364,16): warning C4244: “初始化”: 从“Py_ssize_t”转换到“int”，可能丢失数据 [E:\projects\ctp-
    swig\6.3.15\build\_thostmduserapi.vcxproj]
    E:\projects\ctp-swig\6.3.15\thostmduserapi_wrap.cxx(316421,16): warning C4244: “初始化”: 从“Py_ssize_t”转换到“int”，可能丢失数据 [E:\projects\ctp-
    swig\6.3.15\build\_thostmduserapi.vcxproj]
    E:\projects\ctp-swig\6.3.15\thostmduserapi_wrap.cxx(316478,16): warning C4244: “初始化”: 从“Py_ssize_t”转换到“int”，可能丢失数据 [E:\projects\ctp-
    swig\6.3.15\build\_thostmduserapi.vcxproj]
    E:\projects\ctp-swig\6.3.15\thostmduserapi_wrap.cxx(316535,16): warning C4244: “初始化”: 从“Py_ssize_t”转换到“int”，可能丢失数据 [E:\projects\ctp-
    swig\6.3.15\build\_thostmduserapi.vcxproj]
    正在创建库 E:/projects/ctp-swig/6.3.15/build/Release/_thostmduserapi.lib 和对象 E:/projects/ctp-swig/6.3.15/build/Release/_thostmduserap
    i.exp
    _thostmduserapi.vcxproj -> E:\projects\ctp-swig\6.3.15\build\Release\_thostmduserapi.dll
    Building Custom Rule E:/projects/ctp-swig/6.3.15/CMakeLists.txt
    thosttraderapi_wrap.cxx
    E:\projects\ctp-swig\6.3.15\win64\ThostFtdcUserApiStruct.h(1,1): warning C4819: 该文件包含不能在当前代码页(936)中表示的字符。请将该文件保存为 Unicode 格式以防止数据丢失
    [E:\projects\ctp-swig\6.3.15\build\_thosttraderapi.vcxproj]
    E:\projects\ctp-swig\6.3.15\win64\ThostFtdcUserApiStruct.h(1153,1): warning C4819: 该文件包含不能在当前代码页(936)中表示的字符。请将 该文件保存为 Unicode 格式以防止数据
    丢失 [E:\projects\ctp-swig\6.3.15\build\_thosttraderapi.vcxproj]
    E:\projects\ctp-swig\6.3.15\win64\ThostFtdcUserApiStruct.h(6943,1): warning C4819: 该文件包含不能在当前代码页(936)中表示的字符。请将 该文件保存为 Unicode 格式以防止数据
    丢失 [E:\projects\ctp-swig\6.3.15\build\_thosttraderapi.vcxproj]
    E:\projects\ctp-swig\6.3.15\win64\ThostFtdcUserApiStruct.h(8014,1): warning C4819: 该文件包含不能在当前代码页(936)中表示的字符。请将 该文件保存为 Unicode 格式以防止数据
    丢失 [E:\projects\ctp-swig\6.3.15\build\_thosttraderapi.vcxproj]
    正在创建库 E:/projects/ctp-swig/6.3.15/build/Release/_thosttraderapi.lib 和对象 E:/projects/ctp-swig/6.3.15/build/Release/_thosttraderap
    i.exp
    _thosttraderapi.vcxproj -> E:\projects\ctp-swig\6.3.15\build\Release\_thosttraderapi.dll
    Building Custom Rule E:/projects/ctp-swig/6.3.15/CMakeLists.txt
    1 file(s) copied.
    1 file(s) copied.
    '/q' is not recognized as an internal or external command,
    operable program or batch file.
    Press any key to continue . . .

</details>
