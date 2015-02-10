from django_assets import Bundle, register
js = Bundle('js/jquery.min.js','js/jquery.dropotron.min.js','js/jquery.scrolly.min.js','js/skel.min.js','js/skel-layers.min.js','js/init.js', filters='jsmin', output='js-packed.js')
register('js_all', js)
css_noscipt = Bundle('css/skel.css','css/style.css','css/style-noscript.css', filters='cssmin', output='css-noscipt-packed.css')
register('css_noscript',css_noscipt)
