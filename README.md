# sPyder
Developed by Peter Nelson<br>
Stern Security<br>
www.sternsecurity.com

Python Automated SMB mounting via CSV ingestion.  This was written for mounting in a \*nix environment.<br>
The code is ugly and it is still a work in progress and was written on the fly when a need arised.

Exception handling and Error output produces output even if the mount is successful.

## Mount Information
Currently the shares a mounted in /mnt/hostname/share name<br>
The script will create the 'hostname/share name' path if it doesn't exist and will mount multiple shares in a hostname directory.


## CSV Format
The CSV file currently needs to be in same location as this script and is named 'spydershares.csv'.<br>
The following is the requirement for the CSV, do not include column headers in the CSV.

remote ip,remote hostname,remote share name<br>
EG. 123.123.123.123,Storage01,UserData


## TODO
* Ask first if authentication is required and change mnt command as required.
* Improve Exception handling
* Improve Error message capture and output
* Move root local mount path "/mnt" into variable or get user input
* Get user input for CSV file

