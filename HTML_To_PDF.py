import pdfkit


url = 'https://wkhtmltopdf.org/'

options = {
    'page-size': 'A4',
    'margin-top': '0.75in',
    'margin-right': '0.75in',
    'margin-bottom': '0.75in',
    'margin-left': '0.75in',
    'encoding': "UTF-8",
    'custom-header': [
        ('Accept-Encoding', 'gzip')
    ],
    'no-outline': None
}

pdfkit.from_url(url, 'out.pdf', options=options, verbose=True)
