from flask_assets import Bundle

bundles = {
    'manager_scss': Bundle(
        'scss/manager/main.scss',
        filters='libsass',
        depends=['scss/main/*.scss', 'scss/manager/*.scss'],
        output='gen/css/main.%(version)s.css'
    ),
    'user_scss': Bundle(
        'scss/user/main.scss',
        filters='libsass',
        depends=['scss/main/*.scss', 'scss/user/*.scss'],
        output='gen/css/main.%(version)s.css'
    ),
    'main_js': Bundle(
        'js/AjaxOps.js',
        'js/CheckUser.js',
        'js/SubmitForms.js',
        'js/ModInterface.js',
        'js/Redir.js',
        filters='jsmin',
        depends='js/*.js',
        output='gen/js/manager_main.%(version)s.js'
    )
}