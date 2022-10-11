import glob
import os
from PIL import Image

# change file type in recursive

target_dir = input("target dir:")
remove_old = input("remove old:(y/n)")

before_ext = "jpg"
after_ext = "png"

input_paths = glob.glob(os.path.join(target_dir, "**/*." + before_ext), recursive=True)
print("input paths:", input_paths)

for input_path in input_paths:
    output_path = input_path.replace("."+before_ext, "."+after_ext)

    img = Image.open(input_path)
    img2 = img.convert("RGB")
    img2.save(output_path, "JPEG")

    if remove_old == "y":
        os.remove(input_path)