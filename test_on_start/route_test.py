import requests
import time
class Route_test():
    def __init__(self):
        self.service_key="liwest 834ffa3f5329897243e0436041f060f75e8f226e"
        self.auth_routes = [
            '/login',
            '/logout',
            '/whoami',
            '/create',
            '/gettoken',
        ]
        self.test_api_routes = [
            '/products',
            '/product-categories',
            'product-groups',
        ]

    def request_route(self, route):
        try:
            resp = str(requests.get(f'http://127.0.0.1:8000/api-v1{route}', headers={"Authorization":self.service_key}).status_code)
            if resp == "200":
                resp = ("\033[1m\033[34m\033[42m"+"route to:"+route+"has code:"+resp+"\033[0m")
            elif resp =="404":
                resp = ("\033[1m\033[34m\033[43m"+"route to:"+route+"has code:"+resp+"\033[0m")
            else:
                resp = ("\033[1m\033[34m\033[41m"+"route to:"+route+"has code:"+resp+"\033[0m")
        except Exception as exp:
            resp = ("\033[041m"+'error: ' + str(exp)[:69]+"\033[0m")
        return resp
    
    def get_report(self):
        time.sleep(20)
        #auth_routes_test
        for i in range(len(self.auth_routes)):
            print(self.request_route(self.auth_routes[i]))
        #test_api_routes
        for i in range(len(self.test_api_routes)):
            print(self.request_route(self.test_api_routes[i]))

resp = Route_test().get_report()