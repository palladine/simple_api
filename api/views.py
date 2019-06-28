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

        try:
            resp, par = getattr(methods, name_method)(data)
        except Exception:
            return JsonResponse(self.form_error(702))

        # проверка на ошибки в методах
        if 'code' in resp:
            return JsonResponse(self.form_error(resp.get('code')))

        return JsonResponse(self.form_data(resp, par))


    def form_error(self, code):
        return {'status': 0, 'code': code, 'error': get_error_by_code(code)}

    def form_data(self, data, par):
        return {'status': 1, 'count': par.get('count'), 'data': data}
