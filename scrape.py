from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from bs4 import BeautifulSoup
import time
import pandas as pd 
 
def scrape_all_books():
    # Criando uma instância do navegador
    navegador = webdriver.Chrome()

    # Acessando o site
    navegador.get("https://books.toscrape.com/index.html")

    # Aguardando os produtos aparecerem na página (em vez de um sleep fixo)
    WebDriverWait(navegador, 10).until(
        EC.presence_of_element_located((By.CSS_SELECTOR, "article.product_pod"))
    )

    all_products = []

    for page in range(1, 51):  # páginas 1 até 50
        soup = BeautifulSoup(navegador.page_source, 'lxml')
        products = soup.select('article.product_pod')

        if not products:
            print(f"Página {page} sem produtos, parando.")
            break

        print(f"Página {page}: {len(products)} produtos encontrados")

        for product in products:
            name = product.select('h3 > a')[0].get('title').strip()
            price = product.select('p.price_color')[0].text.strip()
            price = price.replace('.', ',')
            url = product.select('h3 > a')[0].get('href').strip()

            all_products.append({
                "nome": name,
                "preco": price,
                "url": url,
            })

        time.sleep(0.5)  # pequena pausa pra você acompanhar a captura

        # Tenta clicar em "next" para ir para a próxima página real
        try:
            next_button = navegador.find_element(By.CSS_SELECTOR, "li.next > a")
            next_button.click()
            WebDriverWait(navegador, 10).until(
                EC.presence_of_element_located((By.CSS_SELECTOR, "article.product_pod"))
            )
        except Exception:
            print("Não há mais páginas, parando.")
            break

    navegador.quit()

    print(f"Total coletado: {len(all_products)}")

    if all_products:
        # Salvando os dados em um arquivo Excel
        df = pd.DataFrame(all_products)
        df.to_excel("itens.xlsx", index=False)
        print("Salvo em itens.xlsx")


if __name__ == "__main__":
    scrape_all_books()