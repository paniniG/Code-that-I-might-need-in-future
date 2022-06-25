import json
import json
import time
import urllib3
import json
import boto3
import csv

def lambda_handler(event, context):
    s3 = boto3.resource('s3')
    bucket = s3.Bucket('pradumtest')
    key = 'yourfilename.csv'
    js={}
    js["shr"]="test"
    l=[]
    l.append(js)
    # f = open("/tmp/csv_file.csv", "w+")
    keys=js.keys()
    #you would need to grab the file from somewhere. Use this incomplete line below to get started:
    # with requests.Session() as s:
    #     getfile = s.get('pradumtest/filename.csv')
    
    #Only then you can write the data into the '/tmp' folder.
    with open("/tmp/filename.csv", 'w', newline='') as output_file:
        dict_writer = csv.DictWriter(output_file, keys)
        dict_writer.writeheader()
        dict_writer.writerows(l)
    #upload the data into s3
    bucket.upload_file('/tmp/filename.csv', Key="139718.csv")
    
