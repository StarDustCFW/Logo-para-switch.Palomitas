#!/usr/bin/env python3

import sys
import os
import subprocess
from PIL import Image
from pathlib import Path
from ips_util import Patch

def exec_cmd(cmd):
    return subprocess.check_output(cmd.split()).decode()

if __name__ == "__main__":
    if len(sys.argv) < 3:
        print("Invalid arguments 3")
        sys.exit(1)

    exefs_dir = Path(sys.argv[1])
    if not exefs_dir.is_dir():
        print("Invalid arguments 1")
        sys.exit(1)

    offset_file = Path(exefs_dir,"offset")
    build_id_file = Path(exefs_dir,"build_id")

    new_logo = Image.open(sys.argv[2])
    new_logo = new_logo.convert("RGBA")

    if len(sys.argv) > 3:
        old_logo = Image.open(sys.argv[3])
    else:
        old_logo = Image.open("logo.png")

    old_logo = old_logo.convert("RGBA")

    #Get The Data to build ips
    with offset_file.open("r") as f:
        offset = int(f.read())

    with build_id_file.open("r") as f:
        build_id = f.read()

    print (offset)
    print (build_id)

    #Build the patch
    new_data =  (b'\x00' * offset) + new_logo.tobytes()
    old_data =  (b'\x00' * offset) + old_logo.tobytes()
    patch = Patch.create(old_data, new_data)
	
    if len(sys.argv) > 4:
        patch_path = Path(sys.argv[4])
    else:
        patch_path = Path("ips", f"{build_id}.ips")
    #save the patch
    with patch_path.open("w+b") as f:
        f.write(patch.encode())	
	
"""		
"""	
	