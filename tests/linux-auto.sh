#!/bin/bash

pys="3.7.17 3.8.18 3.9.18 3.10.13 3.11.6 3.12.0"

for py in $pys; do
    echo "########################################## TEST $py #####################################"
    pyenv local $py
    python auto.py
    pyenv local --unset
done
