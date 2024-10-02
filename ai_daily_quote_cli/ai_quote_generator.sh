#!/bin/zsh

# Function to show a falling snowflake animation like actual snowfall
function snowflake_animation() {
  local cols=$(tput cols)    # Get terminal width
  local lines=$(tput lines)  # Get total number of rows in the terminal

  # Calculate the starting row for the animation (below the quote)
  local quote_height=2  # Assuming the quote takes up 2 rows
  local start_row=$((quote_height + 3))

  # Loop to create a simultaneous snowfall effect
  for ((row = start_row; row <= lines; row++)); do
    # Generate random positions for each snowflake in the current row
    for ((i = 0; i < 10; i++)); do
      local col=$((RANDOM % cols + 1))  # Random column position for the snowflake

      # Print the snowflake at the random position
      printf "\033[%d;%dH❄️" $row $col
    done

    sleep 0.1  # Pause briefly to simulate falling speed

    # Clear previous snowflakes from the current row
    if (( row > start_row )); then
      for ((i = 0; i < 10; i++)); do
        local col=$((RANDOM % cols + 1))
        printf "\033[%d;%dH " $((row - 1)) $col
      done
    fi
  done

  # Clear the screen lines used by the snowflake animation (only)
  for ((row = start_row; row <= lines; row++)); do
    printf "\033[%d;1H%${cols}s" $row " "
  done

  # Place the cursor just below the quote, ready for input
  printf "\033[%d;1H" $((start_row))
}

# Request an AI-generated quote from Amazon Bedrock
quote=$(aws bedrock-runtime invoke-model \
  --model-id 'amazon.titan-text-express-v1' \
  --body '{"inputText": "Give me a short, positive, motivational quote.", "textGenerationConfig" : {"maxTokenCount": 30}}' \
  --cli-binary-format raw-in-base64-out \
  invoke-model-output-text.txt)

# Extract the motivational quote from the JSON response using jq
quote=$(jq -r '.results[0].outputText' invoke-model-output-text.txt)

# Strip everything before the first quote character (") and trim spaces
quote=$(echo "$quote" | sed 's/^[^"]*//' | sed 's/[[:space:]]*$//' | sed 's/^[[:space:]]*//')

# If no quote is generated, fall back to a default
if [[ -z "$quote" ]]; then
  quote="Stay positive, work hard, and make it happen."
fi

# Output the quote with sparkle (position it at the top)
clear
echo -e "$quote ✨"

# Show snowflake animation below the quote
snowflake_animation
