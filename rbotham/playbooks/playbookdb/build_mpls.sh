#!bin/bash

clear

echo "--------------------------------------"

echo "Cleaning up /config-repository ..."

echo "--------------------------------------"

echo "Running ansible build-mpls_lsp.yml..."

echo "--------------------------------------"

rm config-repository/*

ansible-playbook build_mpls_lsp.yml 

tree -A config-repository

