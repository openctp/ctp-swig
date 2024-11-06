@echo off

if "%~1"=="" (
    echo "Usage: ./%~n0.bat <ctpapi version 1: 6.3.19> <ctpapi version 2: 6.6.7> ..."
    exit /b 1
)

set pys=3.7.9;3.8.10;3.9.13;3.10.11;3.11.8;3.12.1;3.13.0

for %%i in (%*) do (

    for %%j in (%pys%) do (
        echo ########################################## Test CTPAPI: %%i Python: %%j #####################################
        pyenv local %%j
        python -V
        python test.py %%i
    )
)
