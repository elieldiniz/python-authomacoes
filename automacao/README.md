Perfeito! Aqui está a versão do `README.md` **sem o esquema de pastas**:

---

````markdown
# 🖱️ Automação de Cadastro de Produtos com PyAutoGUI e Pandas

Este projeto é uma automação em Python que preenche automaticamente um formulário web com dados de um arquivo `.csv`, utilizando `PyAutoGUI` para simular ações do teclado e mouse, e `pandas` para ler os dados.

## 🚀 Objetivo

Automatizar o cadastro de produtos em um site, evitando o trabalho manual e acelerando o processo com precisão.

## 🧠 Tecnologias Utilizadas

- **Python 3.11**
- [PyAutoGUI](https://pyautogui.readthedocs.io/en/latest/)
- [Pandas](https://pandas.pydata.org/)
- Módulo `time` (padrão do Python)

## 📄 Estrutura esperada do CSV

O arquivo `produto.csv` deve conter:

```csv
codigo,marca,tipo,categoria,preco_unitario,custo,obs
P001,Nike,Tênis,Calçados,299.90,180.00,"Promoção mês dos pais"
P002,Adidas,Camiseta,Vestuário,129.90,70.00,"Nova coleção verão"
````

## 🛠️ Como Usar

1. Instale as dependências:

```bash
pip install pyautogui pandas
```

2. Execute o script:

```bash
python codigo.py
```

O script fará o seguinte:

* Abrirá o navegador Chrome
* Acessará a URL do formulário
* Realizará login automaticamente
* Lerá os dados da planilha `produto.csv`
* Preencherá e enviará o formulário para cada produto da planilha

## ⚠️ Cuidados

* Certifique-se de que a janela do navegador esteja maximizada e na mesma posição sempre que for rodar o script.
* Durante a execução, **não mova o mouse nem digite nada**.
* As coordenadas dos cliques devem ser ajustadas para o seu monitor. Você pode usar:

```python
pyautogui.position()
```

para descobrir as posições corretas na tela.

## ✅ Melhorias Futuras

* Detecção de campos com reconhecimento de imagem ao invés de coordenadas fixas
* Tratamento de erros e mensagens de log
* Leitura de múltiplas linhas da planilha de forma dinâmica (já parcialmente implementado)

## 👨‍💻 Autor

**Eliel Diniz**

```

---

Se quiser, posso também gerar o README diretamente formatado como arquivo `.md`. Deseja isso?
```
