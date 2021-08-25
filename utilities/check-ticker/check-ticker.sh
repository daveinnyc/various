date >> check-ticker-results
python3 <PATH-TO_SCRIPT>/check-ticker.py >> check-ticker-results    # Substitute real value

tail -11 check-ticker-results 

echo 
echo "BEST-WORST"
grep current check-ticker-results | sort | tail -1
grep red check-ticker-results | sort | tail -1


CURRENT_LIST="<LIST_OF_STOCKS_TO_CHECK>"    # Substitute real value
for STK in ${CURRENT_LIST} ; do grep ${STK} check-ticker-results | sort -rk 3 | tail -1 ; done

echo 

for STK in ${CURRENT_LIST} ; do grep ${STK} check-ticker-results | sort -rk 3 | head -1 ; done

echo
