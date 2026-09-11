"""Testes das regras e de partidas completas, com entradas reproduzíveis."""

import io
import unittest
from contextlib import redirect_stdout
from unittest.mock import patch

from forca import jogar, main, revelar_palavra, validar_letra


class TestRevelarPalavra(unittest.TestCase):
    def test_comeca_oculta(self):
        self.assertEqual(revelar_palavra("dados", set()), "_ _ _ _ _")

    def test_revela_todas_as_ocorrencias(self):
        self.assertEqual(revelar_palavra("dados", {"d"}), "d _ d _ _")

    def test_palavra_completa(self):
        self.assertEqual(revelar_palavra("dados", set("dados")), "d a d o s")


class TestValidarLetra(unittest.TestCase):
    def test_normaliza_maiuscula_e_espacos(self):
        self.assertEqual(validar_letra(" A ", set()), "a")

    def test_rejeita_entradas_invalidas(self):
        for entrada in ("", "  ", "ab", "1", "!", "á", "ç", "🙂"):
            with self.subTest(entrada=entrada), self.assertRaises(ValueError):
                validar_letra(entrada, set())

    def test_rejeita_repetida_depois_de_normalizar(self):
        with self.assertRaisesRegex(ValueError, "já tentou"):
            validar_letra(" A ", {"a"})

    def test_validacao_nao_modifica_tentadas(self):
        tentadas = {"a"}
        validar_letra("b", tentadas)
        self.assertEqual(tentadas, {"a"})


class TestPartida(unittest.TestCase):
    def executar_partida(self, palavra, entradas, max_erros=6):
        saida = io.StringIO()
        with patch("builtins.input", side_effect=entradas) as ler:
            with redirect_stdout(saida):
                venceu = jogar(palavra, max_erros)
        return venceu, saida.getvalue(), ler.call_count

    def test_vitoria_com_letras_repetidas_na_palavra(self):
        venceu, saida, leituras = self.executar_partida("dados", ["d", "a", "o", "s"])
        self.assertTrue(venceu)
        self.assertEqual(leituras, 4)
        self.assertIn("Você venceu! A palavra era: dados", saida)
        self.assertIn("Palavra: d a d o s", saida)

    def test_derrota_apos_exatamente_seis_erros(self):
        venceu, saida, leituras = self.executar_partida("a", list("bcdefg"))
        self.assertFalse(venceu)
        self.assertEqual(leituras, 6)
        self.assertIn("Erros: 6/6", saida)
        self.assertIn("Você perdeu! A palavra era: a", saida)

    def test_entradas_invalidas_nao_consumem_chances(self):
        venceu, saida, _ = self.executar_partida("a", ["", "ab", "1", "!", "á", " A "], 1)
        self.assertTrue(venceu)
        self.assertIn("Erros: 0/1", saida)

    def test_repetir_erro_nao_desconta_outra_chance(self):
        venceu, saida, leituras = self.executar_partida("a", ["b", " B ", "a"], 2)
        self.assertTrue(venceu)
        self.assertEqual(leituras, 3)
        self.assertIn("Você já tentou essa letra", saida)
        self.assertIn("Erros: 1/2", saida)

    def test_repetir_acerto_nao_desconta_chance(self):
        venceu, saida, _ = self.executar_partida("ab", ["a", "a", "b"], 1)
        self.assertTrue(venceu)
        self.assertIn("Erros: 0/1", saida)

    def test_vence_apos_cinco_erros(self):
        venceu, saida, _ = self.executar_partida("a", list("bcdefa"))
        self.assertTrue(venceu)
        self.assertIn("Erros: 5/6", saida)

    def test_rejeita_palavra_incompativel_com_as_regras(self):
        for palavra in ("", "Python", "ação", "duas palavras", "123"):
            with self.subTest(palavra=palavra), self.assertRaises(ValueError):
                jogar(palavra)

    def test_rejeita_limite_invalido(self):
        for limite in (0, -1, 1.5, True, "6"):
            with self.subTest(limite=limite), self.assertRaises(ValueError):
                jogar("python", limite)


class TestEncerramento(unittest.TestCase):
    def test_fim_da_entrada_e_interrupcao(self):
        for erro in (EOFError, KeyboardInterrupt):
            with self.subTest(erro=erro.__name__):
                saida = io.StringIO()
                with patch("builtins.input", side_effect=erro), redirect_stdout(saida):
                    main()
                self.assertIn("Partida encerrada", saida.getvalue())


if __name__ == "__main__":
    unittest.main()
