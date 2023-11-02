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