# Grep through rsync logs for common output to check is any unusual 
#    lines appear after running backup


INPUT=$1
DATE=$(date +'%Y-%m-%d')
TMPFILE="TMPFILE.."${DATE}

grep -v deleting ${INPUT} > ${TMPFILE}.01
grep -v 'f+++' ${TMPFILE}.01 > ${TMPFILE}.02
grep -v 'cd+++' ${TMPFILE}.02 > ${TMPFILE}.03
grep -v 'Number of' ${TMPFILE}.03 > ${TMPFILE}.04
grep -v ' Total ' ${TMPFILE}.04 > ${TMPFILE}.05
grep -v 'File list '  ${TMPFILE}.05 > ${TMPFILE}.06
grep -v 'total size ' ${TMPFILE}.06 > ${TMPFILE}.07
grep -v 'Literal data' ${TMPFILE}.07 > ${TMPFILE}.08
grep -v 'Matched data' ${TMPFILE}.08 > ${TMPFILE}.09
grep -v 'building file' ${TMPFILE}.09 > ${TMPFILE}.10
grep -v ' sent '  ${TMPFILE}.10 > ${TMPFILE}.11
grep -v 'fcsT..'  ${TMPFILE}.11 > ${TMPFILE}.12
grep -v 'fc.T..'  ${TMPFILE}.12 > ${TMPFILE}.13

wc -l ${TMPFILE}.*

# Don't delete intermediates in case anything looks suspicious
#   show rm line for easy cut and paste if everything is ok
echo "rm ${TMPFILE}*"