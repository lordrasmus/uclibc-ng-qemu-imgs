#!/usr/bin/python


import glob

confs = glob.glob("*.config")


checks= ["CONFIG_SIGNALFD", "CONFIG_TIMERFD","CONFIG_SYSVIPC","CONFIG_POSIX_MQUEUE", "INOTIFY_USER","UNIX", "CONFIG_INET", "CONFIG_SWAP","CONFIG_PRINTK_TIME","CONFIG_IKCONFIG","CONFIG_IKCONFIG_PROC"]

for c in confs:
    with open(c,"r") as f:
        data = f.read()
        

    print( c )
    
    for ch in checks:
        if not ch+"=y" in data:
            print( "   \033[01;32m" + ch + "\033[00m aktivieren" )


