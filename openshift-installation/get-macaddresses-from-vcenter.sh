#!/bin/bash
function getmac() {
        govc vm.info -json=true /Datacenter/vm/security/$1 | jq '.VirtualMachines[] | .Config | .Hardware | .Device[] | select( (.DeviceInfo | .Label)=="Network adapter 1")' |jq '.MacAddress'

}
hosts=(bootstrap-0 control-plane-0 control-plane-1 control-plane-2 compute-0 compute-1 compute-2)
for host in ${hosts[@]}; do
        echo $host $(getmac $host)
done
