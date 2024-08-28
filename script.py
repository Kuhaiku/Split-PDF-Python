import os
from PyPDF2 import PdfReader, PdfWriter

def split_pdf(file_path, max_size_mb=10):
    # Captura o nome base do arquivo (sem extensão)
    base_name = os.path.splitext(os.path.basename(file_path))[0]
    
    # Define a pasta de destino baseada no nome do arquivo
    destination_folder = os.path.join("./PDF-Destin", base_name)
    
    # Verifica se a pasta de destino existe, se não, cria
    if not os.path.exists(destination_folder):
        os.makedirs(destination_folder)
    
    # Convertendo tamanho máximo para bytes
    max_size = max_size_mb * 1024 * 1024
    
    # Lendo o arquivo PDF
    reader = PdfReader(file_path)
    total_pages = len(reader.pages)
    
    output_pdf_writer = PdfWriter()
    output_file_number = 1
    
    for i in range(total_pages):
        # Adiciona página ao PDF de saída atual
        output_pdf_writer.add_page(reader.pages[i])
        
        # Calcula o tamanho aproximado do PDF atual
        with open("temp.pdf", "wb") as temp_output:
            output_pdf_writer.write(temp_output)
            current_size = os.path.getsize(temp_output.name)
        
        # Se o tamanho atual exceder o limite, salve o PDF atual e comece um novo
        if current_size > max_size:
            output_file_path = os.path.join(destination_folder, f"output_{output_file_number}.pdf")
            with open(output_file_path, "wb") as output_file:
                output_pdf_writer.write(output_file)
            
            output_file_number += 1
            
            # Reinicia o PdfWriter para o próximo arquivo
            output_pdf_writer = PdfWriter()
            output_pdf_writer.add_page(reader.pages[i])
    
    # Salva o último arquivo, se tiver páginas restantes
    if len(output_pdf_writer.pages) > 0:
        output_file_path = os.path.join(destination_folder, f"output_{output_file_number}.pdf")
        with open(output_file_path, "wb") as output_file:
            output_pdf_writer.write(output_file)
    
    # Remova o arquivo temporário
    os.remove("temp.pdf")

# Caminho para o seu arquivo PDF
pdf_path = "origen"

# Tamanho máximo em MB (modifique aqui)
max_size_mb = 9

split_pdf(pdf_path, max_size_mb)
