# Consultor Inteligente de Carreiras em TI

## Sobre o projeto

Este projeto foi desenvolvido como atividade da disciplina de **Inteligência Artificial**, do curso de Ciência da Computação da UNIPAC.

O objetivo é criar um Sistema Especialista capaz de recomendar uma área de atuação em Tecnologia da Informação com base nos interesses, conhecimentos e preferências do usuário.

O sistema utiliza regras lógicas do tipo **SE–ENTÃO** para analisar as respostas de um questionário e identificar a carreira mais compatível com o perfil informado.

## Tecnologias utilizadas

- **Python:** linguagem utilizada no desenvolvimento do sistema.
- **Experta:** biblioteca responsável pelo motor de inferência e pela execução das regras.
- **Streamlit:** biblioteca utilizada para desenvolver a interface web.
- **Unittest:** ferramenta utilizada para realizar testes automatizados.

## Como funciona

O funcionamento do sistema é dividido em quatro etapas:

1. **Questionário:** o usuário responde a 10 perguntas relacionadas aos seus interesses e preferências profissionais.
2. **Análise das respostas:** as informações fornecidas são transformadas em fatos para o motor de inferência.
3. **Aplicação das regras:** o Experta verifica quais das 25 regras lógicas são compatíveis com as respostas.
4. **Recomendação:** o sistema apresenta a carreira mais adequada, acompanhada das justificativas que contribuíram para a escolha.

O sistema utiliza o conceito de **encadeamento para frente**, partindo dos fatos informados pelo usuário para chegar a uma conclusão.

## Carreiras disponíveis

O sistema pode recomendar uma das seguintes áreas:

1. Desenvolvimento Back-end
2. Desenvolvimento Front-end & UI/UX
3. Ciência de Dados e Machine Learning
4. Engenharia de Dados
5. Cibersegurança
6. DevOps & SRE
7. Computação em Nuvem
8. Desenvolvimento Mobile
9. Engenharia de Qualidade e Testes (QA)
10. Gestão de Produtos

## Estrutura dos arquivos

- `app.py`: interface web desenvolvida com Streamlit.
- `conhecimento.py`: perguntas, respostas possíveis e informações das carreiras.
- `motor_inferencia.py`: implementação das 25 regras e do motor de inferência utilizando Experta.
- `exemplo_console.py`: permite utilizar o questionário diretamente pelo terminal.
- `testes.py`: contém os testes automatizados para verificar o funcionamento do sistema.
- `requirements.txt`: lista as bibliotecas necessárias para executar o projeto.

## Como executar

Recomenda-se utilizar Python 3.10 em um ambiente virtual.

**1. Instalar as dependências**

```bash
python -m pip install -r requirements.txt
```

**2. Executar os testes**

```bash
python testes.py
```

**3. Iniciar a interface web**

```bash
python -m streamlit run app.py
```

Após executar o comando, a aplicação poderá ser acessada pelo navegador, normalmente no endereço:

`http://localhost:8501`

Também é possível utilizar o sistema pelo terminal:

```bash
python exemplo_console.py
```

## Testes e validação

Foram desenvolvidos testes automatizados para verificar o funcionamento do motor de inferência.

A validação contempla as dez carreiras disponíveis, a aplicação das regras, o tratamento de respostas inválidas e situações de empate ou resultados inconclusivos.

Durante os testes realizados no PyCharm, o sistema apresentou o seguinte resultado:

```text
Ran 9 tests in 0.986s

OK
```

Esse resultado indica que os nove testes automatizados foram executados sem apresentar falhas.

## Observações

As recomendações são realizadas com base em regras previamente definidas, considerando as características e preferências informadas pelo usuário.

O sistema possui finalidade educacional e não substitui uma orientação profissional especializada.

Quando nenhuma regra é ativada, o resultado é considerado inconclusivo. Em situações de empate, o sistema considera o objetivo profissional informado ou a ordem das carreiras definida na base de conhecimento.

A biblioteca Experta também pode apresentar problemas de compatibilidade com determinadas versões do Python devido a dependências antigas, como o `frozendict`.
