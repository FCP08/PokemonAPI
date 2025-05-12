
# 🧪 Projeto: Pokemon API Teste

Script em Python que coleta informações de Pokémon a partir da **PokeAPI** e do site **PokémonDB**, traduz a descrição para o português usando a **Deep Translator**, e organiza os dados em uma planilha Excel.

## 🔍 Funcionalidades
- Consulta de dados de um Pokémon específico (por número)
- Tradução da biografia do Pokémon (extraída via web scraping)
- Coleta de tipos, habilidades e estatísticas base (HP, ataque, defesa etc.)
- Exportação dos dados para um arquivo Excel
- Execução automatizada com uso de navegador invisível via Selenium

## 🛠️ Tecnologias utilizadas
- Python
- Requests
- Selenium (modo headless)
- BeautifulSoup
- Pandas
- Deep Translator
- Excel (via pandas)

## 🚀 Como executar o projeto

1. Clone o repositório:
```bash
git clone https://github.com/seu-usuario/pokemon-api-teste.git
cd pokemon-api-teste
```

2. Instale as dependências:
```bash
pip install -r requirements.txt
```

3. Execute o script:
```bash
python PokemonAPITeste.py
```

> Certifique-se de ter o ChromeDriver instalado e compatível com a sua versão do navegador Google Chrome.

## 📄 Licença
Este projeto está sob a licença MIT. Sinta-se livre para usar e adaptar!
