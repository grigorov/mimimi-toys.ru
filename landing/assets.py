from django_assets import Bundle, register

js = Bundle('js/jquery.min.js','js/jquery.dropotron.min.js','js/jquery.scrolly.min.js','js/jquery.onvisible.min.js','js/skel.min.js','js/skel-layers.min.js','js/init.js', filters='yui_js', output='all.js')
register('js_all', js)

css_noscipt = Bundle('css/skel.css','css/style.css','css/style-noscript.css', filters='cssmin', output='css-noscipt.css')
register('css_noscript',css_noscipt)
