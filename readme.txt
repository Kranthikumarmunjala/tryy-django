#video 76:-
upload images in django models
pip install requirements.txt
some changes in models then we do makemigrations
we add images from computer

#video77:-
view for handling file or image uploads
in this video we create image-form.html in templates folder
we change some code in recipe_ingredient_image_upload
finally run the server

#video 78:-
uploading files with django&HTMX
in templates->recipes->partials->we create a file image-upload-form.html
and run the server
when we add a image it can loaded that we can see in output

#video 79:-
Microservice API for Text Extraction from uploaded images
python -c"import secrets; print(secrets.token_urlsafe(32)"
pip install requests
we create services.py file in recipes
run the server choose a file and upload it
in recipes-models.py add extracted variable file and do makemigration and migrate

#video 80:-
Deploy Django to do app platform via doctl CLI
hear we install doctl
(brew install doctl)
crate app (doctl apps create--spec.do/app.yaml

#video 81:-
CI&CD For Django+Github+Digitalocean
hear worked on github digitalocean
trydjango->github->windows->main.yaml

#video 82:-
Automating collectstatic with github acations
python manage.pyb collectstatic --noinput
pip install pre-commit
github/workflows->collectstatic.yaml
github/workflows->prod.yaml and we create a file in static->recipes->js->css
we add css,js files (git add static/css(or)js/) and we can push into github(git push origin main)
same when we update code in collecstatic.yaml agin we push the code

#video 83:-
parsing OCR Microservice Results
we create a file in recipes extract-example.py
add parse_paragraph_to_recipe_line variable
we import list from typing and unitRegistry from pint

#video 84:-
Microsrvice to database
in views from utils import convert_to_qty_units
adding lower() into models and validatorsfile and do makemigrations and migrate
and run the server

#video 85:-
Adding Boostrap &the trip of the Bootstrap Iceberg
create navbar.html file in templates->base
copy from bootstrap required meta tags and bootstrap css
and paste in navbar.html

#video86:-
Creating the meal Queue
create mealstatus,mealqueryset,meal manager,meal functions in models
register meal name in admin
write appname(meals in settings->installed apps)

#video87:-
Toggle Recipes into Meal Queue & Test
copy from recipes->test.py code into meals->test.py
take test_pending_meals and test_completed_meals functions
and lastly take test_add_item_via_toggle and run(python manage.py test meals)

#video88:-
Meal Queue Toggle View
take meal_queue_toggle_view function in views
add url path in trydjango urls
create queue-toggle html file in templates-meals-partials

