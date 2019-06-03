#!/bin/bash

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
esac
python main_$LAB.py examples/example$2_$3.m
