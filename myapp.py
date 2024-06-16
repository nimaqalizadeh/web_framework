from webob import Request, Response

class API:
    def __init__(self):
        self.routes = {}

    def __call__(self, environ, start_response):
        request = Request(environ)
        response = self.handle_request(request)
        return response(environ, start_response)
    
    def handle_request(self, request):
        for path, handler in self.routes.items():
            if path == request.path:
                response = handler(request)
                return response
        response = self.default_response(request)
        return response
        
    def default_response(self, request):
        response = Response()
        response.status_code = 404
        response.text = "Page Not Found"
        return response
    
    def route(self, path):
        def wrapper(handler):
            self.routes[path] = handler
            return handler
        return wrapper

    
app = API()

@app.route("/")
def index(req):
    response = Response()
    response.text = "Hi, from Index Page"
    return response

@app.route("/about")
def about(req):
    response = Response()
    response.text = "Hi, from About Page"
    return response