
# REMProxy -  HTTP/S Static Proxy Server

REMProxy is a HTTP/S static webpage proxy server implemented in python. To use it you can go to <br>
**[13.95.108.154](http://13.95.108.154/)**
## Installation
There are few steps you need to do before running REMProxy.
 1. You need Python3 in your server. Also you need some additional libraries: <br>
**django, django-crispy_forms, pywebcopy, pillow** <br>
You can install libraries using the following command:
	>pip3 install django django-crispy_forms pywebcopy pillow
2. You need to open both HTTP(80) and HTTPS(443) ports on your server. 
3. You need to add your server's ip address to the allowed hosts in the **website/rem_proxy/settings.py line:28**
	>ALLOWED_HOSTS = ['13.95.108.154']
4. You might need to change WEBSITE_LOCATION variable in **website/pages/proxy.py line:9** to match your **pywebcopy** download directory
	>WEBPAGE_LOCATION = "/home/remproxy/website/static/temp"
------
## Running the Server
Once you installed all the required packages go into website directory and run the following command <br>
>sudo python3 manage.py runserver 0.0.0.0:80 <br>

If you are running the server for the first time you might need to run the following command once only <br>
>python3 manage.py migrate
------
![Screenshot of Page](https://github.com/ekremcet/ProxyServer/blob/master/img/screenshot.PNG?raw=true "Hey")
