rename "IMG" "img" *
rename "PNG" "png" *
mogrify -format jpg -quality 95%% -background white -flatten *.png
