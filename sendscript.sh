IP_ADDRESS="192.168.86.60"
USERNAME="diegocuadros"

if [ -z "$IP_ADDRESS" ]; then
    echo "Could not find Raspberry Pi. Is it connected to the network?"
    exit 1
fi

echo "Found Raspberry Pi at $IP_ADDRESS"

scp -r run.py $USERNAME@$IP_ADDRESS:~