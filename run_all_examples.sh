#!/bin/sh

clear
case $1 in
	lab1)
		LAB=scanner
		;;
	lab2)
		LAB=parser
		;;
	lab3)
		LAB=treeprinter
		;;
	lab4)
		LAB=typechecker
		;;
	lab5)
		LAB=interpreter
		;;
esac
for FILE in ` ls examples/ | grep "\.m"`
do
	python main_$LAB.py examples/$FILE
done
