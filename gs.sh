#!/bin/sh

git pull 
git add --all
git commit --amend --no-edit --date "$(date)"



git push


# ./gs.sh 를 시행하면 git에 바로 넣을 수 있음.
