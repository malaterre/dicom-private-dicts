#!/bin/bash
#set -x
set -e

dirs="hitachi agfa fuji other"
for d in $(ls -d $dirs)
do
  wget --quiet -t 1 -e robots=off -c --directory-prefix=$d -i $d/lists.txt
done

for d in $(ls -d $dirs)
do
  md5sum --quiet -c ${d}/lists.md5
done
echo "success"
