from flask_assets import Bundle

bundles = {
    'main_scss': Bundle(
        'scss/main.scss',
        filters='libsass',
        depends='scss/*.scss',
        output='gen/css/main.%(version)s.css'
    ),
    'main_js': Bundle(
        'js/menu_mod.js',
        filters='jsmin',
        depends='js/*.js',
        output='gen/js/main.%(version)s.js'
    )
}