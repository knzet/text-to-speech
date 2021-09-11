#!/bin/bash

#sentence=$1
dir="."
cd lib
#echo "24 LATER KENNEDY ATE POPCORN 23" > test_file &&
echo $1 > $dir/test_file &&
farcompilestrings --symbols=$dir/wl.cmu --unknown_symbol="<unk>" $dir/test_file > $dir/test_cmu_file2.far &&
farextract $dir/test_cmu_file2.far &&
# where is test cmu file-1 coming from? how to control outfilename of farextract
fstcompose $dir/test_file-1 $dir/cmu.trans.fsm > $dir/cmustring.trans.fsm &&
fstproject --project_type=output $dir/cmustring.trans.fsm > $dir/output.far &&
#this fixed the error with multiple arcs from one state
fstdeterminize $dir/output.far $dir/out.fst 
farprintstrings --symbols=$dir/pl.cmu $dir/out.fst > ../output.txt
