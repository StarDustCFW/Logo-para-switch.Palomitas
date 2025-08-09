#!/usr/bin/env python3

import sys
import os
import subprocess
from PIL import Image
from pathlib import Path

def exec_cmd(cmd):
    return subprocess.check_output(cmd.split()).decode()

if __name__ == "__main__":
    if len(sys.argv) < 2:
        print("Invalid arguments")
        sys.exit(1)

    exefs_dir = Path(sys.argv[1])
    basename = os.path.basename(sys.argv[1])
    exefs_dir_out = Path("data.txt")
    if not exefs_dir.is_dir():
        print("Invalid arguments")
        sys.exit(1)
    
    old_logo = Image.open("logo.png")
    old_logo = old_logo.convert("RGBA")

    uncomp_path = Path(exefs_dir, "main_unc")

    out = exec_cmd(f"hactool -t nso {Path(exefs_dir, 'main')} --uncompressed {uncomp_path}")
    build_id = out.split("Build Id:", 1)[1].split("\n", 1)[0].strip()

    with uncomp_path.open("rb") as f:
        old_data = f.read()

    offset = old_data.find(old_logo.tobytes())
	
    print (build_id + " --> " + str(offset))
    print (basename + ',' + build_id + ',' + str(offset) + '\n')
    mec = Path(exefs_dir_out)
    with mec.open("a+") as b:
        b.write(basename + ',' + build_id + ',' + str(offset) + '\n')

    os.remove(uncomp_path)
"""
    mec = Path(exefs_dir_out,"offset")
    with mec.open("w") as b:
        b.write(str(offset))
"""
#	int("197A80", 16)


	
	
"""		
"""	
	