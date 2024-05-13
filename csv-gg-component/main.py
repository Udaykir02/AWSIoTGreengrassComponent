import csv
import json
import boto3
import os
import time

# Initialize Boto3 clients
s3_client = boto3.client('s3',aws_access_key_id='XXXXXXX', 
                      aws_secret_access_key='XXXXXX')

def convert_csv_to_json(csv_file):
    json_objects = []
    with open(csv_file, mode='r') as file:
        csv_reader = csv.reader(file)
        for row in csv_reader:
            data = {
                "tag_name": row[0],
                "date_time": row[1],
                "value": float(row[2]),
                "quality": bool(row[3].capitalize() == "True")  # Convert "True" or "False" to boolean
            }
            json_objects.append(data)
    return json_objects


def upload_json_to_s3(json_data, s3_bucket, s3_key):
    s3_client.put_object(Body=json.dumps(json_data), Bucket=s3_bucket, Key=s3_key)

def main():
    csv_directory = '/home/admin/uday/csv_files'  # Update this with the directory path where your CSV files are located
    s3_bucket = 'your-ggbucket-data'  # Replace with your S3 bucket name

    while True:
        # Get list of CSV files in the directory
        csv_files = [file for file in os.listdir(csv_directory) if file.endswith('.csv')]
        
        for csv_file in csv_files:
            csv_file_path = os.path.join(csv_directory, csv_file)
            json_data = convert_csv_to_json(csv_file_path)
            s3_key = f'{csv_file[:-4]}.json'  # Use CSV file name without extension as S3 key for JSON file
            upload_json_to_s3(json_data, s3_bucket, s3_key)
        
        time.sleep(60)

if __name__ == "__main__":
    main()
