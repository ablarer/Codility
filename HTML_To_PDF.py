import pdfkit


url = 'https://wkhtmltopdf.org/'

options = {
    'page-size': 'A4'
}

pdfkit.from_url(url, 'out.pdf', options=options, verbose=True)
