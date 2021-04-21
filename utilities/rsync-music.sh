MUSIC_DIR=/mnt/f/
BACKUP_DIR=/mnt/e/MUSIC/
DIR_LIST=$(ls ${MUSIC_DIR} |grep -v 'System ' | grep -v CYCLE)

 echo ${DIR_LIST}

 for d in ${DIR_LIST} ; do
    rsync --verbose \
          --recursive \
          --checksum \
          --delete-during \
          --force \
          --no-perms \
          --progress \
          --itemize-changes \
          --log-file=rsync-log-music..$(date +'%Y-%m-%d') \
          ${MUSIC_DIR}${d}   ${BACKUP_DIR}
 done

 #--dry-run \
 #  /cygdrive/f/MUSIC/${1}   /cygdrive/z/MUSIC/
