#This awk script will check which entries are present in the README file
BEGIN { FS=":" }
NR > 0 {
    print $1
}
