# 📚 Books to Scrape - Web Scraper

Script em Python que percorre todas as páginas do site [books.toscrape.com](https://books.toscrape.com/index.html), coleta nome, preço e URL de cada livro, e exporta os dados para uma planilha Excel (`itens.xlsx`).

## Funcionalidades

- Navega automaticamente por até 50 páginas do catálogo, seguindo o botão **"next"**.
- Extrai de cada livro:
  - **Nome** (`title` do link do produto)
  - **Preço** (com vírgula como separador decimal, ex.: `£51,77`)
  - **URL** (link relativo para a página do produto)
- Usa `WebDriverWait` para aguardar o carregamento dos produtos em vez de `sleep` fixo, tornando a coleta mais confiável.
- Interrompe a coleta automaticamente quando não há mais páginas ou produtos.
- Salva o resultado final em um arquivo Excel (`itens.xlsx`).

## Pré-requisitos

- Python 3.8+
- Google Chrome instalado
- ChromeDriver compatível com a versão do Chrome (gerenciado automaticamente pelo Selenium Manager a partir do Selenium 4.6+)

## Dependências

Instale as bibliotecas necessárias com:

```bash
pip install selenium beautifulsoup4 lxml pandas openpyxl
```

| Biblioteca | Uso |
|---|---|
| `selenium` | Automação do navegador (Chrome) |
| `beautifulsoup4` | Parsing do HTML da página |
| `lxml` | Parser rápido usado pelo BeautifulSoup |
| `pandas` | Estruturação e exportação dos dados |
| `openpyxl` | Necessário para o pandas salvar arquivos `.xlsx` |

## Como executar

1. Clone ou baixe o script.
2. Instale as dependências (comando acima).
3. Execute o script:

```bash
python scraper.py
```

4. Ao final da execução, o arquivo `itens.xlsx` será criado no mesmo diretório, contendo as colunas:

| nome | preco | url |
|---|---|---|
| A Light in the Attic | £51,77 | catalogue/a-light-in-the-attic_1000/index.html |

## Estrutura do código

- **`scrape_all_books()`**: função principal que:
  1. Abre o Chrome e acessa a página inicial do site.
  2. Aguarda o carregamento dos produtos.
  3. Para cada página (até 50), extrai os dados dos livros com BeautifulSoup.
  4. Clica no botão "next" para avançar de página.
  5. Repete até não haver mais páginas ou produtos.
  6. Fecha o navegador e salva os dados coletados em Excel.

## Observações

- O script usa `time.sleep(0.5)` entre páginas apenas para facilitar o acompanhamento visual da coleta — pode ser removido sem prejuízo funcional.
- As URLs coletadas são **relativas**; para acessá-las diretamente, é necessário concatenar com `https://books.toscrape.com/` (ou `https://books.toscrape.com/catalogue/`, dependendo da página de origem).
- O site [books.toscrape.com](https://books.toscrape.com/index.html) é um ambiente público criado especificamente para prática de web scraping, sem restrições de uso.
