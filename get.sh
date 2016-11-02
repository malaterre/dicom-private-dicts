#!/bin/bash
set -x
set -e
dirs="hitachi agfa fuji other"
for d in $(ls -d $dirs)
do
  #echo $d
  #wget -c -i $i
  wget --quiet -t 1 -e robots=off -c --directory-prefix=$d -i $d/lists.txt
done

#for d in $(ls -d $dirs)
#do
#  md5sum ${d}/*.pdf > ${d}/lists.md5
#  pdffiles=(${d}/*.PDF)
#  if [ -e "${pdffiles[0]}" ];
#  then
#    md5sum ${d}/*.PDF >> ${d}/lists.md5
#  fi
#done

for d in $(ls -d $dirs)
do
  md5sum --quiet -c ${d}/lists.md5
done
echo "success"
