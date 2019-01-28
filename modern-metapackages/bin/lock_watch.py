#!/usr/bin/python3

# Watch for xscreensaver lock / unlock events to pause notifications etc

import subprocess
import sys

for line in sys.stdin:
        state = line.strip().split()[0]
        if state == 'LOCK':
            subprocess.run('killall -SIGUSR1 dunst', shell=True)
            subprocess.run('echo RELOADAGENT | gpg-connect-agent', shell=True)
            subprocess.run('ssh-add -D', shell=True)
        elif state == 'UNBLANK':
            subprocess.run('killall -SIGUSR2 dunst', shell=True)
