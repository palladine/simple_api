from django.shortcuts import render
from django.http import JsonResponse
from django.views.generic import View
from django.views.decorators.csrf import csrf_exempt
from django.utils.decorators import method_decorator
import json
from api.errors import get_error_by_code
from api import methods


class RespInfo(View):
    @method_decorator(csrf_exempt)
    def dispatch(self, request):
        if request.method == 'POST':
            return self.post(request)
        else:
            return JsonResponse(self.form_error(701))

    def post(self, request):
        name_method = json.loads(request.body).get('method')
        data = json.loads(request.body).get('data')
        if not name_method:
            return JsonResponse(self.form_error(711))

        return JsonResponse(self.form_data(getattr(methods, name_method)(data)))


    def form_error(self, code):
        return {'status': 0, 'code': code, 'error': get_error_by_code(code)}

    def form_data(self, data):
        return {'status': 1, 'data': data}
