# [TRAINS](https://github.com/allegroai/trains) Jupyter Plugin

trains-jupyter-plugin is a jupyter notebook extension enabling users to push ipython notebooks to git repository.
The git [button](#Screenshots) is displayed in the notebook toolbar. After saving any notebook
the user can push notebook to pre-specified git repository.
Currently this extension supports commits to a pre initialized git repository and pre-defined branch.
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

![Extension](docs/extension.png?raw=true "Extension added to toolbar")

![Commit Message](docs/commit.png?raw=true "Commit Message")

![Success Message](docs/success.png?raw=true "Success Message")

## Credits

Thanks to https://github.com/Lab41/sunny-side-up & https://github.com/sat28/githubcommit for laying the foundation of this extension.