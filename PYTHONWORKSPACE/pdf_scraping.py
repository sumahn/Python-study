import camelot

file = 'sample2.pdf'

tables = camelot.read_pdf(file)
print("Total tables extracted: ", tables.n)