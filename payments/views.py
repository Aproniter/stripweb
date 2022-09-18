import stripe

from django.conf import settings
from django.http.response import JsonResponse
from django.views.decorators.csrf import csrf_exempt
from django.shortcuts import render
from django.shortcuts import get_object_or_404

from .models import Item, Order


def home_page(request):
    items = Item.objects.all()
    order = Order.objects.filter(payer=request.user).first()
    return render(request,'payments/home.html', context={'items': items, 'order': order})


def item_page(request, id):
    item = get_object_or_404(
        Item,
        id=id
    )
    order = Order.objects.filter(payer=request.user).first()
    in_order = order in item.order.all()
    return render(
        request, 'payments/item.html',
        context={'item': item, 'order': order, 'in_order': in_order}
    )


def add_to_cart(request, id):
    item = get_object_or_404(
        Item,
        id=id
    )
    order, _ = Order.objects.get_or_create(
        payer=request.user
    )
    order.items.add(item)
    return JsonResponse({'item_add_to_cart': item.name})


def del_from_cart(request, id):
    item = get_object_or_404(
        Item,
        id=id
    )
    order = get_object_or_404(
        Order,
        payer=request.user
    )
    order.items.remove(item)
    return JsonResponse({'item_del_from_cart': item.name})


def success_page(request):
    return render(request,'payments/success.html')


def cancelled_page(request):
    return render(request,'payments/cancelled.html')


@csrf_exempt
def stripe_config(request):
    if request.method == 'GET':
        stripe_config = {'publicKey': settings.STRIPE_PUBLISHABLE_KEY}
        return JsonResponse(stripe_config, safe=False)


@csrf_exempt
def create_checkout_session(request, id):
    if request.method == 'GET':
        order = request.GET.get('order')
        domain_url = 'http://localhost/'
        stripe.api_key = settings.STRIPE_SECRET_KEY
        if order:
            items = get_object_or_404(
                Order,
                payer=request.user
            ).items.all()
        else:
            items = Item.objects.filter(id=id)
        try:
            checkout_session = stripe.checkout.Session.create(
                payment_method_types=['card'],
                line_items=[
                    {
                        'price_data': {
                            'currency': item.currency,
                            'unit_amount': item.price * 100, # Добавляем цене 2 разряда для Strip API 
                            'product_data': {
                                'name': item.name,
                                'description': item.description,
                            },
                        },
                        'quantity': 1,
                    } for item in items
                ],
                mode='payment',
                success_url=domain_url + 'success?session_id={CHECKOUT_SESSION_ID}',
                cancel_url=domain_url + 'cancelled/'
            )
            return JsonResponse({'sessionId': checkout_session['id']})
        except Exception as e:
            return JsonResponse({'error': str(e)})