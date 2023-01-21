from io import BytesIO
from django.http import HttpResponse
from django.template.loader import get_template
from xhtml2pdf import pisa


def renderPdf(template, content={}):
    t=get_template(template)
    send_data=t.render(content)
    result=BytesIO()
    pdf=pisa.CreatePDF(BytesIO(send_data.encode("UTF-8")),dest=result,path = 'C:/Users/preec/Downloads/BookShop (2)/BookShop/order/__dummy__')
    if not pdf.err:
        return HttpResponse(result.getvalue(),content_type='application/pdf')
    else:
        return None