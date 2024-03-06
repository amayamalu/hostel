# Generated by Django 2.0.9 on 2024-01-05 03:32

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='chat',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('type', models.CharField(max_length=200)),
                ('date', models.CharField(default=1, max_length=200)),
                ('message', models.CharField(default=1, max_length=200)),
            ],
        ),
        migrations.CreateModel(
            name='complaint',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('date', models.CharField(max_length=200)),
                ('complaintt', models.CharField(max_length=200)),
                ('reply', models.CharField(max_length=200)),
                ('reply_date', models.CharField(max_length=200)),
            ],
        ),
        migrations.CreateModel(
            name='feedback',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('date', models.CharField(max_length=200)),
                ('feedbackk', models.CharField(max_length=200)),
            ],
        ),
        migrations.CreateModel(
            name='food',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=200)),
                ('image', models.CharField(default=1, max_length=200)),
            ],
        ),
        migrations.CreateModel(
            name='food_status',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('date', models.CharField(max_length=200)),
                ('reason', models.CharField(max_length=200)),
            ],
        ),
        migrations.CreateModel(
            name='hostel',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=200)),
                ('image', models.CharField(max_length=200)),
                ('latitude', models.CharField(max_length=200)),
                ('longitude', models.CharField(max_length=200)),
                ('phone', models.CharField(max_length=200)),
                ('email', models.CharField(max_length=200)),
            ],
        ),
        migrations.CreateModel(
            name='hostelowner',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=200)),
                ('email', models.CharField(max_length=200)),
                ('phone', models.CharField(max_length=200)),
                ('place', models.CharField(max_length=200)),
                ('pin', models.CharField(max_length=200)),
                ('post', models.CharField(max_length=200)),
            ],
        ),
        migrations.CreateModel(
            name='laundry',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('date', models.CharField(max_length=200)),
                ('time', models.CharField(max_length=200)),
                ('HOSTEL_OWNER', models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, to='hostel_app.hostelowner')),
            ],
        ),
        migrations.CreateModel(
            name='login',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('username', models.CharField(max_length=200)),
                ('password', models.CharField(max_length=200)),
                ('usertype', models.CharField(max_length=200)),
            ],
        ),
        migrations.CreateModel(
            name='notifications',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('notification', models.CharField(max_length=200)),
                ('date', models.CharField(max_length=200)),
                ('HOSTEL_OWNER', models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, to='hostel_app.hostelowner')),
            ],
        ),
        migrations.CreateModel(
            name='payment',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('pay_date', models.CharField(max_length=200)),
                ('month_year', models.CharField(max_length=200)),
                ('amount', models.CharField(max_length=200)),
                ('status', models.CharField(max_length=200)),
                ('fine_note', models.CharField(max_length=200)),
            ],
        ),
        migrations.CreateModel(
            name='rating',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('rating', models.CharField(max_length=200)),
                ('date', models.CharField(max_length=200)),
                ('review', models.CharField(max_length=200)),
                ('HOSTEL', models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, to='hostel_app.hostel')),
            ],
        ),
        migrations.CreateModel(
            name='room',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Room_no', models.CharField(max_length=200)),
                ('floor', models.CharField(max_length=200)),
                ('vaccancy', models.CharField(max_length=200)),
                ('image', models.CharField(default=1, max_length=200)),
                ('amount', models.CharField(max_length=200)),
                ('type', models.CharField(default=1, max_length=200)),
                ('HOSTEL', models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, to='hostel_app.hostel')),
            ],
        ),
        migrations.CreateModel(
            name='room_request',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('date', models.CharField(max_length=200)),
                ('status', models.CharField(max_length=200)),
                ('ROOM', models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, to='hostel_app.room')),
            ],
        ),
        migrations.CreateModel(
            name='user',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=200)),
                ('age', models.CharField(max_length=200)),
                ('email', models.CharField(max_length=200)),
                ('phone', models.CharField(max_length=200)),
                ('image', models.CharField(max_length=200)),
                ('place', models.CharField(max_length=200)),
                ('adhar', models.CharField(max_length=200)),
                ('parent_name', models.CharField(default=1, max_length=200)),
                ('parent_contact', models.CharField(default=1, max_length=200)),
                ('parent_email', models.CharField(default=1, max_length=200)),
                ('LOGIN', models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, to='hostel_app.login')),
            ],
        ),
        migrations.AddField(
            model_name='room_request',
            name='USER',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, to='hostel_app.user'),
        ),
        migrations.AddField(
            model_name='rating',
            name='USER',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, to='hostel_app.user'),
        ),
        migrations.AddField(
            model_name='payment',
            name='ROOM_REQUEST',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, to='hostel_app.room_request'),
        ),
        migrations.AddField(
            model_name='laundry',
            name='ROOM_REQUEST',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, to='hostel_app.room_request'),
        ),
        migrations.AddField(
            model_name='hostelowner',
            name='LOGIN',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, to='hostel_app.login'),
        ),
        migrations.AddField(
            model_name='hostel',
            name='HOSTEL_OWNER',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, to='hostel_app.hostelowner'),
        ),
        migrations.AddField(
            model_name='food_status',
            name='ROOM_REQUEST',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, to='hostel_app.room_request'),
        ),
        migrations.AddField(
            model_name='feedback',
            name='LOGIN',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, to='hostel_app.login'),
        ),
        migrations.AddField(
            model_name='complaint',
            name='USER',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, to='hostel_app.user'),
        ),
        migrations.AddField(
            model_name='chat',
            name='HOSTELOWNER',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, to='hostel_app.hostelowner'),
        ),
        migrations.AddField(
            model_name='chat',
            name='USER',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, to='hostel_app.user'),
        ),
    ]