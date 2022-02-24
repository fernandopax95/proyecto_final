'''
from weasyprint import HTML
from django.conf import settings
settings.configure()
#from refugio.wsgi import *


def printReport():
    template = get_template("base-pdf.html")
    context = {'name': 'William'}
    html_template = template.render(context)
    HTML(string = html_template).write_pdf(target = "reporteMascotas.pdf")

printReport()'''

from django.template.loader import get_template
from xhtml2pdf import pisa
from io import BytesIO
from django.http import HttpResponse

def render_to_pdf(template_src, context_dict={}):
    template = get_template(template_src)
    html = template.render(context_dict)
    result = BytesIO()
    pdf = pisa.pisaDocument(BytesIO(html.encode("ISO-8859-1")), result)
    if not pdf.err:
        return HttpResponse(result.getvalue(),content_type="application/pdf")
    return None