import requests

class APIClient:
    def __init__(self, base_url,headers = None,token = None):
        self.base_url = base_url.rstrip("/")
        self.session = requests.Session()
        self.session.headers.update({"Accept":"application/json"})
        if headers:
            self.session.headers.update(headers)

        if token:
            self.session.headers.update({"Authorization":f"Bearer {token}"})


    def get(self, endpoint, params=None):
        return self.session.get(f"{self.base_url}/{endpoint.lstrip('/')}",
                                params=params,timeout=15)

    def post(self,endpoint,payload):
        return self.session.post(f"{self.base_url}/{endpoint.lstrip('/')}",
                                 json=payload,timeout=15)

    def put(self,endpoint,payload):
        return self.session.put(f"{self.base_url}/{endpoint.lstrip('/')}",
                                json=payload,timeout=15)
    def patch(self,endpoint,payload):
        return self.session.patch(f"{self.base_url}/{endpoint.lstrip('/')}",
                                  json=payload,timeout=15)
    def delete(self,endpoint):
        return self.session.delete(f"{self.base_url}/{endpoint.lstrip('/')}",
                                   timeout=15)
    
    