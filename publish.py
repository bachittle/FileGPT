import os
import getpass

TOOLS = ["twine", "setuptools", "wheel"]

def install_tools():
    os.system(f"pip install {' '.join(TOOLS)}")

def build_package():
    os.system("rm -r dist") # Remove old build
    os.system("python setup.py sdist bdist_wheel") # Build new build

def check_package():
    os.system("twine check dist/*")

def upload_package(username, password):
    os.environ['TWINE_USERNAME'] = username
    os.environ['TWINE_PASSWORD'] = password
    os.system("twine upload dist/* --skip-existing")
    del os.environ['TWINE_USERNAME']
    del os.environ['TWINE_PASSWORD']

def main():
    install_tools()
    build_package()
    check_package()

    # Check for environment variables
    username = os.environ.get('TWINE_USERNAME')
    password = os.environ.get('TWINE_PASSWORD')

    if username is None or password is None:
        # If not found in environment variables, ask for user input
        username = input("Enter your PyPI username: ")
        password = getpass.getpass("Enter your PyPI password: ")

    upload_package(username, password)

if __name__ == "__main__":
    main()