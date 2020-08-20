import argparse
import logging 
import random 
import pandas as pd 
import string 
import struct 
#from pyspark.sql import sparkSession 


# GLobal Variables 
df_schema = pd.read_json("spec.json")
#print(df_schema)


def colspecs():
    v_list= []
    for index, row in df_schema.iterrows(): 
        v_list.append(row["Offsets"])
    return (v_list)


def Headerspecs():
    v_list= []
    for index, row in df_schema.iterrows(): 
        v_list.append(row["ColumnNames"])
    return (v_list)
            
    

def GetArgs():
        """
        Supports the command-line arguments listed below.
        """
        parser = argparse.ArgumentParser(description='Two arguments needs to be passed -o (number of rows ), -f (file name)')
        parser.add_argument('-o', '--activity_n', type =int, action='store',required=True, 
                                           help='Number of rows ')
        parser.add_argument('-f', '--output_file_name', action='store',required=True, 
                                           help='creates FWF and CSV in the local directory')
        args = parser.parse_args()
      #  print (args)
        return args 
        

    

def SetupLogging():
# logs all activity in a file called fwf.log in the local directory 
    try:
        debug = 0
        if debug == 1 :
           info = logging.DEBUG
        else :
           info = logging.INFO
        logger = logging.getLogger()
        logger.setLevel(info)
        #create a file handler
        handler = logging.FileHandler('fwf.log')
        handler.setLevel(info)
        # create a logging format
        formatter = logging.Formatter('%(asctime)s - %(name)s - %(levelname)s - %(message)s')
        handler.setFormatter(formatter)
        # add the handlers to the logger
        logger.addHandler(handler)
    except IOError:
        logger.error("cannot open log file",exc_info=True)



def CreateLine():
    try:
        line= ""
        for index, row in df_schema.iterrows(): 
            v_width = row["Offsets"]
            v_string = string.ascii_letters
            v_field = ''.join(random.choice(v_string) for i in range(v_width))
            line = line + " " + v_field
        #print(line)    
        return (line )
            
        
    except:
        logging.error(sys.exc_info()[0])
        
def CreateFWF(v_activity_n,v_output_file_name):
    try:
        #v_output_file_name = "random_data"
        #v_activity_n = 5
        v_output_file_name = v_output_file_name
        v_activity_n = v_activity_n
        file_name = v_output_file_name + ".txt"
        with open(file_name, 'w', encoding = 'utf-8' ) as out_file:
            for i in range(v_activity_n):
                line = CreateLine()
                out_file.write(line + "\n")
               
    except:
        logging.error(sys.exc_info()[0])
        
def ReadFWF_savetoCSV(v_output_file_name):
    try:
        v_list = colspecs()
        v_header = Headerspecs()
        file_name = v_output_file_name + ".txt"
        out_csv = v_output_file_name + ".csv" 
        df_read = pd.read_fwf(file_name , width = v_list,error_bad_lines = False , warn_bad_lines = True  )
        df_read.to_csv(out_csv,header = v_header, encoding = 'utf-8' , index=False )
    except:
        logging.error(sys.exc_info()[0])

def Main():
    v_args = GetArgs() 
    logging.info(v_args.activity_n)
    v_activity_n=v_args.activity_n
    v_output_file_name=v_args.output_file_name
    return v_activity_n, v_output_file_name   
#MAIN

SetupLogging()
v_activity_n, v_output_file_name = Main() 
CreateFWF(v_activity_n, v_output_file_name)
ReadFWF_savetoCSV(v_output_file_name)

