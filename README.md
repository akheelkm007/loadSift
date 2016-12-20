# loadSift

Extract SIFT features from a pgm image.



64 bit Ubuntu Multiarch systems

Follow this answer only if the output of file file-name shows,

file-name: ELF 32-bit LSB  executable, Intel 80386, version 1 (SYSV), dynamically linked (uses shared libs), for GNU/Linux 2.6.8, not stripped
To run 32bit executable file in a 64 bit multi-arch Ubuntu system, you have to add i386 architecture and also you have to install libc6:i386,libncurses5:i386,libstdc++6:i386 these three library packages.

sudo dpkg --add-architecture i386
sudo apt-get update
sudo apt-get install libc6:i386 libncurses5:i386 libstdc++6:i386
./file-name
