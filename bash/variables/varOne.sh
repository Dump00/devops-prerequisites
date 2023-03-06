#! user/bun/bash

myname="cisco"
myage="30"

echo $myname
echo "Hello, my name is $myname."
echo "I'm $myage years old."


files=$(ls)
path=$(pwd)
now=$(date)
echo $files
echo $path
echo $now