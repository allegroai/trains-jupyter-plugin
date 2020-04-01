# [Trains](https://github.com/allegroai/trains) Jupyter Plugin

[![GitHub license](https://img.shields.io/github/license/allegroai/trains-jupyter-plugin.svg)](https://img.shields.io/github/license/allegroai/trains-jupyter-plugin.svg)
[![PyPI pyversions](https://img.shields.io/pypi/pyversions/trains-jupyter-plugin.svg)](https://img.shields.io/pypi/pyversions/trains-jupyter-plugin.svg)
[![PyPI version shields.io](https://img.shields.io/pypi/v/trains-jupyter-plugin.svg)](https://img.shields.io/pypi/v/trains-jupyter-plugin.svg)
[![PyPI status](https://img.shields.io/pypi/status/trains-jupyter-plugin.svg)](https://pypi.python.org/pypi/trains-jupyter-plugin/)

**trains-jupyter-plugin** is a Jupyter Notebook extension which enables you to push ipython notebooks to a git repository,
using a [git button](#Screenshots) added to the notebook toolbar.

After saving a notebook, you can push the notebook to a predefined git repository (currently, pushing to a specific predefined branch is supported).

When clicking the *version-control* button:
* The notebook `.ipynb` file will be pushed to the git repository based on the folder structure in which it is located
* The notebook will also be converted to a `.py` script, pushed alongside the `.ipynb` file
* A `requirements.txt` will be created and updated according to the notebook imports, and pushed alongside the `.ipynb` file

For example, if you have two repositories:
```
repo1/
├── .git
└── experiment1/
   └── notebook.ipynb

repo2/
├── .git
└── experiment2/
   └── notebook2.ipynb
```

`notebook1.ipynb` will be pushed to the `repo1` repository, and `notebook2.ipynb` will be pushed to the `repo2` repository.

In order to select the predefined branch into which the files will be pushed, use `git checkout` on the jupyter host machine.

For example, switch to `branch2` in `repo2`:
```
$ cd ~/repo2
$ git checkout branch2
```
From this point onwards the jupyter notebook push will be done to the `branch2` branch in the `repo2` repository.

## Installation

To use the plugin, execute the following script which installs the plugin and configures Jupyter to use it:

```
pip install trains-jupyter-plugin

if [ ! -f ~/.jupyter/jupyter_notebook_config.py ]; then
   jupyter notebook --generate-config
fi
echo 'c.NotebookApp.disable_check_xsrf = True' >> ~/.jupyter/jupyter_notebook_config.py

jupyter serverextension enable --py trains-jupyter-plugin
sudo jupyter nbextension install --py trains-jupyter-plugin
```

To enable the extension for all notebooks:

```
jupyter nbextension enable --py trains-jupyter-plugin
```

## How to use

Once the Plugin is installed and Jupyter configured:

1. Clone your git repository to a folder that will be assigned to a specific user

1. Checkout a specific branch for the current user

1.  Make sure git is configured with the correct credentials (we recommend verifying a password/passphrase is required when pushing)

1. Run Jupyter Notebook

1. Any commit/push of notebooks from this specific folder will be done to the checked out branch

## Screenshots

An additional button to the Jupyter toolbar:

![Extension](https://github.com/allegroai/trains-jupyter-plugin/blob/master/docs/extension.png?raw=true "Extension added to toolbar")

The git push dialog for pushing the notebook:

![Commit Message](https://github.com/allegroai/trains-jupyter-plugin/blob/master/docs/commit.png?raw=true "Commit Message")

![Success Message](https://github.com/allegroai/trains-jupyter-plugin/blob/master/docs/success.png?raw=true "Success Message")

## Additional Documentation

For detailed information about the **Trains** open source suite, see our [Trains Documentation](https://allegro.ai/docs).

## Acknowledgements

Thanks to [Lab41/sunny-side-up](https://github.com/Lab41/sunny-side-up) & [sat28/githubcommit](https://github.com/sat28/githubcommit) for laying the foundations for this plugin.

## Community & Support

* If you have a question, consult our **Trains** [FAQs](https://allegro.ai/docs/faq/faq) or tag your questions on [stackoverflow](https://stackoverflow.com/questions/tagged/trains) with "*trains*".
* To request features or report bugs, see our [GitHub issues](https://github.com/allegroai/trains-jupyter-plugin/issues).
* Email us at *[trains@allegro.ai](mailto:trains@allegro.ai?subject=Trains)*

## Contributing

We encourage your contributions! See our **Trains** [Guidelines for Contributing](https://github.com/allegroai/trains/blob/master/docs/contributing.md).

