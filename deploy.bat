echo off
git add .
git commit -m update
git push origin master
pm2 deploy production