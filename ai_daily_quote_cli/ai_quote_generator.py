import boto3
import json
from botocore.exceptions import ClientError

# Initialize the client for Amazon Bedrock
def create_client(region='us-east-1'):
    return boto3.client('bedrock-runtime', region_name=region)

# Function to get a motivational quote from Amazon Bedrock
def get_motivational_quote(client):
    # The JSON payload as a Python dictionary
    payload = {
        "inputText": "Give me a short, positive, motivational quote."
    }

    try:
        # Invoke the model
        response = client.invoke_model(
            modelId='amazon.titan-text-express-v1',
            body=json.dumps(payload),  # Convert dictionary to JSON string
            contentType='application/json',
            accept='application/json'
        )

        # Read and parse the response body
        response_body = response['body'].read().decode('utf-8')
        decoded_body = json.loads(response_body)

        # Extract the output text from the response
        if 'results' in decoded_body and len(decoded_body['results']) > 0:
            raw_output = decoded_body['results'][0]['outputText']
            # Modify this line to match the specific cleanup done in your Mac script
            cleaned_output = raw_output.split(":", 1)[-1].strip() if ":" in raw_output else raw_output.strip()
            return cleaned_output
        else:
            return "Stay positive, work hard, make it happen."  # Custom fallback quote

    except ClientError as e:
        print(f"AWS Client error: {e}")
        return "Stay positive, work hard, make it happen."  # Custom fallback quote in case of an error
    except Exception as e:
        print(f"An error occurred: {e}")
        return "Stay positive, work hard, make it happen."  # Custom fallback quote in case of an unexpected error

# Initialize client and get a motivational quote
if __name__ == "__main__":
    client = create_client()  # You can specify a different region here if needed
    quote = get_motivational_quote(client)
    print(f"\n✨ {quote} ✨\n")