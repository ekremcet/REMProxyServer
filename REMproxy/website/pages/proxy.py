import pywebcopy
import os
import sys
import subprocess
import time
from PIL import Image

DOWNLOAD_LOCATION = "./static"
WEBPAGE_LOCATION = "/home/remproxy/website/static/temp"
PROJECT_NAME = "temp"

class RequestProxy:
    def make_request(self, url):
        # Save all the content in the webpage
        pywebcopy.config.setup_config(project_url=url, project_folder=DOWNLOAD_LOCATION, project_name=PROJECT_NAME)
        pywebcopy.config["zip_project_folder"] = False
        pywebcopy.config["PARSER"] = "html.parser"  # They claim this is faster
        pywebcopy.save_webpage(project_url=url, project_folder=DOWNLOAD_LOCATION)


    def get_folder_size(self):
        return subprocess.check_output(['du','-sk', WEBPAGE_LOCATION]).split()[0].decode('utf-8')
        
    def compress_image(self, img_file):
        try:
            picture = Image.open(img_file)
            isPNG = False if img_file.endswith(tuple([".jpg", ".jpeg"])) else True
            if isPNG:
                if len(picture.getbands()) == 3:  # Make sure PNG is not transparent
                    picture = picture.convert("RGB")
                else:  # Do not compress if image is RGBA
                    return

            picture.save(img_file, "JPEG", optimize=True, quality=70)
        except OSError as e:
            return
    
    def compress_folder(self):
        st = time.time()
        oldsize = self.get_folder_size()
        for dirpath, dirnames, filenames in os.walk(WEBPAGE_LOCATION):
            for filename in [f for f in filenames if f.endswith(tuple([".jpg", ".jpeg", ".png"]))]:
                self.compress_image(os.path.join(dirpath, filename))
        newsize = self.get_folder_size()
        et = time.time()
        print("Time Passed: " + str(et - st))
        print("Compressed from {} to {} \n".format(oldsize, newsize))

        return str(int(oldsize) - int(newsize))
        
    def return_html(self):
        size = self.get_folder_size()
        for dirpath, dirnames, filenames in os.walk("."):
            for filename in [f for f in filenames if f.endswith(".html") and "_log" not in f and not f[0].isdigit()]:
                html_path = DOWNLOAD_LOCATION + os.path.join(dirpath, filename)[1:]

                return html_path, size

    @staticmethod
    def clear_folder():
        # Clear the folder so that new website can be downloaded
        subprocess.call('rm -rf ' + WEBPAGE_LOCATION, shell=True)
 
def request(request_url, compress=True):
    proxy = RequestProxy()
    try:
       proxy.clear_folder()
    except OSError as oe:
       print("Cannot delete path: {}".format(str(oe)))
       pass
    proxy.make_request(url=request_url)
    compressed_kb = 0
    if compress:
        compressed_kb = proxy.compress_folder()
    file_path, folder_size = proxy.return_html()
    file_path = file_path.replace("static", "static/{}".format(PROJECT_NAME))
        
    return file_path, folder_size, compressed_kb
    
