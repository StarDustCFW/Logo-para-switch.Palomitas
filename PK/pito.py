#!/usr/bin/env python3

import sys
import os
import subprocess
from PIL import Image
from pathlib import Path
from ips_util import Patch

import io
import ips
import argparse

def single(base_patch,Datts):
    #Get Offset And build ID
    build_id = Datts[0:64]
    offset = int(Datts[64:-1]+Datts[-1])

    print (Datts)
    print (build_id)
    print (offset)
    
    tmp_p = ips.Patch()

    for r in base_patch.records:
        tmp_p.add_record(r.offset + offset, r.content, r.rle_size)

    #Build the patch
    if len(sys.argv) > 4:
        patch_path = Path(sys.argv[4])
    else:
        patch_path = Path("ips", f"{build_id}.ips")
    #save the patch
    with patch_path.open("w+b") as f:
        f.write(bytes(tmp_p))	

def Multiple(base_patch,Datts):
    print(base_patch)
    print(Datts)
    
    # Using readlines()
    file1 = open(Datts, 'r')
    Lines = file1.readlines()
     
    count = 0
    # Strips the newline character
    for line in Lines:
        txt = line.strip()
        x = txt.split(",")
        print(x)
        single(base_patch,x[1]+x[2])

if __name__ == "__main__":
    if len(sys.argv) < 3:
        print("Invalid arguments 3")
        sys.exit(1)

    #load the new Image 
    new_logo = Image.open(sys.argv[2])
    new_logo = new_logo.convert("RGBA")

    #load the base image
    if len(sys.argv) > 3:
        old_logo = Image.open(sys.argv[3])
    else:
        old_logo = Image.open("logo.png")

    old_logo = old_logo.convert("RGBA")
    

    base_patch = ips.Patch.create(old_logo.tobytes(), new_logo.tobytes())
    Datts = sys.argv[1]
    if Datts == 'data.txt':
        Multiple(base_patch,Datts)
    else:
        single(base_patch,Datts)
	


