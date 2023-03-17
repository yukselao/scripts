#!/bin/bash

firewall-cmd --zone=public --add-port=$1/tcp  --permanent
firewall-cmd --zone=trusted --add-port=$1/tcp  --permanent
firewall-cmd --zone=dmz --add-port=$1/tcp  --permanent

firewall-cmd --reload
