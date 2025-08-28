# IQ Option API (Custom Fork)

[![Python Version](https://img.shields.io/badge/python-3.8%2B-blue.svg)](https://www.python.org/)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)

Este é um fork customizado da API não-oficial para a plataforma de negociação IQ Option, contendo modificações e atualizações específicas, como a inclusão de novos pares de ativos.

## 📖 Descrição

Esta biblioteca em Python fornece uma interface para interagir com a API da IQ Option, permitindo que desenvolvedores criem robôs de negociação, automatizem estratégias e acessem dados de mercado em tempo real. A comunicação é feita principalmente via WebSockets.

Este fork foi extraído do projeto [SyncMT4](https://github.com/williansandi/Sync_MT4_Py) e é mantido separadamente para facilitar a reutilização e o versionamento.

## ✅ Instalação

Atualmente, a biblioteca pode ser instalada diretamente do GitHub.

Adicione a seguinte linha ao seu arquivo `requirements.txt`:

```
-e git+https://github.com/williansandi/iqoptionapi-2025-Atualizada-.git#egg=iqoptionapi
```

Ou instale via `pip`:

```sh
pip install git+https://github.com/williansandi/iqoptionapi-2025-Atualizada-.git
```

## 🚀 Uso Básico

Aqui está um exemplo simples de como se conectar e obter o saldo da conta:

```python
from iqoptionapi.stable_api import IQ_Option
import logging

# Ativa o log para ver as mensagens da API
logging.basicConfig(level=logging.INFO, format='%(asctime)s %(message)s')

# Suas credenciais
email = "seu-email@exemplo.com"
senha = "sua-senha"

# Cria uma instância da API
Iq = IQ_Option(email, senha)

# Conecta à IQ Option
check, reason = Iq.connect()

if check:
    print("Conectado com sucesso!")
    
    # Define o tipo de conta (PRACTICE / REAL)
    Iq.change_balance('PRACTICE')
    
    # Obtém o saldo
    balance = Iq.get_balance()
    print(f"Saldo da conta: {balance}")
    
else:
    print(f"Falha na conexão: {reason}")

```

## 🛠️ Principais Funcionalidades

*   Conexão e reconexão automática.
*   Seleção de conta (Real ou Prática).
*   Execução de ordens (Binárias e Digitais).
*   Verificação do resultado das operações.
*   Acesso a dados de velas (`get_candles`).
*   Obtenção de informações de ativos abertos.
*   E muito mais.

## 🤝 Contribuição

Contribuições são bem-vindas! Se você tiver sugestões ou correções, sinta-se à vontade para abrir uma *issue* ou um *pull request*.

1.  Faça um Fork do projeto.
2.  Crie sua Feature Branch (`git checkout -b feature/NovaFuncionalidade`).
3.  Faça o Commit de suas alterações (`git commit -m 'Adiciona NovaFuncionalidade'`).
4.  Faça o Push para a Branch (`git push origin feature/NovaFuncionalidade`).
5.  Abra um Pull Request.

## 📄 Licença

Distribuído sob a Licença MIT.