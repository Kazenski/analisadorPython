# 🚀 Automação de Análise de Mercado (Python + Scraping)

Este projeto é uma ferramenta de **Data Mining** e **Automação** desenvolvida para fins pedagógicos. O objetivo central é demonstrar como extrair dados brutos da web (Web Scraping) e transformá-los em informações estruturadas (Excel) para tomada de decisão em tempo real, eliminando processos manuais de coleta.

---

## 🎯 Objetivo Pedagógico e Visão Geral

O foco desta aula é capacitar o aluno a entender o ciclo de vida do dado na automação. Diferente de uma navegação comum, o script "lê" o site através do seu código-fonte, identificando tags HTML e seletores CSS dinâmicos. 

Neste projeto, exploramos a **Resiliência de Código**, implementando seletores múltiplos para que a automação suporte mudanças de layout no site alvo, além da **Engenharia de Dados**, que envolve o tratamento de strings, conversão de tipos (Texto para Float) e a exportação de relatórios profissionais em formatos aceitos pelo mercado, como o `.xlsx`.

---

## 🛠️ Configuração do Ambiente no VS Code

Para que o projeto funcione corretamente, o ambiente de desenvolvimento deve estar preparado com as seguintes ferramentas:

1.  **Extensões:** Instale a extensão oficial do **Python** (Microsoft) no VS Code.
2.  **Versão do Python:** É necessário o Python 3.10 ou superior (verifique com `python --version`).
3.  **Dependências Técnicas:** Execute o comando abaixo no terminal para instalar o "motor" da aplicação:
    ```bash
    pip install requests beautifulsoup4 pandas openpyxl
    ```
    * **requests:** Realiza a conexão HTTP com o servidor.
    * **beautifulsoup4:** Interpreta o HTML e extrai os dados (o "garimpeiro").
    * **pandas:** Organiza os dados em tabelas (DataFrames).
    * **openpyxl:** Permite a escrita física do arquivo Excel.

---

## 📂 Estrutura e Execução do Projeto

A estrutura de arquivos é simplificada para facilitar o entendimento:

* **`analisador.py`**: O "cérebro" da automação contendo a lógica de scraping.
* **`.gitignore`**: Configurado para ignorar arquivos temporários e manter o repositório limpo.
* **`README.md`**: Este guia completo de documentação.

**Como rodar:** 1. Abra o terminal no VS Code (`Ctrl + '`).
2. Digite `python analisador.py`.
3. Insira o nome de qualquer produto (ex: `cadeira gamer` ou `monitor 4k`). 
O script fará a busca em tempo real e criará o arquivo Excel automaticamente na pasta do projeto.

---

## 📊 O Produto Final: Inteligência de Dados

Ao final da execução, um arquivo Excel é gerado com as seguintes informações estruturadas, permitindo análise imediata:

* **Produto:** Nome completo conforme anunciado, permitindo identificação precisa.
* **Preço (R$):** Valor convertido em formato numérico, pronto para fórmulas matemáticas e médias.
* **Link:** URL direta para auditoria do dado ou conversão de compra.
* **Data:** Registro temporal para controle de histórico e flutuação de mercado.

---

## ⚠️ Fundamentos Técnicos e Resiliência

A automação utiliza conceitos avançados para garantir a integridade e a entrega do dado:

* **User-Agent (Simulação de Identidade):** O script envia cabeçalhos HTTP que identificam a requisição como vinda de um navegador real (Chrome/Edge), evitando bloqueios de segurança do Mercado Livre.
* **Seletores Resilientes:** Utilizamos o método `soup.select` com operadores lógicos. Se o site mudar uma classe CSS, o código tenta caminhos alternativos automaticamente para evitar falhas.
* **Data Cleaning (Tratamento de Dados):** O Python identifica o padrão de moeda brasileiro (R$ 1.500,00), remove pontos de milhar e converte vírgulas em pontos decimais. Isso garante que o Excel reconheça o valor como um **Número** e não como "Texto", permitindo que o aluno crie somas, filtros e gráficos de BI imediatamente após a extração.

---

> **💡 Dica de Aula:** *"Na automação, o código é o seu assistente digital que nunca dorme. Ele não apenas busca o dado, ele o organiza para que você transforme informação bruta em conhecimento estratégico."*
