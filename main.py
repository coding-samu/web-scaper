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
                with open(save_path + '\\' + str(i) + '.html', 'r', encoding='utf-8') as file:
                    pass
            except FileNotFoundError:
                print(f'Il file {str(i)}.html non esiste, lo sto creando...')

                # Configura il percorso del EdgeDriver
                edge_driver_path = driver_path

                # Configura il servizio del EdgeDriver
                service = Service(edge_driver_path)

                # Inizializza il driver del browser
                driver = webdriver.Edge(service=service)

                # Apri la pagina web
                driver.get(urls[i])

                # Attendi un po' di più per assicurarti che tutto il contenuto sia caricato
                time.sleep(5)

                # Estrai l'HTML completo della pagina
                page_source = driver.page_source

                # Salva l'HTML in un file
                with open(save_path + '\\' + str(i) + '.html', 'w', encoding='utf-8') as file:
                    file.write(page_source)

                # Chiudi il driver del browser
                driver.quit()
            else:
                print(f'Il file {str(i)}.html esiste già')
                continue

        finally:
            print('--------------------------------------------------')

# Esegui lo scraper
if __name__ == '__main__':
    urls = ['Inserisci qui gli URL delle pagine web da scaricare']
    driver_path = 'Inserisci qui il percorso del file msedgedriver.exe'
    save_path = 'Inserisci qui il percorso in cui salvare i file HTML'
    web_scraper(urls, driver_path, save_path)