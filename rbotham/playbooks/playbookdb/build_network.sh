#!bin/bash

clear

echo "--------------------------------------"

echo "Cleaning up /config-repository ..."

echo "--------------------------------------"

echo "Running ansible build-network.yml..."

echo "--------------------------------------"

rm config-repository/*

ansible-playbook build_network.yml 

tree -A config-repository

