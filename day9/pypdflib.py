from PyPDF2 import PdfReader
from PyPDF2 import PdfMerger
import os
reader= PdfReader(r"C:\Users\Gautam G\OneDrive\Desktop\_Java_Module 5.pdf")        
print(len (reader.pages))
merger=PdfMerger()
merger.append(r"C:\Users\Gautam G\OneDrive\Desktop\_Java_Module 5.pdf")
merger.append(r"C:\Users\Gautam G\OneDrive\Desktop\MODULE-3 (1) (2).pdf")
merger.write("merged.pdf")
merger.close()