#!/bin/bash
#count.bash - lists out all regular files in the current directory and lists the number of lines and words in each file
#
#Abir Razzak
#4/20/2018
#
#Platform: Linux cci-uc15205.cci.drexel.edu 4.4.0-104-generic #127-Ubuntu SMP Mon Dec 11 12:16:42 UTC 2017 x86_64
#

for file in * ; do
	if [[ -f "$file" ]] ; then
		#do something
		lines="$(wc -l < "$file")"
		words="$(wc -w < "$file")"
		echo "$file $lines $words"
	fi
done
