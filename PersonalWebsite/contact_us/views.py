from django.shortcuts import redirect
from django.core.mail import send_mail,EmailMultiAlternatives
from django.template.loader import get_template
from contact_us.models import Enquery
import time

def s_mail(lst):
    #variable sections
            #data={
                #'name':lst[0],
                #'desig':lst[1],
                #'qual':lst[2],
                #'exp':lst[3],
                #'expert':lst[4],
                #'email':lst[5],
                #'mob':lst[6]
                # }
    subject='New Entry In Database'+str(time.strftime("%H%M%S"))
    subject1='THANK YOU FOR CONTACTING-US '+str(time.strftime("%H%M%S"))
    form_mail='testing8854mail@gmail.com'
    to='mayuradhayge@gmail.com'
    #rendering the html file msg
    msg=get_template('display_mail.html').render({
                                                    'name':lst[0],
                                                    'email':lst[1],
                                                    'massage':lst[2],
                                                 })
    #############
    ms=EmailMultiAlternatives(subject,msg,form_mail,[form_mail])
    msg34=get_template('customer_mail.html').render()
    cs=EmailMultiAlternatives(subject1,msg34,form_mail,[lst[1]])
    cs.content_subtype='html'
    ms.content_subtype='html'
    cs.send()
    ms.send()
    return

def submits(request):
    try:
        if request.method=="POST":
                print("data is here")
                en= Enquery()
                en.name=request.POST.get("name")
                en.email=request.POST.get("email")
                en.massage=request.POST.get('msg')
               


                #profile=request.FILES['profile']
                #en= Information(
                    #name= m_name,
                    #designation= m_desigination,
                    #qualification= m_qulification,
                    #experiance= m_experiance,
                    #expetarea= m_expertarea,
                    #email= m_email,
                    #mob= m_mob)
                en.save()
                l=[en.name,en.email,en.massage,]
                s_mail(l)
                return redirect('/')
    except Exception as e:
        return redirect('/')
