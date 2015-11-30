#!/bin/sh -e

set -x

URL=http://folk.uio.no/jonsm/open/MR/CDVIEWER/mrgcom3.dct
#http://homepages.rpi.edu/~tichyj/ben/xRays/eFilmLite/mrgcom3.dct

wget "$URL"
