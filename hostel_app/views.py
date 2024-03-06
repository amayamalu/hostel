import datetime
import email
import smtplib
from email.mime.text import MIMEText

from django.core.files.storage import FileSystemStorage
from django.http import HttpResponse, JsonResponse
from django.shortcuts import render, redirect

from hostel_app.models import *

def index(request):
    return render(request,"index.html")

def admin_index(request):
    return render(request,"admin/admin_index.html")

def admin_home(request):
    return render(request,"admin/admin_home.html")

def loginform(request):
    return render(request,"login.html")

def login_post(request):
    uname=request.POST['textfield']
    pswd=request.POST['textfield2']
    data=login.objects.filter(username=uname,password=pswd)
    print(data,"f")
    if data.exists():
        data=data[0]
        request.session['lid']=data.id
        request.session['log']='lo'
        if data.usertype=="admin":
            return redirect('/admin_index')
        elif data.usertype=="hostelowner":
            # return redirect('/hostelowner_home')
            return redirect('/hostel_owner_index')
    return HttpResponse("ok")

def view_requested_hostelowner(request):
    if request.session['log']!='lo':
        return HttpResponse("<script>alert('logout succesfully');window.location='/'</script>")
    res=hostelowner.objects.filter(LOGIN__usertype="pending")
    return render(request,"admin/view_hostelowner_requests.html",{"data":res})

def approve_request(request,id):
    if request.session['log']!='lo':
        return HttpResponse("<script>alert('logout succesfully');window.location='/'</script>")
    login.objects.filter(id=id).update(usertype="hostelowner")
    return HttpResponse("<script>alert('approved');window.location='/view_requested_hostelowner'</script>")

def reject_request(request,id):
    if request.session['log']!='lo':
        return HttpResponse("<script>alert('logout succesfully');window.location='/'</script>")
    login.objects.filter(id=id).update(usertype="rejected")
    return HttpResponse("<script>alert('rejected');window.location='/view_requested_hostelowner'</script>")


def view_approved_hostelowner(request):
    if request.session['log']!='lo':
        return HttpResponse("<script>alert('logout succesfully');window.location='/'</script>")
    res=hostelowner.objects.filter(LOGIN__usertype="hostelowner")
    return render(request,"admin/view_approved_hostelowner.html",{'data':res})

def view_user(request):
    if request.session['log']!='lo':
        return HttpResponse("<script>alert('logout succesfully');window.location='/'</script>")
    res=user.objects.all()
    return render(request,"admin/view_user.html",{"data":res})

def view_feedback(request):
    if request.session['log']!='lo':
        return HttpResponse("<script>alert('logout succesfully');window.location='/'</script>")
    res=feedback.objects.all()
    return render(request,"admin/view_feedback.html",{'data':res})

def view_rating(request):
    if request.session['log']!='lo':
        return HttpResponse("<script>alert('logout succesfully');window.location='/'</script>")
    res=rating.objects.all()
    return render(request,"admin/view_rating.html",{"data":res})


def view_comaplint(request):
    if request.session['log']!='lo':
        return HttpResponse("<script>alert('logout succesfully');window.location='/'</script>")
    res=complaint.objects.all()
    return render(request,"admin/view_complaint.html",{"data":res})

def send_reply(request,id):
    if request.session['log']!='lo':
        return HttpResponse("<script>alert('logout succesfully');window.location='/'</script>")
    id=id
    return render(request,"admin/send_reply.html",{"id":id})

def send_reply_post(request,id):
    reply=request.POST['textfield']
    date=datetime.datetime.now().strftime("%Y/%m/%d")
    complaint.objects.filter(id=id).update(reply=reply,reply_date=date)
    return HttpResponse("<script>alert('Replied');window.location='/view_comaplint'</script>")

#################################################################################################################################################

def hostel_owner_index(request):
    return render(request,"hostel_owner/Hostelowner_index.html")


def hostelowner_home(request):
    return render(request,"hostel_owner/hostelowner_home.html")

def register_hostelowner(request):
    return render(request,"hostel_owner/register_hostelowner.html")

def register_hostelowner_post(request):
    name=request.POST['textfield']
    email=request.POST['textfield2']
    phone=request.POST['textfield3']
    post=request.POST['textfield4']
    pin=request.POST['textfield5']
    place=request.POST['textfield6']
    password=request.POST['textfield7']
    i=hostelowner.objects.filter(email=email)
    if i.exists():
        return HttpResponse("<script>alert('already registered email');window.location='/'</script>")
    else:
        obj = login()
        obj.username = email
        obj.password = password
        obj.usertype = "pending"
        obj.save()

        obj1 = hostelowner()
        obj1.name = name
        obj1.email = email
        obj1.phone = phone
        obj1.place = place
        obj1.post = post
        obj1.pin = pin
        obj1.LOGIN = obj
        obj1.save()
        return HttpResponse("<script>alert('registered');window.location='/'</script>")


def add_hostel(request):
    if request.session['log']!='lo':
        return HttpResponse("<script>alert('logout succesfully');window.location='/'</script>")
    return render(request,"hostel_owner/add_hostel.html")

def add_hostel_post(request):
    hid=hostelowner.objects.get(LOGIN=request.session['lid'])
    nm=request.POST['textfield']
    email=request.POST['textfield2']
    phone=request.POST['textfield3']
    latitude=request.POST['textfield4']
    longitude=request.POST['textfield5']
    image=request.FILES['fileField']
    d=datetime.datetime.now().strftime("%Y/%m/%d-%H%M%S")
    fs=FileSystemStorage()
    fs.save(r"C:\Users\amaya\PycharmProjects\Hostel_management\hostel_app\static\image\\"+d+'.jpg',image)
    path="/static/image/"+d+'.jpg'
    i=hostel.objects.filter(name=nm,email=email)
    if i.exists():
        return HttpResponse("<script>alert('Added');window.location='/add_hostel'</script>")
    else:
        obj = hostel()
        obj.name = nm
        obj.email = email
        obj.phone = phone
        obj.image = path
        obj.latitude = latitude
        obj.longitude = longitude
        obj.HOSTEL_OWNER_id=hid.id
        obj.save()
        return HttpResponse("<script>alert('Added');window.location='/add_hostel'</script>")

def view_hostel(request):
    if request.session['log']!='lo':
        return HttpResponse("<script>alert('logout succesfully');window.location='/'</script>")
    res=hostel.objects.filter(HOSTEL_OWNER__LOGIN=request.session['lid'])
    return render(request,"hostel_owner/view_hostel.html",{"data":res})

def update_hostel(request,id):
    if request.session['log']!='lo':
        return HttpResponse("<script>alert('logout succesfully');window.location='/'</script>")
    res=hostel.objects.get(id=id)
    return render(request,"hostel_owner/update_hostel.html",{"data":res})

def update_hostel_post(request,id):
    try:
        nm = request.POST['textfield']
        email = request.POST['textfield2']
        phone = request.POST['textfield3']
        latitude = request.POST['textfield4']
        longitude = request.POST['textfield5']
        image = request.FILES['fileField']
        d = datetime.datetime.now().strftime("%Y/%m/%d-%H%M%S")
        fs = FileSystemStorage()
        fs.save(r"C:\Users\amaya\PycharmProjects\Hostel_management\hostel_app\static\image\\" + d + '.jpg', image)
        path = "/static/image/" + d + '.jpg'
        hostel.objects.filter(id=id).update(name=nm,email=email,phone=phone,latitude=latitude,longitude=longitude,image=path)
        return HttpResponse("<script>alert('updated');window.location='/view_hostel'</script>")
    except Exception as e:
        nm = request.POST['textfield']
        email = request.POST['textfield2']
        phone = request.POST['textfield3']
        latitude = request.POST['textfield4']
        longitude = request.POST['textfield5']
        hostel.objects.filter(id=id).update(name=nm,email=email,phone=phone,latitude=latitude,longitude=longitude)
        return HttpResponse("<script>alert('updated');window.location='/view_hostel'</script>")

def delete_hostel(request,id):
    if request.session['log']!='lo':
        return HttpResponse("<script>alert('logout succesfully');window.location='/'</script>")
    hostel.objects.filter(id=id).delete()
    return HttpResponse("<script>alert('deleted');window.location='/view_hostel'</script>")


def add_room(request,id):
    if request.session['log']!='lo':
        return HttpResponse("<script>alert('logout succesfully');window.location='/'</script>")
    return render(request,"hostel_owner/add_room.html",{"id":id})

def add_room_post(request,id):
    type=request.POST['textfield5']
    rm_no=request.POST['textfield4']
    vaccancy=request.POST['textfield3']
    amount=request.POST['textfield2']
    floor=request.POST['textfield']
    image=request.FILES['fileField']
    d = datetime.datetime.now().strftime("%Y/%m/%d-%H%M%S")
    fs = FileSystemStorage()
    fs.save(r"C:\Users\amaya\PycharmProjects\Hostel_management\hostel_app\static\image\\" + d + '.jpg', image)
    path = "/static/image/" + d + '.jpg'
    i=room.objects.filter(type=type,Room_no=rm_no,floor=floor)
    if i.exists():
        return HttpResponse("<script>alert('added');window.location='/view_room'</script>")
    else:
        obj = room()
        obj.Room_no = rm_no
        obj.vaccancy = vaccancy
        obj.amount = amount
        obj.floor = floor
        obj.image = path
        obj.type = type
        obj.HOSTEL_id=id
        obj.save()
        return HttpResponse("<script>alert('added');window.location='/view_room'</script>")


def view_room(request,id):
    if request.session['log']!='lo':
        return HttpResponse("<script>alert('logout succesfully');window.location='/'</script>")
    res=room.objects.filter(HOSTEL_id=id)
    print(res)
    return render(request,"hostel_owner/view_room.html",{"data":res})

def update_room(request,id):
    if request.session['log']!='lo':
        return HttpResponse("<script>alert('logout succesfully');window.location='/'</script>")
    res=room.objects.get(id=id)
    return render(request,"hostel_owner/update_room.html",{"data":res})

def update_room_post(request,id):
    try:
        type = request.POST['textfield5']
        rm_no = request.POST['textfield4']
        vaccancy = request.POST['textfield3']
        amount = request.POST['textfield2']
        floor = request.POST['textfield']
        image = request.FILES['fileField']
        d = datetime.datetime.now().strftime("%Y/%m/%d-%H%M%S")
        fs = FileSystemStorage()
        fs.save(r"C:\Users\amaya\PycharmProjects\Hostel_management\hostel_app\static\image\\" + d + '.jpg', image)
        path = "/static/image/" + d + '.jpg'
        room.objects.filter(id=id).update(type=type,Room_no=rm_no,vaccancy=vaccancy,amount=amount,floor=floor,image=path)
        return HttpResponse("<script>alert('updated');window.location='/view_room'</script>")
    except Exception as e:
        type = request.POST['textfield5']
        rm_no = request.POST['textfield4']
        vaccancy = request.POST['textfield3']
        amount = request.POST['textfield2']
        floor = request.POST['textfield']
        room.objects.filter(id=id).update(type=type, Room_no=rm_no, vaccancy=vaccancy, amount=amount, floor=floor)
        return HttpResponse("<script>alert('updated');window.location='/view_room'</script>")

def delete_room(request,id):
    if request.session['log']!='lo':
        return HttpResponse("<script>alert('logout succesfully');window.location='/'</script>")
    room.objects.filter(id=id).delete()
    return HttpResponse("<script>alert('deleted');window.location='/hostel_owner_index'</script>")



def add_food(request):
    if request.session['log']!='lo':
        return HttpResponse("<script>alert('logout succesfully');window.location='/'</script>")
    return render(request,"hostel_owner/add_food.html")

def add_food_post(request):
    name=request.POST['textfield']
    image=request.FILES['fileField']
    d = datetime.datetime.now().strftime("%Y/%m/%d-%H%M%S")
    fs = FileSystemStorage()
    fs.save(r"C:\Users\amaya\PycharmProjects\Hostel_management\hostel_app\static\image\\" + d + '.jpg', image)
    path = "/static/image/" + d + '.jpg'
    i=food.objects.filter(name=name)
    if i.exists():
        return HttpResponse("<script>alert('added');window.location='/view_food'</script>")
    else:
        obj = food()
        obj.name = name
        obj.image = path
        obj.save()
        return HttpResponse("<script>alert('added');window.location='/view_food'</script>")


def view_food(request):
    if request.session['log']!='lo':
        return HttpResponse("<script>alert('logout succesfully');window.location='/'</script>")
    res=food.objects.all()
    return render(request,"hostel_owner/view_food.html",{"data":res})

def update_food(request,id):
    if request.session['log']!='lo':
        return HttpResponse("<script>alert('logout succesfully');window.location='/'</script>")
    res=food.objects.get(id=id)
    return render(request,"hostel_owner/update_food.html",{"data":res})

def update_food_post(request,id):
    try:
        name = request.POST['textfield']
        image = request.FILES['fileField']
        d = datetime.datetime.now().strftime("%Y/%m/%d-%H%M%S")
        fs = FileSystemStorage()
        fs.save(r"C:\Users\amaya\PycharmProjects\Hostel_management\hostel_app\static\image\\" + d + '.jpg', image)
        path = "/static/image/" + d + '.jpg'
        food.objects.filter(id=id).update(name=name,image=path)
        return HttpResponse("<script>alert('updated');window.location='/view_food'</script>")

    except Exception as E:
        name = request.POST['textfield']
        food.objects.filter(id=id).update(name=name)
        return HttpResponse("<script>alert('updated');window.location='/view_food'</script>")



def delete_food(request,id):
    if request.session['log']!='lo':
        return HttpResponse("<script>alert('logout succesfully');window.location='/'</script>")
    food.objects.filter(id=id).delete()
    return HttpResponse("<script>alert('deleted');window.location='/view_food'</script>")


def view_room_request(request):
    if request.session['log']!='lo':
        return HttpResponse("<script>alert('logout succesfully');window.location='/'</script>")
    res=room_request.objects.filter(status="pending")
    return render(request,"hostel_owner/view_room_request.html",{"data":res})

def approve_room(request,id):
    if request.session['log']!='lo':
        return HttpResponse("<script>alert('logout succesfully');window.location='/'</script>")
    room_request.objects.filter(id=id).update(status="approved")
    return HttpResponse("<script>alert('approved');window.location='/view_room_request'</script>")

def reject_room(request,id):
    if request.session['log']!='lo':
        return HttpResponse("<script>alert('logout succesfully');window.location='/'</script>")
    room_request.objects.filter(id=id).update(status="rejected")
    return HttpResponse("<script>alert('rejected');window.location='/view_room_request'</script>")

def view_approved_room(request):
    if request.session['log']!='lo':
        return HttpResponse("<script>alert('logout succesfully');window.location='/'</script>")
    res=room_request.objects.filter(status="approved")
    return render(request,"hostel_owner/view_approved_room_requests.html",{"data":res})

def add_notification(request):
    if request.session['log']!='lo':
        return HttpResponse("<script>alert('logout succesfully');window.location='/'</script>")
    return render(request,"hostel_owner/add_notification.html")

def add_notification_post(request):
    hid=hostelowner.objects.get(LOGIN=request.session['lid'])
    noti=request.POST['textfield']
    datee=datetime.datetime.now().strftime("%Y/%m%d-%H%M%S")
    obj=notifications()
    obj.notification=noti
    obj.date=datee
    obj.HOSTEL_OWNER_id=hid
    obj.save()
    return HttpResponse("<script>alert('added');window.location='/add_notification'</script>")

def view_notification(request):
    if request.session['log']!='lo':
        return HttpResponse("<script>alert('logout succesfully');window.location='/'</script>")
    res=notifications.objects.all()
    return render(request,"hostel_owner/view_notification.html",{"data":res})

def delete_notification(request,id):
    if request.session['log']!='lo':
        return HttpResponse("<script>alert('logout succesfully');window.location='/'</script>")
    notifications.objects.filter(id=id).delete()
    return HttpResponse("<script>alert('deleted');window.location='/view_notification'</script>")

def send_feedback(request):
    if request.session['log']!='lo':
        return HttpResponse("<script>alert('logout succesfully');window.location='/'</script>")
    return render(request,"hostel_owner/send_feedback.html")

def send_feedback_post(request):
    feedb=request.POST['textfield']
    date=datetime.datetime.now().strftime("%Y/%m/%d-%H%M%S")
    i=feedback.objects.filter(LOGIN_id=request.session['lid'],feedbackk=feedb)
    if i.exists():
        return HttpResponse("<script>alert('send');window.location='/view_notification'</script>")
    else:
        obj = feedback()
        obj.feedbackk = feedb
        obj.date = date
        obj.save()
        return HttpResponse("<script>alert('send');window.location='/view_notification'</script>")


def change_password(request):
    if request.session['log']!='lo':
        return HttpResponse("<script>alert('logout succesfully');window.location='/'</script>")
    return render(request,"hostel_owner/change_password.html")

def change_password_post(request):
    curr=request.POST['textfield']
    new=request.POST['textfield2']
    confirm=request.POST['textfield3']
    data=login.objects.filter(id=request.session['lid'])
    data=data[0]
    if data.password==curr:
        if new==confirm:
            login.objects.filter(id=data.id).update(password=confirm)
            return HttpResponse("<script>alert('Changed');window.location='/view_notification'</script>")
        else:
            return HttpResponse("<script>alert('Mismatch');window.location='/view_notification'</script>")
    else:
        return HttpResponse("<script>alert('Not foud');window.location='/view_notification'</script>")


def view_rating_review(request,id):
    if request.session['log']!='lo':
        return HttpResponse("<script>alert('logout succesfully');window.location='/'</script>")
    res=rating.objects.filter(HOSTEL_id=id)
    return render(request,"hostel_owner/view_rating_review.html",{"data":res})

def add_laundry(request,id):
    if request.session['log']!='lo':
        return HttpResponse("<script>alert('logout succesfully');window.location='/'</script>")
    return render(request,"hostel_owner/add_laundry.html",{"id":id})

def add_laundry_post(request,id):
    d=request.POST['textfield']
    t=request.POST['textfield2']
    obj=laundry()
    obj.date=d
    obj.time=t
    obj.HOSTEL_id=id
    obj.save()
    return HttpResponse("<script>alert('added');window.location='/view_hostel'</script>")

def view_laundry(request,id):
    res=laundry.objects.filter(HOSTEL=id)
    return render(request,"hostel_owner/view_laundry.html",{"data":res})

def update_laundry(request,id):
    res=laundry.objects.get(id=id)
    return render(request,"hostel_owner/update_laundry.html",{"data":res})

def update_laundry_post(request,id):
    d = request.POST['textfield']
    t = request.POST['textfield2']
    laundry.objects.filter(id=id).update(date=d,time=t)
    return HttpResponse("<script>alert('updated');window.location='/view_laundry'</script>")

def add_payment(request,id):
    if request.session['log']!='lo':
        return HttpResponse("<script>alert('logout succesfully');window.location='/'</script>")
    id=id
    return render(request,"hostel_owner/add_payment.html",{"id":id})

def add_payment_post(request,id):
    pd=request.POST['textfield']
    my=request.POST['textfield2']
    statuss=request.POST['textfield3']
    Fine=request.POST['textfield4']
    Amount=request.POST['textfield5']

    obj=payment()
    obj.pay_date=pd
    obj.month_year=my
    obj.status=statuss
    obj.fine_note=Fine
    obj.t=Amount
    obj.amount= int(obj.t)+int(obj.fine_note)
    obj.ROOM_REQUEST_id=id
    obj.save()
    return HttpResponse("<script>alert('Payment Added Succesfully');window.location='/view_approved_room'</script>")

def view_payment(request,id):
    if request.session['log']!='lo':
        return HttpResponse("<script>alert('logout succesfully');window.location='/'</script>")
    res=payment.objects.filter(ROOM_REQUEST_id=id)
    print(res)
    return render(request, "hostel_owner/view_payment.html",{"data":res, "id":id})

def update_payment(request,id):
    if request.session['log']!='lo':
        return HttpResponse("<script>alert('logout succesfully');window.location='/'</script>")
    res=payment.objects.get(ROOM_REQUEST_id=id)
    return render(request,"hostel_owner/update_payment.html",{"data":res,"id":id})

def update_payment_post(request,id):
    pd = request.POST['textfield1']
    my = request.POST['textfield2']
    statuss = request.POST['textfield3']
    Fine = request.POST['textfield4']
    Amount = request.POST['textfield5']
    payment.objects.filter(ROOM_REQUEST_id=id).update(pay_date=pd,month_year=my,status=statuss,amount=Amount,fine_note=Fine)
    return HttpResponse("<script>alert('Updated');window.location='/view_approved_room'</script>")

def set_as_paid(request,id):
    payment.objects.filter(ROOM_REQUEST_id=id).update(status="paid")
    return HttpResponse("<script>alert('Updated');window.location='/view_approved_room'</script>")


def view_updated_food_status(request):
    if request.session['log']!='lo':
        return HttpResponse("<script>alert('logout succesfully');window.location='/'</script>")
    res=food_status.objects.all()
    return render(request,"hostel_owner/view_food_updation_status.html",{'data':res})

def update_vaccant_room(request,id):
    room_request.objects.filter(ROOM_id=id).update(status="vaccate")
    data=room.objects.filter(id=id)
    v=int(data[0].vaccancy)+1
    room.objects.filter(id=id).update(vaccancy=v)
    return HttpResponse("<script>alert('vaccancy updated');window.location='/view_approved_room'</script>")



def send_mail(request,id):
  return render(request,"hostel_owner/mail.html",{"id":id})

def send_mail_post(request,id):

    email = room_request.objects.get(id = id).USER.parent_email
    msg = request.POST['textarea']
    try:
        gmail = smtplib.SMTP('smtp.gmail.com', 587)

        gmail.ehlo()

        gmail.starttls()

        gmail.login('riss.amayakm@gmail.com', 'rynv kchx fddr fecs')

    except Exception as e:
        print("Couldn't setup email!!" + str(e))

    msg = MIMEText(msg)

    msg['Subject'] = 'Verification'

    msg['To'] = email

    msg['From'] = 'riss.amayakm@gmail.com'

    try:

        gmail.send_message(msg)

    except Exception as e:

        print("COULDN'T SEND EMAIL", str(e))

    return HttpResponse("Send")


def chat_user(request,id):
    request.session['uid']=id
    return render(request,"hostel_owner/chat.html",{"id":id})


def chatsnd(request,u):
      if request.method=="POST":
        # db=Db()
        d=datetime.datetime.now().strftime("%Y-%m-%d")
        t=datetime.datetime.now().strftime("%H:%M:%S")
        c = request.session['lid']
        b=request.POST['n']
        print(b)
        print(u,"userrrrrrrrrr")
        m=request.POST['m']
        cc = hostelowner.objects.get(LOGIN_id=c)
        uu = user.objects.get(id=request.session['uid'])
        obj=chat()
        obj.date=d
        obj.type='owner'
        obj.HOSTELOWNER=cc
        obj.USER=uu
        obj.message=m
        obj.save()
        return JsonResponse({"status":"ok"})



def chatrply(request):
        c = request.session['uid']
        cc=user.objects.get(id=c)
        uu=hostelowner.objects.get(LOGIN=request.session['lid'])
        res = chat.objects.filter(HOSTELOWNER=uu,USER=cc)
        v = []
        if len(res) > 0:
            print(len(res))
            for i in res:
                v.append({
                    'type':i.type,
                    'chat':i.message,
                })
            print(v)
            return JsonResponse({"status": "ok", "data": v, "id": cc.id})
        else:
            return JsonResponse({"status": "error"})



def logout(request):
    request.session['log']=""
    request.session.clear()
    return HttpResponse("<script>alert('logout successfully');window.location='/'</script>")

##########################################################################################################################################3

def login_user(request):
    uname=request.POST['username']
    pswd=request.POST['password']

    data=login.objects.filter(username=uname,password=pswd,usertype="user")
    if data.exists():
        return JsonResponse({"status":"ok","id":data[0].id})
    else:
        return JsonResponse({"status":"no"})


def register_user(request):
    name=request.POST['name']
    email=request.POST['email']
    age=request.POST['age']
    place=request.POST['place']
    phone=request.POST['phone']
    aadhar=request.POST['aadhar']
    parent_name=request.POST['parent_name']
    parent_email=request.POST['parent_email']
    parent_contact=request.POST['parent_phone']
    password=request.POST['password']
    image=request.FILES['pic']
    d=datetime.datetime.now().strftime("%Y/%m/%d-%H%M%S")
    fs=FileSystemStorage()
    fs.save(r"C:\Users\amaya\PycharmProjects\Hostel_management\hostel_app\static\images\\"+d+'.jpg',image)
    path="/static/images/"+d+'.jpg'

    obj=login()
    obj.username=email
    obj.password=password
    obj.usertype="user"
    obj.save()

    obj1=user()
    obj1.name=name
    obj1.email=email
    obj1.age=age
    obj1.phone=phone
    obj1.place=place
    obj1.adhar=aadhar
    obj1.parent_name=parent_name
    obj1.parent_contact=parent_contact
    obj1.parent_email=parent_email
    obj1.image=path
    obj1.LOGIN=obj
    obj1.save()

    return JsonResponse({"status":"ok"})



def view_verified_hospital_owner(request):
    oid=request.POST['hsid']
    res=hostelowner.objects.get(id=oid)
    return JsonResponse({'status':"ok",'name':res.name,'email':res.email,'phone':res.phone,'place':res.place,'pin':res.pin,'post':res.post})


def view_hostels(request):
    res=hostel.objects.filter(HOSTEL_OWNER__LOGIN__usertype="hostelowner")
    data = []
    for i in res:
        data.append(
            {
                'id':i.id,
                'name':i.name,
                'image':i.image,
                'latitude':i.latitude,
                'longitude':i.longitude,
                'phone':i.phone,
                'email':i.email,
                'HOSTEL_OWNER_id':i.HOSTEL_OWNER.id,
            }
        )
    return JsonResponse({"status":"ok","data":data})

def view_rooms(request):
    hid=request.POST['id']
    res=room.objects.filter(HOSTEL=hid)
    arr=[]
    for i in res:
        arr.append(
            {
                'id':i.id,
                'room_no':i.Room_no,
                'floor':i.floor,
                'vaccancy':i.vaccancy,
                'amount':i.amount,
                'type':i.type,
                'image':i.image,

            }
        )

    return JsonResponse({"status":"ok","data":arr})

def book_rooms(request):
    rid=request.POST['rid']
    lid=request.POST['lid']
    d=datetime.datetime.now().strftime("%Y/%m/%d")
    uid=user.objects.get(LOGIN_id=lid)
    obj=room_request()
    obj.date=d
    obj.status="pending"
    obj.ROOM_id=rid
    obj.USER_id=uid.id
    obj.save()
    return JsonResponse({"status":"ok"})


def send_rating(request):
    rid=request.POST['rid']
    rev=request.POST['review']
    rat=request.POST['rating']
    lid=request.POST['lid']
    uid=user.objects.get(LOGIN_id=lid)
    d=datetime.datetime.now().strftime("%Y/%m/%d")
    obj=rating()
    obj.rating=rat
    obj.review=rev
    obj.date=d
    obj.USER_id=uid.id
    obj.HOSTEL_id=room_request.objects.get(id=rid).ROOM.HOSTEL_id
    obj.save()
    return JsonResponse({"status":"ok"})

def view_rating_user(request):
    rid=request.POST['rid']
    lid=request.POST['rid']
    hid=room_request.objects.get(id=rid).ROOM.HOSTEL_id
    res=rating.objects.filter(HOSTEL_id=hid)
    data=[]
    for i in res:
        data.append(
            {
                "id":i.id,
                "date":i.date,
                "rating":i.rating,
                "review":i.review,
                "USER":i.USER.name,
            }
        )
        print(data)
    return JsonResponse({"status":"ok","data":data})


def send_feedbackk(request):
    f=request.POST['feedback']
    id=request.POST['lid']
    d=datetime.datetime.now().strftime("%Y/%m/%d")
    obj=feedback()
    obj.feedbackk=f
    obj.LOGIN_id=id
    obj.date=d
    obj.save()
    return JsonResponse({"status":"ok"})


def send_Complaint(request):
    c=request.POST['complaint']
    lid=request.POST['lid']
    uid=user.objects.get(LOGIN_id=lid)
    d=datetime.datetime.now().strftime("%Y/%m/%d")
    obj=complaint()
    obj.date=d
    obj.complaintt=c
    obj.reply="pending"
    obj.USER_id=uid.id
    obj.save()
    return JsonResponse({"status":"ok"})


def view_reply(request):
    lid = request.POST['lid']
    uid=user.objects.get(LOGIN_id=lid)
    res=complaint.objects.filter(USER=uid)
    data=[]
    for i in res:
        data.append(
            {
                "id":i.id,
                "date":i.date,
                "complaint":i.complaintt,
                "reply":i.reply,
                "reply_date":i.reply_date,
            }
        )
    return JsonResponse({"status":"ok","data":data})

def view_booking_status(request):
    lid = request.POST['lid']
    uid = user.objects.get(LOGIN=lid)
    res = room_request.objects.filter(USER=uid)
    data=[]
    for i in res:
        data.append(
            {
                'id':i.id,
                'date':i.date,
                'ROOM':i.ROOM.Room_no,
                'status':i.status
            }
        )
    return JsonResponse({"status":"ok","data":data})

def delete_booking_request(request):
    rid=request.POST['rid']
    room_request.objects.filter(id=rid).delete()
    return JsonResponse({"status":"ok"})

def view_payment_status(request):
    rid=request.POST['rid']
    res=payment.objects.get(ROOM_REQUEST=rid)
    return JsonResponse({'status':"ok",'date':res.pay_date,'month':res.month_year,'amount':res.amount,'statuss':res.status,'fine_note':res.fine_note})

def food_status_updation(request):
    rid=request.POST['rid']
    date=request.POST['date']
    reason=request.POST['reason']
    obj=food_status()
    obj.date=date
    obj.reason=reason
    obj.ROOM_REQUEST_id=rid
    obj.save()
    return JsonResponse({"status":"ok"})

def view_laundryy(request):
    uid=request.POST['lid']
    hid=room_request.objects.get(USER__LOGIN=uid,status='approved')
    res=laundry.objects.get(HOSTEL=hid.ROOM.HOSTEL.id)
    return JsonResponse({"status":"ok",'date':res.date,'time':res.time})


def view_notifications(request):
    uid = request.POST['lid']
    hid = room_request.objects.get(USER__LOGIN=uid)
    hoid=hid.ROOM.HOSTEL.HOSTEL_OWNER_id
    res=notifications.objects.filter(HOSTEL_OWNER=hoid)
    data=[]
    for i in res:
        data.append(
            {
                "id":i.id,
                "date":i.date,
                "notification":i.notification,
            }
        )
    return JsonResponse({"status":"ok","data":data})


def change_passwordd(request):
    cur=request.POST['current']
    new=request.POST['new']
    confrm=request.POST['confirm']
    id=request.POST['lid']
    data=login.objects.filter(password=cur)
    if data.exists():
        if new==confrm:
            login.objects.filter(id=id).update(password=new)
            return JsonResponse({"status":"ok"})
        else:
            return JsonResponse({"status":"no"})
    else:
        return JsonResponse({"status":"ok"})





def and_chat_user(request,id):
    request.session['uid']=id
    return render(request,"hostel_owner/chat.html",{"id":id})


def and_chatsnd(request,u):
      if request.method=="POST":
        # db=Db()
        d=datetime.datetime.now().strftime("%Y-%m-%d")
        t=datetime.datetime.now().strftime("%H:%M:%S")
        c = request.session['lid']
        b=request.POST['n']
        print(b)
        print(u,"userrrrrrrrrr")
        m=request.POST['m']
        cc = hostelowner.objects.get(LOGIN_id=c)
        uu = user.objects.get(id=request.session['uid'])
        obj=chat()
        obj.date=d
        obj.type='owner'
        obj.HOSTELOWNER=cc
        obj.USER=uu
        obj.message=m
        obj.save()
        return JsonResponse({"status":"ok"})


