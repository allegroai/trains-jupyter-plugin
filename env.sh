#!/bin/bash

####################### Change in jupyter config ###########################
if [ ! -f ~/.jupyter/jupyter_notebook_config.py ]; then
   jupyter notebook --generate-config
fi

echo 'c.NotebookApp.disable_check_xsrf = True' >> ~/.jupyter/jupyter_notebook_config.py
