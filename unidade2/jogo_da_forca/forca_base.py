"""Versão inicial do jogo da forca, preservada para comparação com forca.py.

Como executar, a partir da raiz do repositório:
    python3 unidade2/jogo_da_forca/forca_base.py

Exemplo de partida:
    Digite p, y, t, h, o e n, uma letra por vez, para descobrir "python".

Como comparar os arquivos:
    1. Configuração: palavra e limite fixos aqui; sorteio e parâmetros na final.
    2. Estado: lista de tentativas aqui; conjunto sem duplicatas na final.
    3. Exibição e vitória: calculadas neste laço; separadas na versão final.
    4. Entrada: sem validação aqui; normalizada e validada na final.
    5. Encerramento: simples aqui; trata Ctrl+C e fim da entrada na final.

As limitações desta base são intencionais para a comparação. Separar funções
é refatoração; corrigir penalidades e acrescentar sorteio muda o comportamento.
"""


def jogar():
    """Executa uma partida com a palavra fixa "python" e até seis erros.

    Não recebe parâmetros. Lê as tentativas pelo teclado e imprime o resultado.
    Retorna None tanto na vitória quanto na derrota. Na versão final, jogar
    recebe a palavra e o limite de erros e retorna um bool com o resultado.

    Exemplo de uso em outro arquivo desta pasta:
        from forca_base import jogar
        jogar()  # Inicia a partida e aguarda a digitação do usuário.

    Nesta base, a função reúne exibição, entrada e regras do jogo. Na final,
    revelar_palavra e validar_letra assumem partes dessas responsabilidades.
    """
    # 1. CONFIGURAÇÃO E ESTADO INICIAL
    # A palavra é sempre a mesma. Na final, main() faz o sorteio e passa a
    # palavra para jogar(), permitindo também escolher uma palavra nos testes.
    palavra = "python"
    # A lista aceita duplicatas: duas entradas "b" ficam armazenadas duas vezes.
    # Na final, tentadas é um set e a validação avisa sobre letras repetidas.
    letras = []
    erros = 0

    # 2. REPETIÇÃO DA PARTIDA
    # O limite 6 está escrito diretamente no laço. Na final, é max_erros.
    # A vitória só será verificada dentro deste while, depois da exibição.
    while erros < 6:
        # 3. EXIBIÇÃO E VERIFICAÇÃO DE VITÓRIA
        # A exibição é reconstruída a cada rodada. Começamos supondo vitória;
        # encontrar qualquer letra ainda oculta muda ganhou para False.
        exibicao = ""
        ganhou = True
        for letra in palavra:
            if letra in letras:
                # Acerto: mostra a letra e um espaço para separar as posições.
                exibicao += letra + " "
            else:
                exibicao += "_ "
                ganhou = False

        # strip() remove o espaço que sobrou no final da exibição.
        # Na final, revelar_palavra() usa join() para montar essa mesma saída,
        # e issubset() verifica a vitória sem precisar da variável ganhou.
        print("Palavra:", exibicao.strip())
        if ganhou:
            print("Você venceu!")
            # Encerra a função imediatamente; o retorno implícito é None.
            return

        # 4. ENTRADA E ATUALIZAÇÃO DAS TENTATIVAS
        # Limitação: input() devolve o texto como foi digitado. "P" e "p" são
        # diferentes, e números ou várias letras não recebem aviso específico.
        # Na final, validar_letra() trata isso antes de registrar a tentativa.
        tentativa = input("Digite uma letra: ")
        letras.append(tentativa)
        # Limitação: repetir "b" desconta outra chance, pois não verificamos
        # se a letra já foi usada. Ex.: "b", "b" resulta em dois erros.
        # Além disso, "" e "py" são substrings de "python": não contam como
        # erro, embora não sejam tentativas válidas de uma única letra.
        if tentativa not in palavra:
            erros += 1
        print("Erros:", erros)

    # 5. ENCERRAMENTO
    # Só chegamos aqui quando o limite de erros é atingido. Na vitória, o
    # return acima já encerrou a função. Esta base não trata Ctrl+C ou EOF.
    print("Você perdeu! A palavra era:", palavra)


# Inicia o jogo apenas quando este arquivo é executado diretamente.
# Importar jogar em outro arquivo não inicia uma partida automaticamente.
if __name__ == "__main__":
    jogar()
