from contextlib import contextmanager
from tokenize import String
import os
import subprocess
from octorest import OctoRest, WorkflowAppKeyRequestResult
from urllib import parse as urlparse
import uvicorn
from fastapi import FastAPI
import time


def make_client(url, apikey):
   try:
       client = OctoRest(url=url, apikey=apikey)
       return client
   except ConnectionError as ex:
       # Handle exception as you wish
       print(ex)

    

def file_names(client):
   message = "The GCODE files currently on the printer are:\n\n"
   for k in client.files()['files']:
       message += k['name'] + "\n"
   return message


def start(self):
    data = {'command': 'start'}
    self._post('/api/job', json=data, ret=False)


def restart(self):
   data = {'command': 'restart'}
   self._post('/api/job', json=data, ret=False)


def _post(self, path, data=None, files=None, json=None, ret=True):
   url = urlparse.urljoin(self.url, path)
   response = self.session.post(url, data=data, files=files, json=json)
   self._check_response(response)

   if ret:
       return response.json()


def select(self, location, *, print=False):
   location = self._prepend_local(location)
   data = {
       'command': 'select',
       'print': print,
   }
   self._post('/api/files/{}'.format(location), json=data, ret=False)


def get_printer_info():
   while True:
       try:
           client = OctoRest(url="http://localhost:5000/?#temp", apikey="C627D33B0D7B4AA9AAC46DB6ECC85FF2")
           message = ""
           message += str(client.version) + "\n"
           message += str(client.job_info()) + "\n"
           printing = client.printer()['state']['flags']['printing']
           
           if printing:
               message += "Currently printing!\n"
               time.sleep(100)
           else:
               message += "Not currently printing...\n"
               break
           
           return message
       
       except Exception as e:
           print(e)


def shark():
   message = ""
   client = make_client("http://localhost:5000/?#temp", "C627D33B0D7B4AA9AAC46DB6ECC85FF2")
   select(client, 'local/hai.gcode')
   start(client)
   if start:
       message += "ja\n"
   else:
       message += "nein\n"
   return message


def octopus():
   message = ""
   client = make_client("http://localhost:5000/?#temp", "C627D33B0D7B4AA9AAC46DB6ECC85FF2")
   select(client, 'local/octopus.gcode')
   start(client)
   if start:
       message += "ja\n"
   else:
       message += "nein\n"
   return message


def whale():
   message = ""
   client = make_client("http://localhost:5000/?#temp", "C627D33B0D7B4AA9AAC46DB6ECC85FF2")
   select(client, 'local/wal.gcode')
   start(client)
   if start:

       message += "ja\n"
   else:
       message += "nein\n"
   return message


def crab():
   message = ""
   client = make_client("http://localhost:5000/?#temp", "C627D33B0D7B4AA9AAC46DB6ECC85FF2")
   select(client, 'local/krabbe.gcode')
   start(client)
   if start:

       message += "ja\n"
   else:
       message += "nein\n"
   return message


def dolphin():
   message = ""
   client = make_client("http://localhost:5000/?#temp", "C627D33B0D7B4AA9AAC46DB6ECC85FF2")
   select(client, 'local/delfin.gcode')
   start(client)
   if start:

       message += "ja\n"
   else:
       message += "nein\n"
   return message


app = FastAPI()


@app.get('/print/{animal}')
def main(animal: str): 
   print(animal)

   if animal == 'shark':
       get_printer_info()
       shark()
   elif animal == 'whale':
       get_printer_info()
       whale()
   elif animal == 'octopus':
       get_printer_info()
       octopus()
   elif animal == 'dolphin':
       get_printer_info()
       dolphin()
   elif animal == 'crab':
       get_printer_info()
       crab()




"""
def main():  
   animal = shark()
   print(animal)
"""

if __name__ == "__main__":
   main()
