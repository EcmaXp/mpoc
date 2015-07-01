#!/bin/bash

echo ERROR! this script should support build by travis?
exit 1

source ./assets/machine/half/setupenv.sh
./gradlew jar
