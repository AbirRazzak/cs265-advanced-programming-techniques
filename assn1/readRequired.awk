BEGIN { FS=":"}
NR > 0 {
# Check for required files and list all the files out
   if ($1 == "required"){
       for ( i=2; i<=NF; i++){
           print $i
       }
   }
}
