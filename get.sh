#!/bin/bash
set -x
#set -e
for d in $(ls -d */)
do
  echo $d
  #wget -c -i $i
  wget --quiet -t 1 -e robots=off -c --directory-prefix=$d -i $d/lists.txt
done

for d in $(ls -d */)
do
  md5sum ${d}*.pdf > ${d}lists.md5
done

for d in $(ls -d */)
do
  md5sum --quiet -c ${d}lists.md5
done
