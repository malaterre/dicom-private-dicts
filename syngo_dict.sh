#!/bin/sh -e

set -x

URL=http://www.healthcare.siemens.com/siemens_hwem-hwem_ssxa_websites-context-root/wcm/idc/groups/public/@global/@healthit/@imagingit/documents/download/mda1/mjy1/~edisp/syngo_fv-02184790.zip

wget -c "$URL"
zipfile=$(basename "$URL")
rm -rf tmp
unzip -d tmp "$zipfile"

SKIP=1477268
COUNT=185436

filename=tmp/syngo_fV/syngo_fV.exe

dd skip=$SKIP count=$COUNT if="$filename" of=syngo_fV.txt bs=1
