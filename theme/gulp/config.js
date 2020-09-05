var util = require('gulp-util');

var production = util.env.production || util.env.prod || false;
var BASE_DIR = '../';
var destPath = BASE_DIR + 'static/cosmeticsyou';

var config = {
    env       : 'development',
    production: production,

    src: {
        root         : 'src',
        templates    : 'src/templates',
        templatesData: 'src/templates/data',
        pagelist     : 'src/index.yaml',
        sass         : 'src/scss',
        // path for sass files that will be generated automatically via some of tasks
        sassGen      : 'src/sass/generated',
        js           : 'src/js',
        img          : 'src/img',
        svg          : 'src/img/svg',
        icons        : 'src/icons',
        // path to png sources for sprite:png task
        iconsPng     : 'src/icons',
        // path to svg sources for sprite:svg task
        iconsSvg     : 'src/icons',
        // path to svg sources for iconfont task
        iconsFont    : 'src/icons',
        fonts        : 'src/fonts',
        lib          : 'src/lib',
        pages        : 'src/pages',
        accounts     : 'src/accounts',
        shares       : 'src/shares'
    },
    dest: {
        root    : destPath,
        html    : destPath,
        css     : destPath + '/css',
        js      : destPath + '/js',
        img     : destPath + '/img',
        fonts   : destPath + '/fonts',
        lib     : destPath + '/lib',
        pages   : BASE_DIR + 'pages/templates',
        accounts: BASE_DIR + 'accounts/templates',
        shares: BASE_DIR + 'shares/templates'
    },

    setEnv: function(env) {
        if (typeof env !== 'string') return;
        this.env = env;
        this.production = env === 'production';
        process.env.NODE_ENV = env;
    },

    logEnv: function() {
        util.log(
            'Environment:',
            util.colors.white.bgRed(' ' + process.env.NODE_ENV + ' ')
        );
    },

    errorHandler: require('./util/handle-errors')
};

config.setEnv(production ? 'production' : 'development');

module.exports = config;
