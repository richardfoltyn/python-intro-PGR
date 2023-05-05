#/!bin/bash

# Bash script to execute SED script and apply 
# modifications in place.
# This applies the modification needed for the course book.

# Determine absolute path to directory in which this files resides
# (requires readlink, which is in coreutils on Debian/Ubuntu)
MYPATH="$(dirname "$(readlink -f "$0")")"

SEDSCRIPT="${MYPATH}/fix-book.sed"

sed -rf "${SEDSCRIPT}" -i "$@"
