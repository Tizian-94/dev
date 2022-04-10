def createOrder(request):

    context = {}
    return render(request, 'accounts/order_form.html', context)