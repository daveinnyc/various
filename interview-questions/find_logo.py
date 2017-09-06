# Notes on the coding samples in this directory
#
# Author: Dave Cuthbert
# Copyright: 2016
# License MIT


selenium-docker-test.py
  While developing the following are useful one liners. Assumes not closing 
  firefox explicitly while working on a particular test:

  -- find and kill any running firefoxes, execute all tests
  FFS=$(ps -e |grep firefox|cut -d" " -f1) ; if [ ${#FFS} -ne 0 ] ; \
  then killall firefox ; fi ; py.test -q -s selenium-docker-test.py


  -- find and kill any running firefoxes, execute only 'test_login'
  FFS=$(ps -e |grep firefox|cut -d" " -f1) ;if [ ${#FFS} -ne 0 ] ; \
  then killall firefox ; fi ; py.test -q -s selenium-docker-test.py::test_login


database-example.sql
  Development command line:
 
  -- remove old DBs, create new one and display query results
  rm *db ; sqlite3 -column -header example.db < database-example.sql


find_logo.py
  The answer to this selenium question required examination of CSS that was
  referenced by an element on the rendered page.

#EOF
