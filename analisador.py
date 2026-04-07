import requests
from bs4 import BeautifulSoup

def capturar_produtos(termo_busca):
    print(f"\n🔍 Buscando por: {termo_busca}...")
    
    # Formatamos a URL para o padrão de busca do ML
    url = f"https://lista.mercadolivre.com.br/{termo_busca.replace(' ', '-')}"
    
    # User-Agent atualizado para parecer um navegador real de 2026
    headers = {
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/120.0.0.0 Safari/537.36",
        "Accept-Language": "pt-BR,pt;q=0.9,en-US;q=0.8,en;q=0.7"
    }

    try:
        response = requests.get(url, headers=headers, timeout=10)
        soup = BeautifulSoup(response.text, 'html.parser')
        
        # Tentativa 1: Seletores de lista (Layout padrão)
        # O ML costuma usar h2 para títulos de produtos
        produtos = []
        cards = soup.find_all(['div', 'li'], class_=['ui-search-result__wrapper', 'ui-search-layout__item'])

        if not cards:
            # Tentativa 2: Se o layout for grade (grid), as classes mudam
            cards = soup.select('.ui-search-result')

        for item in cards[:10]:
            # Buscamos o título (geralmente dentro de um h2 ou h3)
            titulo = item.find(['h2', 'h3'])
            
            # Buscamos o preço (procuramos pela classe que contém a fração do valor)
            preco = item.find('span', class_='andes-money-amount__fraction')
            
            if titulo and preco:
                produtos.append({
                    "nome": titulo.text.strip(),
                    "preco": preco.text.strip()
                })

        return produtos

    except Exception as e:
        print(f"❌ Erro de conexão: {e}")
        return []

if __name__ == "__main__":
    busca = input("O que pesquisar? ")
    resultados = capturar_produtos(busca)

    if resultados:
        print("\n✅ PRODUTOS ENCONTRADOS:")
        print("-" * 40)
        for p in resultados:
            print(f"📦 {p['nome'][:50]}... | 💰 R$ {p['preco']}")
        print("-" * 40)
    else:
        print("\n⚠️ O Mercado Livre bloqueou o acesso ou mudou as classes CSS.")
        print("Dica: Tente rodar novamente ou verifique se o site abre no seu navegador.")