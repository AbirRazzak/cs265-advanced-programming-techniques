BEGIN { FS=":"}
NR > 0 {
# Check for index files and list all the files out
   if ($1 == "index"){
       for ( i=2; i<=NF; i++){
           print $i
       }
   }
}
