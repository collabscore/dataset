#!/bin/bash
FILES=./*.json
EXTENSIONS=("json")

for f in ./*.json
do
  filename=$(basename -- "$f")
  ext="${filename##*.}"
  score_ref="${filename%.*}"
   echo "Found JSON file $filename, for score $score_ref"
   curl  -u collabscore:local -X POST "http://localhost:8000/rest/collections/all:collabscore:saintsaens-ref:${score_ref}/_sources/iiif/_file/"  -F "dmos.json=@${filename}"
done
