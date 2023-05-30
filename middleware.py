'''

def my_middleware(get_response):

    def my_function(reqquest):

        print("Code to be executes before view function is called")

        res=get_response(request):

        print("Code to be executed after view function is called")

        return res
        
    return my_function    
    '''

class MyMiddleware:

    def __init__(self,get_response):
        self.get_response=get_response

    def __call__(self,reqquest):
        print("Code to be executed before view called-class Based Middleware")
        res=self.get_response(request)
        print("Code to be executed after view called-class Based Middleware")

        return res           