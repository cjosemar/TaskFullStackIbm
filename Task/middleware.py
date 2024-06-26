from django.shortcuts import render


class ExceptionHandlingMiddleware:
    def __init__(self, get_response):
        self.get_response = get_response

    def __call__(self, request):
        response = self.get_response(request)
        return response

    def process_exception(self, request, exception):
        # Log the exception here
        print(f"Exception caught: {exception}")
        return render(request, 'error.html', {'message': exception})
