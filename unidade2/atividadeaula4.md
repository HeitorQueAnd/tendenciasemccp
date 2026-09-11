# Atividade prática - Programação assistida por inteligência artificial

**Entrega em notebook:** [atividadeaula4.ipynb](atividadeaula4.ipynb), com os códigos completos e comentados, comparação das versões, demonstrações e testes executáveis.

- **Aluno:** Heitor Andrade
- **Curso:** Ciência da Computação - UDF
- **Disciplina:** Tendências em Ciência da Computação
- **Professora:** Kadidja Valéria
- **Unidade:** 2
- **Data:** 10/09/2026
- **Miniprojeto escolhido:** Jogo da Forca - nível intermediário
- **Ferramentas utilizadas nesta entrega:** Python, terminal e Codex como assistente de IA.

## 1. Objetivo e escolha do projeto

A proposta da atividade é usar a IA como apoio durante a programação, construir uma base e depois avaliar e melhorar o código. O trabalho segue o ciclo apresentado no material: contextualizar, avaliar criticamente, refatorar e decidir o que integrar.

Escolhi o jogo da forca porque ele permite trabalhar com repetição, condições, coleções e funções em um problema fácil de visualizar. Apesar de parecer simples, o jogo exige atenção a situações como repetir uma letra, digitar uma entrada inválida ou descobrir uma letra que aparece várias vezes na palavra.

O objetivo foi entregar um jogo de terminal que funcionasse e cujo código fosse fácil de explicar. A atividade foi desenvolvida com assistência de IA, incluindo implementação, revisão e execução dos testes. Não houve uma sessão separada com GitHub Copilot, Replit ou Colab; o ambiente utilizado foi o projeto local com Python.

## 2. Regras definidas

1. O programa sorteia uma palavra de uma lista ligada à computação.
2. A palavra começa oculta, com um traço para cada letra.
3. O jogador informa uma letra por vez e pode cometer até seis erros.
4. Um acerto revela todas as ocorrências daquela letra.
5. Uma letra válida que não pertence à palavra consome uma chance.
6. Letras repetidas e entradas inválidas não consomem chances.
7. Letras maiúsculas são convertidas para minúsculas; espaços nas extremidades são removidos.
8. O jogador vence ao descobrir todas as letras e perde ao atingir o limite de erros.
9. Ao terminar, o programa informa o resultado e revela a palavra.

Para manter o escopo adequado à atividade, o jogo aceita letras de **A a Z, sem acentos**. O banco de palavras segue essa regra. Não há cadastro, acesso à internet nem instalação de bibliotecas externas.

## 3. Versão inicial

Código completo: [forca_base.py](jogo_da_forca/forca_base.py).

A base usa a palavra fixa `python`, uma lista para guardar as tentativas e um `while` para manter a partida em execução. Dentro do laço, um `for` percorre a palavra e monta sua exibição. A mesma função concentra a entrada, as regras e as mensagens.

Essa versão permite jogar com entradas simples, mas apresenta limitações:

- A mesma letra errada desconta uma chance a cada repetição.
- Letras maiúsculas não são normalizadas.
- Números, símbolos e entradas com várias letras não são validados.
- A palavra é sempre a mesma.
- A mistura entre regras e interface dificulta testar partes isoladas.

Um detalhe interessante é que a entrada vazia passa pela condição `tentativa not in palavra` sem contar como erro, porque a string vazia está contida em qualquer string em Python. Mesmo assim, o programa não explica ao jogador que a entrada é inválida. Isso mostra como uma condição aparentemente simples pode não representar a regra desejada.

### Evidência do problema

Na execução da base com as entradas `b`, `b`, `p`, `y`, `t`, `h`, `o`, `n`, o contador passou de **1 para 2** após repetir `b`. O jogador acabou vencendo, mas recebeu duas penalidades pela mesma tentativa. Essa execução foi reproduzida no terminal com entradas controladas.

A versão inicial foi preservada para permitir a comparação com a solução final.

## 4. Roteiro de prompts estruturados

Os prompts abaixo são um roteiro reproduzível para orientar a construção, a revisão e a validação desta solução. Eles não são uma transcrição de conversas anteriores nem comprovantes de uso de outra ferramenta.

### Prompt 1 - Contexto e construção da base

```text
Atue como um parceiro de programação em Python para um estudante de Ciência
da Computação. Preciso desenvolver um jogo da forca de terminal para uma
atividade sobre colaboração entre humanos e IA.

Comece com uma versão básica usando a palavra fixa "python", uma lista de
tentativas e até seis erros. Mostre as letras descobertas, informe vitória
ou derrota e use apenas a biblioteca padrão. Explique o funcionamento e
aponte as limitações dessa primeira versão, sem tratá-la como produto pronto.
```

Esse pedido delimita o problema e o nível de complexidade. Também pede uma análise das limitações, para que a primeira resposta seja um ponto de partida.

### Prompt 2 - Refatoração com critérios verificáveis

```text
Revise a versão inicial em forca_base.py e produza uma versão refatorada.
Separe a exibição da palavra, a validação da letra e o controle da partida
em funções. Use um conjunto para armazenar tentativas sem duplicação.

Regras: aceite uma letra de A a Z sem acento, normalize maiúsculas e espaços
nas extremidades, rejeite entradas vazias e não desconte chances por letras
repetidas ou entradas inválidas. Revele todas as ocorrências de um acerto.
Sorteie a palavra de uma lista e mostre as tentativas e os erros na tela.

Mantenha o código compreensível para um estudante. Explique quais alterações
são de organização e quais corrigem ou acrescentam comportamentos.
```

Aqui o pedido deixa de ser apenas “melhore esse código”. As regras permitem conferir se a alteração resolveu o problema. Separar funções é uma refatoração; mudar o tratamento de entradas e sortear palavras são correções e melhorias de comportamento.

### Prompt 3 - Depuração de um problema concreto

```text
Na versão inicial, a palavra é "python". Ao digitar "b" duas vezes, o
contador de erros passa de 0 para 1 e depois para 2. Pela regra definida,
uma letra repetida deve gerar um aviso e manter o contador em 1.

Identifique a causa e organize a validação antes da atualização do estado.
Verifique também se " B " é reconhecida como a mesma tentativa.
```

Esse prompt informa entrada, resultado observado e resultado esperado. A causa está na ausência de uma verificação de repetição antes de incrementar os erros. Na solução final, a entrada é normalizada e validada antes de entrar no conjunto de tentativas.

### Prompt 4 - Validação da solução

```text
Crie testes com unittest para as regras do jogo e para partidas completas.
Cubra vitória, derrota após seis erros, letra repetida, entrada vazia,
números, acentos, maiúsculas e palavras com letras repetidas.

Use entradas controladas para que os testes não dependam de digitação nem
de sorteio. Verifique também o encerramento por fim de entrada ou Ctrl+C.
Execute os testes e informe o resultado real, sem inventar evidências.
```

## 5. Solução final e decisões de implementação

Código completo: [forca.py](jogo_da_forca/forca.py).

| Parte | Responsabilidade | Motivo da escolha |
|---|---|---|
| `revelar_palavra` | Montar a palavra com letras descobertas e traços | Permite testar a exibição sem iniciar uma partida. |
| `validar_letra` | Normalizar e verificar a entrada | Evita alterar o jogo com uma tentativa inválida. |
| `jogar` | Controlar tentativas, erros e resultado | Reúne as regras e recebe uma palavra conhecida para os testes. |
| `main` | Sortear a palavra e tratar o encerramento | Separa o início do programa da execução de uma partida. |

As tentativas ficam em um `set`, que é uma coleção sem elementos duplicados. A função de validação continua necessária: o conjunto evita armazenar duplicatas, mas sozinho não impede que o código desconte outra chance.

Para descobrir a vitória, o programa verifica se todas as letras distintas da palavra estão entre as tentadas, usando `issubset`. Na palavra `dados`, por exemplo, basta acertar `d`, `a`, `o` e `s`: a letra `d` aparece duas vezes na tela, mas precisa ser informada apenas uma vez.

A exibição usa `join` para juntar letras e traços com espaços. Como conjuntos não garantem uma ordem de apresentação apropriada para o jogador, o histórico é mostrado em ordem alfabética com `sorted`.

### Comparação entre as versões

| Critério | Versão inicial | Versão final |
|---|---|---|
| Palavra | Fixa: `python` | Sorteada de seis opções |
| Estrutura | Uma função concentra tudo | Funções com responsabilidades definidas |
| Letras tentadas | Lista com possíveis repetições | Conjunto e validação de repetição |
| Entrada inválida | Sem aviso específico | Mensagem e nova tentativa sem penalidade |
| Maiúsculas e espaços externos | Não tratados | Normalizados antes da comparação |
| Erro repetido | Consome outra chance | Mostra aviso e mantém o contador |
| Exibição | Palavra e erros | Palavra, limite de erros e histórico |
| Validação automatizada | Base preservada como comparação | 16 testes automatizados |

Para este tamanho de jogo, considero a clareza e a correção mais importantes do que buscar ganhos de velocidade. O conjunto também facilita consultas, mas não foi feito benchmark; portanto, não atribuo um percentual de desempenho à refatoração.

## 6. Testes e resultados

Arquivo: [test_forca.py](jogo_da_forca/test_forca.py).

Os testes foram executados no ambiente local com **Python 3.13.3**, usando `unittest` e entradas simuladas por `unittest.mock`. Os cenários são determinísticos: o teste passa a palavra diretamente para `jogar`, evitando depender do sorteio.

| Cenário | Resultado verificado |
|---|---|
| Nenhuma letra descoberta | Palavra totalmente oculta. |
| Letra presente várias vezes | Todas as ocorrências aparecem. |
| Todas as letras descobertas | Palavra completa e vitória. |
| Entrada ` A ` | Convertida para `a`. |
| Entrada vazia, números, símbolos, acentos e múltiplas letras | Rejeitados. |
| Letra repetida após normalização | Rejeitada com mensagem específica. |
| Validação de uma letra | Não modifica o conjunto recebido. |
| Partida com `dados` e tentativas `d`, `a`, `o`, `s` | Vitória em quatro entradas. |
| Seis letras erradas distintas | Derrota exatamente no sexto erro. |
| Entradas inválidas durante a partida | Não consomem chances. |
| Repetição de erro ou acerto | Não gera nova penalidade. |
| Acerto depois de cinco erros | Vitória ainda permitida. |
| Palavra ou limite incompatível com as regras | Erro de configuração informado. |
| Fim da entrada ou Ctrl+C | Encerramento com mensagem, sem traceback. |

Alguns métodos verificam várias entradas usando `subTest`, por isso a quantidade de exemplos é maior que o número de métodos de teste.

Comando executado a partir da raiz do repositório:

```bash
python3 -B -m unittest discover -s unidade2/jogo_da_forca -p 'test_*.py' -v
```

Resultado observado:

```text
Ran 16 tests in 0.008s

OK
```

O tempo pode variar em outra execução. Os testes demonstram o funcionamento dos cenários cobertos; não significam que qualquer problema possível foi eliminado.

### Exemplo de partida validada

Também foi executada uma partida com a palavra `dados` e a sequência `1`, `x`, `x`, `D`, `a`, `o`, `s`.

| Entrada | Comportamento observado | Total de erros |
|---|---|---:|
| `1` | Rejeitada por não ser letra | 0 |
| `x` | Letra ausente na palavra | 1 |
| `x` | Aviso de letra repetida | 1 |
| `D` | Normalizada; revela `d _ d _ _` | 1 |
| `a` | Revela `d a d _ _` | 1 |
| `o` | Revela `d a d o _` | 1 |
| `s` | Revela `d a d o s` e encerra com vitória | 1 |

Trecho final da saída real:

```text
Palavra: d a d o s
Erros: 1/6
Você venceu! A palavra era: dados
```

## 7. Análise crítica dos exemplos de refatoração do material

### Soma de lista

Trocar um `while` com índice por `sum(numeros)` deixa a intenção mais clara e elimina o controle manual do índice. Para uma lista de inteiros, ambas as versões percorrem os elementos e têm complexidade de tempo **O(n)**. Portanto, reduzir o número de linhas não significa mudar automaticamente a ordem de complexidade.

```python
numeros = [10, 20, -5]
soma = sum(numeros)
assert soma == 25
assert sum([]) == 0
```

### Verificação de número primo

O material mostra a redução da busca por divisores até a raiz quadrada do número. A ideia funciona porque, se um número composto é escrito como produto de dois fatores, pelo menos um deles é menor ou igual à sua raiz quadrada.

Porém, as versões apresentadas precisam de uma verificação para `n < 2`. Sem ela, `0` e `1` acabam classificados como primos; na versão com `sqrt`, números negativos ainda podem provocar erro. A solução abaixo usa `isqrt`, que calcula a raiz quadrada inteira sem conversão para ponto flutuante.

```python
from math import isqrt


def eh_primo(n: int) -> bool:
    if n < 2:
        return False
    for divisor in range(2, isqrt(n) + 1):
        if n % divisor == 0:
            return False
    return True


assert not eh_primo(-7)
assert not eh_primo(0)
assert not eh_primo(1)
assert eh_primo(2)
assert eh_primo(97)
assert not eh_primo(49)
```

A função recebe números inteiros. A contagem de candidatos a divisor cai de **O(n)** para **O(√n)** no pior caso, considerando cada operação aritmética com custo constante. O `+ 1` é necessário para incluir a raiz inteira no teste e identificar quadrados perfeitos, como `49`.

### Inversão de string

O fatiamento `texto[::-1]` expressa a inversão de forma curta e legível. A versão que coloca cada letra no início de uma nova string copia trechos progressivamente maiores, tendo custo quadrático; o fatiamento percorre o texto com custo linear e produz uma nova string.

```python
def inverte_texto(texto: str) -> str:
    return texto[::-1]


assert inverte_texto("python") == "nohtyp"
assert inverte_texto("") == ""
assert inverte_texto("a") == "a"
```

Essa inversão opera sobre os pontos de código da string. Ela atende aos exemplos simples da aula, mas não resolve sozinha a inversão visual de todos os emojis compostos ou caracteres com marcas combinantes.

Esses exemplos mostram por que a revisão continua necessária: um código pode ficar menor ou mais eficiente e ainda ter um erro nas condições de entrada.

## 8. Reflexão sobre a colaboração humano-IA

### Em que a IA contribuiu?

A IA apoiou a criação das versões, a separação das funções, o tratamento de entradas e a elaboração dos testes. Ela também ajudou a transformar regras escritas em comportamentos verificáveis, como não penalizar uma letra repetida.

### O que precisa continuar sob decisão humana?

É necessário definir as regras, avaliar se as sugestões fazem sentido e compreender o que será entregue. Por exemplo, aceitar acentos ou permitir que o jogador tente a palavra inteira são decisões do projeto, não algo que a IA deveria presumir sem contexto.

Minha avaliação é que a regra de repetição merece atenção especial. Mesmo utilizando um conjunto, o erro continuaria existindo se o contador fosse atualizado antes da validação. A escolha da estrutura de dados não substitui a análise da ordem das operações.

### Qual foi a melhoria mais relevante?

Considero a separação entre validar e alterar o estado a melhoria mais relevante. Primeiro o programa verifica a entrada; somente depois registra a tentativa e decide se aumenta os erros. Isso torna a regra mais fácil de entender e evita penalidades indevidas.

### Quais são os limites da solução?

O banco contém apenas seis palavras, não há níveis de dificuldade, pontuação persistente ou interface gráfica. A validação aceita apenas letras sem acento e não permite tentar a palavra inteira. Essas limitações são compatíveis com a proposta de um miniprojeto de terminal.

Uma evolução possível seria separar também toda a entrada e saída das regras, permitindo reaproveitar o jogo em outra interface. Para esta entrega, funções pequenas e testes de partidas foram suficientes para manter o código compreensível.

### O que levo da atividade?

Para mim, a principal conclusão é que usar IA para programar exige saber avaliar o resultado. Um prompt estruturado ajuda, mas a confiança no código precisa vir da compreensão das regras e da validação. O exemplo de números primos reforça isso: otimizar o laço sem tratar `0` e `1` deixaria a solução incorreta.

## 9. Como executar e conferir a entrega

É necessário ter **Python 3.10 ou superior**. Os comandos abaixo devem ser executados na raiz do repositório. Não é preciso instalar pacotes com `pip`.

Para jogar a versão final:

```bash
python3 unidade2/jogo_da_forca/forca.py
```

Para executar a base e comparar:

```bash
python3 unidade2/jogo_da_forca/forca_base.py
```

Para verificar os testes:

```bash
python3 -B -m unittest discover -s unidade2/jogo_da_forca -p 'test_*.py' -v
```

No Windows, se `python3` não estiver disponível, pode-se usar `py -3` no lugar dele.

### Arquivos da entrega

- [atividadeaula4.md](atividadeaula4.md): relatório, roteiro de prompts, análise crítica e resultados.
- [forca_base.py](jogo_da_forca/forca_base.py): versão inicial preservada.
- [forca.py](jogo_da_forca/forca.py): jogo refatorado e executável.
- [test_forca.py](jogo_da_forca/test_forca.py): testes das regras e das partidas.

## 10. Material de referência

VALÉRIA, Kadidja. **Programação Assistida por Inteligência Artificial: o novo paradigma da colaboração humano-máquina.** Material da disciplina, UDF, disponibilizado em [Collaborative_AI_Programming_AtividadePrática.pdf](Collaborative_AI_Programming_AtividadePrática.pdf).

Foram utilizados o ciclo de colaboração da página 4, os exemplos de refatoração das páginas 5 a 7, o desafio de miniprojeto da página 9, o roteiro de prompts da página 10 e a discussão sobre responsabilidade das páginas 11 e 12.
