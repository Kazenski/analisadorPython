import requests
from bs4 import BeautifulSoup
import pandas as pd # Para criar o Excel
from datetime import datetime

def minerar_mercado_livre(termo_busca):
    print(f"\n🚀 Iniciando extração de dados para: {termo_busca}...")
    
    url = f"https://lista.mercadolivre.com.br/{termo_busca.replace(' ', '-')}"
    headers = {
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/120.0.0.0 Safari/537.36"
    }

    try:
        response = requests.get(url, headers=headers, timeout=10)
        soup = BeautifulSoup(response.text, 'html.parser')
        
        dados_completos = []
        # Seleciona os containers de produtos
        cards = soup.find_all(['div', 'li'], class_=['ui-search-result__wrapper', 'ui-search-layout__item'])

        for item in cards:
            titulo = item.find(['h2', 'h3'])
            preco_inteiro = item.find('span', class_='andes-money-amount__fraction')
            link = item.find('a', class_='ui-search-link')
            
            # Alguns itens têm frete grátis, vamos tentar capturar isso também
            frete = item.find('span', class_='ui-pb-highlight')
            frete_texto = frete.text.strip() if frete else "Não informado"

            if titulo and preco_inteiro and link:
                # Limpamos o preço para que o Excel entenda como NÚMERO e não texto
                valor_limpo = float(preco_inteiro.text.replace('.', '').replace(',', '.'))
                
                dados_completos.append({
                    "Produto": titulo.text.strip(),
                    "Preço (R$)": valor_limpo,
                    "Frete": frete_texto,
                    "Link": link['href'],
                    "Data da Consulta": datetime.now().strftime("%d/%m/%Y %H:%M")
                })

        return dados_completos

    except Exception as e:
        print(f"❌ Erro fatal: {e}")
        return []

if __name__ == "__main__":
    busca = input("Qual produto deseja exportar para Excel? ")
    resultados = minerar_mercado_livre(busca)

    if resultados:
        # Criamos um DataFrame (como se fosse uma tabela de SQL/Excel na memória)
        df = pd.DataFrame(resultados)
        
        # 1. Mostra no Terminal (Formatado)
        print("\n📊 PRÉVIA DOS DADOS:")
        print(df[["Produto", "Preço (R$)"]].head(10)) # Mostra os 10 primeiros
        
        # 2. Exporta para Excel
        nome_arquivo = f"analise_{busca.replace(' ', '_')}.xlsx"
        df.to_excel(nome_arquivo, index=False)
        
        print(f"\n✅ SUCESSO!")
        print(f"📂 Arquivo gerado: {nome_arquivo}")
        print(f"📈 Total de itens capturados: {len(df)}")
    else:
        print("\n⚠️ Nenhuma informação capturada para exportação.")