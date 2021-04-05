if [[ $1 ]]
then
    PROBLEM=$1
else
    exit
fi

mkdir solutions/$PROBLEM
cd solutions/$PROBLEM
touch "${PROBLEM}.py"
touch "${PROBLEM}.js"
