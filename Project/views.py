import json
from django.http import HttpResponse
from django.http.response import JsonResponse
from rest_framework.decorators import api_view
'''
HEADER
======
content_type="application/json"

URLs
====
http://127.0.0.1:8000/home/add/
http://127.0.0.1:8000/home/sub/
http://127.0.0.1:8000/home/mul/
http://127.0.0.1:8000/home/div/
http://127.0.0.1:8000/home/pow/
http://127.0.0.1:8000/home/fact/

REQUEST BODY
============
JSON_BODY = {
    "x": 5,
    "y": 5
}
'''

List_of_operation = ['add', 'sub','mul']

@api_view(['GET', 'PUT', 'DELETE'])
def mathOpe(req, oper):
    if req.method == 'GET':
        data = json.loads(req.body)
        if oper == 'add' and oper in List_of_operation:
            add = int(data['x']) + int(data['y'])
            return JsonResponse({'Addition Result': add})
        if oper == 'sub' and oper in List_of_operation:
            add = int(data['x']) - int(data['y'])
            return JsonResponse({'Subtraction Result': add})
        if oper == 'mul' and oper in List_of_operation:
            add = int(data['x']) * int(data['y'])
            return JsonResponse({'Multiplication Result': add})
        if oper == 'div' and oper in List_of_operation:
            add = int(data['x']) / int(data['y'])
            return JsonResponse({'Division Result': add})
        if oper == 'pow' and oper in List_of_operation:
            add = int(data['x']) ** int(data['y'])
            return JsonResponse({'Power Result': add})
        if oper == 'fact' and oper in List_of_operation:
            x = lambda num: 1 if num <= 1 else num * x(num - 1)
            return JsonResponse({'Factorial Result': x(int(data['x']))})
        else:
            data = json.dumps({'Choose Proper operation from given List': List_of_operation})
            return HttpResponse(data, content_type="application/json", status=300)

    if req.method == 'PUT':
        if oper in List_of_operation:
            data = json.dumps({'Operator is available in List, Choose other Operator': List_of_operation})
            return HttpResponse(data, content_type="application/json", status=300)
        else:
            List_of_operation.append(oper)
            data = json.dumps({'Operator is added in List': List_of_operation})
            return HttpResponse(data, content_type="application/json", status=200)

    if req.method == 'DELETE':
        if oper in List_of_operation:
            List_of_operation.remove(oper)
            data = json.dumps({'Operator is deleted from the List': List_of_operation})
            return HttpResponse(data, content_type="application/json", status=200)
        else:
            data = json.dumps({'Operator is not available in the List, Choose other Operator': List_of_operation})
            return HttpResponse(data, content_type="application/json", status=300)


