import boto3
import json
import time
import random
import os
from botocore.exceptions import ClientError

# Initialize the client for Amazon Bedrock
def create_client(region='us-east-1'):
    return boto3.client('bedrock-runtime', region_name=region)

# Function to get a motivational quote from Amazon Bedrock
def get_motivational_quote(client):
    payload = {
        "inputText": "Give me a short, positive, motivational quote."
    }

    try:
        response = client.invoke_model(
            modelId='amazon.titan-text-express-v1',
            body=json.dumps(payload),
            contentType='application/json',
            accept='application/json'
        )

        response_body = response['body'].read().decode('utf-8')
        decoded_body = json.loads(response_body)

        if 'results' in decoded_body and len(decoded_body['results']) > 0:
            raw_output = decoded_body['results'][0]['outputText']
            cleaned_output = raw_output.split(":", 1)[-1].strip() if ":" in raw_output else raw_output.strip()
            return cleaned_output
        else:
            return "Stay positive, work hard, make it happen."

    except ClientError as e:
        print(f"AWS Client error: {e}")
        return "Stay positive, work hard, make it happen."
    except Exception as e:
        print(f"An error occurred: {e}")
        return "Stay positive, work hard, make it happen."

# Function to display a snowflake animation without affecting the quote
def display_with_snowflakes(quote):
    # Clear the screen initially
    os.system('cls' if os.name == 'nt' else 'clear')

    # Display the quote
    print(f"\n✨ {quote} ✨\n")

    # Get terminal size (set default rows, cols for compatibility)
    rows, cols = 20, 80

    # Generate snowflakes for a few iterations
    for _ in range(30):  # Adjust the range for the duration of snowfall
        # Create a list of random snowflake positions
        snowflake_positions = [(random.randint(4, rows - 1), random.randint(0, cols - 1)) for _ in range(15)]

        # Display the snowflakes at their positions
        for (y, x) in snowflake_positions:
            print(f"\033[{y};{x}H*", end="")  # Using "*" for snowflake

        # Flush the output to the terminal
        print("\033[0;0H", end="", flush=True)
        time.sleep(0.2)

        # Clear snowflakes from the previous frame
        for (y, x) in snowflake_positions:
            print(f"\033[{y};{x}H ", end="")

    # Clear all snowflakes and refresh the display
    os.system('cls' if os.name == 'nt' else 'clear')

    # Re-display the quote cleanly without snowflakes
    print(f"\n✨ \"{quote}\" ✨\n")

    # Place the cursor at the end, below the quote
    print("\033[22;0H")

    #testing this and want to be able to print some other state,ent 

# Initialize client and get a motivational quote
if __name__ == "__main__":
    client = create_client()  # You can specify a different region here if needed
    quote = get_motivational_quote(client)
    display_with_snowflakes(quote)