from flask_assets import Bundle

bundles = {
    'main_scss': Bundle(
        'scss/main/main.scss',
        filters='libsass',
        depends='scss/*.scss',
        output='gen/css/main.%(version)s.css'
    ),
    'manager_scss': Bundle(
        'scss/manager/main.scss',
        filters='libsass',
        depends='scss/manager/*.scss',
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