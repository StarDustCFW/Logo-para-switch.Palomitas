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
        print("Invalid arguments")
        sys.exit(1)

    exefs_dir = Path(sys.argv[1])
    if not exefs_dir.is_dir():
        print("Invalid arguments")
        sys.exit(1)

    new_logo = Image.open(sys.argv[2])
    new_logo = new_logo.convert("RGBA")

    if len(sys.argv) > 3:
        old_logo = Image.open(sys.argv[3])
    else:
        old_logo = Image.open("logo.png")

    old_logo = old_logo.convert("RGBA")

    uncomp_path = Path(exefs_dir, "main_unc")

    out = exec_cmd(f"hactool -t nso {Path(exefs_dir, 'main')} --uncompressed {uncomp_path}")
    build_id = out.split("Build Id:", 1)[1].split("\n", 1)[0].strip()

    with uncomp_path.open("rb") as f:
        old_data = f.read()
        
        
    
    offset = old_data.find(old_logo.tobytes())
    print (offset)
#	int("197A80", 16)

    new_data =  (b'\x00' * offset) + new_logo.tobytes()
    old_data =  (b'\x00' * offset) + old_logo.tobytes()
    patch = Patch.create(old_data, new_data)
	
    mec = Path("ips/en.raw")
    with mec.open("w+b") as b:
        b.write(new_data)

    mec = Path("ips/eo.raw")
    with mec.open("w+b") as b:
        b.write(old_data)


#    new_data = old_data.replace(old_logo.tobytes(), new_logo.tobytes())

#    patch = Patch.create(old_data, new_data)
#    patch = Patch.create(old_logo.tobytes(), new_logo.tobytes())

    if len(sys.argv) > 4:
        patch_path = Path(sys.argv[4])
    else:
        patch_path = Path("ips", f"{build_id}.ips")

    with patch_path.open("w+b") as f:
        f.write(patch.encode())

    os.remove(uncomp_path)
	
	
"""		
"""	
	