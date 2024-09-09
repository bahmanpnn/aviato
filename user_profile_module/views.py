from django.shortcuts import render
from django.views import View


class UserProfileView(View):
    template_name='user_profile_module/dashboard.html'
    
    def get(self,request):
        return render(request,self.template_name)

    def post(self,request):
        pass


class UserCompletedOrders(View):
    template_name='user_profile_module/orders.html'
    
    def get(self,request):
        return render(request,self.template_name)

    def post(self,request):
        pass


class UserProfileDetail(View):
    template_name='user_profile_module/profile_details.html'
    
    def get(self,request):
        return render(request,self.template_name)

    def post(self,request):
        pass


class UserAddress(View):
    template_name='user_profile_module/address.html'
    
    def get(self,request):
        return render(request,self.template_name)

    def post(self,request):
        pass