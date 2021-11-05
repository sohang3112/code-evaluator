# Project Goals:
## Problem Statement - Latest Amendments by Sir:
We need a standalone **light-wieght** application which a teacher can easily install in a laptop. The program will display a **GUI** (either Desktop App, or browser page on `localhost`) through which problem statement and tests can be uploaded. The program will then start a server (on the specified port number) on the teacher's laptop, and students can then access the problem through a web page that shows the problem statement and allows them to upload their solution, within a time frame specified by the teacher.

Another alternative is to run the program on a dedicated server, which can be accessed by both teachers and students (after login). Teachers will see a webpage that allows them to upload a problem statement & tests, and see students' programs' results. Students will see a webpage that allows them to upload their solutions within specified time frame.

## Part 1 (Minor):
### Version 1 
Make a simple server program to which a CLI 
client program can connect and return 
compile/execute status (cte/rte etc). 

### Version 2 
Make the server multi-threaded.

### Version 3 
Convert the source code into a jar application 
that can be used in standalone mode. It should 
allow user to specify a folder for source code 
and another folder for test instances, and 
compile-execute-test all the source files and 
store the result in a properly formatted 
destination file (try to support csv/excel and pdf).

## Part 2(Major):
Implement a MOSS-based application that does 
effective plag check and displays the plag 
percentage for all course code files, one row per 
file. 
