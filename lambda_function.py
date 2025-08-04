import json

def lambda_handler(event, context):
    print("Received S3 Event:")
    print(json.dumps(event, indent=2))
    
    # Example logic: Print uploaded file name from event
    try:
        bucket = event['Records'][0]['s3']['bucket']['name']
        key = event['Records'][0]['s3']['object']['key']
        print(f"File uploaded: {key} in bucket: {bucket}")
        
        return {
            'statusCode': 200,
            'body': json.dumps(f"File {key} processed successfully from bucket {bucket}")
        }
        
    except Exception as e:
        print(f"Error: {str(e)}")
        return {
            'statusCode': 500,
            'body': json.dumps("Error processing file")
        }
