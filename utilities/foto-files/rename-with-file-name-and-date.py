'''
Adds a date to a foto with an existing filename
'''


from PIL import Image
from PIL.ExifTags import TAGS
import os
import re
import datetime

is_jpg = re.compile("jpg$", re.IGNORECASE)
num = 1
for f in os.listdir("."):
    if os.path.isfile(f):
        if re.search(is_jpg, f):
            try:
                # Try to open the file to extract data
                image_file = Image.open(f)
                tags = image_file._getexif()
                file_name_base = f[:-4].lower()
                image_file.close()
                try:
                    # Try to get date foto taken
                    date_part = tags[36867][:10]
                    year, month, day = date_part.split(":")
                except Exception as e:
                    print("ERROR: processing {}  {}".format(f, str(e)))
                    raw_alt_date = str(datetime.datetime.fromtimestamp(os.path.getctime(f)))
                    year, month, day = raw_alt_date[:10].split("-")
                    file_name_base = "MISSING_CREATE_DATE.." + file_name_base
                file_number = str(num).zfill(3)
                new_file_name = "{}..{}-{}-{}..{}.jpg".format(file_name_base, 
                                                              year, month, day,
                                                              file_number)
                os.rename(f, new_file_name)
            except Exception as e:
                print("ERROR: processing {}  {}".format(f, str(e)))
           