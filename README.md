# sPyder
Python Automated SMB mounting via CSV ingestion.  This was written for mounting in a \*nix environment.
The code is ugly and it is still a work in progress.  This was written on the fly when it need arised.

Exception handling and Error output needs work but the mounting works.

## Mount Information
Currently the shares a mounted in /mnt/hostname/share name
The script will create the 'hostname/share name' path if it doesn't exist and will mount multiple shares in a hostname directory.


## CSV Format
The following is the requirement for the CSV, do not include column headers in the CSV.
remote ip,remote hostname,remote share name

EG. 123.123.123.123,Storage01,UserData


## TODO
Ask first if authentication is required and change mnt command as required.
Improve Exception handling
Improve Error message capture and output
Move root local mount path "/mnt" into variable or get user input

