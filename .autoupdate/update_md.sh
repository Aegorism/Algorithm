#!/bin/bash

output=($(python3 count.py | tr -d '[],'))
statement=$(echo "총 ${output[0]}개의 문제와 ${output[1]}개의 해답이 업로드되었습니다.")

sed '3d' README.md | sed "2a\\${statement}" >> NEW.md
rm README.md
mv NEW.md README.md