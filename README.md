# FileGPT

FileGPT is a simple command-line tool that uses OpenAI's GPT-3.5-turbo or GPT-4 to autocomplete text files. It reads text input from a file or standard input (stdin) and outputs the completed text to standard output (stdout). FileGPT is useful for generating content, adding context or explanations, and autocompleting code, among other use cases.

## Prerequisites

To use FileGPT, you need:

1. An OpenAI API key (sign up for one [here](https://platform.openai.com))
2. Python 3.6 or later

## Installation

Install FileGPT directly from PyPI:

```
pip install filegpt
```

## Setup

Set the OpenAI API key as an environment variable:

```
export OPENAI_API_KEY=<your_api_key>
```

(for Windows, use `set OPENAI_API_KEY=<your_api_key>`)

## Usage

To use FileGPT, run the following command:

```
filegpt
```

You can provide input to FileGPT in two ways:

1. By passing one or more input text files as arguments, using the `-f` or `--file` flag:

```
filegpt -f input1.txt input2.txt
```

2. By providing input through standard input (stdin):

```
echo "Hello, this is FileGPT!" | filegpt
```

To specify the model to use for autocompletion, use the `-m` or `--model` flag:

```
filegpt -f input.txt -m gpt-3.5-turbo # old model
filegpt -f input.txt -m gpt-4 # new model
```

If no model is specified, FileGPT will use the default model (gpt-3.5-turbo).

## Logging

FileGPT generates log messages for major operations and saves them to a local log file named `filegpt.log`. You can check this file for any issues or status updates during execution.

## Example

Let's create an example input file for FileGPT. Write the following content to a file named `input.txt`:

```
Once upon a time, in a small village near a dense forest,
```

Now, we can use FileGPT to autocomplete the story:

```
filegpt -f input.txt
```

Sample output:

```
Once upon a time, in a small village near a dense forest, there lived a young boy named Jack. Jack was an adventurous and curious child who loved to explore the woods with his trusty dog, Toby.

One sunny morning, Jack and Toby ventured deep into the forest, far from the village. As they wandered through the beautiful landscape, they discovered a hidden cave amidst the trees. Filled with curiosity, Jack decided to explore the cave with Toby by his side.

Inside the cave, they found an ancient treasure chest, overflowing with gold and precious gems. But guarding the treasure was a fierce dragon, awakened by the sound of their footsteps. Jack had heard stories of dragons and knew that they were dangerous creatures, so he needed to think of a plan to escape the cave without alerting the dragon.

As Jack carefully considered his options, he remembered a folk tale his father had once told him about a dragon's weakness: their inability to resist the sound of a beautiful melody. Jack took a deep breath and began to sing the most enchanting song he could muster. As the sweet music filled the cave, the dragon's fiery eyes softened, and it listened intently, captivated by the melody.

Seizing the opportunity, Jack and Toby made their way past the enchanted dragon, out of the cave, and back into the sunlight. They returned to their village, treasure in hand, and shared their incredible adventure with the villagers. From that day on, Jack was known as a hero in the small village, and his tale of bravery and wit was passed down through generations. And as for Toby, he was never far from Jack's side, the two forging a lifelong bond the likes of which the village had never seen.
```

add a new section to this readme detailing the new use of personalities

## Personalities

FileGPT now includes personalities that allow you to adjust the style and format of the output. Currently, there are two available personalities:

1. Py Coder: Generates code-based responses, usually with comments for user interaction. Currently only for python, will experiment with other langs later.
2. Writer: Generates text-based content in Markdown format, suitable for documentation, blog posts, and other textual use cases.

To specify a personality when using FileGPT, use the `-p` or `--personality` flag:

```
filegpt -f input.txt -p py-coder
filegpt -f input.txt -p writer
```

You can also list the available personalities by running the following command:

```
filegpt p-ls
```

### Example with Personalities

Let's create an example input file for FileGPT using the 'py-coder' personality. Write the following content to a file named `code_input.txt`:

```
# Calculate the factorial of a number
def factorial(n):
    if n == 0:
        return 1
```

Now, we can use FileGPT to autocomplete the code:

```
filegpt -f code_input.txt -p py-coder
```

Sample output:

```
# Calculate the factorial of a number
def factorial(n):
    if n == 0:
        return 1
    else:
        return n * factorial(n - 1)

# Now, let's test the factorial function
n = 5
result = factorial(n)
print(f"The factorial of {n} is {result}")
```

When using the 'writer' personality, FileGPT will produce text-based content with Markdown formatting. This can be useful for generating documentation or writing blog posts.