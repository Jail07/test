#!/bin/bash

LINK="$1"

git init
git add .
git commit -m "update"
git branch -M master
git remote add origin "$LINK"
git push -u origin master


#mnbnbm