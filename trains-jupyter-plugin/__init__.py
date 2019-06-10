from .handlers import setup_handlers
# Jupyter Extension points
def _jupyter_server_extension_paths():
    return [{
        'module': 'trains-jupyter-plugin',
    }]

def _jupyter_nbextension_paths():
    return [{
        "section": "notebook",
        "dest": "trains-jupyter-plugin",
        "src": "static",
        "require": "trains-jupyter-plugin/main"
    }]

def load_jupyter_server_extension(nbapp):
    setup_handlers(nbapp.web_app)
