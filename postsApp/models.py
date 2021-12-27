from django.db import models
from django.conf import settings


class Post(models.Model):
    postedOn=models.DateTimeField(auto_created=True,auto_now_add=True)
    username=models.CharField(null=True,blank=True,max_length=60)
    location=models.CharField(null=True,blank=True,max_length=60)
    caption=models.TextField(null=True,blank=True)
    logo=models.ImageField(upload_to='media',null=True,blank=True)
    image=models.ImageField(upload_to='media',null=True,blank=True)
    isLiked=models.BooleanField(null=True,default=False)
    isSaved=models.BooleanField(null=True,default=False)
    likes=models.IntegerField(null=True,blank=True,default=0)

    def __str__(self) -> str:
        return str(self.username)+"<-->"+str(self.id)+"<-->"+str(self.postedOn)

class Comment(models.Model):
    post=models.ForeignKey(Post,related_name='comment',on_delete=models.CASCADE)
    user= models.CharField(null=True,blank=True,max_length=200)
    msg= models.TextField(null=True,blank=True)
    logo=models.ImageField(upload_to='media',null=True,blank=True)
    commentedOn=models.DateTimeField(auto_created=True,auto_now_add=True)

    def __str__(self) -> str:
        return str(self.user)+"<-->"+str(self.id)

class Test(models.Model):
    field1=models.TextField(null=True,blank=True,max_length=200)
    field2=models.TextField(null=True,blank=True,max_length=200)

    def __str__(self) -> str:
        return str(self.field1)+"<-->"+str(self.field2)

class Demo(models.Model):
    test=models.ForeignKey(Test,related_name='demo',on_delete=models.CASCADE)
    demo1=models.TextField(null=True,blank=True,max_length=200)
    demo2=models.TextField(null=True,blank=True,max_length=200)

    def __str__(self) -> str:
        return str(self.demo1)+"<-->"+str(self.demo2)

class ImageTest(models.Model):
    sample1=models.ImageField(null=True,blank=True,upload_to="media/test")
    sample2=models.FileField(null=True,blank=True,upload_to="media/test")
    # sample3=models.FilePathField(null=True,blank=True)

    def __str__(self):
        return str(self.sample1)

'''
sample data of post
    username: 'starletnova',
    location: 'chennai',
    caption:
    'Tag that competitive programmer😂\n.\n©: LinkedIn il suttathu\n.\n.\n.\n.\n.\n.\n.\n.\n.\n.\n#maranacoder #css #frontend #backend #code #infosys #itdood #itmemes #tcs #google #Infosys #ithunammapage #c #java #tamil #mokkapostu #leetcode #competitiveprogramming #codechef #hackerrank #code #officememes #office #tamil #itteam #itdood #tamilmemes #google #coder #hoodie #interview #linkedin',
    logo: 'image1.jpg',
    image: 'image2.jpg',
    isLiked: false,
    isSaved: false,
    likes: 100,
    comment: [{ user: 'username', msg: 'comment' }],
'''