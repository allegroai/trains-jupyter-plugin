define(['base/js/namespace','base/js/dialog','jquery'],function(IPython, dialog, $){

    // we will define an action here that should happen when we ask to clear and restart the kernel.
    var git_commit_push  = {
        help: 'trainsai.io: Commit current notebook and push to git repository',
        icon : 'fa-code-fork',
        help_index : '',
        handler : function (env) {
            IPython.notebook.save_notebook();
            var on_success = undefined;
            var on_error = undefined;
            var gitCredentialsChecked = function() {
                if ($('#git_credentials').is(":checked")) {
                    $('#git_user').prop("disabled", false);
                    $('#git_pass').prop("disabled", false);
                } else {
                    $('#git_user').prop("disabled", true);
                    $('#git_pass').prop("disabled", true);
                }
            };
            var p = $('<p/>').text("Please enter your commit message. Only this notebook will be committed.");
            var input = $('<textarea rows="4" cols="80" style="width: 100%; resize:none; background-color: white; color: black"></textarea></br>');
            var checkbox = $('<label><input type="checkbox" id="git_credentials" name="git credentials" value="credentials"/>&nbsp Use the following git credentials: &nbsp</label>').on("click", gitCredentialsChecked);
            var git_userpass = $('</br>' +
                '<textarea rows="1" cols="28" style="resize:none;" id="git_user" disabled=true>username</textarea></br>\n' +
                '<textarea rows="1" cols="28" style="resize:none;" id="git_pass" disabled=true>password</textarea>\n');
            var div = $('<div/>');

            //div.append(checkbox)
            div.append(p)
                .append(input)
                .append(checkbox).append(git_userpass);

            // get the canvas for user feedback
            var container = $('#notebook-container');

            function on_ok(){
                var re = /^\/notebooks(.*?)$/;
                var filepath = window.location.pathname.match(re)[1];
                var payload = {
                             'filename': filepath,
                             'msg': input.val(),
                             'commit_only_source': 2,
                             'git_credentials': $("#git_credentials").prop('checked'),
                             'git_user': $("#git_user").prop('value'),
                             'git_pass': $("#git_pass").prop('value')
                           };
                var settings = {
                    url : '/git/commit',
                    processData : false,
                    type : "PUT",
                    dataType: "json",
                    data: JSON.stringify(payload),
                    contentType: 'application/json',
                    success: function(data) {

                        // display feedback to user
                        var container = $('#notebook-container');
                        var feedback = '<div class="commit-feedback alert alert-success alert-dismissible" role="alert"> \
                                          <button type="button" class="close" data-dismiss="alert" aria-label="Close"><span aria-hidden="true">&times;</span></button> \
                                          '+data.statusText+' \
                                           \
                                        </div>';

                        // display feedback
                        $('.commit-feedback').remove();
                        container.prepend(feedback);
                    },
                    error: function(data) {

                        // display feedback to user
                        var feedback = '<div class="commit-feedback alert alert-danger alert-dismissible" role="alert"> \
                                          <button type="button" class="close" data-dismiss="alert" aria-label="Close"><span aria-hidden="true">&times;</span></button> \
                                          <strong>Warning!</strong> Something went wrong. \
                                          <div>'+data.statusText+'</div> \
                                        </div>';

                        // display feedback
                        $('.commit-feedback').remove();
                        container.prepend(feedback);
                    }
                };

                // display preloader during commit and push
                var preloader = '<img class="commit-feedback" ' +
                    'style="display: block; margin-bottom: 2%; margin-top: 1%; margin-left: auto;  margin-right: auto;" ' +
                    'src='+ window.location.protocol + '//' + window.location.hostname + ':' + window.location.port +
                    '/nbextensions/trains-jupyter-plugin/dring.gif alt="committing & pushing git...">';
                console.info(preloader);
                container.prepend(preloader);

                // commit and push
                $.ajax(settings);
            }


            dialog.modal({
                body: div ,
                title: 'Commit and Push Notebook',
                buttons: {
                    'trainsai.io':{class:'btn btn-link btn-xs pull-left', tabindex: -1,
                    click: function(){ window.open('https://trainsai.io', '_blank'); } },
                    'Commit and Push':
                            { class:'btn-primary btn-large',
                              click:on_ok,
                              tabindex: 0,
                            },
                    'Cancel':{tabindex: 1,},
                    },
                notebook:env.notebook,
                keyboard_manager: env.notebook.keyboard_manager,
            })

        }
    };

    function _on_load(){

        // log to console
        console.info('Loaded trainsai.io Jupyter extension: Git Commit and Push');

        // register new action
        var action_name = IPython.keyboard_manager.actions.register(git_commit_push, 'commit-push', 'jupyter-git');

        // add button for new action
        IPython.toolbar.add_buttons_group([action_name]);
    }

    return {load_ipython_extension: _on_load };
});
