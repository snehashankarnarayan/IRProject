#!/bin/bash

./process_data.py books.qrels books-ranked-list.txt 2
./process_data.py robust.qrels robust-class-ranked-list.txt 2
./process_data.py robust04.qrels robust-queries-ranked-list.txt 1
