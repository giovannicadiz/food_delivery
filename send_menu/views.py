from django.template.loader import get_template
from django.http import HttpResponse
from django.core.mail import EmailMessage
from slackclient import SlackClient
from product.models import Menu


# Create your views here.
def send_email(request):

    obj = Menu.objects.all()
    for i in obj:
        obj_name = i.name
        obj_mainCourse = i.mainCourse
        obj_sideDish = i.sideDish
        obj_salad = i.salad
        obj_dessert = i.dessert
        obj_drink = i.drink

    # Context
    context = {
        "obj": obj,
        "obj_name": obj_name,
        "obj_mainCourse": obj_mainCourse,
        "obj_sideDish": obj_sideDish,
        "obj_salad": obj_salad,
        "obj_dessert": obj_dessert,
        "obj_drink": obj_drink
    }

    subject = "Menu de hoy"
    to = ['myemail@gmail.com']
    from_email = 'myemail@gmail.com'
    message = get_template('email.html').render(context)
    msg = EmailMessage(subject, message, to=to, from_email=from_email)
    msg.content_subtype = 'html'
    msg.send()

    return HttpResponse('send_email')

# Slack Token
SLACK_TOKEN = 'xxx-666'

def send_slack(request):

    obj = Menu.objects.all()
    for i in obj:
        obj_name = i.name
        obj_mainCourse = i.mainCourse
        obj_sideDish = i.sideDish
        obj_salad = i.salad
        obj_dessert = i.dessert
        obj_drink = i.drink

    # Context
    context = {
        "obj": obj,
        "obj_name": obj_name,
        "obj_mainCourse": obj_mainCourse,
        "obj_sideDish": obj_sideDish,
        "obj_salad": obj_salad,
        "obj_dessert": obj_dessert,
        "obj_drink": obj_drink
    }

    sc = SlackClient(SLACK_TOKEN)
    message = get_template('email.html').render(context)
    sc.api_call(

        "chat.postMessage",
        channel="#menu",
        # text="Hola,Dejo el menu de hoy :) por slack"
        text=message

    )
    return HttpResponse('send_slack')
