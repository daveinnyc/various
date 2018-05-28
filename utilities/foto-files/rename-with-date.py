from PIL import Image
from PIL.ExifTags import TAGS
import os
import re
import datetime

is_jpg = re.compile("jpg$", re.IGNORECASE)
index_num = 1
current_date = ["0","0","0"]
for f in os.listdir("."):
    if os.path.isfile(f):
        if re.search(is_jpg, f):
            try:
                # Try to open the file to extract data
                image_file = Image.open(f)
                tags = image_file._getexif()
                file_name_base = ""
                image_file.close()
                try:
                    # Try to get date foto was taken
                    date_part = tags[36867][:10]
                    year, month, day = date_part.split(":")
                except Exception as e:
                    print("ERROR: processing {}  {}".format(f, str(e)))
                    raw_alt_date = str(datetime.datetime.fromtimestamp(os.path.getctime(f)))
                    year, month, day = raw_alt_date[:10].split("-")
                    file_name_base = "MISSING_CREATE_DATE.."

                # Check if there are already files with this date, increment 
                #   index counter as needed. Only works for sequential 
                #   processing. Check for uniqueness before name change
                current_working_date = [year, month, day]
                if current_date == current_working_date:
                    index_num += 1
                else:
                    current_date = current_working_date
                    index_num = 1                 
                file_number = str(index_num).zfill(3)

                new_file_name = "{}{}-{}-{}..{}.jpg".format(file_name_base, 
                                                            year, month, day,
                                                            file_number)

                if f != new_file_name:
                    while os.path.isfile(new_file_name):
                        print("COLLISION: {}".format(new_file_name))
                        possible_index = int(new_file_name[-7:-4]) + 1
                        file_number = str(possible_index).zfill(3)
                        new_file_name = "{}{}-{}-{}..{}.jpg".format(file_name_base, 
                                                                    year, month, day,
                                                                    file_number)

                    os.rename(f, new_file_name)
                    print("{}  {}".format(f, new_file_name))
                else:
                    print("Skip {}".format(f))
            except Exception as e:
                print("ERROR: processing {}  {}".format(f, str(e)))
