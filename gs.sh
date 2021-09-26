#!/bin/sh

DATE=`date +%Y-%m-%d`
MSG="$DATE"
if [ $# -gt 0 ]; then
    MSG="$1"
fi

#git checkout master

git diff --numstat origin/master

git add --all
git commit -am "${MSG}"

git push origin master

# ./gs.sh 를 시행하면 git에 바로 넣을 수 있음.
