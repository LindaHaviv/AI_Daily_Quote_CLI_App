#!/bin/zsh

# Request an AI-generated quote from Amazon Bedrock
quote=$(aws bedrock-runtime invoke-model \
  --model-id 'amazon.titan-text-express-v1' \
  --body '{"inputText": "Give me a short, positive, motivational quote.", "textGenerationConfig" : {"maxTokenCount": 30}}' \
  --cli-binary-format raw-in-base64-out \
 invoke-model-output-text.txt)

# Extract the motivational quote from the JSON response using jq
quote=$(jq -r '.results[0].outputText' invoke-model-output-text.txt)

# If no quote is generated, fall back to a default
if [[ -z "$quote" ]]; then
  quote="Stay positive, work hard, and make it happen."
fi

# Output the quote
echo -e "\n✨ $quote ✨\n"
