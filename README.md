# PontoBateitorDefinitiveEdition - 🕒 Automação de Registro de Folha de Ponto - Python + Selenium

Este projeto automatiza o preenchimento da folha de ponto no sistema SARH, utilizando Python e Selenium. Ele identifica dias com saldo negativo e insere justificativas automaticamente como "Evento Externo", poupando tempo e evitando esquecimentos.

---

## 🚀 Funcionalidades

- Acessa o sistema SARH automaticamente.
- Identifica dias editáveis no mês atual e anterior.
- Preenche campos com base no saldo negativo do dia.
- Insere justificativa configurada.
- Salva os registros automaticamente.

---

## 🛠️ Tecnologias Utilizadas

- Python 3.x
- Selenium WebDriver
- Google Chrome + ChromeDriver

---

## 📁 Estrutura dos Arquivos

- `main.py`: Script principal da automação.
- `util.py`: Funções auxiliares (validação, leitura e escrita de arquivos).
- `variaveis.py`: Armazena o texto da justificativa e a URL do Painel do Servidor.

---

## ⚙️ Pré-requisitos

1. Ter Python 3 instalado.
2. Instalar a biblioteca `selenium`:
3. Ter o chromedriver.exe compatível com sua versão do Google Chrome na raiz do projeto.
4. Acesso à rede interna que permita abrir o endereço do sistema.


## ▶️ Como usar
Clone o repositório e execute o script:

git clone https://github.com/brunoaraujosoares/PontoBateitorDefinitiveEdition.git
cd automacao-folha-ponto
python main.py

No primeiro uso, o navegador será aberto e você poderá inserir sua senha manualmente. O sistema armazenará o link do Painel do Servidor para usos futuros.

🔐 Aviso
Este projeto é de uso pessoal e educacional. Certifique-se de seguir as diretrizes da sua instituição antes de utilizar esta automação.
