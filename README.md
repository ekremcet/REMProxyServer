# ProxyServer
A basic proxy server that can handle both HTTP and HTTPS requests

To use it go to 
3.120.225.225 

------
# Installation
First you need to install Python3 on your server. Then you need the following python packages <br>
>pip3 install django <br>
>pip3 install django-crispy_forms <br>
>pip3 install pywebcopy <br>
>pip3 install pillow <br> 
Then you need to add your server's ip address to the allowed hosts in the rem_proxy/settings.py <br>
>ALLOWED_HOSTS = ['13.95.108.154'] <br>
Also you might need to change WEBSITE_LOCATION variable in proxy.py to match your directory <br>
>WEBSITE_LOCATION = 'home/remproxy/pages/temp'
------
# Running the Server
Once you installed all the required packages go into website directory and run the following command <br>
>python3 manage.py runserver 0.0.0.0:80 <br>
If you are running the server for the first time you might need to run the following command once only <br>
>python3 manage.py migrate

------

![Screenshot of Page](https://github.com/ekremcet/ProxyServer/blob/master/img/screenshot.PNG?raw=true "Hey")
