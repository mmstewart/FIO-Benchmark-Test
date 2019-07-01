#!/usr/bin/python
# -*- coding: utf-8 -*-

import subprocess
import os

cmd = subprocess.Popen(["sudo", "fio", "--filename=/dev/sdg", "--name=test1", "--ioengine=libaio", 
"--bs=4k", "--rw=read", "--iodepth=32", "--runtime=10"], 
stdout = subprocess.PIPE, stderr = subprocess.PIPE, preexec_fn = os.setpgrp)

print(cmd.stdout.read().decode())
