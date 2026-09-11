"""Versão final do jogo da forca, para comparar com forca_base.py.

Como executar, a partir da raiz do repositório:
    python3 unidade2/jogo_da_forca/forca.py

Como executar os testes:
    python3 -B -m unittest discover -s unidade2/jogo_da_forca -p 'test_*.py' -v

O que foi refatorado:
    - A montagem da palavra foi extraída para revelar_palavra().
    - A validação da entrada ganhou uma função própria: validar_letra().
    - O início do programa ficou em main(), separado do controle da partida.
    - A lista de tentativas foi substituída por um conjunto (set).
    - A concatenação manual virou join(); a vitória é verificada por issubset().

Correções e funcionalidades acrescentadas à base:
    - Entradas inválidas e letras repetidas não descontam chances.
    - Maiúsculas e espaços nas extremidades são normalizados.
    - A palavra é sorteada e o limite de erros pode ser configurado.
    - O histórico é exibido e Ctrl+C/fim da entrada encerram com uma mensagem.

Os blocos numerados correspondem aos assuntos comentados em forca_base.py.
"""

# Os dois recursos pertencem à biblioteca padrão: não exigem instalar pacotes.
# random.choice escolhe uma palavra; ascii_lowercase contém "abcdefghijklmnopqrstuvwxyz".
import random
from string import ascii_lowercase


# 1. CONFIGURAÇÃO
# Na base, a palavra e o limite estavam dentro de jogar(). Aqui, as constantes
# reúnem os valores padrão. A tupla PALAVRAS contém apenas palavras sem acento.
PALAVRAS = ("python", "algoritmo", "dados", "variavel", "teclado", "computador")
MAX_ERROS = 6


# As anotações str, set[str] e bool documentam os tipos esperados e ajudam a IDE.
# Elas não validam valores automaticamente: as verificações aparecem no código.
def revelar_palavra(palavra: str, tentadas: set[str]) -> str:
    """Recebe a palavra e as letras tentadas; devolve sua exibição como texto.

    Não imprime nem modifica o conjunto recebido, facilitando testes isolados.
    Substitui a montagem manual de exibicao dentro do while da versão base.

    Exemplos:
        >>> revelar_palavra("dados", set())
        '_ _ _ _ _'
        >>> revelar_palavra("dados", {"d"})
        'd _ d _ _'
    """
    # 3. EXIBIÇÃO: para cada posição, escolhe a letra descoberta ou um traço.
    # join() une esses elementos com espaços, revelando também letras repetidas.
    return " ".join(letra if letra in tentadas else "_" for letra in palavra)


def validar_letra(entrada: str, tentadas: set[str]) -> str:
    """Recebe o texto digitado e o histórico; retorna uma letra válida e inédita.

    Lança ValueError se a entrada não for uma única letra de A a Z sem acento
    ou se ela já tiver sido tentada. Não acrescenta a letra ao conjunto.
    Na base, esse cuidado não existia: a entrada ia diretamente para a lista.

    Exemplos:
        >>> validar_letra(" A ", set())
        'a'
        >>> validar_letra("B", {"a"})
        'b'

    validar_letra("a", {"a"}) gera ValueError por repetição.
    validar_letra("12", set()) gera ValueError por formato inválido.
    """
    # 4. VALIDAÇÃO: strip() remove espaços externos; lower() converte para
    # minúsculas. Assim, " A " e "a" são reconhecidas como a mesma tentativa.
    letra = entrada.strip().lower()
    # É preciso conferir o tamanho e o alfabeto permitido. Apenas isalpha()
    # também aceitaria letras acentuadas, que estão fora das regras deste jogo.
    if len(letra) != 1 or letra not in ascii_lowercase:
        raise ValueError("Digite apenas uma letra de A a Z, sem acento.")
    # Normalizar antes desta comparação impede repetir "a" digitando "A".
    if letra in tentadas:
        raise ValueError("Você já tentou essa letra. Escolha outra.")
    return letra


def jogar(palavra: str, max_erros: int = MAX_ERROS) -> bool:
    """Controla uma partida pelo terminal e retorna True na vitória ou False na derrota.

    palavra: texto não vazio, apenas com letras minúsculas de a a z.
    max_erros: inteiro positivo; se omitido, usa o padrão de seis erros.
    Configurações inválidas geram ValueError antes de começar a partida.

    Exemplos de uso interativo (aguardam digitação):
        jogar("dados")               # Digite d, a, o, s para vencer.
        jogar("python", max_erros=3) # A derrota ocorre ao cometer três erros.

    Na base, jogar() não recebia argumentos e não devolvia o resultado.
    Receber a palavra permite testar partidas sem depender do sorteio.
    """
    # 1. CONFIGURAÇÃO E ESTADO INICIAL
    # Como agora a palavra pode vir de quem chama a função, validamos se ela
    # respeita o mesmo alfabeto aceito pela entrada do jogador.
    if not palavra or any(letra not in ascii_lowercase for letra in palavra):
        raise ValueError("A palavra deve conter apenas letras minúsculas de a a z.")
    # A comparação exata de tipo também rejeita True/False: em Python, bool
    # é uma subclasse de int, mas não representa um limite adequado aqui.
    if type(max_erros) is not int or max_erros < 1:
        raise ValueError("O limite de erros deve ser um inteiro positivo.")

    # O set guarda valores únicos. Ex.: set("dados") contém d, a, o e s.
    # tentadas guarda acertos e erros; letras_da_palavra guarda o alvo da vitória.
    tentadas: set[str] = set()
    letras_da_palavra = set(palavra)
    erros = 0

    print("\n=== JOGO DA FORCA ===")
    print(f"Descubra a palavra. Você pode errar até {max_erros} vezes.")
    print("Digite uma letra por vez, sem acento. Use Ctrl+C para sair.")

    # 2. REPETIÇÃO DA PARTIDA
    # Continua enquanto há chances E ainda faltam letras. issubset() verifica
    # se todas as letras da palavra estão nas tentadas, substituindo a variável
    # ganhou que a versão base recalculava durante a montagem da exibição.
    while erros < max_erros and not letras_da_palavra.issubset(tentadas):
        # 3. EXIBIÇÃO: a função extraída substitui o for de concatenação da base.
        print("\nPalavra:", revelar_palavra(palavra, tentadas))
        print(f"Erros: {erros}/{max_erros}")
        # sorted() organiza o conjunto alfabeticamente. Se estiver vazio,
        # join() produz "" e o operador or seleciona a mensagem "nenhuma".
        print("Letras tentadas:", ", ".join(sorted(tentadas)) or "nenhuma")

        # 4. ENTRADA E ATUALIZAÇÃO DAS TENTATIVAS
        # A tentativa só entra no estado do jogo depois de passar na validação.
        try:
            letra = validar_letra(input("Sua letra: "), tentadas)
        except ValueError as erro:
            print(erro)
            # Volta ao início do while sem registrar a letra nem aumentar erros.
            # Corrige a base, que penalizava novamente uma letra errada repetida.
            continue

        # Só uma letra válida e inédita pode alterar o estado da partida.
        # O set sozinho não resolveria a penalidade duplicada: a validação acima
        # é o que impede uma tentativa repetida de chegar ao contador de erros.
        tentadas.add(letra)
        if letra in letras_da_palavra:
            print("Boa! Essa letra está na palavra.")
        else:
            erros += 1
            print("Essa letra não está na palavra.")

    # 5. ENCERRAMENTO
    # O laço terminou por vitória ou limite de erros. A mesma condição de
    # conjunto identifica qual dos dois aconteceu, sem depender da última letra.
    venceu = letras_da_palavra.issubset(tentadas)
    print("\nPalavra:", revelar_palavra(palavra, tentadas))
    print(f"Erros: {erros}/{max_erros}")
    if venceu:
        print(f"Você venceu! A palavra era: {palavra}")
    else:
        print(f"Você perdeu! A palavra era: {palavra}")
    # Além da mensagem ao jogador, fornece um resultado verificável nos testes.
    return venceu


def main() -> None:
    """Inicia uma partida com palavra sorteada e trata a saída do usuário.

    Não recebe argumentos e retorna None. É chamada ao executar o arquivo.
    Também pode ser usada com `from forca import main; main()` em um console
    Python aberto nesta pasta; a partida aguardará entradas pelo teclado.

    Na base, jogar() era chamada diretamente e não havia sorteio nem tratamento
    de interrupção. Aqui, jogar() continua disponível para partidas controladas.
    """
    try:
        # O sorteio fica fora de jogar(): nos testes podemos usar sempre "dados".
        jogar(random.choice(PALAVRAS))
    except (EOFError, KeyboardInterrupt):
        # EOFError: terminou a entrada disponível. KeyboardInterrupt: Ctrl+C.
        # Trata esses encerramentos com uma mensagem, sem exibir traceback.
        print("\nPartida encerrada. Até a próxima!")


# Mantido da base: executa ao rodar o arquivo, mas não ao importá-lo nos testes.
if __name__ == "__main__":
    main()
