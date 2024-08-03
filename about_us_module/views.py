from django.shortcuts import render
from django.views import View
from django.http import HttpResponse
# --2
# import io
# from django.http import FileResponse
# from reportlab.pdfgen import canvas

# # --3
# from django.conf import settings
# from easy_pdf.views import PDFTemplateView

class AboutUsView(View):
    template_name='about_us_module/about_us.html'
    
    def get(self,request):
        return render(request,self.template_name)
    
def download_shop_pdf(request):
    pdf_url='/static/show_pdf.pdf'
    content=f'<embed src="{pdf_url}" width="500" height="375" type="application/pdf">'
    return HttpResponse(content)
    

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
    
    
