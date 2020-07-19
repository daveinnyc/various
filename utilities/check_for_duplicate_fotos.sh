# Use to confirm if suspected dupicate fotos really are. 


# set -x

SAVED="../2018/05..May/"

 # Make sure there is a directory so files don't get stomped
if [ -d md5dups ]
   then
   echo "DIR: md5dups exists"
else
   mkdir md5dups
fi

for f in $(ls)
    do
       if [ -f ${SAVED}/${f} ]
          then
          suspect=($(md5sum ${f}))
          saved=($(md5sum ${SAVED}/${f}))
          if [ ${suspect} == ${saved} ]
             then
               # Move matches for now
               mv ${f} md5dups
          else
             echo "DOESN'T MATCH: ${f}"    
          fi
       fi
    done

echo "There are $(ls |wc -l) entities left"   
