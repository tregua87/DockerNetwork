#!/bin/bash

NDEV=$1

echo "NDEV: $NDEV"

for i in `seq $NDEV`; do
  echo $i
  docker cp dockernetwork_peer_$i:/local.txt ./log\_$i.txt
done;
