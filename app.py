import google.generativeai as genai
import os

print("="*50)
print("🛡️ Iniciando SegurIA - Assistente de Segurança")
print("="*50)

# 1. COLE A SUA CHAVE DE API AQUI (DENTRO DAS ASPAS)
CHAVE_API = "COLE_SUA_CHAVE_AQUI"

try:
    genai.configure(api_key=CHAVE_API)

    # 2. Passando as Regras e Base de Conhecimento para a IA (O nosso Prompt!)
    instrucoes = """
    Atue como um especialista em segurança bancária. 
    Sua tarefa é acalmar o cliente e dar instruções claras sobre como agir em caso de fraude.
    Use linguagem simples, não invente dados financeiros e nunca peça a senha do usuário.
    Baseie-se apenas nestas diretrizes:
    1. Cartão Clonado: Orientar a bloquear o cartão imediatamente no app e contestar a compra.
    2. Golpe do Pix: Orientar a acionar o chat do banco urgente para tentar o bloqueio cautelar (MED) e registrar um B.O.
    3. Phishing (Links Falsos): O banco nunca envia links pedindo senhas. Se o cliente clicou, ele deve trocar a senha imediatamente.
    """

    # Configurando o modelo (o Gemini)
    modelo = genai.GenerativeModel(
        model_name="gemini-1.5-flash",
        system_instruction=instrucoes
    )

    # Iniciando a conversa
    chat = modelo.start_chat(history=[])
    print("\n[Sistema pronto! Digite 'sair' para encerrar]\n")

    while True:
        pergunta = input("Você: ")
        if pergunta.lower() == 'sair':
            print("\nSegurIA: Obrigado por entrar em contato. Fique seguro!")
            break
        
        print("SegurIA está digitando...")
        resposta = chat.send_message(pergunta)
        print(f"\nSegurIA: {resposta.text}\n")

except Exception as e:
    print(f"\n[ERRO] Ops! Verifique se você colou a sua chave de API corretamente. Detalhe do erro: {e}")
