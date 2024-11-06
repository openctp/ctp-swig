#!/bin/bash

if [ $# -eq 0 ]; then
  echo "Usage: $0 <ctpapi version 1: 6.3.19> <ctpapi version 2: 6.6.7> ..."
  exit 1
fi

pys="3.7.17 3.8.18 3.9.18 3.10.13 3.11.6 3.12.0 3.13.0"

for arg in "$@"; do
    for py in $pys; do
        echo -e "\n########################################## Test CTPAPI: $arg	Python: $py #####################################\n"
        pyenv local $py
	echo $(python -V)
        python test.py $arg
        pyenv local --unset
    done
done
