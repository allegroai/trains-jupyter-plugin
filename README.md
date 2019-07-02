# [TRAINS](https://github.com/allegroai/trains) Jupyter Plugin

[![GitHub license](https://img.shields.io/github/license/allegroai/trains-jupyter-plugin.svg)](https://img.shields.io/github/license/allegroai/trains-jupyter-plugin.svg)
[![PyPI pyversions](https://img.shields.io/pypi/pyversions/trains-jupyter-plugin.svg)](https://img.shields.io/pypi/pyversions/trains-jupyter-plugin.svg)
[![PyPI version shields.io](https://img.shields.io/pypi/v/trains-jupyter-plugin.svg)](https://img.shields.io/pypi/v/trains-jupyter-plugin.svg)
[![PyPI status](https://img.shields.io/pypi/status/trains-jupyter-plugin.svg)](https://pypi.python.org/pypi/trains-jupyter-plugin/)

**trains-jupyter-plugin** is a jupyter notebook extension enabling users to push ipython notebooks to a git repository,
using the git [button](#Screenshots) added to the notebook toolbar.

After saving a notebook, a user can push the notebook to a predefined git repository. The extension currently supports pushing to a predefined branch in the repository.

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


## Installation <a name="installation"></a>

Install directly from pypi:

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

* Install package using the commands [above](#installation)
* Clone your git repository to a folder that will be assigned to a specific user
* Checkout a specific branch for the current user
* Make sure git is configured with the correct credentials
(we recommend verifying a password/passphrase is required when pushing)
* Run jupyter notebook
* Any commit/push of notebooks from this specific folder will be done to the selected branch

## Screenshots

![Extension](https://github.com/allegroai/trains-jupyter-plugin/blob/master/docs/extension.png?raw=true "Extension added to toolbar")

![Commit Message](https://github.com/allegroai/trains-jupyter-plugin/blob/master/docs/commit.png?raw=true "Commit Message")

![Success Message](https://github.com/allegroai/trains-jupyter-plugin/blob/master/docs/success.png?raw=true "Success Message")

## Credits

Thanks to [Lab41/sunny-side-up](https://github.com/Lab41/sunny-side-up) & [sat28/githubcommit](https://github.com/sat28/githubcommit) for laying the foundations for this extension.
