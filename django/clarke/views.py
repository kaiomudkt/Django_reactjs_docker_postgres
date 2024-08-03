from django.http import JsonResponse

def teste(request):
    if request.method == 'GET':
        teste1 = {
            'id': 1,
            'mensagem': 'Olá Mundo!'
        }
        return JsonResponse(teste1)
