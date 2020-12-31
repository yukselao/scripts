#!/bin/bash

function getmac() {
        govc vm.info -json=true /Datacenter/vm/security/$1 | jq '.VirtualMachines[] | .Config | .Hardware | .Device[] | select( (.DeviceInfo | .Label)=="Network adapter 1")' |jq '.MacAddress'

}
hosts=(bootstrap-0 control-plane-0 control-plane-1 control-plane-2 compute-0 compute-1 compute-2)
cp /opt/openshift/config/dhcpd.conf /tmp/dhcpd.conf
for host in ${hosts[@]}; do
        macaddr=$(getmac $host |tr -d '"')
        sed -r -i "s#%""$host""%#""$macaddr""#g" /tmp/dhcpd.conf
done
cp /tmp/dhcpd.conf /etc/dhcp/dhcpd.conf
systemctl restart dhcpd
