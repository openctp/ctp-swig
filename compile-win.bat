@echo off

if "%~1"=="" (
    echo "Usage: ./%~n0.bat <ctpapi version 1: 6.3.19> <ctpapi version 2: 6.6.7> ..."
    exit /b 1
)

set pys=37_3.7.9;38_3.8.10;39_3.9.13;310_3.10.11;311_3.11.8;312_3.12.1;313_3.13.0

for %%i in (%*) do (
    echo ############################### Enter CTPAPI: %%i ##############################
    echo.
    cd %%i

    echo.
    echo ############################ Clear files ###############################
    echo.

    rmdir /s /q build
    del *_wrap.*
    del CMakeLists.txt

    echo.
    echo ########################## Swig generate cpp/py files ##################
    echo.

    mkdir py
    swig -threads -c++ -python -outdir py -outcurrentdir -Iwin64 ..\thosttraderapi.i
    swig -threads -c++ -python -outdir py -outcurrentdir -Iwin64 ..\thostmduserapi.i

    for %%j in (%pys%) do (
        for /f "tokens=1,2 delims=_" %%a in ("%%j") do (
            echo.
            echo ############################### Compile CTPAPI: %%i Python: %%a ###############
            echo.

            copy ..\CMakeLists.txt .

            mkdir build
            mkdir py\py%%a

            cmake -S . -B build -DPY_VER="%%b" -DPY_LIB=%%a -A x64
            cmake --build build --config Release --clean-first

            copy build\Release\_thosttraderapi.dll py\py%%a\_thosttraderapi.pyd
            copy build\Release\_thostmduserapi.dll py\py%%a\_thostmduserapi.pyd

            rmdir /s /q build
        )
    )

    echo.
    echo ############################ Clear files ###############################
    echo.

    del *_wrap.*
    del CMakeLists.txt
    cd ..
)