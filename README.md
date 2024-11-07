<h1 align="center"> ctp-swig </h1>

<div>
    <a href="#"><img src="https://flat.badgen.net/badge/os/Win-x86_64/cyan?icon=windows" /></a>
    <a href="#"><img src="https://img.shields.io/badge/os-Linux_x86_64-white?style=flat-square&logo=linux&logoColor=white&color=rgb(35%2C189%2C204)" /></a>
    <a href="#"><img src="https://flat.badgen.net/badge/CTPAPI/6.3.15~6.7.7/blue" /></a>
    <a href="#"><img src="https://flat.badgen.net/badge/Python/3.7~3.13/blue" /></a>
    <a href="https://pepy.tech/project/openctp-ctp" ><img src="https://static.pepy.tech/badge/openctp-ctp" /></a>
    <a href="#" ><img src="https://flat.badgen.net/badge/License/BSD-3/blue?" /></a>
    <a href="#" ><img src="https://flat.badgen.net/badge/Test/PASS/green?" /></a>
</div>

<br>

Swig 转换 CTPAPI 为 Python 最全攻略!!!

## 快速使用

不需要自己编译的小伙伴，可以参考以下两种方式直接使用编译完成的库

### 方式一 pip install

```bash
pip install openctp-ctp==6.7.2.* -i https://pypi.tuna.tsinghua.edu.cn/simple --trusted-host=pypi.tuna.tsinghua.edu.cn
```

### 方式二 官网下载

从 openctp 官方网站下载编译完成的库，手动配置，[CTPAPI-Python接口下载](http://openctp.cn/download.html)

## 环境准备

提供了在 Windows / Linux 两种平台下的编译方案, 各软件版本号为作者实际编译时使用的版本

### Windows

- Windows 10
- CMake 3.30.4
- VisualStudio 2022
- Swig 4.1.1
- Python 3.7 ~ 3.13

  作者需要编译多个Python版本， 使用 pyenv-win 安装，简单方便. [参考文章](https://zhuanlan.zhihu.com/p/638559475)

### Linux

- Debian 12
- CMake 3.25.1
- g++ 12.2.0
- Swig 4.2.1
- Python 3.7 ~ 3.13

## Swig 转换

准备好环境后，进行编译实践

### 1. 克隆仓库

```bash
git clone https://github.com/openctp/ctp-swig.git
```

或

```bash
git clone git@github.com:openctp/ctp-swig.git
```

### 2. 修改文件

#### Windows

- compile-win.bat
  ```text
  set pys=37_3.7.9;38_3.8.10;39_3.9.13;310_3.10.11;311_3.11.8;312_3.12.1;313_3.13.0
  ```
  将 `pys` 设置成需要编译的Python版本(已经安装), 如 安装了 3.7.17、3.12.7，则设置成
  ```text
  set pys=37_3.7.17;312_3.12.7
  ``` 
- CMakeLists.txt
  ```text
  if (${CMAKE_SYSTEM_NAME} MATCHES "Windows")
      SET(PY_VER "python_value" CACHE STRING "Python Version")
      SET(PY_LIB "python_lib_value" CACHE STRING "Python Lib Version")

      include_directories(${PROJECT_SOURCE_DIR}
          ${PROJECT_SOURCE_DIR}/win64
          D:/pyenv-win/pyenv-win/versions/${PY_VER}/include
          )
      link_directories(${PROJECT_SOURCE_DIR}
          ${PROJECT_SOURCE_DIR}/win64
          D:/pyenv-win/pyenv-win/versions/${PY_VER}/libs
          )
      add_compile_options(/bigobj /MT)
  ```
  上面有两个路径需要修改
    - Python头文件路径 `D:/pyenv-win/pyenv-win/versions//${PY_VER}/include`
    - Python库路径 `D:/pyenv-win/pyenv-win/versions/${PY_VER}/libs`

  将前缀部分`D:/pyenv-win/pyenv-win/versions/`替换为本地安装的Python目录

#### Linux

- CMakeLists.txt
  ```text
  elseif (${CMAKE_SYSTEM_NAME} MATCHES "Linux")
    include_directories(${PROJECT_SOURCE_DIR}
        ${PROJECT_SOURCE_DIR}/lin64
        /root/.pyenv/versions/3.12.0/include/python3.12/
        )  
  ```
  将上面的路径 `/root/.pyenv/versions/3.12.0/include/python3.12/` 修改为安装的Python对应的目录

### 3. 构建编译

可以选择一次性编译 **一个** 或 **多个** CTPAPI 版本

- Windows

  ```shell
  ./compile-win.bat 6.3.19 6.6.7
  ```

- Linux

  ```shell
  ./compile-linux.sh 6.3.19 6.6.7
  ```

编译成功后，可在对应版本的 CTPAPI 文件夹下发现多出了一个 `py` 文件夹，里面是编译成功的Python接口文件, 由于 Windows
下各Python版本编译的Python库不可共用，所以每个Python版都有一个对应的接口文件夹

### 附带编译展示

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

## 如何使用

#TODO

## 字符集问题

在Linux下使用，由于CTPAPI是GBK编码，需要安装中文字符集，否则导入时报错：

```text
>>> import openctp_ctp
terminate called after throwing an instance of 'std::runtime_error'
what():  locale::facet::_S_create_c_locale name not valid
Aborted
```

或

```text
>>> import openctp_ctp
Aborted
```

需要安装 `GB18030` 字符集，这里提供 ubuntu/debian/centos 的方案：

```bash
# Ubuntu (20.04)
sudo apt-get install -y locales
sudo locale-gen zh_CN.GB18030

# Debian (11/12)
sudo apt install locales-all
sudo localedef -c -f GB18030 -i zh_CN zh_CN.GB18030

# CentOS (7)
sudo yum install -y kde-l10n-Chinese
sudo yum reinstall -y glibc-common

# CentOS (8/9)
sudo yum install langpacks-zh_CN.noarch
sudo yum reinstall glibc-common
```

## 注意

- 本仓库涉及的CTPAPI均为生产版本，不可用于穿透测试。

## 声明

**用于实盘前请充分测试相应的功能，openctp不对此承担任何责任**
