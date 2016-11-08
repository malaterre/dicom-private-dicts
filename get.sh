#!/bin/bash
#set -x
set -e

dirs="hitachi agfa fuji other gems"

# I cannot use --continue, so instead simply use --no-clobber
# http://bugs.debian.org/cgi-bin/bugreport.cgi?bug=843620
file='other/McKesson Radiology 12.1.1 DICOM Conformance Statement rev1.0.pdf'
#rm -f "$file"
for d in $(ls -d $dirs)
do
  #wget --quiet -t 1 --no-content-disposition -e robots=off -c --directory-prefix=$d -i $d/lists.txt
  # $ curl -C - -O -J -L  http://www.mckesson.com/documents/providers/mckesson-radiology-12-dicom-conformance-statement/
  wget --quiet -t 1 --content-disposition -e robots=off -nc --directory-prefix=$d -i $d/lists.txt
done

for d in $(ls -d $dirs)
do
  md5sum --quiet -c ${d}/lists.md5
done
echo "success"
