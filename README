PASOS:

- Crear el directorio raíz del proyecto
	mkdir curso-django
	cd curso-django

- Crear el virtualenv
	virtualenv venv

- Instalar los paquetes de PIP
	pip install django south

- Guardar las dependencias de PIP
	pip freeze > requirements.txt

- Crear el proyecto de django
	django-admin.py startproject django_blog
	cd django_blog

- Añadir South a settings.INSTALLED_APPS
	INSTALLED_APPS = (
		......
		......
	    'south',
	)

- Crear la base de datos y un usuario admin
	python manage.py syncdb

- Crear la aplicación de los blogs
	python manage.py startapp blog_engine

- Añadir la nueva aplicación a settings.INSTALLED_APPS
	INSTALLED_APPS = (
		......
		......
	    'south',
	    'blog_engine',
	)

- Crear la primera migración de South
	python manage.py schemamigration --initial blog_engine

- Aplicar la migración
	python manage.py migrate


