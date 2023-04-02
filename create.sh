# changelog of autocompletion commands used

# filegpt -f filegpt/*.py setup.py README.md -m gpt-4 >> README.md # update readme based on the new code: it is now a package
# filegpt -f filegpt/FileGPT.py >> filegpt/FileGPT.py # update filegpt to get personality list
# filegpt -f filegpt/*.py setup.py README.md -m gpt-4 >> README.md # update readme to introduce personalities
filegpt -f README.md setup.py docs/publish.md -m gpt-4 >> docs/publish.md # document steps on how to publish to pypi