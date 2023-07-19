from contextlib import contextmanager
from octorest import OctoRest

def make_client(url, apikey):
    try:
        client = make_client("http://192.168.2.106:5000/","C627D33B0D7B4AA9AAC46DB6ECC85FF2") 
        return client
    except Exception as e:
        print(e)

def _prepend_local(self, location):
    if location.split('/')[0] not in ('local', 'sdcard'):
        return 'local/' + location
    return location

@contextmanager
def _file_tuple(self, file):

    mime = 'application/octet-stream'

    try:
        exists = os.path.exists(file)
    except:
        exists = False

    if exists:
        filename = os.path.basename(file)
        with open(file, 'rb') as f:
            yield (filename, f, mime)
    else:
        yield file + (mime,)


def upload(self, file, *, location='local',
               select=False, print=False, userdata=None, path=None):
        """Upload file or create folder
        http://docs.octoprint.org/en/master/api/files.html#upload-file-or-create-folder

        Upload a given file
        It can be a path or a tuple with a filename and a file-like object
        """
        with self._file_tuple(file) as file_tuple:
            files = {'file': file_tuple, 'select': (None, select), 'print': (None, print)}
            if userdata:
                files['userdata'] = (None, userdata)
            if path:
                files['path'] = (None, path)

            return self._post('/api/files/{}'.format(location),
                              files=files)

def select(self, location, *, print=False):
        """Issue a file command
        http://docs.octoprint.org/en/master/api/files.html#issue-a-file-command

        Selects a file for printing

        Location is target/filename, defaults to local/filename
        If print is True, the selected file starts to print immediately
        """
        location = self._prepend_local(location)
        data = {
            'command': 'select',
            'print': print,
        }
        self._post('/api/files/{}'.format(location), json=data, ret=False)


def tri():
    message = ""
    client = make_client("http://192.168.2.106:5000/","C627D33B0D7B4AA9AAC46DB6ECC85FF2") 
    filename = tuple(["CE3E3V2_Heart_Keychain.gcode"])
    upload(client, filename)
    select(client)
    if select:
        message += "ja\n"
    else:
        message += "nein\n"

def main():
    t = tri()
    print(t)

if __name__ == "__main__":
    main()
