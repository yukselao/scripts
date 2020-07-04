#!/bin/bash

start=$1
end=$(date -I -d "$2 + 1 day")
while [ "$start" != $end ]; do
  echo $start
  start=$(date -I -d "$start + 1 day")
done
