from django.shortcuts import get_object_or_404, redirect
from django.http import HttpResponse
from django.contrib.auth.decorators import login_required
from order_module.models import OrderBasket,OrderSubmittedAddress
from zibal_payment.client import ZibalClient
from zibal_payment.exceptions import ZibalError
from zibal_payment.client import ZibalClient


# https://help.zibal.ir/article/44
# https://pypi.org/project/zibal-payment/
# https://github.com/Mohammad222PR/zibal-payment/blob/main/examples/payment_example_request.py
# https://help.zibal.ir/IPG/API/#authentication

@login_required
def send_request(request):
    try:
        current_basket,is_created=OrderBasket.objects.prefetch_related('order_detail').get_or_create(is_paid=False,user_id=request.user.id)
        fullname=request.POST['full_name']
        address=request.POST['user_address']
        zip_code=request.POST['zipcode']
        city=request.POST['city']
        country=request.POST['country']

        if request.user.id == current_basket.user.id:
            new_paying_info,is_created_submitter_address=OrderSubmittedAddress.objects.get_or_create(order_basket_id=current_basket.id,user_id=request.user.id,fullname=fullname,address=address,zip_code=zip_code,city=city,country=country)
            new_paying_info.save()
        else:
            return HttpResponse('user of basket and user that is paying not match!!')

        # zibal
        client = ZibalClient(merchant_id="zibal",sandbox=True,enable_logging=True)

        # Step 1: Create a payment request
        print('step 1')
        response = client.payment_request(
            amount=1000,
            callback_url="bahmanpournazari.pythonanywhere.com/zibal/verify-payment/",
            description="Test Payment"
        )
        track_id = response.get("trackId")
        
        print('_'*85)
        # Step 2: Generate the payment URL
        print('step 2')
        payment_url = client.generate_payment_url(track_id)
        print(f"Direct user to this URL for payment: {payment_url}")
        print('_'*85)

        # Step 3: After payment, verify the transaction
        print('step 3')
        verification = client.payment_verify(track_id)
        print("Payment verification details:", verification)
        print('_'*85)


    except ZibalError as e:
        print(f"An error occurred: {e}")
    
    finally:
        return redirect(payment_url)

@login_required
def verify_payment(request):
    try:    
        merchant_id = "zibal"
        client = ZibalClient(merchant_id)
        track_id=request.GET.get('trackId')
        current_basket=get_object_or_404(OrderBasket,is_paid=False,user_id=request.user.id)
        current_basket.is_paid=True
        from datetime import datetime
        current_basket.payment_date=datetime.now()

        response = client.payment_verify(track_id)
        print(f"Verification response: {response}")
        message='success'
        print(message)
        current_basket.save()
        return redirect('confirm-checkout')
    
    except ZibalError as e:
        print(f"Error: {e}")
        message='error'
        print(message)
        return redirect('products')
    
