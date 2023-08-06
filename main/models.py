from django.db import models

# Create your models here.
class Expericence(models.Model):
    job = models.CharField(max_length=200,verbose_name='Kasbi')
    working = models.CharField(max_length=200,verbose_name='Ishlagan joyi')
    date = models.CharField(max_length=9,verbose_name='Ishlagan vaqti',
                            help_text='shu ko\'rinishda kiriting: 2024-2030')
    body = models.TextField(verbose_name='Qilgan ishim',help_text='Ishda nimalar qilgansiz va qanday natijalarga erishgansiz')
    created_on = models.DateTimeField(auto_now_add=True,verbose_name='Yaratilgan vaqt')

    def __str__(self):
        return self.working

class About_me(models.Model):
    name = models.CharField(max_length=100,verbose_name='To\'liq ism:')
    job = models.CharField(max_length=50,verbose_name='Kasbi')
    body = models.TextField(verbose_name='Men haqimda:')
    degree = models.CharField(max_length=100,verbose_name='Darajas:')
    phone_number = models.CharField(max_length=9,verbose_name='Telefon nomer:')
    address = models.CharField(max_length=300,verbose_name='Manzil:')
    birthday = models.CharField(max_length=20,verbose_name='Tug\'ilgan sana:', help_text='ushbu ko\'rinishda kiriting: 01.12.2024')
    experience = models.CharField(max_length=2,verbose_name='Tajriba', help_text='Yil kiriting')
    email = models.EmailField(max_length=100,verbose_name='Elektron pochta:')
    created_on = models.DateTimeField(auto_now_add=True,verbose_name='Yaratilgan vaqt')
    image = models.ImageField(upload_to='my_image')
    social_telegram = models.CharField(max_length=400,blank=True,null=True, verbose_name='Telegram:')
    social_linkedin = models.CharField(max_length=400, blank=True, null=True, verbose_name='LinkedIn:')
    social_youtube = models.CharField(max_length=400,blank=True,null=True, verbose_name='You Tube:')
    social_instagram = models.CharField(max_length=400,blank=True,null=True, verbose_name='Instagram:')
    social_facebook = models.CharField(max_length=400,blank=True,null=True, verbose_name='Facebook:')
    github = models.CharField(max_length=400, blank=True, null=True, verbose_name='Git Hub:')

    def __str__(self):
        return self.name

class Portfolio(models.Model):
    name = models.CharField(max_length=150)
    image = models.ImageField(upload_to='portfolio-images')
    link = models.TextField()
    created_on = models.DateTimeField(auto_now_add=True,verbose_name='Yaratilgan vaqt')

    def __str__(self):
        return self.name
    

class Service(models.Model):
    title = models.CharField(max_length=150)
    body = models.CharField(max_length=500)
    created_on = models.DateTimeField(auto_now_add=True,verbose_name='Yaratilgan vaqt')

    def __str__(self):
        return self.title

class Contact(models.Model):
    name = models.CharField(max_length=100)
    email = models.EmailField(max_length=100)
    subject = models.CharField(max_length=100)
    message = models.TextField()
    created_on = models.DateTimeField(auto_now_add=True,verbose_name='Yaratilgan vaqt')

    def __str__(self):
        return self.name

class Skill(models.Model):
    title = models.CharField(max_length=100,verbose_name='Skill nomi')
    degree = models.CharField(max_length=3,verbose_name='Skillning bilish darajasi')
    created_on = models.DateTimeField(auto_now_add=True,verbose_name='Yaratilgan vaqt')

    def __str__(self):
        return self.title
    
class Testimonial(models.Model):
    name = models.CharField(max_length=50)
    body = models.CharField(max_length=150)
    job = models.CharField(max_length=50,verbose_name='Kasbi:')
    image = models.ImageField(upload_to='client-images',default='client-images/default.jpg')

    def __str__(self):
        return self.name
    