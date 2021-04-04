if [[ $1 ]]
then
    PROBLEM=$1
else
    exit
fi

mkdir $PROBLEM
cd $PROBLEM
touch "${PROBLEM}.py"
touch "${PROBLEM}.js"