import subprocess
from langchain_core.tools import tool
from langchain_ollama import OllamaLLM
from langchain_core.prompts import ChatPromptTemplate, MessagesPlaceholder
from langchain_core.runnables import RunnableLambda
from langchain_core.messages import AIMessage, HumanMessage


# ---- Ferramenta que executa comando no Linux ----
@tool
def terminal(command: str) -> str:
    """Executa comandos no Linux e retorna a saída."""
    try:
        result = subprocess.check_output(command, shell=True, stderr=subprocess.STDOUT)
        return result.decode("utf-8")
    except subprocess.CalledProcessError as e:
        return e.output.decode("utf-8")


tools = [terminal]

# ---- Modelo local via Ollama (NOVO) ----
llm = OllamaLLM(model="mistral")


# ---- Prompt ----
prompt = ChatPromptTemplate.from_messages([
    ("system", "Você é um agente que pode usar ferramentas. "
               "Quando quiser rodar comandos Linux, use a ferramenta 'terminal'."),
    ("user", "{input}"),
    MessagesPlaceholder("history")
])


# ---- Lógica do agente ----
def agent_logic(inputs):
    formatted = prompt.invoke(inputs)
    response = llm.invoke(formatted)

    # Caso o modelo peça para usar ferramenta via JSON
    if isinstance(response, dict) and "tool" in response:
        tool_name = response["tool"]["name"]
        tool_input = response["tool"]["input"]

        for t in tools:
            if t.name == tool_name:
                result = t.run(tool_input)
                return AIMessage(content=result)

    # Se for string simples
    if isinstance(response, str):
        return AIMessage(content=response)

    # Se for mensagem com conteúdo
    return response


agent = RunnableLambda(agent_logic)

print("\n🤖 Agente IA Local (Mistral + Ollama) iniciado!")
print("Digite 'sair' para encerrar.\n")

history = []

while True:
    user_input = input("Você: ")

    if user_input.lower() in ["sair", "exit", "quit"]:
        print("Agente encerrado.")
        break

    result = agent.invoke({"input": user_input, "history": history})

    history.append(HumanMessage(content=user_input))
    history.append(result)

    print("\n" + result.content + "\n")
