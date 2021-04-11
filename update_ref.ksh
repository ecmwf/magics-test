#!/bin/ksh


while getopts p:t: opt

do
    case $opt in

        p)      path=$OPTARG ;;

        t)      test=$OPTARG ;;


     esac

done


echo "Updating reference "  $test in $path

current=`pwd`

 print $current

cd $path 
python3 $test.py
mv $test.png $current/reference

