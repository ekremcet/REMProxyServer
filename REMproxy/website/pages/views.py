from django.views.generic import TemplateView
from django.shortcuts import render

import pages.proxy as rem
from django.views.decorators.cache import never_cache
import requests, time, datetime

from django.contrib.auth.decorators import login_required



#@login_required(login_url='/users/login')
@never_cache
def home(request):
    compress = False
    if (request.POST.get('mybtn')):
        st = time.time()
        url = request.POST.get('text_urlinput', " ")
        print("This is the url obtained from the template: {}".format(url))
        compression = request.POST.get('compression', "nocompression")
        if compression == "compression":
            print("Compression enabled!")
            compress = True
        
        if url == "":
            print("Empty input. No action.")
            return render(request, 'home.html', {"url_path": "/static/empty.html"})
        elif "http" not in url:
            url = "{}{}".format("http://", url)
        file_path, file_size, compressed = rem.request(request_url=url, compress = compress)
        file_size = round(int(file_size)/1024,3)
        print("File path: {}".format(file_path))
        et = time.time()
        elapsed = round((et-st),3)
        print("For webpage: {} it took {} seconds.".format(url, elapsed))
        return render(request, 'home.html', {"url_path": file_path[file_path.index("static")-1:], "page_url": url,
                                             "elapsed_time": elapsed, "file_size": file_size, "compressed_amount": compressed})
    else:
        return render(request, 'home.html', {"url_path": "/static/empty.html", "page_url": "",
                                             "elapsed_time": "0", "file_size": "0", "compressed_amount": "0"})




