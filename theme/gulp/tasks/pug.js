var gulp    = require('gulp');
var pug     = require('gulp-pug');
var config  = require('../config.js');
var plumber = require('gulp-plumber');


function emmitTemplates(pathFrom, pathTo) {
    return gulp.src(pathFrom + '/*.pug')
        .pipe(plumber())
        .pipe(pug({
            pretty: process.env.NODE_ENV !== 'production'
        }))
        .pipe(gulp.dest(pathTo));
}

gulp.task('html:pages', () => {
    return emmitTemplates(config.src.pages, config.dest.pages);
});
gulp.task('html:accounts', () => {
    return emmitTemplates(config.src.accounts, config.dest.accounts);
});
gulp.task('html:shares', () => {
    return emmitTemplates(config.src.shares, config.dest.shares);
});
gulp.task('html', ['html:pages', 'html:accounts', 'html:shares']);

gulp.task('html:watch', function() {
    gulp.watch(config.src.root + '/**/*.{html,pug}', ['html']);
});