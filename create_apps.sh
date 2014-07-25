#!/bin/bash

for i in $( < list_of_apps.txt ); do
	python manage.py startapp $i
done
