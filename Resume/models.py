from xml.dom import ValidationErr
from django.db import models
from django.core.validators import MaxValueValidator,MinValueValidator

GENDER_CHOICES = [
 ('Male', 'Male'),
 ('Female', 'Female')
]

JOB_CITY_CHOICE = [
 ('Delhi', 'Delhi'),
 ('Gurgaon','Gurgaon'),
 ('Noida','Noida'),
 ('Banglore', 'Banglore'),
 ('Pune', 'Pune'),
 ('Ranchi', 'Ranchi'),
 ('Mumbai', 'Mumbai'),
 ('Dhanbad', 'Dhanbad'),
  ('Bihar', 'Bihar')
]

STATE_CHOICE = (
 ('Andaman & Nicobar Islands','Andaman & Nicobar Islands'),
 ('Andhra Pradesh','Andhra Pradesh'),
 ('Arunachal Pradesh','Arunachal Pradesh'),
 ('Assam','Assam'),
 ('Bihar','Bihar'),
 ('Chandigarh','Chandigarh'),
 ('Chhattisgarh','Chhattisgarh'),
 ('Dadra & Nagar Haveli','Dadra & Nagar Haveli'),
 ('Daman and Diu','Daman and Diu'),
 ('Delhi','Delhi'),
 ('Goa','Goa'),
 ('Gujarat','Gujarat'),
 ('Haryana','Haryana'),
 ('Himachal Pradesh','Himachal Pradesh'),
 ('Jammu & Kashmir','Jammu & Kashmir'),
 ('Jharkhand','Jharkhand'),
 ('Karnataka','Karnataka'),
 ('Kerala','Kerala'),
 ('Lakshadweep','Lakshadweep'),
 ('Madhya Pradesh','Madhya Pradesh'),
 ('Maharashtra','Maharashtra'),
 ('Manipur','Manipur'),
 ('Meghalaya','Meghalaya'),
 ('Mizoram','Mizoram'),
 ('Nagaland','Nagaland'),
 ('Odisha','Odisha'),
 ('Puducherry','Puducherry'),
 ('Punjab','Punjab'),
 ('Rajasthan','Rajasthan'),
 ('Sikkim','Sikkim'),
 ('Tamil Nadu','Tamil Nadu'),
 ('Telangana','Telangana'),
 ('Tripura','Tripura'),
 ('Uttarakhand','Uttarakhand'),
 ('Uttar Pradesh','Uttar Pradesh'),
 ('West Bengal','West Bengal'),
)


class ResumeModel(models.Model):
 name = models.CharField(max_length=100)
 email = models.EmailField()
 dob = models.DateField(auto_now=False, auto_now_add=False)
 gender = models.CharField(choices=GENDER_CHOICES,max_length=50)
 locality = models.CharField(max_length=100)
 city = models.CharField(choices=JOB_CITY_CHOICE,max_length=100)
 pin = models.PositiveIntegerField() #validators=[MaxValueValidator(6),MinValueValidator(6)]
 mobile = models.PositiveIntegerField()
 state = models.CharField(choices=STATE_CHOICE, max_length=50)
 job_city = models.CharField(max_length=50)
 profile_image = models.ImageField(upload_to='profileimg', blank=True)
 my_file = models.FileField(upload_to='doc', blank=True)

 def __str__(self):
    return "%s %s " %(self.name,self.email)