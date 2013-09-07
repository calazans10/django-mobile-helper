# django-mobile-helper

Helps django developers to support mobile users, features:

 * Detection of requests starting with m. or mobile.yoursite.com
 * Detection of requests with HTTP_USER_AGENT of mobile browsers
 * Decorator to provide a simple way provide template for mobile devices

## Installation

Download the code; put in into your project's directory,
if you want a system-wide instalation you can run

	python setup.py install

or

	sudo easy_install django-mobile-helper


REQUIREMENTS: django !

## SETTINGS.py

### MOBILE_PATTERN

Regular expression to match mobile user in HTTP_USER_AGENT header.
default: constants.py

## USAGE

### MIDDLEWARE

In your settings.py add:

	MIDDLEWARE_CLASSES = (
		(...) #your middleware classes
		# if you added to you project's folder:
		'your_project.django_mobile.middleware.MobileMiddleware'
		# if you installed on site-packages:
		'django_mobile.middleware.MobileMiddleware'
	)


### DECORATOR

You can use it in any view function:

	from django_mobile.middleware import MobileMiddleware


	@login_required
	@render_to(template='desktop.html', mobile_template='mobile_template.html')
	def view_function(request):
		(...) # do your stuff here
		return locals()
