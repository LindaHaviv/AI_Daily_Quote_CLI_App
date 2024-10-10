
# AI Motivational Quote Generator with Snowflake Animation ❄️

This repository contains two versions of a CLI application that generates a motivational quote using an AI model and displays a snowflake animation in your terminal. You can choose to use either the Python version or the Zsh version—**you only need to set up one of them, not both**.

## Features

- Retrieves a motivational quote using Amazon Bedrock.
- Displays a falling snowflake animation in the terminal.
- Two different implementations available: Python and Zsh.

## Prerequisites

You must have the following installed before running the app:

- **AWS CLI**: Installed and configured with permissions to use Amazon Bedrock. [Install AWS CLI](https://docs.aws.amazon.com/cli/latest/userguide/install-cliv2.html)
- **jq** (for Zsh version only): Used for parsing JSON responses. [Install jq](https://stedolan.github.io/jq/download/)
- **Python 3.x** (for Python version only): Install the `boto3` and `termcolor` libraries. [Install Python](https://www.python.org/downloads/)

### AWS CLI Configuration

To configure the AWS CLI, follow the official AWS documentation: [AWS CLI Configuration](https://docs.aws.amazon.com/cli/latest/userguide/cli-configure-files.html).

Run the following command to configure your AWS CLI:

```bash
aws configure
```

You will be prompted for:

- **AWS Access Key ID**
- **AWS Secret Access Key**
- **Default Region Name**
- **Default Output Format**

Ensure that your IAM user has the necessary permissions to invoke Amazon Bedrock models by adding the correct policies.

## Choose One Setup: Python or Zsh

You can choose to set up either the **Python version** or the **Zsh version** of the app. Follow the instructions for the one you prefer. **You don't need to set up both.**

### Python Version Setup

1. Install the required Python libraries:

   ```bash
   pip install boto3 termcolor
   ```

2. Clone or download this repository to your local machine.

3. Run the Python version:

   ```bash
   python ai_quote_generator.py
   ```

### Zsh Version Setup

1. Install `jq` if it’s not already installed. You can do so with:

   ```bash
   sudo apt-get install jq  # For Debian/Ubuntu
   # or
   brew install jq  # For macOS
   ```

2. Clone or download this repository to your local machine.

3. Make the Zsh script executable (if it's not already):

   ```bash
   chmod +x ai_quote_generator.sh
   ```

4. Run the Zsh version:

   ```bash
   ./ai_quote_generator.sh
   ```

## How to Automatically Run the Script When Terminal Opens

You can set the script to automatically run each time your terminal opens. Follow the steps below depending on whether you chose the Python or Zsh version.

### Zsh Version

1. **Open or create your `.zshrc` file** (this file runs every time a new Zsh session is started):

   ```bash
   nano ~/.zshrc
   ```

2. **Add the following line** to the end of the `.zshrc` file to run the Zsh version of your script when the terminal opens:

   ```bash
   # Run AI Quote Generator when terminal starts
   ~/path-to-your-script/ai_quote_generator.sh
   ```

   Replace `~/path-to-your-script/` with the actual path to the directory where your `ai_quote_generator.sh` is located.

3. **Save and close the file**, then reload your terminal configuration:

   ```bash
   source ~/.zshrc
   ```

   The script will now run automatically each time you open a new Zsh terminal session.

### Bash Version (Python Script)

1. **Open or create your `.bashrc` file** (this file runs every time a new Bash session is started):

   ```bash
   nano ~/.bashrc
   ```

2. **Add the following line** to the end of the `.bashrc` file to run the Python version of your script when the terminal opens:

   ```bash
   # Run AI Quote Generator when terminal starts
   python3 ~/path-to-your-script/ai_quote_generator.py
   ```

   Replace `~/path-to-your-script/` with the actual path to the directory where your `ai_quote_generator.py` is located.

3. **Save and close the file**, then reload your terminal configuration:

   ```bash
   source ~/.bashrc
   ```

   The script will now run automatically each time you open a new Bash terminal session.

### Conditional Execution (Optional)

If you'd like the script to run only under certain conditions (like when you're in a specific directory), you can add a condition to your `.bashrc` or `.zshrc` file. For example:

```bash
# Only run the AI Quote Generator when in the home directory
if [[ $PWD == "$HOME" ]]; then
    ~/path-to-your-script/ai_quote_generator.sh
fi
```

This ensures the script only runs when your terminal is opened in the home directory.

## How It Works

### Python Version

The Python version uses `boto3` to request a motivational quote from Amazon Bedrock, based on the prompt in the script. It displays the quote in your terminal with some basic formatting and color.

### Zsh Version

The Zsh version uses the AWS CLI to call Amazon Bedrock, parses the response with `jq`, and displays the quote with a falling snowflake animation.

## Links to Relevant Documentation

- [AWS CLI Installation](https://docs.aws.amazon.com/cli/latest/userguide/install-cliv2.html)
- [AWS CLI Configuration](https://docs.aws.amazon.com/cli/latest/userguide/cli-configure-files.html)
- [Amazon Bedrock](https://aws.amazon.com/bedrock/)
- [Boto3 Python Library](https://boto3.amazonaws.com/v1/documentation/api/latest/index.html)
- [jq Manual](https://stedolan.github.io/jq/manual/)

