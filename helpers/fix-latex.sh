#/!bin/bash

# Bash script to execute SED script and apply 
# modifications in place.

# Determine absolute path to directory in which this files resides
# (requires readlink, which is in coreutils on Debian/Ubuntu)
MYPATH="$(dirname "$(readlink -f "$0")")"

SEDSCRIPT="${MYPATH}/fix-latex.sed"

sed -rf "${SEDSCRIPT}" -i "$@"
