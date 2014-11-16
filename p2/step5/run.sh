#!/bin/bash

./process_data.py books.qrels books-title.snehas.tr100 2
./process_data.py robust.qrels robust-title.snehas.tr100 2
./process_data.py robust04.qrels robust-full-galago 1
