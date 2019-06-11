# [TRAINS](https://github.com/allegroai/trains) Jupyter Plugin

[![GitHub license](https://img.shields.io/github/license/allegroai/trains-jupyter-plugin.svg)](https://img.shields.io/github/license/allegroai/trains-jupyter-plugin.svg)
[![PyPI pyversions](https://img.shields.io/pypi/pyversions/trains-jupyter-plugin.svg)](https://img.shields.io/pypi/pyversions/trains-jupyter-plugin.svg)
[![PyPI version shields.io](https://img.shields.io/pypi/v/trains-jupyter-plugin.svg)](https://img.shields.io/pypi/v/trains-jupyter-plugin.svg)
[![PyPI status](https://img.shields.io/pypi/status/trains-jupyter-plugin.svg)](https://pypi.python.org/pypi/trains-jupyter-plugin/)

TRAINS-jupyter-plugin is a jupyter notebook extension enabling users to push ipython notebooks to git repository,
using the git [button](#Screenshots) added to the notebook toolbar. 

After saving a notebook, a user can push the notebook to a pre-specified git repository.
Currently this extension supports commits to a pre-initialized git repository on a pre-defined branch.

The notebook will be pushed to the git repository, based on the folder structure it is located in.
The notebook will also be converted to `.py` script and pushed together with the `.ipynb`.
Additionally, a `requirements.txt` will be created and updated according to the notebook imports. 
The requirements file will also be pushed to the git.


Examples of two repositories: "notebook1.ipynb" will be pushed to "repo1" and "notebook2.ipynb" to "repo2":
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


Selection of a specific branch is done using git checkout from the jupyter host machine.

For example, switch to branch2 in repo2:
```
$ cd ~/repo2
$ git checkout branch2
```
From this point onwards the jupyter notebook push will be done to "branch2"


## Installation

You can install directly from pypi:

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

## Steps

* Install package using above commands
* Clone your Git repository to a folder that will be assigned to a specific user 
* Checkout a specific branch for the current user
* Make sure git is configured with the correct credentials 
(it is advised to verify there is need to for password/passphrase when pushing)
* Run jupyter notebook 
* Any commit/push of notebooks from this specific folder will be done to the selected branch

## Screenshots

![Extension](https://github.com/allegroai/trains-jupyter-plugin/blob/master/docs/extension.png?raw=true "Extension added to toolbar")

![Commit Message](https://github.com/allegroai/trains-jupyter-plugin/blob/master/docs/commit.png?raw=true "Commit Message")

![Success Message](https://github.com/allegroai/trains-jupyter-plugin/blob/master/docs/success.png?raw=true "Success Message")

## Credits

Thanks to https://github.com/Lab41/sunny-side-up & https://github.com/sat28/githubcommit for laying the foundation of this extension.
