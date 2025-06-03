
# 🤖 Repositório de Automações com Python

Este repositório contém scripts desenvolvidos em Python para automatizar tarefas repetitivas, como o preenchimento de formulários e o uso de dados em arquivos `.csv`.

## 📌 Automações Disponíveis

### ✅ Cadastro de Produtos

Automação que preenche um formulário de cadastro de produtos em um site, usando como base os dados de um arquivo `produto.csv`.

**Funcionalidades:**
- Abre o navegador e acessa a URL de login.
- Realiza o login automaticamente com usuário e senha.
- Lê os dados da planilha `produto.csv`.
- Preenche o formulário com os dados do produto.
- Envia o formulário e repete o processo para cada item.

## ▶️ Como Executar

### 1. Instale os requisitos:

```bash
pip install pandas pyautogui
````

### 2. Prepare os arquivos:

* `codigo.py`: script principal da automação.
* `produto.csv`: planilha com os dados dos produtos.

### 3. Execute o script:

```bash
python codigo.py
```

⚠️ **Importante:** Não mexa no mouse nem no teclado durante a execução, pois o `pyautogui` depende da posição e interação com a tela.

## 📝 Sobre o CSV

Exemplo de estrutura do `produto.csv`:

```csv
codigo,marca,tipo,categoria,preco_unitario,custo,obs
P001,Nike,Tênis,Calçados,299.90,180.00,"Promoção mês dos pais"
P002,Adidas,Camiseta,Vestuário,129.90,70.00,"Nova coleção verão"
```

## 📅 Próximas Automações

* [ ] Automação de envio de e-mails com anexos
* [ ] Preenchimento automático de relatórios em Excel
* [ ] Integração com sistemas internos via navegador

Essas automações serão adicionadas neste mesmo repositório.

## 👤 Autor

**Eliel Diniz**
📧 [elielidniz@gomal.com](mailto:elielidniz@gomal.com)

