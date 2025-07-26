# Guru do Brasileirão ⚽

![Flask](https://img.shields.io/badge/Flask-000000?style=for-the-badge&logo=flask&logoColor=white)
![Python](https://img.shields.io/badge/Python-3776AB?style=for-the-badge&logo=python&logoColor=white)
![JavaScript](https://img.shields.io/badge/JavaScript-F7DF1E?style=for-the-badge&logo=javascript&logoColor=black)
![HTML5](https://img.shields.io/badge/HTML5-E34F26?style=for-the-badge&logo=html5&logoColor=white)
![CSS3](https://img.shields.io/badge/CSS3-1572B6?style=for-the-badge&logo=css3&logoColor=white)

Este é um projeto de chatbot, o "Guru do Brasileirão", focado em fornecer informações e curiosidades sobre o Campeonato Brasileiro de Futebol. A aplicação é construída com um backend em Flask (Python) e um frontend em HTML, CSS e JavaScript puro.

Uma característica central do projeto é o uso de uma estrutura de dados de **Árvore B** customizada para mapear as intenções do usuário e buscar respostas de forma eficiente. Além disso, o chatbot se conecta à API do Cartola FC para obter dados de jogadores em tempo real.

## 🖼️ Screenshot
![Guru do Brasileirão](https://github.com/lucaslmp2/GuruDoBrasileir-o/blob/main/Capturadetela2025-07-26163434.png)

## ✨ Funcionalidades

- **📜 História do Campeonato**: Detalhes sobre a criação e evolução do Brasileirão.
- **🏆 Campeões por Ano**: Consulte o time campeão de uma edição específica.
- **🥇 Maior Campeão**: Descubra qual time possui mais títulos.
- **🥅 Maiores Artilheiros**: Conheça os goleadores históricos do campeonato.
- **👨‍🏫 Técnicos**: Informações sobre os técnicos atuais dos times da Série A.
- **⚽ Informações de Jogadores**: Busque dados de jogadores (gols, assistências) através da API do Cartola FC.
- **🛡️ Informações de Clubes**: Veja detalhes e escudos dos clubes.
- **🤓 Curiosidades**: Fatos interessantes sobre o campeonato.

## 🛠️ Tecnologias Utilizadas

- **Backend**:
  - **Python 3**
  - **Flask**: Micro-framework web para servir a aplicação e a API.
  - **Flask-CORS**: Para permitir requisições do frontend.
  - **Requests**: Para consumir a API externa do Cartola FC.

- **Frontend**:
  - **HTML5**
  - **CSS3**
  - **JavaScript (Vanilla)**: Para manipulação do DOM, lógica do chat e requisições `fetch`.

- **Estrutura de Dados**:
  - **Árvore B**: Implementação própria para busca e recuperação de respostas baseadas na entrada do usuário.

## 📂 Estrutura do Projeto

```
.
├── meuChatbot.py       # Arquivo principal da aplicação Flask (backend)
├── btree_node.py       # Implementação da Árvore B
├── requirements.txt    # Dependências do Python
├── templates/
│   └── index.html      # Estrutura principal da página do chat
└── static/
    ├── css/
    │   └── style.css   # Estilização da página
    ├── js/
    │   └── script.js   # Lógica do frontend (interação, requisições)
    ├── *.json          # Arquivos de dados (clubes, campeões, etc.)
    └── *.png           # Imagens e ícones
```

## 🚀 Como Executar o Projeto

Siga os passos abaixo para rodar o projeto em sua máquina local.

### Pré-requisitos

- Python 3.8+
- `pip` (gerenciador de pacotes do Python)

### Instalação

1. **Clone o repositório:**
   ```bash
   git clone https://github.com/seu-usuario/chatBot_guru_do_brasileiro.git
   cd chatBot_guru_do_brasileiro
   ```

2. **Crie e ative um ambiente virtual (recomendado):**
   ```bash
   # Para Windows
   python -m venv venv
   .\venv\Scripts\activate

   # Para macOS/Linux
   python3 -m venv venv
   source venv/bin/activate
   ```

3. **Instale as dependências:**
   ```bash
   pip install -r requirements.txt
   ```

4. **Inicie o servidor Flask:**
   ```bash
   python meuChatbot.py
   ```

5. **Acesse a aplicação:**
   Abra seu navegador e acesse http://127.0.0.1:5000.

## 💬 Como Usar

Após iniciar a aplicação, a interface do chat será exibida. Você pode interagir digitando os comandos sugeridos no menu inicial (ex: `historia do campeonato`, `clubes`, `jogadores`) ou fazendo perguntas diretas, como `historia do flamengo` ou `tecnico do palmeiras`.