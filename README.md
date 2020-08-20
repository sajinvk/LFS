# LFS
LFS Data Engineer Test 

Steps :
Copy all the contents in to a folder with read write access ( SYS IO is not been verified in the code)
Build Docker using command: docker build --tag lfs-fixedwidthfile .
Run Docker using command : docker run lfs-fixedwidthfile -o 1000 -f file2 
( -o option is for number of records , -f : file name (.txt and .csv file will be create in the same directory )
Actual Python file to run : 

Python file can be run separately :

(base) [root@informix-test-01 LFS]# python3 fixed_width_file.py -h
usage: fixed_width_file.py [-h] -o ACTIVITY_N -f OUTPUT_FILE_NAME

Two arguments needs to be passed -o (number of rows ), -f (file name)

optional arguments:
  -h, --help            show this help message and exit
  -o ACTIVITY_N, --activity_n ACTIVITY_N
                        Number of rows
  -f OUTPUT_FILE_NAME, --output_file_name OUTPUT_FILE_NAME
                        creates FWF and CSV in the local directory





