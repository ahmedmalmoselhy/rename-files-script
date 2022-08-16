import os
import shutil
from datetime import datetime


def rename_with_timestamp(src, des):
    now = datetime.now()
    current_time = now.strftime("%H%M%S")
    print(":: Renaming Files With Timestamps ::")
    for filename in os.listdir(src):
        name_array = os.path.splitext(filename)
        old_name = name_array[0]
        ext = name_array[1]
        new_name = old_name + "_" + current_time + "_" + ext
        print(":: file: " + src + "/" + filename + " will be renamed to " + des + "/" + new_name + " ::")
        shutil.copyfile(src + "/" + filename, des + "/" + new_name)

    return ":: Done ::"

