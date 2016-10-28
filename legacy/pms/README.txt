filetype:pdf www.medical.philips.com/main/company/connectivity/assets/docs/dicomcs/

Most DCS from philips are very difficult to parse since the private element are spread throughout the DCS...

TODO:
I found PMS-THORA-5.1, EnVisor, Threedp and INTEGRIS... woohoo nobody else got them !

TODO:
Get 0019/0029: dci.pdf
Check mr81.pdf but it looks like PHILIPS-MR-1 was renamed PHILIPS IMAGING DD 001
Get 2001 from : CS_DI_Eleva_R1.pdf
Get 2001 from : ELEVA-DI-DITTO-R232-DICOMCS-02.pdf
Get SPI-P-Private_ICS Release 1;5 from ev_41.pdf 

 iU22_9171-0009a.pdf contains table with VR=UN elements...


turn all pdf into txt:
$ for i in `ls *.pdf`; do /home/mmalaterre/Desktop/xpdf-3.02-linux/pdftotext -nopgbrk -layout $i; done

get all potential private elements:
grep -e " [0-9A-Fa-f][0-9A-Fa-f][0-9A-Fa-f][13579BDFbdf]," *.txt   

To get an idea of which file contains the most tags:
$ for i in `ls *.txt`; do grep -e " [0-9A-Fa-f][0-9A-Fa-f][0-9A-Fa-f][13579BDFbdf]," $i | wc && echo $i  ; done   

== Getting new DCS ==

Google search for:
site:www.medical.philips.com/main/company/connectivity/assets/docs/dicomcs/ filetype:pdf

and hope google is in good mood, results greatly depends on the day...

save page as search1 then tidy it up:

 tidy search1 | grep www | grep gnb > out1    
 tidy search2 | grep www | grep gnb > out2    

 cat out1 out2 > out

edit out with vim to cleanup url to please wget, store it as lists.txt, then

 wget -N -i lists.txt   

(-N will not download a file that is already present locally (check time-stamp))



UPDATE:
google:
site:http://incenter.medical.philips.com/doclib/ "DICOM Conformance"
-> newlists.txt
