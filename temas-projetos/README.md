# Temas de projeto – React (Expo) + Firebase

Pasta de distribuição dos projetos finais. Cada aluno (ou dupla) recebe **um** tema e parte do projeto-base de cadastro de alunos. *Material para o professor; os documentos de cada tema são escritos para os alunos.*

O **tema livre** (`04-tema-livre/`) não tem assunto fixo: o grupo propõe o app, o professor aprova a proposta e o grupo cumpre requisitos mínimos e escolhe diferenciais de um cardápio.

## Temas

| Tema | Pasta | Coleção principal | Diferencial |
|---|---|---|---|
| Controle de Rebanho | `01-controle-de-rebanho/` | `animais` | Histórico de manejo e alerta de vacina |
| Estoque de Insumos | `02-estoque-de-insumos/` | `insumos` | Movimentações de estoque e alertas |
| Manutenção de Máquinas | `03-manutencao-de-maquinas/` | `maquinas` | Painel da frota e ordens de manutenção |
| Tema Livre | `04-tema-livre/` | `(definida pelo grupo)` | Escolhidos pelo grupo no cardápio de diferenciais |

## Conteúdo de cada pasta

| Arquivo | Uso |
|---|---|
| `tema.md` | Fonte em Markdown (GitHub/VS Code) |
| `tema-moodle.html` | HTML com estilos embutidos para colar no Moodle |
| `tema.pdf` | Versão para impressão/anexo |

## Arquivos comuns

- `guia-projeto-base.*` – como o projeto-base funciona e como adaptá-lo.
- `referencias.*` – links da documentação oficial.
- `_gerador/` – scripts que geram HTML e PDF a partir do conteúdo (`python _gerador/gerar.py`).

## Estrutura comum das atividades (100 pontos)

| Atividade | Pontos |
|---|---|
| 1 – Preparação do ambiente | 5 |
| 2 – Autenticação (login e logout) | 10 |
| 3 – Cadastro (registro) | 10 |
| 4 – Listagem | 10 |
| 5 – Alteração e exclusão | 15 |
| 6 – Identidade visual | 5 |
| 7 – Funcionalidade diferencial: Diferencial do tema | 20 |
| 8 – Documentação e repositório | 10 |
| 9 – Apresentação em grupo (até 15 minutos) | 15 |

## Como usar no Moodle

1. Crie um recurso **Página** (ou uma descrição de **Tarefa**) e abra o editor.
2. No editor (Atto ou TinyMCE), clique no botão `<>` (**Editar código-fonte / HTML**).
3. Cole todo o conteúdo de `tema-moodle.html` e salve.
4. Anexe o `tema.pdf` como arquivo complementar.

## Distribuição sugerida

Sorteie ou deixe os alunos escolherem, limitando o número de duplas por tema. Peça que **cada um crie o seu projeto Firebase** para não compartilharem credenciais.

## Observação sobre os links

As referências apontam para a documentação oficial. Confira se continuam válidos a cada semestre.