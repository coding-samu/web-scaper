from selenium import webdriver
from selenium.webdriver.edge.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
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
    for url in urls:
        try:
            print("Sto accedendo alla pagina " + url)
            # Verifica se esiste già un file con lo stesso nome
            try:
                with open(save_path + '\\' + url + '.html', 'r', encoding='utf-8') as file:
                    pass
            except FileNotFoundError:
                print(f'Il file {url}.html non esiste, lo sto creando...')

                # Configura il percorso del EdgeDriver
                edge_driver_path = driver_path

                # Configura il servizio del EdgeDriver
                service = Service(edge_driver_path)

                # Inizializza il driver del browser
                driver = webdriver.Edge(service=service)

                # Apri la pagina web
                driver.get(url)

                # Attendi un po' di più per assicurarti che tutto il contenuto sia caricato
                time.sleep(5)

                # Estrai l'HTML completo della pagina
                page_source = driver.page_source

                # Salva l'HTML in un file
                with open(save_path + '\\' + url + '.html', 'w', encoding='utf-8') as file:
                    file.write(page_source)

                # Chiudi il driver del browser
                driver.quit()
            else:
                print(f'Il file {url}.html esiste già')
                continue

        finally:
            print('--------------------------------------------------')