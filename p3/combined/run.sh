#!/bin/bash

./process_data.py books.qrels books-ranked.txt 2
./process_data.py robust.qrels robust-class-ranked.txt 2
./process_data.py robust04.qrels robust-comb-ranked.txt 1
