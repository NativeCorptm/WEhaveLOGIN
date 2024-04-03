import os
import time
from tqdm import tqdm
import urllib.parse

def search_and_write_lines_with_keyword(file_name, keyword):
    relevant_content = ""  # Inizializziamo una stringa vuota per memorizzare il contenuto del file
    decoding_errors = 0
    with open(file_name, 'r', encoding='utf-8') as file:
        for row in file:  # Rinominiamo la variabile 'line' in 'row'
            try:
                if keyword in row:  # Rinominiamo la variabile 'line' in 'row'
                    relevant_content += row.strip() + "\n"  # Aggiungiamo la riga al contenuto rilevante
            except UnicodeDecodeError:
                decoding_errors += 1
    return relevant_content, decoding_errors

def clean_file_name(file_name):
    invalid_characters = ['/', '\\', ':', '*', '?', '"', '<', '>', '|']
    for char in invalid_characters:
        file_name = file_name.replace(char, '_')
    return file_name

print("                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                               ")

def main():
    print(" " * 50000 + "\u001b[92m               WEhaveLOGIN\u001b[0m");
    print(" " * 500)
    db_folder = ("/sdcard/WEhaveLOGIN/")
    
    if not os.path.isdir(db_folder):
        print(f"\u001b[35m The command '{db_folder}' does not exist\u001b[0m")
        return

    keyword = input("\u001b[35m Type the site or URL:\u001b[0m");print(" " * 50000)
    encoded_keyword = urllib.parse.quote(keyword)

    output_file_name = f" {clean_file_name(encoded_keyword)}.txt"
    output_file_path = os.path.join(db_folder, output_file_name)

    txt_files = [file for file in os.listdir(db_folder) if file.endswith('.txt')]

    if not txt_files:
        print(f"\u001b[35mWe found nothing '{db_folder}'.\u001b[0m")
        return
        
    with tqdm(total=len(txt_files), desc="") as progress_bar:
        total_lines_found = 0
        total_decoding_errors = 0
        with open(output_file_path, 'w') as output_file:  # Modifica qui per salvare il file nella directory specificata
            for txt_file in txt_files:
                file_path = os.path.join(db_folder, txt_file)
                relevant_content, decoding_errors = search_and_write_lines_with_keyword(file_path, keyword)
                total_lines_found += len(relevant_content.splitlines())  # Aggiorniamo il conteggio delle righe rilevanti
                total_decoding_errors += decoding_errors
                if relevant_content:
                    output_file.write(relevant_content)  # Scriviamo il contenuto rilevante direttamente nel file
                    output_file.write("\n\n")
                progress_bar.update(1)
                time.sleep(0.1)

    if total_lines_found == 0:
        print("\u001b[35mWe didn't find anything.\u001b[0m")
    else:
        print(f"\u001b[35mLogins found: {total_lines_found}, you will find it on your folder\u001b[0m")

if __name__ == "__main__":
    main()
    
