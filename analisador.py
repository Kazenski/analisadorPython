import requests
from bs4 import BeautifulSoup
import pandas as pd

def capturar_produtos(termo_busca):
    print(f"\n🔍 Iniciando busca por: {termo_busca}...")
    
    url = f"https://lista.mercadolivre.com.br/{termo_busca.replace(' ', '-')}"
    headers = {
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/120.0.0.0 Safari/537.36"
    }

    try:
        response = requests.get(url, headers=headers)
        # O soup transforma o HTML bruto em uma árvore de objetos navegável
        soup = BeautifulSoup(response.text, 'html.parser')
        
        lista_resultados = []
        
        # O seletor 'li.ui-search-layout__item' isola cada card de produto
        itens = soup.find_all('li', class_='ui-search-layout__item')

        for item in itens[:15]: # Limitando aos 15 primeiros para a aula
            nome = item.find('h2', class_='ui-search-item__title')
            
            # O preço no ML é dividido em frações e centavos, pegamos a principal
            preco = item.find('span', class_='andes-money-amount__fraction')
            link = item.find('a', class_='ui-search-link')

            if nome and preco:
                dados = {
                    "Produto": nome.text.strip(),
                    "Preço": f"R$ {preco.text.strip()}",
                    "Link": link['href'] if link else "N/A"
                }
                lista_resultados.append(dados)

        return lista_resultados

    except Exception as e:
        print(f"❌ Erro na conexão: {e}")
        return []

# --- Fluxo de Execução ---
if __name__ == "__main__":
    busca = input("O que você deseja pesquisar no Mercado Livre? ")
    resultados = capturar_produtos(busca)

    if resultados:
        # Usando Pandas para mostrar uma tabela bonita no terminal
        df = pd.DataFrame(resultados)
        print("\n--- RESULTADOS ENCONTRADOS ---")
        print(df[['Produto', 'Preço']]) # Mostra apenas colunas principais
        
        # Automação Extra: Salvar em CSV para os alunos
        df.to_csv("resultado_busca.csv", index=False, encoding='utf-8-sig')
        print("\n✅ Arquivo 'resultado_busca.csv' gerado com sucesso!")
    else:
        print("⚠️ Nenhum resultado encontrado. Tente outro termo.")
