#!/bin/bash

pys="3.7.17 3.8.18 3.9.18 3.10.13 3.11.6 3.12.0 3.13.0"

for py in $pys; do
    echo -e "\n########################################## Test $py #####################################\n"
    pyenv local $py
    python test.py
    pyenv local --unset
done
