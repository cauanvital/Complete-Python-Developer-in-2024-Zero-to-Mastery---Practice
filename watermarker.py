import PyPDF2

template = PyPDF2.PdfReader(open('./PDF/super.pdf', 'rb'))
watermark = PyPDF2.PdfReader(open('./PDF/wtr.pdf', 'rb')).pages[0]
writer = PyPDF2.PdfWriter()

for page in template.pages:
    page.merge_page(watermark)
    writer.add_page(page)
    
writer.write('./PDF/super_wtr.pdf')
