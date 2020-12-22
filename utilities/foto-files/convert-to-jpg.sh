for f in $(ls) 
  do 
     mv ${f} $(echo ${f} |tr 'A-Z' 'a-z') 
  done

mogrify -format jpg -quality 100%% -background white -flatten *.png
