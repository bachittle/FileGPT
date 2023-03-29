import sys
import argparse
import os
import openai

def read_input(files=None):
    if files:
        contents = []
        for file in files:
            with open(file, "r") as f:
                contents.append(f.read())
        content = "\n".join(contents)
    else:
        content = sys.stdin.read()
    return content

def write_output(content):
    openai.api_key = os.getenv("OPENAI_API_KEY")

    message = {"role": "user", "content": content}

    completion = openai.ChatCompletion.create(
        model="gpt-3.5-turbo",
        messages=[message]
    )

    sys.stdout.write(completion.choices[0].message.content)

def main():
    parser = argparse.ArgumentParser(description="FileGPT - A simple bot that repeats what the user says.")
    parser.add_argument("-f", "--file", help="Specify one or more text files as input.", type=str, nargs="+")
    args = parser.parse_args()

    input_content = read_input(args.file)
    write_output(input_content)

if __name__ == "__main__":
    main()