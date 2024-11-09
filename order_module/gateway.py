# import requests

# class Zibal:

#     def request(self, amount, order_id, mobile, description=None, multiplexingInfos=None):
#         data = {
#             'merchant': 'zibal',
#             'callbackUrl': 'http://127.0.0.1:8000/zibal/verify-payment/',
#             'amount': amount,
#             'orderId': order_id,
#             'mobile': mobile,
#             'description': description,
#             'multiplexingInfos': multiplexingInfos
#         }

#         response = self.post_to('request', data)
#         return response

#     def verify(self, trackId):
#         data = {
#             'merchant': self.merchant,
#             'trackId': trackId
#         }
#         return self.post_to('verify', data)

#     def post_to(self, path, parameters):
#         url = "https://gateway.zibal.ir/v1/" + path
#         response = requests.post(url=url, json=parameters)
#         return response.json()