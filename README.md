## **📌 Índice**  
- [**📌 Índice**](#-índice)
- [**📜 Sobre o Projeto**](#-sobre-o-projeto)
- [**🛠 Tecnologias Utilizadas**](#-tecnologias-utilizadas)
- [**📂 Estrutura do Projeto**](#-estrutura-do-projeto)
- [**🚀 Como Executar o Projeto**](#-como-executar-o-projeto)
  - [**1️⃣ Clonando o Repositório**](#1️⃣-clonando-o-repositório)
  - [**2️⃣ Instalando as Dependências**](#2️⃣-instalando-as-dependências)
  - [**3️⃣ Configurando a Chave da API**](#3️⃣-configurando-a-chave-da-api)
  - [**4️⃣ Rodando o Chatbot**](#4️⃣-rodando-o-chatbot)
- [**🔍 Explicação do Código**](#-explicação-do-código)
  - [**1️⃣ Importação das Bibliotecas**](#1️⃣-importação-das-bibliotecas)
  - [**2️⃣ Configuração do Modelo da Groq**](#2️⃣-configuração-do-modelo-da-groq)
  - [**3️⃣ Gerenciamento do Histórico**](#3️⃣-gerenciamento-do-histórico)
    - [**Carregar Histórico**](#carregar-histórico)
    - [**Salvar Histórico**](#salvar-histórico)
    - [**Apagar Histórico**](#apagar-histórico)
  - [**4️⃣ Função Principal (`chat_interativo()`)**](#4️⃣-função-principal-chat_interativo)
- [**📖 Glossário**](#-glossário)
- [**🤝 Contribuição**](#-contribuição)
- [**📄 Licença**](#-licença)

---

## **📜 Sobre o Projeto**  
Este projeto implementa um chatbot com **memória persistente**, permitindo interações contínuas com contexto armazenado. O histórico da conversa é salvo em um arquivo `JSON`, garantindo que o chatbot se lembre de mensagens passadas, mesmo após o programa ser encerrado.  

- **Plataforma de IA:** [Groq API](https://groq.com/)  
- **Armazenamento de histórico:** Arquivo JSON (`historico.json`)  
- **Gerenciamento de conversas:** `LangChain`  

---

## **🛠 Tecnologias Utilizadas**  
- **Python 3.8+**  
- **LangChain** – Para gerenciamento de histórico e execução de modelos de IA  
- **Groq API** – Para processamento de linguagem natural  
- **dotenv** – Para carregar variáveis de ambiente  
- **JSON** – Para armazenamento de histórico  

---

## **📂 Estrutura do Projeto**  
```bash
AI-APPLICATIONS-WITH-MEMORY/
│── historico.json       # Armazena o histórico da conversa
│── main.py              # Código principal do chatbot
│── .env                 # Armazena a chave da API do Groq (não deve ser compartilhado)
│── requirements.txt     # Lista de dependências do projeto
└── README.md            # Documentação do projeto
```

---

## **🚀 Como Executar o Projeto**  

### **1️⃣ Clonando o Repositório**  
Primeiro, baixe o código para sua máquina local:  

```bash
git clone https://github.com/MeirelesAndre/AI-APPLICATIONS-WITH-MEMORY.git
cd AI-APPLICATIONS-WITH-MEMORY
```

### **2️⃣ Instalando as Dependências**  
No diretório do projeto, instale as bibliotecas necessárias:  

```bash
pip install -r requirements.txt
```

### **3️⃣ Configurando a Chave da API**  
Crie um arquivo `.env` na raiz do projeto e adicione sua chave da **Groq API**:  

```
GROQ_API_KEY=YOUR_API_KEY_HERE
```

Substitua `YOUR_API_KEY_HERE` pela chave real obtida na [plataforma Groq](https://groq.com/).  

### **4️⃣ Rodando o Chatbot**  
Execute o arquivo principal para iniciar a interação com o chatbot:  

```bash
python main.py
```

---

## **🔍 Explicação do Código**  

### **1️⃣ Importação das Bibliotecas**
O código importa as bibliotecas essenciais para carregar variáveis de ambiente (`dotenv`), processar mensagens (`LangChain`), interagir com a API da Groq e gerenciar histórico de conversas em JSON.  

### **2️⃣ Configuração do Modelo da Groq**
Carregamos a chave da API e inicializamos o modelo:  
```python
load_dotenv()
GROQ_API_KEY = os.getenv("GROQ_API_KEY")

model = ChatGroq(
    model="gemma2-9b-it",
    groq_api_key=GROQ_API_KEY
)
```

### **3️⃣ Gerenciamento do Histórico**  
O histórico é armazenado no arquivo `historico.json`, permitindo que o chatbot lembre de interações anteriores.  

#### **Carregar Histórico**  
```python
def carregar_historico(session_id: str) -> ChatMessageHistory:
```
- Lê o `historico.json`  
- Se houver um histórico salvo, ele é carregado na memória  
- Caso contrário, cria um novo histórico  

#### **Salvar Histórico**  
```python
def salvar_historico(session_id: str):
```
- Converte as mensagens do chat para JSON  
- Atualiza o `historico.json` com a conversa  

#### **Apagar Histórico**  
```python
def apagar_historico():
```
- Escreve um dicionário vazio no `historico.json`  
- Reinicia o histórico na memória  

### **4️⃣ Função Principal (`chat_interativo()`)**
```python
def chat_interativo():
```
- Exibe instruções iniciais  
- Aguarda a entrada do usuário em um loop  
- Se o usuário digitar `sair`, o chat encerra  
- Se digitar `apagar histórico`, o histórico é apagado e a conversa reinicia  

---

## **📖 Glossário**  
| Termo              | Definição |
|--------------------|-----------|
| **Chatbot**       | Programa que simula uma conversa humana. |
| **Groq API**      | Plataforma que processa linguagem natural para gerar respostas inteligentes. |
| **LangChain**     | Framework para conectar modelos de IA com histórico de conversas. |
| **Memória Persistente** | Capacidade do chatbot de lembrar interações anteriores. |
| **JSON**          | Formato de armazenamento de dados estruturados em texto. |
| **.env**          | Arquivo que armazena variáveis sensíveis, como chaves de API. |

---

## **🤝 Contribuição**  
Sinta-se à vontade para contribuir!  

1. **Faça um fork** do repositório  
2. Crie uma **branch** (`git checkout -b minha-feature`)  
3. Faça as alterações e **commite** (`git commit -m 'Minha nova feature'`)  
4. Envie um **push** para sua branch (`git push origin minha-feature`)  
5. Abra um **Pull Request** 🚀  

---

## **📄 Licença**  
Este projeto está sob a licença MIT. Você pode usá-lo, modificá-lo e distribuí-lo livremente.  