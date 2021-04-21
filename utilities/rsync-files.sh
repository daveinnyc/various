rsync --stats \
       --recursive \
       --checksum \
       --delete-during \
       --no-perms \
       --progress \
       --itemize-changes \
       --log-file=rsync-log-files..$(date +'%Y-%m-%d')\
       /mnt/g/${1}   /mnt/e/FILES/


 #     --verbose \
 #     --dry-run \
 #
 #     ls > top-dirs
 #     Remove windows sys files from top-dirs
 # USAGE:  for i in $(cat top-dirs) ; do ./rsync-files.sh ${i} ; done
