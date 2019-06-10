from notebook.utils import url_path_join as ujoin
from notebook.base.handlers import IPythonHandler
import os, json, requests, sys
import subprocess
import six

try:
    from urllib.parse import unquote, quote
except ImportError:
     from urlparse import unquote, quote


class GitCommitHandler(IPythonHandler):

    def data_received(self, chunk):
        pass

    def error_and_return(self, reason):
        # send error
        self.send_error(500, reason=reason)

    def put(self):
        try:
            return self._put()
        except Exception as e:
            print(e)
            self.error_and_return("Could not push to remote repository:</br>{}".format(str(e)))

    def _put(self):
        # get current directory (to return later)
        cwd = os.getcwd()
        print('cwd', cwd)

        # obtain filename and msg for commit
        data = json.loads(self.request.body.decode('utf-8'))
        print('data', data)
        msg = data['msg']
        send_git_credentials = data['git_credentials']

        # commit_only_source = data['commit_only_source']
        filename = unquote(data['filename']).strip()
        if filename.startswith('/'):
            filename = filename[1:]
        fullpath_ipynb = os.path.join(cwd, filename)
        if not os.path.exists(fullpath_ipynb):
            cwd = os.path.expanduser(self.settings.get('server_root_dir'))
            fullpath_ipynb = os.path.join(cwd, filename)
            if not os.path.exists(fullpath_ipynb):
                raise ValueError("Could not locate ipynb file {}".format(fullpath_ipynb))
        code_dir = os.path.dirname(fullpath_ipynb)
        # commit current notebook
        # client will sent pathname containing git directory; append to git directory's parent
        subprocess.check_output(['jupyter', 'nbconvert', fullpath_ipynb, '--to', 'script'], cwd=code_dir)
        fullpath_py = fullpath_ipynb.replace('.ipynb', '.py')

        fullpath_req = os.path.join(code_dir, 'requirements.txt')
        process = subprocess.Popen(['pigar', '-P', code_dir, '-p', fullpath_req], cwd=code_dir, stdin=subprocess.PIPE,
                                   stdout=subprocess.PIPE, shell=True)
        # TODO: replace with imports to pigar and removing the guessed packages
        process.communicate(input=b'\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n'
                                  b'\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n')
        process.wait()

        # add the files (if they weren't already there)
        subprocess.check_output(['git', 'add', fullpath_py, fullpath_ipynb, fullpath_req], cwd=code_dir)

        # check if there is a change
        git_status = subprocess.check_output(['git', 'status', '-s', fullpath_py, fullpath_ipynb, fullpath_req],
                                             cwd=code_dir, universal_newlines=True).strip()
        # print('git_diff', git_diff)
        if not git_status or '\nA  ' not in '\n'+git_status and '\nM  ' not in '\n'+git_status:
            # close connection
            print('git diff: returned nothing')
            # self.write({'status': 200, 'statusText': 'Commit skipped: no changes detected in {}'.format(filename)})
        else:
            # commit the changes
            print('git committing:', git_status)
            subprocess.check_output(['git', 'commit', '-m', '\"{}\n\nUpdated {}\"'.format(msg, filename),
                                     fullpath_py, fullpath_ipynb, fullpath_req], cwd=code_dir)

        git_branch = subprocess.check_output(['git', 'rev-parse', '--abbrev-ref', 'HEAD'], cwd=code_dir,
                                             universal_newlines=True).strip()
        git_commit = subprocess.check_output(['git', 'rev-parse', 'HEAD'], cwd=code_dir,
                                             universal_newlines=True).strip()
        # push to server
        if send_git_credentials:
            git_repo = subprocess.check_output(["git", "remote", "get-url", "origin"], cwd=code_dir,
                                               universal_newlines=True).strip()
            origin = git_repo.replace('://', '://' + data['git_user'].replace('@', '%40')
                                      + ':' + data['git_pass'].replace('@', '%40') + '@')
            print('origin', origin)
        else:
            origin = 'origin'

        try:
            subprocess.check_output(['git', 'push', origin, git_branch], stderr=subprocess.PIPE,
                                    input='\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n',
                                    universal_newlines=True, cwd=code_dir)
        except subprocess.CalledProcessError as e:
            self.error_and_return("Could not push to remote repository: </br>{}</br>{}".format(
                str(e.output.encode('utf-8'))[2:-1].replace('\\n', '</br>'),
                str(e.stderr.encode('utf-8'))[2:-1].replace('\\n', '</br>')))
            return

        # close connection
        self.write({'status': 200,
                    'statusText': 'Git committed and pushed successfully</br>'
                                  'Changes to [{}] captured on branch [{}] commit id [{}]'.
                   format(filename, git_branch, git_commit)})


def setup_handlers(nbapp):
    route_pattern = ujoin(nbapp.settings['base_url'], '/git/commit')
    nbapp.add_handlers('.*', [(route_pattern, GitCommitHandler)])

