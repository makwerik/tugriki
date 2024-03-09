from django.shortcuts import render


# Create your views here.
def converter(request):
    if request.POST:
        amount = request.POST.get('converter')
        result = float(amount) * 1337

    data = {
        'amount': amount,
        'result': result
    }
    return render(request, 'main/converter.html', data)
