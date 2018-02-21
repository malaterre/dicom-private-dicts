#!/bin/sh -e

set -x

URL=https://static.healthcare.siemens.com/siemens_hwem-hwem_ssxa_websites-context-root/wcm/idc/groups/public/@global/@healthit/@imagingit/documents/download/mda2/mtcw/~edisp/vx57n-03122234.zip
#URL=http://www.healthcare.siemens.com/siemens_hwem-hwem_ssxa_websites-context-root/wcm/idc/groups/public/@global/@healthit/@imagingit/documents/download/mda1/mjy1/~edisp/syngo_fv-02184790.zip
#https://static.healthcare.siemens.com/siemens_hwem-hwem_ssxa_websites-context-root/wcm/idc/groups/public/@global/@healthit/@imagingit/documents/download/mda2/mtcw/~edisp/vx57n-03122234.zip

wget -c "$URL"
zipfile=$(basename "$URL")
rm -rf tmp
unzip -d tmp "$zipfile"

SKIP=1477268
COUNT=185436

#infile=tmp/syngo_fV/syngo_fV.exe
infile=tmp/VX57N_syngo_fV/syngo_fV.exe
tmpfile=syngo_tmp.txt
outfile=syngo_fV.txt

# extract all 3 dicts at once, they will be separated by 2 or 3 '0A' (end of file) character.
dd skip=$SKIP count=$COUNT if="$infile" of="$tmpfile" bs=1

# curly single quotes (U+2018 and U+2019, which are 0x91 and 0x92 in CP1252
# (also known as MS-ANSI and WINDOWS-1252; a common 8-bit encoding on Windows)).
iconv -o "$outfile" -f WINDOWS-1252 -t UTF8 $tmpfile

# Prefer UNIX eol:
sed -i 's/\r//' "$outfile"

# fix end of file:
echo "" >> "$outfile"
