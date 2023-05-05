#!/bin/bash

# Perform initial steps export Jupyter notebooks to LaTeX and
# apply initial fixes.
# pdflatex is not run as manual fixes need to be applied first!

# Determine absolute path to directory in which this files resides
# (requires readlink, which is in coreutils on Debian/Ubuntu)
MYPATH="$(dirname "$(readlink -f "$0")")"

BASEDIR=$(realpath "${MYPATH}/..")

for f in "${BASEDIR}"/lectures/unit*.ipynb; do
    echo "Exporing ${f}"

    jupyter nbconvert \
        --execute \
        --to=latex \
        --output-dir="${BASEDIR}/latex" \
        "${f}"
done

for f in "${BASEDIR}"/latex/unit*.tex; do
    echo "Fixing LaTeX stuff in ${f}"
    "${BASEDIR}/helpers/fix-latex.sh" "${f}"
done