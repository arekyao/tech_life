#!/bin/bash

for i in `ls *.MOV`;
do
	echo $i;
	stat $i;
	sec=`stat -t "%s" $i | awk  '{print $12}' | sed 's/"//g'`
	name_2=`date -r "$sec" "+%Y%m%d_%H%M%S"`
	name_1=`echo $i | sed 's/.MOV//'`
	newname=`echo $name_1"_"$name_2".MOV"`
	cp $i output/$newname
done

