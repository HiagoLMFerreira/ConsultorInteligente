"""Quatro perfis de teste e uma verificação de entrada inconclusiva."""
from motor_inferencia import analisar_respostas

BASE = dict(matematica='media', atividade='apis', ferramenta='java', entrega='sistema',
            ambiente='programacao', resolver='codigo', estudo='apis',
            programacao='gosto', aspecto='logica', objetivo='sistemas')

CASOS = [
    ('Back-end', BASE, 'backend'),
    ('Ciência de Dados', dict(BASE, matematica='alta', atividade='modelos',
        ferramenta='python', entrega='previsoes', resolver='padroes',
        estudo='machine_learning', aspecto='inteligencia', objetivo='ia'), 'ciencia'),
    ('Cibersegurança', dict(BASE, atividade='seguranca', ferramenta='linux',
        entrega='protecao', ambiente='seguranca', resolver='riscos',
        estudo='criptografia', aspecto='protecao', objetivo='seguranca'), 'seguranca'),
    ('Front-end', dict(BASE, atividade='interfaces', ferramenta='javascript',
        entrega='interface', ambiente='design', resolver='usuario',
        estudo='interfaces', aspecto='usabilidade', objetivo='experiencias'), 'frontend'),
]

for nome, respostas, esperado in CASOS:
    resultado = analisar_respostas(respostas)
    assert resultado['codigo'] == esperado, (nome, resultado)
    print(f"[OK] {nome}: {resultado['carreira']} ({len(resultado['motivos'])} regras)")

if __name__ == '__main__':
    print('Testes concluídos.')
