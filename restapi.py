import http.client
from korbit.close import Close

class RestApi():
    def __init__(self, host):
        self.conn = http.client.HTTPSConnection(host, 443)

    @Close
    def request(self, api, method, payload=None, headers=None):
        if headers is None:
            headers = {}
            
        self.conn.request(method.value, api, payload, headers)    
        res = self.conn.getresponse()
        print(dir(res))
        data = res.read()
        return data.decode('utf-8')

    def close(self):
        self.conn.close()
