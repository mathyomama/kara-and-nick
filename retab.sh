#!/bin/bash

set -e

for file in $(find ./ -type f -regextype posix-extended -regex '.*/(models|views|urls|admin|forms)\.py'); do
	vim -c 'set ts=4|retab|wq' $file
done
