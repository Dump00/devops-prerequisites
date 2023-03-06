#! user/bin/bash

numnum=25


# eq - equal

if [ $numnum -eq 25 ]
then
    echo "The condition is True"
else
    echo "The condition is False"
fi


# ne - not equal

if [ $numnum -ne 20 ]
then
    echo "Not equal to 20"
fi


# gt - greater than

if [ $numnum -gt 10 ]
then
    echo "Greater than 10"
fi


# check files exist in file system

# for files -f
# dor directories -d

if [ -f ~/myfile.txt ]
then
    echo "File exists"
else
    echo "File does not exists"
fi


path=/media/optimus-prime/blackhole/devops/bash/if-statement/test.txt

if [ -f $path ]
then
    echo "Present"
else
    echo "Not present"
    echo "Creating file test.txt...."
    touch test.txt
    echo "File created"
fi

