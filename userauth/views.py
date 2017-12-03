from django.shortcuts import render,redirect
from userauth.models import UserInfo
# Create your views here.
def log_in(request):

    if request.method=="POST":
        username=request.POST['user']
        password=request.POST['pwd']

        user=UserInfo.objects.filter(username=username,password=password)

        if user:
            #设置session内部的字典内容
            request.session['is_login']='true'
            request.session['username']=username

            #登录成功就将url重定向到后台的url
            return redirect('/backend/')

    #登录不成功或第一访问就停留在登录页面
    return render(request,'login.html')
def backend(request):
    print(request.session,"------cookie")
    print(request.COOKIES,'-------session')
    """
    这里必须用读取字典的get()方法把is_login的value缺省设置为False，
    当用户访问backend这个url先尝试获取这个浏览器对应的session中的
    is_login的值。如果对方登录成功的话，在login里就已经把is_login
    的值修改为了True,反之这个值就是False的
    """

    is_login=request.session.get('is_login',False)
    #如果为真，就说明用户是正常登陆的
    if is_login:
        #获取字典的内容并传入页面文件
        cookie_content=request.COOKIES
        session_content=request.session

        username=request.session['username']

        return render(request,'backend.html',locals())
    else:
        """
        如果访问的时候没有携带正确的session，
        就直接被重定向url回login页面
        """
        return redirect('/login/')

def log_out(request):
    """
    直接通过request.session['is_login']回去返回的时候，
    如果is_login对应的value值不存在会导致程序异常。所以
    需要做异常处理
    """
    try:
        #删除is_login对应的value值
        del request.session['is_login']

        # OR---->request.session.flush() # 删除django-session表中的对应一行记录

    except KeyError:
        pass
    #点击注销之后，直接重定向回登录页面
    return redirect('/login/')