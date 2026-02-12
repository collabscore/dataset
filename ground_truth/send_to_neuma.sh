#!/bin/bash

for f in ./*.mei
do
  filename=$(basename -- "$f")
  ext="${filename##*.}"
  score_ref="${filename%.*}"
   echo "Found MEI file $filename, for score $score_ref"
   curl  -u collabscore:local -X POST "http://localhost:8000/rest/collections/all:collabscore:saintsaens-ref:${score_ref}/_sources/ref_mei/_file/"  -F "score_mei.xml=@${filename}"
done
