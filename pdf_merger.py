import PyPDF2
import sys

inputs = sys.argv[1:]

def pdf_combiner(pdf_list:list):
    merger = PyPDF2.PdfMerger()
    
    for pdf in pdf_list:
        with open(f'./PDF/{pdf}', 'rb') as file:
            merger.append(file)
            
    merger.write('./PDF/super.pdf')
            
        
pdf_combiner(inputs)
