#!/usr/bin/env python

import sys
import argparse
import os
import openai
import logging
import tempfile

import tiktoken

MODELS = [
    "gpt-3.5-turbo",
    "gpt-4"
]

# give a warning if the user tries to use too many tokens
TOKEN_LIMIT = {
    "gpt-3.5-turbo": 4096,
    "gpt-4": 8196 
}

def setup_logging():
    log_dir = tempfile.gettempdir()
    log_file = os.path.join(log_dir, "filegpt.log")
    logging.basicConfig(filename=log_file, level=logging.INFO, format="%(asctime)s [%(levelname)s]: %(message)s")
    logging.info("Starting FileGPT")

def parse_arguments():
    parser = argparse.ArgumentParser(description="FileGPT - A simple tool that autocompletes text files.")
    parser.add_argument("-f", "--file", help="Specify one or more text files as input.", type=str, nargs="+")
    parser.add_argument("-m", "--model", help="Specify the model to use for autocompletion.", type=str)
    return parser.parse_args()

def read_input(files=None):
    if files:
        logging.info("Reading input from files: %s", files)
        contents = []
        for file in files:
            with open(file, "r") as f:
                contents.append(f.read())
        content = "\n".join(contents)
    else:
        logging.info("Reading input from stdin")
        print("Reading from stdin (press CTRL+D for linux/mac or Enter+CTRL+Z+Enter for windows to stop)...")
        content = sys.stdin.read()
    return content

def select_model(model_name):
    use_default = True
    for name in MODELS:
        if model_name == name:
            use_default = False
            break

    if use_default:
        logging.info("Using default model: %s", MODELS[0])
        model_name = MODELS[0]
    else:
        logging.info("Using specified model: %s", model_name)

    return model_name

def get_openai_response(model_name, content):
    logging.info("Setting up OpenAI API")
    openai.api_key = os.getenv("OPENAI_API_KEY")
    message = {"role": "user", "content": content}
    
    logging.info("Sending request to OpenAI API")
    response = openai.ChatCompletion.create(
        model=model_name,
        messages=[message],
        stream=True
    )
    return response

def write_output(response):
    logging.info("Writing output")
    response_str = ""

    for chunk in response:
        chunk_msg = chunk['choices'][0]['delta']
        if 'content' in chunk_msg:
            sys.stdout.write(chunk_msg['content'])
            response_str += chunk_msg['content']
            sys.stdout.flush()
    
    return response_str

def main():
    setup_logging()
    args = parse_arguments()
    input_content = read_input(args.file)
    model_name = select_model(args.model)

    enc = tiktoken.encoding_for_model(model_name)

    logging.info("Input has %d tokens", len(enc.encode(input_content)))

    response = get_openai_response(model_name, input_content)
    resp_str = write_output(response)
    logging.info("FileGPT finished, response has %d tokens", len(enc.encode(resp_str)))

if __name__ == "__main__":
    main()

# (run FileGPT on itself and ask it the question below, using `python FileGPT.py -f FileGPT.py`)
# come up with some more tools or features that could be made