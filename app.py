import os
import json
from dotenv import load_dotenv
from langchain_groq import ChatGroq
from langchain_community.chat_message_histories import ChatMessageHistory
from langchain_core.chat_history import BaseChatMessageHistory
from langchain_core.messages import HumanMessage, AIMessage

# Carrega variáveis de ambiente
load_dotenv()

# Obtém a chave da API do Groq
GROQ_API_KEY = os.getenv("GROQ_API_KEY")

# Inicializa o modelo da Groq
model = ChatGroq(
    model="gemma2-9b-it",
    groq_api_key=GROQ_API_KEY
)

# Caminho para armazenar o histórico da conversa
HISTORICO_FILE = "AI-APPLICATIONS-WITH-MEMORY\historico.json"

# Dicionário global para armazenar os históricos de conversação
store = {}


def carregar_historico(session_id: str) -> ChatMessageHistory:
    """Carrega o histórico de mensagens do arquivo JSON ou cria um novo."""
    if os.path.exists(HISTORICO_FILE):
        try:
            with open(HISTORICO_FILE, "r", encoding="utf-8") as f:
                data = json.load(f)
                if session_id in data:
                    mensagens = [
                        HumanMessage(content=m["content"]) if m["type"] == "human" else AIMessage(
                            content=m["content"])
                        for m in data[session_id]
                    ]
                    store[session_id] = ChatMessageHistory(messages=mensagens)
        except Exception as e:
            print("Erro ao carregar histórico:", e)

    # Se não houver histórico carregado, cria um novo
    if session_id not in store:
        store[session_id] = ChatMessageHistory()

    return store[session_id]


def salvar_historico(session_id: str):
    """Salva o histórico de mensagens no arquivo JSON."""
    data = {}
    if os.path.exists(HISTORICO_FILE):
        try:
            with open(HISTORICO_FILE, "r", encoding="utf-8") as f:
                data = json.load(f)
        except Exception as e:
            print("Erro ao ler histórico:", e)

    # Atualiza os dados da sessão
    data[session_id] = [
        {"type": "human", "content": msg.content} if isinstance(msg, HumanMessage)
        else {"type": "ai", "content": msg.content}
        for msg in store[session_id].messages
    ]

    try:
        with open(HISTORICO_FILE, "w", encoding="utf-8") as f:
            json.dump(data, f, ensure_ascii=False, indent=4)
    except Exception as e:
        print("Erro ao salvar histórico:", e)


def apagar_historico():
    """Apaga todo o histórico salvo no arquivo JSON."""
    if os.path.exists(HISTORICO_FILE):
        try:
            with open(HISTORICO_FILE, "w", encoding="utf-8") as f:
                json.dump({}, f)  # Escreve um dicionário vazio no arquivo
            print("Histórico apagado com sucesso!")
        except Exception as e:
            print("Erro ao apagar histórico:", e)
    else:
        print("Nenhum histórico encontrado para apagar.")


def chat_interativo():
    """Função que permite conversar com o chatbot em tempo real e mantém o histórico salvo."""
    session_id = "chat1"  # Pode ser modificado para cada usuário, se necessário
    history = carregar_historico(session_id)

    print("Olá! Sou um assistente virtual. Para sair, digite 'sair'.")
    print("Para apagar o histórico da conversa, digite 'apagar histórico'.\n")

    while True:
        # Remove espaços extras e ignora maiúsculas/minúsculas
        user_input = input("Você: ").strip().lower()

        if user_input == "sair":
            print("Encerrando o chat. Até logo!")
            salvar_historico(session_id)
            break

        if user_input == "apagar histórico":
            apagar_historico()
            # Reseta o histórico na memória também
            store[session_id] = ChatMessageHistory()
            print("Seu histórico foi apagado. Começamos um novo chat!\n")
            continue

        # Adiciona a mensagem do usuário ao histórico
        history.add_user_message(user_input)

        # Gera a resposta do chatbot
        response = model.invoke(history.messages)

        # Adiciona a resposta da IA ao histórico
        history.add_ai_message(response.content)

        # Exibe a resposta
        print("Chatbot:", response.content)

        # Salva o histórico atualizado
        salvar_historico(session_id)


if __name__ == "__main__":
    chat_interativo()
