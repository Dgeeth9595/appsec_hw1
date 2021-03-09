from os import walk
import os

f = []
path = "./part3/Fuzzer_Output/output/queue/"
for (dirpath, dirnames, filenames) in walk(path):
    f.extend(filenames)
    for filename in filenames:
        print filename
        output1 = os.system("./../giftcardreader 1 "+ path+filename)
        output2 = os.system("./../giftcardreader 1 "+ path+filename)
        print output1
        print ""
        print output2
    break
