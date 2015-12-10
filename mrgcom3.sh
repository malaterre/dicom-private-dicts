#!/bin/sh -e

set -x

URL=http://folk.uio.no/jonsm/open/MR/CDVIEWER/mrgcom3.dct
#http://homepages.rpi.edu/~tichyj/ben/xRays/eFilmLite/mrgcom3.dct
#http://www.sepc.ac.cn/uploads/share3/%E9%B2%81%E5%9B%BD%E7%91%9E%E5%A4%87%E4%BB%BD/code/vs2005project/Mode/2012_TanYue/IPPScintnowcast_shenhua/IPPScintnowcast_shen/scintillation_plot/bin/bin.x86/dicomex/mrgcom3.dct

wget "$URL"
