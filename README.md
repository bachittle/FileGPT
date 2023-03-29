# FileGPT

FileGPT is a simple command-line tool that uses OpenAI's GPT-3.5-turbo or GPT-4 to autocomplete text files. It reads text input from a file or standard input (stdin) and outputs the completed text to standard output (stdout). FileGPT is useful for generating content, adding context or explanations, and autocompleting code, among other use cases.

## Prerequisites

To use FileGPT, you need:

1. An OpenAI API key (sign up for one [here](https://platform.openai.com))
2. Python 3.6 or later

## Setup

1. Clone this repository:

```
git clone https://github.com/bachittle/FileGPT.git
```

2. Change directory to the cloned repository:

```
cd FileGPT
```

3. Install the required dependencies:

```
pip install -r requirements.txt
```

4. Set the OpenAI API key as an environment variable:

```
export OPENAI_API_KEY=<your_api_key>
```

(for Windows, use `set OPENAI_API_KEY=<your_api_key>`)

## Usage

To use FileGPT, run the following command:

```
python FileGPT.py
```

You can provide input to FileGPT in two ways:

1. By passing one or more input text files as arguments, using the `-f` or `--file` flag:

```
python FileGPT.py -f input1.txt input2.txt
```

2. By providing input through standard input (stdin):

```
echo "Hello, this is FileGPT!" | python FileGPT.py
```

To specify the model to use for autocompletion, use the `-m` or `--model` flag:

```
python FileGPT.py -f input.txt -m gpt-3.5-turbo
```

If no model is specified, FileGPT will use the default model (gpt-3.5-turbo).

## Logging

FileGPT generates log messages for major operations and saves them to a local log file named `filegpt.log`. You can check this file for any issues or status updates during execution.
