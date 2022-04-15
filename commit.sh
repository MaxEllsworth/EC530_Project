#!/bin/bash

git pull origin user_modules
echo "#`date -d @$(date +%s)`" >> pushes.py
git add .
git commit -m "`date -d @$(date +%s)`"
git push origin main:user_modules
