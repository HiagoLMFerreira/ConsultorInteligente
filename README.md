## Arquivos
- `conhecimento.py`: perguntas, valores internos e nomes das dez carreiras.
- `motor_inferencia.py`: 25 regras `@Rule` e diagnóstico explicável.
- `exemplo_console.py`: questionário executável no terminal.
- `testes.py`: quatro perfis para verificação automática.

## Executar
Use preferencialmente Python 3.10 em um ambiente virtual:

```bash
python -m pip install -r requirements.txt
python testes.py
python exemplo_console.py
```

**Compatibilidade:** a dependência `Experta` pode apresentar problemas em algumas versões de Python por causa de dependências antigas (`frozendict`). Se a instalação não funcionar, verifique a versão do Python e das bibliotecas; não altere as regras para contornar o problema.

## Observações
As regras são heurísticas educacionais, não um teste psicométrico validado. A ausência de regras ativadas gera um resultado inconclusivo. Empates são resolvidos por objetivo declarado, quando ele faz parte dos empatados, ou pela ordem das carreiras definida em `conhecimento.py`.
