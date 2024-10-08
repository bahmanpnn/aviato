from django.shortcuts import render
from django.views import View
from django.http import HttpResponse
from site_setting_module.models import SiteSetting


class AboutUsView(View):
    template_name='about_us_module/about_us.html'
    
    def get(self,request):
        site_settings=SiteSetting.objects.filter(is_main_setting=True).first()

        return render(request,self.template_name,{
            'site_settings':site_settings
        })
    



# --2
# import io
# from django.http import FileResponse
# from reportlab.pdfgen import canvas

# def some_view(request):
#     # Create a file-like buffer to receive PDF data.
#     buffer = io.BytesIO()

#     # Create the PDF object, using the buffer as its "file."
#     p = canvas.Canvas(buffer)

#     # Draw things on the PDF. Here's where the PDF generation happens.
#     # See the ReportLab documentation for the full list of functionality.
#     p.drawString(100, 100, "Hello world.")

#     # Close the PDF object cleanly, and we're done.
#     p.showPage()
#     p.save()

#     # FileResponse sets the Content-Disposition header so that browsers
#     # present the option to save the file.
#     buffer.seek(0)
#     return FileResponse(buffer, as_attachment=True, filename="hello.pdf")


# # --3
# from django.conf import settings
# from easy_pdf.views import PDFTemplateView
# pip install django-easy-pdf WeasyPrint
# class ShowPDFView(PDFTemplateView):
#     template_name = 'about_us_module/show_pdf.html'

#     base_url = 'file://' + settings.STATIC_ROOT
#     download_filename = 'show_pdf.pdf'

#     def get_context_data(self, **kwargs):
#         return super(ShowPDFView, self).get_context_data(
#             pagesize='A4',
#             title='Hi there!',
#             **kwargs
#         )
    
    

''' way4
    from django.http import FileResponse
    import os

    def pdf_view(request):
        pdf_path=os.path.join('static','show_pdf.pdf')
        
        return FileResponse(open(pdf_path,'rb'),content_type='application/pdf')


    def show_pdf_view(request):
        return render(request,'about_us_module/pdf_template.html')
'''