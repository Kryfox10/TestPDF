# Create your views here.

# from reportlab.pdfgen import canvas
# from django.http import HttpResponse

# def some_view(request):
#     # Create the HttpResponse object with the appropriate PDF headers.
#     response = HttpResponse(content_type='application/pdf')
#     response['Content-Disposition'] = 'attachment; filename="somefilename.pdf"'

#     # Create the PDF object, using the response object as its "file."
#     p = canvas.Canvas(response)

#     # Draw things on the PDF. Here's where the PDF generation happens.
#     # See the ReportLab documentation for the full list of functionality.
#     p.drawString(100, 100, "Hello world.")

#     # Close the PDF object cleanly, and we're done.
#     p.showPage()
#     p.save()
#     return response

# from io import BytesIO
# from reportlab.pdfgen import canvas
# from django.http import HttpResponse

# def some_view(request):
#     # Create the HttpResponse object with the appropriate PDF headers.
#     response = HttpResponse(content_type='application/pdf')
#     response['Content-Disposition'] = 'attachment; filename="somefilename.pdf"'

#     buffer = BytesIO()

#     # Create the PDF object, using the BytesIO object as its "file."
#     p = canvas.Canvas(buffer)

#     # Draw things on the PDF. Here's where the PDF generation happens.
#     # See the ReportLab documentation for the full list of functionality.
#     p.drawString(100, 100, "Hello world.")

#     # Close the PDF object cleanly.
#     p.showPage()
#     p.save()

#     # Get the value of the BytesIO buffer and write it to the response.
#     pdf = buffer.getvalue()
#     buffer.close()
#     response.write(pdf)
#     return response
import cStringIO as StringIO
from xhtml2pdf import pisa
from django.template.loader import get_template
from django.template import Context
from django.http import HttpResponse
from generatepdf.models import Syllia
from cgi import escape

def render_to_pdf(source, context_dict):
    template = get_template(source)
    context = Context(context_dict)
    html  = template.render(context)
    result = StringIO.StringIO()

    pdf = pisa.pisaDocument(StringIO.StringIO(html.encode("ISO-8859-1")), result)
    if not pdf.err:
        response = HttpResponse(result.getvalue(), mimetype='application/pdf')
        response['Content-Disposition'] = 'filename=Syllia.pdf'
        return response
    return HttpResponse('We had some errors<pre>%s</pre>' % escape(html))

def myview(request):
    #Retrieve data or whatever you need
    syl = Syllia.objects.get(id=1)
    college = syl.college
    course_code = syl.course_code
    instructor = syl.instructor
    return render_to_pdf(
            'syllabustemplate.html',
            {
                'pagesize':'A4',
                'college': college,
                'course_code': course_code,
                'instructor': instructor,
            }
        )
