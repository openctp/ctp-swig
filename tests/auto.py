"""
@Author: Jedore(https://github.com/Jedore)
@Date: 04/11/2024
"""

import os
import shutil
import platform
import sys

ctp_version = ['6.3.15']
pys = ['37', '38', '39', '310', '311', '312', '313']


def delete():
    # delete old files
    files = [
        '__init__.py',
        'auto.py',
        'test_mdapi.py',
        'test_tdapi.py',
        'win-auto.bat',
    ]
    for file in os.listdir('.'):
        if file not in files:
            if os.path.isfile(file):
                os.remove(file)
            else:
                shutil.rmtree(file)


def test():
    delete()

    for ctp in ctp_version:
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

        os.system('python test_mdapi.py')
        os.system('python test_tdapi.py')

    delete()


if __name__ == '__main__':
    test()