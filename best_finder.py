import csv
from lxml import html
from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
from time import sleep

print('''Escolha a categoria de livros que deseja saber os seus best-sellers:
[1] Administração
[2] Autoajuda
[3] Computação
[4] Direito
[5] Infantil
[6] Literatura clássica
[7] Medicina
[8] Religião
[9] Mais vendidos''')

escolha=int(input('Digite o número correspondente a categoria escolhida: '))

def scrape_bestsellers(category_url):

    chrome_options = Options()
    chrome_options.add_experimental_option("detach", True)
    chrome_options.add_argument("window-size-1024,768")

    chrome_driver = Service(ChromeDriverManager().install())

    driver = webdriver.Chrome(service=chrome_driver, options=chrome_options)

    driver.get(category_url)

    sleep(2)

    driver.refresh()

    sleep(2)

    dados = html.fromstring(driver.page_source)

    csv_headers= ['Rank', 'Título', 'Autor','Preço']
    with open('best_finder.csv', 'w', encoding='utf-8',
        newline='') as f:
        writer = csv.writer(f)
        writer.writerow(csv_headers)

    for produto_dados in dados.xpath('.//div[@id="gridItemRoot"]'):
        ranking = produto_dados.xpath('.//span[@class="zg-bdg-text"]/text()')
        title = produto_dados.xpath('.//a/span/div[@class="_cDEzb_p13n-sc-css-line-clamp-1_1Fn1y"]/text()')
        title2 = produto_dados.xpath('.//a[1]/span/div[@class="_cDEzb_p13n-sc-css-line-clamp-2_EWgCb"]/text()')
        autor = produto_dados.xpath('.//div[1]/span/div[@class="_cDEzb_p13n-sc-css-line-clamp-1_1Fn1y"]/text()')
        autor2 = produto_dados.xpath('.//div[1]/a/div[@class="_cDEzb_p13n-sc-css-line-clamp-1_1Fn1y"]/text()')
        price = produto_dados.xpath('.//span[@class="_cDEzb_p13n-sc-price_3mJ9Z"]/text()')

        with open('best_finder.csv', 'a', encoding='utf-8', newline='') as f:
            writer = csv.writer(f)
            writer.writerow([ranking,title+title2,autor+autor2,price])
        
    driver.quit()

    return csv


if escolha == 1:
    category_url = "https://www.amazon.com.br/gp/bestsellers/books/7872854011/ref=zg_bs_nav_books_1"  # Administração category URL
    bestsellers_df = scrape_bestsellers(category_url)
    print(bestsellers_df)


elif escolha == 2:
    category_url = "https://www.amazon.com.br/gp/bestsellers/books/7841720011/ref=zg_bs_nav_books_1"  # Autoajuda category URL
    bestsellers_df = scrape_bestsellers(category_url)
    print(bestsellers_df)

elif escolha == 3:
    category_url = "https://www.amazon.com.br/gp/bestsellers/books/7842641011/ref=zg_bs_nav_books_1"  # Computação category URL
    bestsellers_df = scrape_bestsellers(category_url)
    print(bestsellers_df)

elif escolha == 4:
    category_url = "https://www.amazon.com.br/gp/bestsellers/books/7874340011/ref=zg_bs_nav_books_1" # Direito category URL
    bestsellers_df = scrape_bestsellers(category_url)
    print(bestsellers_df)

elif escolha == 5:
    category_url = "https://www.amazon.com.br/gp/bestsellers/books/7844001011/ref=zg_bs_nav_books_1" # Infantil category URL
    bestsellers_df = scrape_bestsellers(category_url)
    print(bestsellers_df)

elif escolha == 6:
    category_url = "https://www.amazon.com.br/gp/bestsellers/books/7872689011/ref=zg_bs_nav_books_2_7872687011" # Literatura category URL
    bestsellers_df = scrape_bestsellers(category_url)
    print(bestsellers_df)

elif escolha == 7:
    category_url = "https://www.amazon.com.br/gp/bestsellers/books/7874461011/ref=zg_bs_nav_books_1" # Medicina category URL
    bestsellers_df = scrape_bestsellers(category_url)
    print(bestsellers_df)

elif escolha == 8:
    category_url = "https://www.amazon.com.br/gp/bestsellers/books/7874675011/ref=zg_bs_unv_books_2_7874677011_2" # Religião category URL
    bestsellers_df = scrape_bestsellers(category_url)
    print(bestsellers_df)

elif escolha == 9:
    category_url = "https://www.amazon.com.br/gp/bestsellers/books/?ie=UTF8&ref_=sv_b_2"  # Mais vendidos category URL
    bestsellers_df = scrape_bestsellers(category_url)
    print(bestsellers_df)

else:
    print('Opção inválida!!')