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


## Example

Let's create an example input file for FileGPT. Write the following content to a file named `input.txt`:

```
Once upon a time, in a small village near a dense forest,
```

Now, we can use FileGPT to autocomplete the story:

```
python FileGPT.py -f input.txt
```

Sample output:

```
Once upon a time, in a small village near a dense forest, there lived a young boy named Jack. Jack was an adventurous and curious child who loved to explore the woods with his trusty dog, Toby.

One sunny morning, Jack and Toby ventured deep into the forest, far from the village. As they wandered through the beautiful landscape, they discovered a hidden cave amidst the trees. Filled with curiosity, Jack decided to explore the cave with Toby by his side.

Inside the cave, they found an ancient treasure chest, overflowing with gold and precious gems. But guarding the treasure was a fierce dragon, awakened by the sound of their footsteps. Jack had heard stories of dragons and knew that they were dangerous creatures, so he needed to think of a plan to escape the cave without alerting the dragon.

As Jack carefully considered his options, he remembered a folk tale his father had once told him about a dragon's weakness: their inability to resist the sound of a beautiful melody. Jack took a deep breath and began to sing the most enchanting song he could muster. As the sweet music filled the cave, the dragon's fiery eyes softened, and it listened intently, captivated by the melody.

Seizing the opportunity, Jack and Toby made their way past the enchanted dragon, out of the cave, and back into the sunlight. They returned to their village, treasure in hand, and shared their incredible adventure with the villagers. From that day on, Jack was known as a hero in the small village, and his tale of bravery and wit was passed down through generations. And as for Toby, he was never far from Jack's side, the two forging a lifelong bond the likes of which the village had never seen.