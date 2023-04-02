from setuptools import setup

setup(
    name="filegpt",
    version="0.1.5",
    description="A tool for autocompleting text files using OpenAI's GPT models.",
    url="https://github.com/bachittle/FileGPT",
    author="Bailey Chittle",
    author_email="bachittle@gmail.com",
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    packages=["filegpt"],
    install_requires=[
        "openai",
        "tiktoken"
    ],
    entry_points={
        "console_scripts": [
            "filegpt = filegpt.FileGPT:main"
        ]
    },
)