from octorest import OctoRest


def make_client():
    try:
        client = make_client("http://192.168.2.106:5000/","C627D33B0D7B4AA9AAC46DB6ECC85FF2") 
        return client
    except Exception as e:
        print(e)

def get_version():
    client = make_client()
    message = "You are using OctoPrint v" + client.version['server'] + "\n"
    return message

def get_printer_info():
    try:
        client = make_client("http://192.168.2.106:5000/","C627D33B0D7B4AA9AAC46DB6ECC85FF2") 
        message = ""
        message += str(client.version) + "\n"
        message += str(client.job_info()) + "\n"
        printing = client.printer()['state']['flags']['printing']
        if printing:
            message += "Currently printing!\n"
        else:
            message += "Not currently printing...\n"
        return message
    except Exception as e:
        print(e)

def _prepend_local(self, location):
    if location.split('/')[0] not in ('local', 'sdcard'):
        return 'local/' + location
    return location

def files(self, location=None, recursive=False):
    payload = {'recursive': str(recursive).lower()}
    if location:
        location = self._prepend_local(location)
        return self._get('/api/files/{}'.format(location), params=payload)
    return self._get('/api/files', params=payload)

def main():
    c = make_client()
    for k in c.files()['files']:
        print(k['name'])

if __name__ == "__main__":
    main()