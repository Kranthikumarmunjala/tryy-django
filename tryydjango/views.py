"""
To render html web pages
"""
import random
from django.http import HttpResponse
from django.template.loader import render_to_string
from artcles.models import Article


def home_view(request, *args, **kwargs):
    """
    Take in a request (Django sends request)
    Return HTML as a response(the pick to return the response)
    """
    name="shiva"
    random_id=random.randint(1,4)
    article_obj=Article.objects.get(id=random_id)
    article_queryset=Article.objects.all()
    #print(article_list)
    #my_list=article_list    #[102,13,342,1331,213]

    context={
        "object_list": article_queryset,
        "objecr":article_obj,
        "title":article_obj.title,
        "id":article_obj.id,
        "content":article_obj.content
    }


    HTML_STRING=render_to_string("home-view.html", context=context)
    #HTML_STRING = """
    #<hi>{title}(id: {id})!</h1>
    #<p>{content}!</p>
    #""".format(**context)
    return HttpResponse(HTML_STRING)