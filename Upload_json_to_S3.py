import json
import json
import time
import urllib3
import json
import boto3
import csv

def lambda_handler(event, context):
    s3 = boto3.client('s3')
    js={}
    js["shr"]="test"
    jss=json.dumps(js, indent = 4) 
    s3.put_object(Body=jss,Bucket='pradumtest',Key="json/dekh_le.json")
    
