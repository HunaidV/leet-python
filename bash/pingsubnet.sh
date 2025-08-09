#!/bin/bash
#ping subnet 192.168.0.0/25


subnet="192.168.0"

echo "Checking the connection on ${subnet}.0/25"

echo "-------------------"

for i in {1..126}; do
    
    (
        ip_add="${subnet}.${i}"

        ping -c 1 -W 1 "${ip_add}" &> /dev/null

        if [ $? -eq 0 ]; then
            echo "${ip_add} is up"
        else
            echo "${ip_add} is down"
            
        fi
    ) &

done
