from django.db import models

class login(models.Model):
    username=models.CharField(max_length=200)
    password=models.CharField(max_length=200)
    usertype=models.CharField(max_length=200)

class hostelowner(models.Model):
    name=models.CharField(max_length=200)
    email=models.CharField(max_length=200)
    phone=models.CharField(max_length=200)
    place=models.CharField(max_length=200)
    pin=models.CharField(max_length=200)
    post=models.CharField(max_length=200)
    LOGIN=models.ForeignKey(login,default=1,on_delete=models.CASCADE)

class user(models.Model):
    name=models.CharField(max_length=200)
    age=models.CharField(max_length=200)
    email=models.CharField(max_length=200)
    phone=models.CharField(max_length=200)
    image=models.CharField(max_length=200)
    place=models.CharField(max_length=200)
    adhar=models.CharField(max_length=200)
    parent_name=models.CharField(max_length=200,default=1)
    parent_contact=models.CharField(max_length=200,default=1)
    parent_email=models.CharField(max_length=200,default=1)
    LOGIN=models.ForeignKey(login,default=1,on_delete=models.CASCADE)

class hostel(models.Model):
    name=models.CharField(max_length=200)
    image=models.CharField(max_length=200)
    latitude=models.CharField(max_length=200)
    longitude=models.CharField(max_length=200)
    phone=models.CharField(max_length=200)
    email=models.CharField(max_length=200)
    HOSTEL_OWNER=models.ForeignKey(hostelowner,default=1,on_delete=models.CASCADE)

class rating(models.Model):
    rating=models.CharField(max_length=200)
    date=models.CharField(max_length=200)
    review=models.CharField(max_length=200)
    USER=models.ForeignKey(user,default=1,on_delete=models.CASCADE)
    HOSTEL=models.ForeignKey(hostel,default=1,on_delete=models.CASCADE)

class feedback(models.Model):
    date=models.CharField(max_length=200)
    feedbackk=models.CharField(max_length=200)
    LOGIN=models.ForeignKey(login,default=1,on_delete=models.CASCADE)

class complaint(models.Model):
    date=models.CharField(max_length=200)
    complaintt=models.CharField(max_length=200)
    reply=models.CharField(max_length=200)
    reply_date=models.CharField(max_length=200)
    USER=models.ForeignKey(user,default=1,on_delete=models.CASCADE)

class room(models.Model):
    Room_no=models.CharField(max_length=200)
    floor=models.CharField(max_length=200)
    vaccancy=models.CharField(max_length=200)
    image=models.CharField(max_length=200,default=1)
    amount=models.CharField(max_length=200)
    type=models.CharField(max_length=200,default=1)
    HOSTEL=models.ForeignKey(hostel,default=1,on_delete=models.CASCADE)

class food(models.Model):
    name=models.CharField(max_length=200)
    image=models.CharField(max_length=200,default=1)

class room_request(models.Model):
    date=models.CharField(max_length=200)
    status=models.CharField(max_length=200)
    ROOM=models.ForeignKey(room,default=1,on_delete=models.CASCADE)
    USER=models.ForeignKey(user,default=1,on_delete=models.CASCADE)

class notifications(models.Model):
    notification=models.CharField(max_length=200)
    date=models.CharField(max_length=200)
    HOSTEL_OWNER=models.ForeignKey(hostelowner,default=1,on_delete=models.CASCADE)

class food_status(models.Model):
    date=models.CharField(max_length=200)
    reason=models.CharField(max_length=200)
    ROOM_REQUEST=models.ForeignKey(room_request,default=1,on_delete=models.CASCADE)

class payment(models.Model):
    pay_date=models.CharField(max_length=200)
    month_year=models.CharField(max_length=200)
    amount=models.CharField(max_length=200)
    status=models.CharField(max_length=200)
    fine_note=models.CharField(max_length=200)
    ROOM_REQUEST=models.ForeignKey(room_request,default=1,on_delete=models.CASCADE)

class laundry(models.Model):
    date=models.CharField(max_length=200)
    time=models.CharField(max_length=200)
    HOSTEL=models.ForeignKey(hostel,default=1,on_delete=models.CASCADE)

class chat(models.Model):
    type=models.CharField(max_length=200)
    date=models.CharField(max_length=200,default=1)
    message=models.CharField(max_length=200,default=1)
    USER=models.ForeignKey(user,default=1,on_delete=models.CASCADE)
    HOSTELOWNER=models.ForeignKey(hostelowner,default=1,on_delete=models.CASCADE)

