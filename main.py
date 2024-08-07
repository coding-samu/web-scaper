import os
import sys
from selenium import webdriver
from selenium.webdriver.edge.service import Service
import time

def web_scraper(urls, driver_path, save_path):
    """
    Scrapes web pages from a list of URLs and saves the HTML content to files.
    Args:
        urls (list): A list of URLs to scrape.
        driver_path (str): The path to the EdgeDriver executable.
        save_path (str): The path to save the scraped HTML files.
    Returns:
        None
    """
    for i in range(len(urls)):
        try:
            print("Sto accedendo alla pagina " + urls[i])
            # Verifica se esiste già un file con lo stesso nome
            try:
                with open(os.path.join(save_path, f'{i}.html'), 'r', encoding='utf-8') as file:
                    pass
            except FileNotFoundError:
                print(f'Il file {i}.html non esiste, lo sto creando...')

                # Configura il servizio del EdgeDriver
                service = Service(driver_path)

                # Inizializza il driver del browser
                driver = webdriver.Edge(service=service)

                # Apri la pagina web
                driver.get(urls[i])

                # Attendi un po' di più per assicurarti che tutto il contenuto sia caricato
                time.sleep(5)

                # Estrai l'HTML completo della pagina
                page_source = driver.page_source

                # Salva l'HTML in un file
                with open(os.path.join(save_path, f'{i}.html'), 'w', encoding='utf-8') as file:
                    file.write(page_source)

                # Chiudi il driver del browser
                driver.quit()
            else:
                print(f'Il file {i}.html esiste già')
                continue

        finally:
            print('--------------------------------------------------')

# Esegui lo scraper
if __name__ == '__main__':
    if len(sys.argv) != 4:
        print("Usage: python main.py <driver_path> <save_path> <url1,url2,...>")
        sys.exit(1)

    driver_path = sys.argv[1]
    save_path = sys.argv[2]
    urls = sys.argv[3].split(',')

    web_scraper(urls, driver_path, save_path)