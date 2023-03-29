import sys
import argparse
import os
import openai

MODELS = [
    "gpt-3.5-turbo",
    "gpt-4"
]

def read_input(files=None):
    if files:
        contents = []
        for file in files:
            with open(file, "r") as f:
                contents.append(f.read())
        content = "\n".join(contents)
    else:
        print("Reading from stdin (press CTRL+D for linux/mac or Enter+CTRL+Z+Enter for windows to stop)...")
        content = sys.stdin.read()
    return content

def write_output(content, model_name):
    openai.api_key = os.getenv("OPENAI_API_KEY")

    message = {"role": "user", "content": content}
    
    use_default = True
    for name in MODELS:
        if model_name == name:
            use_default = False
            break

    if use_default:
        # print(f"Using default model: {MODELS[0]}")
        # print(f"to change this, pass the model as a string, ex: FileGPT.py -m {MODELS[1]}\n")
        model_name = MODELS[0]

    # print(f"using model {model_name}")
    response = openai.ChatCompletion.create(
        model=model_name,
        messages=[message],
        stream=True
    )

    for chunk in response:
        chunk_msg = chunk['choices'][0]['delta']
        if 'content' in chunk_msg:
            sys.stdout.write(chunk_msg['content'])
            sys.stdout.flush()

def main():
    parser = argparse.ArgumentParser(description="FileGPT - A simple tool that autocompletes text files.")
    parser.add_argument("-f", "--file", help="Specify one or more text files as input.", type=str, nargs="+")
    parser.add_argument("-m", "--model", help="Specify the model to use for autocompletion.", type=str)
    args = parser.parse_args()

    input_content = read_input(args.file)
    write_output(input_content, args.model)

if __name__ == "__main__":
    main()

# (autocompete this with `python FileGPT.py -f FileGPT.py`)
# what does this program do?