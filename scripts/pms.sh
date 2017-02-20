#!/bin/sh -e

set -x

URL=https://raw.githubusercontent.com/Kevin-Mattheus-Moerman/GIBBON/master/dicomDict/PMS-R32-dict.txt

wget "$URL"
