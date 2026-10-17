# Monitoramento de Reservatório de Água

Projeto educacional em Python que simula o monitoramento de um reservatório pelo terminal. O usuário informa um nível de 1 a 5 e o programa exibe a situação com a cor correspondente, utilizando a biblioteca Colorama.

## Níveis e cores

| Nível | Situação | Cor |
|---|---|---|
| 1 | Muito baixo (crítico) | Vermelho |
| 2 | Baixo | Amarelo |
| 3 | Médio | Verde |
| 4 | Alto | Ciano |
| 5 | Muito alto (alerta) | Azul |

## Requisitos

- Python 3 instalado.
- Terminal com suporte a cores.
- Biblioteca Colorama, instalada conforme as instruções abaixo.

## Instalação e execução

Baixe o projeto pelo botão **Code → Download ZIP** do GitHub e extraia os arquivos. Abra um terminal dentro da pasta extraída.

Instale a dependência:

```bash
python -m pip install -r requirements.txt
```

Execute o programa:

```bash
python reservatorio.py
```

Use o mesmo interpretador Python para instalar a dependência e executar o arquivo. No Windows, se você utiliza o comando `py`, substitua `python` por `py` nos dois comandos.

## Exemplo de uso

```text
=== Monitoramento do reservatório ===
Informe o nível da água (1 a 5): 3
Nível 3: Médio
```

A última linha aparece em verde. O programa encerra após uma consulta; execute-o novamente para testar outro nível.

## Organização do código

- `situacoes`: lista com as cinco mensagens.
- `definir_cor(nivel)`: retorna a cor correspondente ao nível.
- `exibir_situacao(nivel)`: valida o intervalo de 1 a 5 e exibe a mensagem colorida.
- `main()`: solicita a entrada e trata valores que não sejam números inteiros.
- `Style.RESET_ALL`: restaura o estilo padrão do terminal após a mensagem.

## Verificação manual

Execute o programa novamente para cada entrada:

| Entrada | Resultado esperado |
|---|---|
| 1 a 5 | Mensagem e cor correspondentes à tabela de níveis |
| 0 ou 6 | Nível inválido. Informe um número entre 1 e 5. |
| abc ou 2.5 | Entrada inválida. Digite um número inteiro. |

## Arquivos

- `reservatorio.py`: código-fonte do programa.
- `requirements.txt`: dependência e versão utilizada.
- `README.md`: documentação do projeto.
- `.gitignore`: arquivos locais que não devem ser versionados.

## Limitação

Esta é uma simulação com entrada manual. O programa não utiliza sensores nem faz leituras automáticas de um reservatório real.
