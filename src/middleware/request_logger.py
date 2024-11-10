import socket
import time
import json

class RequestLogMiddleware():
    def __init__(self, get_response):
        self.get_response = get_response

    
    def __call__(self, request):
        self.start_time = time.time()
        response = self.get_response(request)
        self.process_response(request,response)
        return response
    
    def process_response(self, request, response):
        data = {
            "user_id": request.user.pk,
            "request_method": request.method,
            "request_path": request.get_full_path(),
            "response_status": response.status_code,
            "remote_address": request.META["REMOTE_ADDR"],
            "server_hostname": socket.gethostname(),
            "run_time": time.time() - self.start_time
        }

