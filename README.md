# Tendências (tendenciasemccp)

Resumo rápido
------------
Projeto para apoiar o plano de aulas sobre análise e interpretação de tendências aplicadas a Ciência da Computação. Este repositório centraliza dados, códigos, materiais didáticos e atividades práticas para os estudantes aprenderem a detectar, analisar e comunicar tendências.

Modelo 5W2H aplicado ao projeto
------------------------------

O QUE? (What)
- O que será feito:
  - Coletar, limpar e analisar séries temporais e dados correlacionados.
  - Identificar padrões, picos e tendências de curto e longo prazo.
  - Produzir relatórios e visualizações que suportem decisões.
- Entregáveis:
  - Notebook(s) com análises exploratórias (Jupyter / RMarkdown).
  - Scripts de ETL para preparação dos dados.
  - Slides e roteiro de aula para atividades práticas.
  - Relatório final com conclusões e recomendações.

POR QUE? (Why)
- Objetivos de aprendizagem do plano de aulas:
  - (1) Compreender conceitos básicos e avançados de análise de tendências.
  - (2) Aplicar métodos estatísticos e de visualização para interpretação de dados.
  - (3) Desenvolver habilidades de comunicação científica e técnica.
  - (4) Promover pensamento crítico sobre fontes de dados e vieses.
- Justificativa:
  - Preparar alunos para interpretar séries temporais em contextos reais e tomar decisões baseadas em evidência.

QUEM? (Who)
- Público-alvo:
  - Estudantes de Ciência da Computação.
- Responsáveis / papéis:
  - Professor(es) / Facilitador(es): planejamento, avaliação e tutoria.
  - Assistente(s) / Monitores: suporte técnico e correção de exercícios.
  - Alunos: execução das atividades, submissão de relatórios.
- Contatos:
  - heitor.andrade@cs.udf.edu.br

ONDE? (Where)
- Local do material:
  - Este repositório: https://github.com/HeitorQueAnd/tendenciasemccp
- Ambientes de execução:
  - Recomendado: Python 3.10+ (Jupyter), ou R 4.x (RMarkdown).
  - Serviços opcionais: Binder, Google Colab, GitHub Pages para hosting de resultados.
- Dados:
  - Pasta /data com datasets (ou links para datasets externos).
  - Atenção a licenciamento e privacidade dos dados (ver seção de dados).

QUANDO? (When)
- Cronograma sugerido (exemplo para um módulo de 4 semanas):
  - Semana 1: Introdução e coleta de dados; preparar ambiente.
  - Semana 2: Limpeza e exploração de dados; exercícios práticos.
  - Semana 3: Modelagem de tendências e técnicas de suavização.
  - Semana 4: Apresentação de relatórios e avaliação final.
- Prazos de entrega:
  - Entrega intermediária (notebook): fim da semana 2.
  - Relatório final: fim da semana 4.

COMO? (How)
- Metodologia:
  - Aulas expositivas + atividades hands-on em notebooks.
  - Exercícios em pares/grupos com revisão por pares.
  - Uso de pipelines reproducíveis (scripts + notebooks).
- Ferramentas e bibliotecas recomendadas:
  - Python: pandas, numpy, matplotlib/seaborn, statsmodels, scikit-learn, prophet (opcional).
  - R: tidyverse, forecast, ggplot2, tsibble, fable.
- Passos rápidos para começar:
  1. Clonar o repositório.
  2. Criar ambiente virtual (venv/conda) e instalar dependências (ver requirements.txt).
  3. Abrir notebooks em Jupyter/Colab e executar as células na ordem.
  4. Submeter relatórios na pasta /submissions ou via plataforma da disciplina.

QUANTO? (How much)
- Recursos necessários:
  - Hardware: computador com 4+ GB RAM (recomenda-se 8GB) ou uso de Colab.
  - Tempo estimado por aluno: ~30 horas (total do módulo) — ajustar conforme objetivo do curso.
  - Custos: acesso à internet; eventuais assinaturas de APIs externas (se usadas) devem ser consideradas.
- Critérios de avaliação (sugestão):
  - Qualidade e reprodutibilidade do notebook (30%).
  - Clareza na interpretação e justificativa das tendências (40%).
  - Apresentação e comunicação do relatório (30%).

Estrutura do repositório
------------------------
- /data — datasets (ou links/descrições dos dados).
- /notebooks — notebooks didáticos e de exercícios.
- /scripts — scripts reutilizáveis (ETL, transformação).
- /slides — material para aula (PDF/markdown).
- /submissions — local para submissão dos trabalhos dos alunos (ou indicar outra plataforma).
- README.md — este arquivo.
- requirements.txt / environment.yml — dependências do projeto.

Boas práticas para uso em sala de aula
-------------------------------------
- Expor claramente objetivos de cada aula e critérios de avaliação.
- Fornecer notebooks parcialmente preenchidos para guiar os alunos.
- Incluir exemplos de dados reais e exercícios de interpretação.
- Promover discussão sobre limitações dos métodos e qualidade dos dados.

Como contribuir
---------------
- Abra uma issue para propor melhorias no material ou novos exercícios.
- Faça fork -> branch -> PR com uma descrição clara das mudanças.
- Siga o estilo de código e inclua comentários nos notebooks.

Dados e ética
-------------
- Sempre documente a origem dos dados e licenças.
- Se dados sensíveis forem usados, aplique anonimização e considere consentimento.
- Incluir seção de limitações em todos os relatórios.

Licença
-------
- [INSERIR LICENÇA — ex.: MIT] (adicione um arquivo LICENSE com a licença escolhida).

Notas finais
-----------
- Personalize as seções entre colchetes [ ... ] com os objetivos e recursos específicos do seu plano de aulas.
- Se desejar, posso gerar um template de plano de aula por semana com atividades detalhadas ou criar os notebooks base já prontos.

O que eu fiz e próximo passo
---------------------------
Criei o README.md estruturado pelo modelo 5W2H e posicionei campos a serem preenchidos com os objetivos específicos do seu plano de aulas. Posso:
- Inserir automaticamente esse README no repositório (faço o commit) — preciso que você confirme para eu executar a gravação e confirmar owner/repo (você já forneceu HeitorQueAnd/tendenciasemccp).
- Gerar templates adicionais (notebook inicial, requisitos, plano de aulas por semana) e adicioná-los ao repositório.

Qual você prefere que eu faça agora: (A) faço o commit do README no repositório, ou (B) gero também um notebook/template de aula antes do commit?
