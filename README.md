



📑 Tabela de Conteúdo

Introdução

Arquitetura

Recursos Principais

Demonstração

Instalação

Como Executar

Exemplos de Uso

Estrutura do Projeto

Extensões Avançadas

Contribuindo

Licença

🚀 Introdução

Este projeto implementa um Agente de IA totalmente local, utilizando:

Ollama para execução de modelos LLM offline

Mistral como modelo principal

LangChain (LCEL) para lógica inteligente

Ferramentas integradas para execução de comandos Linux

Ideal para automação, DevOps, segurança, SOC, aprendizado ou estudos sobre agentes inteligentes.

🏗 Arquitetura
flowchart TD

User --> AgenteIA
AgenteIA -->|consulta| LLM[Mistral via Ollama]
LLM -->|decisão| FerramentaTerminal[Tool: Terminal Linux]
FerramentaTerminal --> Linux[Ubuntu VM]

AgenteIA --> Histórico[Memória da Conversa]

✨ Recursos Principais

✔ IA totalmente offline (sem API externa)
✔ Execução de comandos Linux via linguagem natural
✔ Histórico das conversas com contexto
✔ Compatível com LangChain moderno
✔ Extensível com novas ferramentas
✔ Seguro, privado e fácil de usar

🎥 Demonstração
🧠 Pergunta simples:
Você: O que é Kubernetes?
IA: Kubernetes é uma plataforma de orquestração de containers...

💻 Execução de comandos:
Você: Liste os arquivos da pasta atual.
IA: (usa a ferramenta terminal e retorna o resultado)

🔧 Criação de arquivo:
Você: Crie um arquivo chamado teste.txt com o conteúdo "agente funcionando".

📦 Instalação
1. Clone o repositório
git clone git@github.com:cleitondss81/agente-ia-ollama.git
cd agente-ia-ollama

2. Ambiente virtual
python3 -m venv ia_agent
source ia_agent/bin/activate

3. Instalar dependências
pip install -r requirements.txt

4. Instalar o Ollama
curl -fsSL https://ollama.com/install.sh | sh
ollama pull mistral

▶️ Como Executar
python agente.py

🧪 Exemplos de Uso
Liste os processos rodando.
Mostre meu uso de memória.
Explique o que é uma VPC.
Crie um script bash que organiza logs automaticamente.
Detecte falhas de login no /var/log/auth.log.

📁 Estrutura do Projeto
agente-ia-ollama/
│
├── agente.py
├── requirements.txt
├── README.md
└── .gitignore

🧩 Extensões Avançadas
🔥 1. Agente SOC Analyst

Leitura e análise de /var/log

Detecção de brute force

Análise de IOC (IP, hash)

Monitoramento de processos

🐳 2. Docker

Dockerfile

Execução isolada

🌐 3. Interface Web

Streamlit

Chat em tempo real

🤖 4. Multiagentes

Planejador + Executor

Uso de LangGraph / LCEL

Se quiser, posso gerar qualquer uma dessas versões.

🤝 Contribuindo

Sinta-se livre para abrir issues ou pull requests.
Toda contribuição é bem-vinda! 💙

📜 Licença

Este projeto está sob a Licença MIT.

👤 Autor

Cleiton S. dos Santos
GitHub: https://github.com/cleitondss81


Linux | DevOps | Segurança | Automação
