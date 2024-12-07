"""
@Author: Jedore(https://github.com/Jedore)
@Date: 04/11/2024
"""

import os
import shutil
import platform
import sys


def delete():
    # delete old files
    files = [
        '__init__.py',
        'test.py',
        'test_mdapi.py',
        'test_tdapi.py',
        'test-win.bat',
        'test-linux.sh',
    ]
    for file in os.listdir('.'):
        if file not in files:
            if os.path.isfile(file):
                os.remove(file)
            else:
                shutil.rmtree(file)


def test(ctp: str):
    delete()

    if platform.system().startswith('Windows'):
        # copy new files & test
        src = os.path.join('..', ctp, 'win64')
        shutil.copy(os.path.join(src, 'thostmduserapi_se.dll'), '.')
        shutil.copy(os.path.join(src, 'thosttraderapi_se.dll'), '.')

        src = os.path.join('..', ctp, 'py')
        shutil.copy(os.path.join(src, 'thostmduserapi.py'), '.')
        shutil.copy(os.path.join(src, 'thosttraderapi.py'), '.')
        py_version = f'py{sys.version_info.major}{sys.version_info.minor}'
        src = os.path.join('..', ctp, 'py', py_version)
        shutil.copy(os.path.join(src, '_thostmduserapi.pyd'), '.')
        shutil.copy(os.path.join(src, '_thosttraderapi.pyd'), '.')

    elif platform.system().startswith('Linux'):
        # copy new files & test
        src = os.path.join('..', ctp, 'lin64')
        shutil.copy(os.path.join(src, 'thostmduserapi_se.so'), '.')
        shutil.copy(os.path.join(src, 'thosttraderapi_se.so'), '.')

        src = os.path.join('..', ctp, 'py')
        shutil.copy(os.path.join(src, 'thostmduserapi.py'), '.')
        shutil.copy(os.path.join(src, 'thosttraderapi.py'), '.')
        shutil.copy(os.path.join(src, '_thostmduserapi.so'), '.')
        shutil.copy(os.path.join(src, '_thosttraderapi.so'), '.')

    os.system('python -V')
    os.system('python test_mdapi.py')
    os.system('python test_tdapi.py')

    delete()


if __name__ == '__main__':
    if len(sys.argv) == 1:
        print(f"Usage: {sys.argv[0]} <ctpapi version: 6.3.15>")
        exit(0)

    test(sys.argv[1])
