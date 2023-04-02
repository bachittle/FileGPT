## Publishing the FileGPT project to PyPI

To publish FileGPT to the Python Package Index (PyPI), follow these steps:

### Prerequisites

1. Make sure you have a PyPI account. If you don't have one, [register here](https://pypi.org/account/register/).
2. Install the necessary tools for publishing packages: `twine`, `setuptools` and `wheel`. You can do this by running the following command:

   ```
   pip install twine setuptools wheel
   ```

### Steps

1. **Update the package version:** Before publishing a new version of the package, you should update the `version` parameter in the `setup` function within `setup.py`. For example:

   ```python
   setup(
       ...
       version="0.1.6",  # Increment this version number
       ...
   )
   ```

   Make sure to use [Semantic Versioning](https://semver.org/) when updating the package version.

2. **Build the package:** Navigate to the project directory where the `setup.py` file is located, and execute the following command to build the package:

   ```
   python setup.py sdist 
   ```

   This will generate a `dist` directory containing the `.tar.gz` and `.whl` distribution files.

3. **Check the package with Twine:** Before uploading the package to PyPI, it's a good idea to check it for errors using Twine:

   ```
   twine check dist/*
   ```

4. **Upload the package to PyPI:** Use Twine to upload the package:

   ```
   twine upload dist/*
   ```

   You will be prompted for your PyPI username and password (or API token).

5. **Verify the publication:** Once the upload is complete, visit the FileGPT package page on [PyPI](https://pypi.org/project/filegpt/) to verify that the new version has been published.

That's it! Your updated FileGPT package is now available for installation through PyPI. Users can install or update it using the following command:

```
pip install --upgrade filegpt
```