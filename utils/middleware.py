from django.http import HttpResponseRedirect, HttpResponse
from django.urls import  reverse
from django.utils.deprecation import MiddlewareMixin

from user.models import User


class BlogMiddleware(MiddlewareMixin):
    def process_request(self, request):
        print('test1 process request')
        path = request.path
        if path == '/user/login/':
            return None

        try:
            user_id = request.session['user_id']
            user = User.objects.get(pk=user_id)
            request.user = user
            return None
        except Exception as e:
            return HttpResponseRedirect(reverse('user:login'))


    def process_view(self, request, view_func, view_args, view_kwargs):
        print('test1 view')

    def process_response(self, request, response):
        print('test1 process response')
        return response