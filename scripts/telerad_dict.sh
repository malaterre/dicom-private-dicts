#!/bin/sh

#set -e
set -x

URL=https://connect.capitalradiology.com.au/InteleViewer/win32/InteleViewer-install-win32.exe
# https://connect.capitalradiology.com.au/InteleViewer/

wget -c "$URL"
zipfile=$(basename "$URL")
rm -rf tmp1
unzip -q -d tmp1 "$zipfile"
# do not set -e here

rm -rf tmp2
unzip -q -d tmp2 tmp1/InstallerData/Disk1/InstData/Resource1.zip

pushd 'tmp2/$IA_PROJECT_DIR$/Resources/dicom_scp/'
jar xf DicomScp.jar
CLASSPATH=DicomScp.jar procyon com/intelerad/lib/dicomtools/PrivateElement > PrivateElement.java
CLASSPATH=DicomScp.jar procyon com/intelerad/lib/dicomtools/PrivateElementEntry > PrivateElementEntry.java
#    public static PrivateElementEntry createImsEntry(final int n, final int n2, final int n3, final String s) {
#        return createEntry(n, n2, n3, s, "INTELERAD MEDICAL SYSTEMS");
#    }
#    
#    public static PrivateElementEntry createIvEntry(final int n, final int n2, final int n3, final String s) {
#        return createEntry(n, n2, n3, s, "INTELERAD MEDICAL SYSTEMS INTELEVIEWER");
#    }
grep "PrivateElementEntry.create" PrivateElement.java > PrivateElement.txt
wc PrivateElement.txt
grep "PrivateElementEntry.createIv" PrivateElement.txt > p1.txt
grep "PrivateElementEntry.createIms" PrivateElement.txt > p2.txt
# 85 entries as of 2018/02/20
wc p1.txt p2.txt
sed -e "s/.*createIvEntry\((.*)\).*/\1/" p1.txt > /tmp/iv.txt
sed -e "s/.*createImsEntry\((.*)\).*/\1/" p2.txt > /tmp/ims.txt
popd
