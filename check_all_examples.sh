#!/bin/sh

if [ "$#" -eq 0 ]; then
	for LAB in "lab1" "lab2" "lab3" "lab4" "lab5"
	do
		./run_all_examples.sh $LAB | grep Traceback
	done
else
	./run_all_examples.sh $1 | grep Traceback
fi
