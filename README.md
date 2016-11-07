# eresults-utils
Python scripts to be used with EResults programs by Oriento Solutions http://www.oriento.fi

## Usage
To use these scripts install Python and add python.exe to %PATH%. When Python is installed download script files the your computer.

## Find battery warnings

find-battery-warnings.py is a script that scan the log files genereated by EResult for battery warning. Script will
find battery warnings for both emit cards and emit posts.

    python.exe find-battery-warnings.py

If EResults is not installed into default directory you may pass the log directory as a parameter:

    python.exe find-battery-warnings.py C:\Ohjelmat\EResultsLite\logsfiles

