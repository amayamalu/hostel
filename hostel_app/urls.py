"""Hostel_management URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path

from hostel_app import views

urlpatterns = [
    # path('admin/', admin.site.urls),
    path('',views.index),
    path('admin_home',views.admin_home),
    path('login_post',views.login_post),
    path('view_requested_hostelowner',views.view_requested_hostelowner),
    path('approve_request/<id>',views.approve_request),
    path('reject_request/<id>',views.reject_request),
    path('view_approved_hostelowner',views.view_approved_hostelowner),
    path('view_user',views.view_user),
    path('view_feedback',views.view_feedback),
    path('view_rating',views.view_rating),
    path('view_comaplint',views.view_comaplint),
    path('send_reply/<id>',views.send_reply),
    path('send_reply_post/<id>',views.send_reply_post),
    path('admin_index',views.admin_index),

    ####################################################################

    path('hostelowner_home',views.hostelowner_home),
    path('hostel_owner_index',views.hostel_owner_index),
    path('register_hostelowner',views.register_hostelowner),
    path('register_hostelowner_post',views.register_hostelowner_post),
    path('add_hostel',views.add_hostel),
    path('add_hostel_post',views.add_hostel_post),
    path('view_hostel',views.view_hostel),
    path('update_hostel/<id>',views.update_hostel),
    path('update_hostel_post/<id>',views.update_hostel_post),
    path('delete_hostel/<id>',views.delete_hostel),
    path('add_room/<id>',views.add_room),
    path('add_room_post/<id>',views.add_room_post),
    path('view_room/<id>',views.view_room),
    path('update_room/<id>',views.update_room),
    path('update_room_post/<id>',views.update_room_post),
    path('delete_room/<id>',views.delete_room),
    path('add_food',views.add_food),
    path('add_food_post',views.add_food_post),
    path('view_food',views.view_food),
    path('update_food/<id>',views.update_food),
    path('update_food_post/<id>',views.update_food_post),
    path('delete_food/<id>',views.delete_food),
    path('view_room_request',views.view_room_request),
    path('approve_room/<id>',views.approve_room),
    path('reject_room/<id>',views.reject_room),
    path('view_approved_room',views.view_approved_room),
    path('add_notification',views.add_notification),
    path('add_notification_post',views.add_notification_post),
    path('view_notification',views.view_notification),
    path('delete_notification/<id>',views.delete_notification),
    path('send_feedback',views.send_feedback),
    path('send_feedback_post',views.send_feedback_post),
    path('change_password',views.change_password),
    path('change_password_post',views.change_password_post),
    path('view_rating_review/<id>',views.view_rating_review),
    path('add_laundry/<id>',views.add_laundry),
    path('add_laundry_post/<id>',views.add_laundry_post),
    path('view_laundry/<id>',views.view_laundry),
    path('update_laundry/<id>',views.update_laundry),
    path('update_laundry_post/<id>',views.update_laundry_post),
    path('add_payment/<id>',views.add_payment),
    path('add_payment_post/<id>',views.add_payment_post),
    path('view_payment/<id>',views.view_payment),
    path('update_payment/<id>',views.update_payment),
    path('update_payment_post/<id>', views.update_payment_post),
    path('set_as_paid/<id>',views.set_as_paid),
    path('view_updated_food_status',views.view_updated_food_status),
    path('update_vaccant_room/<id>',views.update_vaccant_room),
    path('send_mail/<id>',views.send_mail),
    path('send_mail_post/<id>',views.send_mail_post),
    path('chat_user/<id>',views.chat_user),
    path('chatsnd/<u>',views.chatsnd),
    path('chatrply',views.chatrply),
    path('logout',views.logout),

    #########################################################################################
    path('login_user',views.login_user),
    path('register_user',views.register_user),
    path('view_verified_hospital_owner',views.view_verified_hospital_owner),
    path('view_hostels',views.view_hostels),
    path('view_rooms',views.view_rooms),
    path('book_rooms',views.book_rooms),
    path('view_booking_status',views.view_booking_status),
    path('send_rating',views.send_rating),
    path('view_rating_user',views.view_rating_user),
    path('send_feedbackk',views.send_feedbackk),
    path('send_Complaint',views.send_Complaint),
    path('view_reply',views.view_reply),
    path('view_notifications',views.view_notifications),
    path('view_payment_status',views.view_payment_status),
    path('food_status_updation',views.food_status_updation),
    path('view_laundryy',views.view_laundryy),
    path('change_passwordd',views.change_passwordd),
    path('delete_booking_request',views.delete_booking_request),
    path('and_chat_user',views.and_chat_user),
    path('and_chatsnd',views.and_chatsnd),




]
