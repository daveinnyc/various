# Space at top 
for i in $(seq 1 8) ; do echo ; done

# Get updates
date >> check-ticker-results
python3 <PATH-TO_SCRIPT>/check-ticker.py >> check-ticker-results    # Substitute real value
tail -8 check-ticker-results 

#Show historical numbers

CURRENT_LIST="blx ge svc t:"

echo
echo "BEST"
for STK in ${CURRENT_LIST} ; do grep ${STK} check-ticker-results | sort -rk 3 | tail -1 ; done

echo 
echo "WORST"
for STK in ${CURRENT_LIST} ; do grep ${STK} check-ticker-results | sort -rk 3 | head -1 ; done

echo 
echo "DOWN"
grep red check-ticker-results | sort | head -1
grep red check-ticker-results | sort | tail -1

echo
echo "UP"
grep current check-ticker-results | sort | head -1
grep current check-ticker-results | sort | tail -1

# Space at bottom
for i in $(seq 1 10) ; do echo ; done
