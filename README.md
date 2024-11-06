# ctp-swig

Swig 转换 CTPAPI 到 Python 全攻略

## 快速使用

#TODO pip安装 及 手动从openctp官网获取dll

## 环境准备

使用以下环境构建，仅供参考

### Windows

- Windows 10
- CMake 3.30.4
- VisualStudio 2022
- Swig 4.1.1

### Linux

- Debian 12
- CMake 3.25.1
- g++ 12.2.0
- Swig 4.2.1

## Swig 转换

#TODO 转换过程，详细说明

<details>
    <summary>Windows 编译示例</summary>

    PS E:\projects\ctp-swig> .\compile-win.bat 6.3.15
    ############################### Enter CTPAPI: 6.3.15 ##############################


    ############################ Clear files ###############################

    The system cannot find the file specified.
    Could Not Find E:\projects\ctp-swig\6.3.15\*_wrap.*
    Could Not Find E:\projects\ctp-swig\6.3.15\CMakeLists.txt

    ########################## Swig generate cpp/py files ##################

    A subdirectory or file py already exists.
    win64\ThostFtdcTraderApi.h(30) : Warning 514: Director base class CThostFtdcTraderSpi has no virtual destructor.
    win64\ThostFtdcMdApi.h(30) : Warning 514: Director base class CThostFtdcMdSpi has no virtual destructor.

    ############################### Compile CTPAPI: 6.3.15 Python: 313 ###############

            1 file(s) copied.
    A subdirectory or file py\py313 already exists.
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
    -- Configuring done (3.1s)
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

    ############################ Clear files ###############################

</details>

<details>
    <summary>Linux编译示例</summary>

    root@Jedore-win:~/ctp-swig# ./compile-linux.sh 6.6.7
    ######################################################## Enter 6.6.7 #######################


    ######################################################## Clear files #######################

    rm: cannot remove '*_wrap.*': No such file or directory

    ################################################ Swig generate cpp/py files ################

    lin64/ThostFtdcTraderApi.h:30: Warning 514: Director base class CThostFtdcTraderSpi has no virtual destructor.
    lin64/ThostFtdcMdApi.h:30: Warning 514: Director base class CThostFtdcMdSpi has no virtual destructor.

    ######################################################### Compile ##########################

    mkdir: cannot create directory ‘py’: File exists
    CMake Deprecation Warning at CMakeLists.txt:1 (cmake_minimum_required):
      Compatibility with CMake < 2.8.12 will be removed from a future version of
      CMake.

      Update the VERSION argument <min> value or use a ...<max> suffix to tell
      CMake that the project does not need compatibility with older versions.


    -- The C compiler identification is GNU 12.2.0
    -- The CXX compiler identification is GNU 12.2.0
    -- Detecting C compiler ABI info
    -- Detecting C compiler ABI info - done
    -- Check for working C compiler: /usr/bin/cc - skipped
    -- Detecting C compile features
    -- Detecting C compile features - done
    -- Detecting CXX compiler ABI info
    -- Detecting CXX compiler ABI info - done
    -- Check for working CXX compiler: /usr/bin/c++ - skipped
    -- Detecting CXX compile features
    -- Detecting CXX compile features - done
    -- Configuring done
    -- Generating done
    -- Build files have been written to: /root/ctp-swig/6.6.7/build
    [ 25%] Building CXX object CMakeFiles/_thosttraderapi.dir/thosttraderapi_wrap.cxx.o
    [ 50%] Linking CXX shared library _thosttraderapi.so
    [ 50%] Built target _thosttraderapi
    [ 75%] Building CXX object CMakeFiles/_thostmduserapi.dir/thostmduserapi_wrap.cxx.o
    [100%] Linking CXX shared library _thostmduserapi.so
    [100%] Built target _thostmduserapi

    ####################################################### Clear files #######################

</details>


<details>
    <summary>Linux编译结果</summary>

    # tree 6.7.7/py
    6.7.7/py
    ├── thostmduserapi.py
    ├── _thostmduserapi.so
    ├── thosttraderapi.py
    └── _thosttraderapi.so 

</details>


<details>
    <summary>Windows编译结果</summary>

    # tree 6.3.15/py
    6.3.15/py
    ├── py310
    │   ├── _thostmduserapi.pyd
    │   └── _thosttraderapi.pyd
    ├── py311
    │   ├── _thostmduserapi.pyd
    │   └── _thosttraderapi.pyd
    ├── py312
    │   ├── _thostmduserapi.pyd
    │   └── _thosttraderapi.pyd
    ├── py313
    │   ├── _thostmduserapi.pyd
    │   └── _thosttraderapi.pyd
    ├── py37
    │   ├── _thostmduserapi.pyd
    │   └── _thosttraderapi.pyd
    ├── py38
    │   ├── _thostmduserapi.pyd
    │   └── _thosttraderapi.pyd
    ├── py39
    │   ├── _thostmduserapi.pyd
    │   └── _thosttraderapi.pyd
    ├── thostmduserapi.py
    └── thosttraderapi.py

</details>

## 如何使用

#TODO 使用

## 声明

#TODO 注意事项及免责声明