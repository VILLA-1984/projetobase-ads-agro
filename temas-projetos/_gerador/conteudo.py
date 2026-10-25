# -*- coding: utf-8 -*-
"""Conteúdo dos 3 temas de projeto. Edite aqui e rode gerar.py para regenerar MD, HTML (Moodle) e PDF."""

PONTOS = {1: 5, 2: 10, 3: 10, 4: 10, 5: 15, 6: 5, 7: 20, 8: 10, 9: 15}

REFERENCIAS = [
    ("Expo", [
        ("Documentação do Expo SDK 54 (versão do projeto)", "https://docs.expo.dev/versions/v54.0.0/"),
        ("Expo Router – introdução", "https://docs.expo.dev/router/introduction/"),
        ("Expo Router – abas (Tabs)", "https://docs.expo.dev/router/advanced/tabs/"),
        ("Usando Firebase com Expo", "https://docs.expo.dev/guides/using-firebase/"),
    ]),
    ("Firebase", [
        ("Firestore – visão geral", "https://firebase.google.com/docs/firestore"),
        ("Firestore – adicionar dados (addDoc, setDoc, updateDoc)", "https://firebase.google.com/docs/firestore/manage-data/add-data"),
        ("Firestore – ler dados (getDoc, getDocs)", "https://firebase.google.com/docs/firestore/query-data/get-data"),
        ("Firestore – excluir dados (deleteDoc)", "https://firebase.google.com/docs/firestore/manage-data/delete-data"),
        ("Firestore – consultas simples e compostas (where, orderBy)", "https://firebase.google.com/docs/firestore/query-data/queries"),
        ("Firestore – subcoleções e modelo de dados", "https://firebase.google.com/docs/firestore/data-model"),
        ("Firestore – regras de segurança", "https://firebase.google.com/docs/firestore/security/get-started"),
        ("Authentication – e-mail e senha na Web", "https://firebase.google.com/docs/auth/web/password-auth"),
    ]),
    ("React e React Native", [
        ("React – useState", "https://react.dev/reference/react/useState"),
        ("React – useCallback", "https://react.dev/reference/react/useCallback"),
        ("React – criando seus próprios Hooks", "https://react.dev/learn/reusing-logic-with-custom-hooks"),
        ("React Native – FlatList", "https://reactnative.dev/docs/flatlist"),
        ("React Native – TextInput", "https://reactnative.dev/docs/textinput"),
        ("React Native – StyleSheet", "https://reactnative.dev/docs/stylesheet"),
        ("react-native-toast-message", "https://github.com/calintamas/react-native-toast-message"),
    ]),
    ("TypeScript", [
        ("TypeScript Handbook", "https://www.typescriptlang.org/docs/handbook/intro.html"),
    ]),
]

# Mapa do projeto-base -> o que o aluno deve reaproveitar
BASE = [
    ("firebase.ts", "Inicializa o Firebase e exporta `auth` e `db`."),
    ("components/frm-login.tsx", "Tela de login com `signInWithEmailAndPassword`."),
    ("components/frm-cad-aluno.tsx", "Formulário que cadastra (`addDoc`) e altera (`updateDoc`) conforme o parâmetro `id`."),
    ("components/lst-aluno.tsx", "Lista (`FlatList`) com botões Alterar e Excluir (`deleteDoc`)."),
    ("hooks/use-alunos.ts", "Hook que consulta a coleção (`getDocs`) e um documento (`getDoc`)."),
    ("hooks/use-focus-refresh.ts", "Recarrega os dados toda vez que a tela recebe foco."),
    ("app/(tabs)/_layout.tsx", "Barra de abas com as cores do tema."),
    ("app/(tabs)/index.tsx", "Tela inicial com botão Sair (`signOut`)."),
]

CORES = [("#1a3a8f", "azul principal"), ("#002d66", "azul escuro (texto)"), ("#F7941D", "laranja de destaque (botões)"),
         ("#f5f7fc", "fundo claro"), ("#e85d04", "laranja-escuro (ações destrutivas)")]

TEMAS = [
    {
        "pasta": "01-controle-de-rebanho",
        "titulo": "Controle de Rebanho",
        "slug": "rebanho",
        "contexto": ("Uma propriedade rural precisa saber quais animais possui, em que pasto estão, quanto pesam e "
                     "quando foram vacinados. Hoje isso fica em cadernos e planilhas. Seu app vai substituir o caderno "
                     "do produtor, funcionando no celular, direto no curral."),
        "colecao": "animais",
        "entidade": "animal",
        "campos": [
            ("brinco", "string", "Sim", "Número do brinco (identificação única)"),
            ("nome", "string", "Não", "Nome ou apelido do animal"),
            ("especie", "string", "Sim", "Bovino, Suíno, Ovino…"),
            ("raca", "string", "Não", "Raça"),
            ("sexo", "string", "Sim", "M ou F"),
            ("nascimento", "string", "Sim", "Data no formato AAAA-MM-DD"),
            ("peso", "number", "Sim", "Peso atual em kg"),
            ("pasto", "string", "Não", "Piquete/pasto onde está"),
            ("status", "string", "Sim", "ativo, vendido ou abatido"),
        ],
        "sub": ("manejos", "animais/{id}/manejos", [
            ("tipo", "string", "vacina, pesagem ou tratamento"),
            ("descricao", "string", "Ex.: Febre aftosa, 1ª dose"),
            ("data", "string", "AAAA-MM-DD"),
            ("pesoKg", "number", "Só para pesagem (opcional)"),
        ]),
        "telas": ["Login", "Início (com Sair)", "Cadastro/edição de animal", "Lista de animais",
                  "Detalhe do animal com histórico de manejos", "Cadastro de manejo"],
        "diferencial": {
            "nome": "Histórico de manejo e alerta de vacina",
            "itens": [
                "Criar a subcoleção `manejos` dentro de cada animal e a tela de cadastro de manejo.",
                "Tela de detalhe do animal listando os manejos em ordem da data mais recente (`orderBy`).",
                "Ao registrar uma pesagem, atualizar o campo `peso` do animal.",
                "Na lista, destacar em laranja-escuro o animal sem vacina nos últimos 180 dias.",
                "Filtro da lista por `status` (ativo/vendido/abatido).",
            ],
        },
        "extras": ["Busca por brinco ou nome", "Contador de animais por pasto na tela inicial"],
        "desafios_fw": ["Navegar da lista para o detalhe do animal passando o `id` pela rota (Expo Router)",
                        "Recarregar a lista ao voltar para a tela sem causar loop de renderização (`useCallback` + `useFocusEffect`)"],
        "desafios_tec": ["Organizar manejos em subcoleção e ordenar do mais recente (`orderBy`)",
                         "Gravar peso como número e datas como texto padronizado; calcular os 180 dias sem vacina"],
    },
    {
        "pasta": "02-estoque-de-insumos",
        "titulo": "Estoque de Insumos",
        "slug": "insumos",
        "contexto": ("Sementes, adubos, defensivos e ração são comprados em grande quantidade e, sem controle, "
                     "vencem no galpão ou acabam no meio da safra. Seu app será o controle de estoque da fazenda, "
                     "avisando o que está acabando e o que está perto de vencer."),
        "colecao": "insumos",
        "entidade": "insumo",
        "campos": [
            ("nome", "string", "Sim", "Nome do produto"),
            ("categoria", "string", "Sim", "semente, fertilizante, defensivo ou racao"),
            ("unidade", "string", "Sim", "kg, L, saco, dose…"),
            ("quantidade", "number", "Sim", "Quantidade atual em estoque"),
            ("estoqueMinimo", "number", "Sim", "Abaixo disso o item entra em alerta"),
            ("validade", "string", "Não", "Data AAAA-MM-DD"),
            ("fornecedor", "string", "Não", "Nome do fornecedor"),
        ],
        "sub": ("movimentacoes", "insumos/{id}/movimentacoes", [
            ("tipo", "string", "entrada ou saida"),
            ("quantidade", "number", "Quantidade movimentada"),
            ("data", "string", "AAAA-MM-DD"),
            ("observacao", "string", "Ex.: Aplicado no talhão 3"),
        ]),
        "telas": ["Login", "Início (com Sair)", "Cadastro/edição de insumo", "Lista de insumos",
                  "Tela de movimentação (entrada/saída)", "Histórico de movimentações do insumo"],
        "diferencial": {
            "nome": "Movimentações de estoque e alertas",
            "itens": [
                "Tela para registrar entrada ou saída, gravando em `movimentacoes` e atualizando `quantidade` do insumo.",
                "Bloquear saída maior que a quantidade em estoque, com mensagem (`Toast`) clara.",
                "Na lista, destacar insumos com `quantidade <= estoqueMinimo` e os que vencem em até 30 dias.",
                "Filtro da lista por `categoria` e busca por nome.",
                "Tela inicial com o total de itens em alerta.",
            ],
        },
        "extras": ["Ordenar por validade", "Relatório de saídas do mês"],
        "desafios_fw": ["Formulário de movimentação com campos numéricos e validação antes de salvar",
                        "Filtro e busca na `FlatList` sem perder desempenho"],
        "desafios_tec": ["Manter `quantidade` do insumo e as `movimentacoes` consistentes (pensar em atualização atômica/transação)",
                         "Impedir saída maior que o estoque e tratar o erro para o usuário"],
    },
    {
        "pasta": "03-manutencao-de-maquinas",
        "titulo": "Manutenção de Máquinas",
        "slug": "maquinas",
        "contexto": ("Trator parado na época de colheita custa caro. A fazenda precisa saber quais máquinas tem, "
                     "quantas horas cada uma já trabalhou e quando é a próxima revisão. Seu app será o painel de "
                     "manutenção da frota."),
        "colecao": "maquinas",
        "entidade": "máquina",
        "campos": [
            ("nome", "string", "Sim", "Identificação (ex.: Trator 01)"),
            ("tipo", "string", "Sim", "trator, colheitadeira, pulverizador, implemento…"),
            ("modelo", "string", "Não", "Marca e modelo"),
            ("ano", "number", "Não", "Ano de fabricação"),
            ("horimetro", "number", "Sim", "Horas de uso atuais"),
            ("proximaRevisao", "number", "Sim", "Horímetro em que será a próxima revisão"),
            ("status", "string", "Sim", "operando, manutencao ou parada"),
        ],
        "sub": ("manutencoes", "maquinas/{id}/manutencoes", [
            ("tipo", "string", "preventiva ou corretiva"),
            ("descricao", "string", "O que foi feito"),
            ("data", "string", "AAAA-MM-DD"),
            ("custo", "number", "Custo em reais"),
            ("horimetro", "number", "Horímetro no momento do serviço"),
        ]),
        "telas": ["Login", "Início com painel (contadores por status)", "Cadastro/edição de máquina",
                  "Lista de máquinas", "Detalhe com histórico de manutenções", "Cadastro de manutenção"],
        "diferencial": {
            "nome": "Painel da frota e ordens de manutenção",
            "itens": [
                "Subcoleção `manutencoes` e tela de registro; ao salvar, atualizar `horimetro` e `proximaRevisao` da máquina.",
                "Painel na tela inicial com a quantidade de máquinas em cada `status` (consulta + contagem no app).",
                "Na lista, destacar a máquina cujo `horimetro` está a 50 horas (ou menos) da `proximaRevisao`.",
                "Alterar o `status` da máquina com um toque (operando ↔ manutenção ↔ parada).",
                "Histórico de manutenções com o custo total por máquina.",
            ],
        },
        "extras": ["Filtro por tipo de máquina", "Gráfico simples de custo por mês"],
        "desafios_fw": ["Painel da tela inicial atualizado a cada vez que a aba recebe foco",
                        "Alterar o `status` com um toque e refletir na lista sem recarregar o app"],
        "desafios_tec": ["Contar máquinas por `status` consultando o Firestore (`where`) ou agrupando no app",
                         "Atualizar `horimetro` e `proximaRevisao` junto com o registro da manutenção"],
    },
]

ATIVIDADES = [
    (1, "Preparação do ambiente", [
        "Clonar/copiar o projeto-base e rodar com `npx expo start`.",
        "Criar o **seu** projeto no console do Firebase, ativar **Authentication (e-mail/senha)** e **Firestore**.",
        "Trocar a configuração em `firebase.ts` pela do seu projeto.",
        "Cadastrar um usuário de teste no console do Firebase.",
        "Definir as regras do Firestore para aceitar apenas usuários autenticados (`request.auth != null`).",
    ], "Print do app rodando + print do console Firebase com o usuário e a coleção criados.",
     "O app abre; o Firebase é o seu; regras não estão abertas para qualquer pessoa."),
    (2, "Autenticação (login e logout)", [
        "Adaptar a tela de login do modelo com a identidade do seu tema.",
        "Mostrar mensagem de erro com `Toast` quando usuário/senha forem inválidos.",
        "Implementar o botão **Sair** que encerra a sessão e volta ao login.",
    ], "Vídeo curto (até 1 min) ou prints: login correto, login errado, logout.",
     "Login/erro/logout funcionam; o Sair volta para a tela de login."),
    (3, "Cadastro ({entidade})", [
        "Criar o formulário com todos os campos obrigatórios do modelo de dados.",
        "Validar os campos obrigatórios e tipos (número, data) antes de gravar.",
        "Gravar com `addDoc` na coleção `{colecao}` e mostrar `Toast` de sucesso ou erro.",
        "Limpar o formulário após salvar.",
    ], "Prints do formulário preenchido e do documento criado no Firestore.",
     "Dados chegam ao Firestore com os tipos certos (número como `number`)."),
    (4, "Listagem", [
        "Criar um **hook** (`hooks/use-{slug}.ts`) seguindo o modelo `use-alunos.ts`.",
        "Listar com `FlatList`, mostrando os principais campos em cartões.",
        "Recarregar a lista ao voltar para a tela (`useFocusRefresh`).",
        "Mostrar mensagem amigável quando a lista estiver vazia.",
    ], "Print da lista com pelo menos 5 registros.",
     "A lista atualiza sozinha após cadastrar/alterar/excluir."),
    (5, "Alteração e exclusão", [
        "Botão **Alterar** abre o formulário com os dados carregados (`getDoc` + parâmetro `id`).",
        "No modo edição, o botão muda para **Alterar** e grava com `updateDoc`.",
        "Botão **Excluir** com confirmação (`Alert`) antes de chamar `deleteDoc`.",
        "Após salvar, o formulário volta ao modo cadastro.",
    ], "Vídeo curto ou prints do fluxo: alterar um registro e excluir outro.",
     "Edição não cria registro duplicado; exclusão pede confirmação."),
    (6, "Identidade visual", [
        "Aplicar a paleta do projeto-base (ou criar uma nova, justificando) em todas as telas.",
        "Usar nomes de abas claros e ícones coerentes com o tema.",
        "Remover do app todo conteúdo de exemplo do template do Expo.",
    ], "Prints de todas as telas.",
     "Visual consistente entre telas; nenhuma tela de template sobrando."),
    (7, "Funcionalidade diferencial: {dif_nome}", None, None, None),  # preenchido por tema
    (8, "Documentação e repositório", [
        "Escrever o `README.md` do seu projeto: objetivo, como rodar, telas e modelo de dados.",
        "Comentar o código nos pontos principais (hooks e consultas ao Firestore).",
        "Subir o código em um repositório Git com commits ao longo do projeto.",
    ], "Link do repositório + README + apresentação.",
     "Qualquer colega consegue rodar o projeto seguindo o seu README."),
    (9, "Apresentação em grupo (até 15 minutos)", [
        "Montar os slides seguindo o **roteiro de apresentação** descrito no fim deste documento.",
        "Mostrar o app funcionando (demonstração ao vivo ou vídeo de reserva).",
        "Explicar a ferramenta (Expo/React Native e Firebase) e os **desafios** que o grupo enfrentou com o framework e com a tecnologia.",
        "Dividir a fala entre **todos** os integrantes e respeitar o tempo de 15 minutos.",
    ], "Slides (PDF) entregues antes da apresentação + apresentação oral.",
     "Cumpre o roteiro, o tempo e mostra domínio do que foi construído (cada integrante responde perguntas)."),
]

# Roteiro da apresentação: (tópico, minutos, o que abordar)
ROTEIRO = [
    ("Abertura e problema", 1, "Nome do grupo, tema escolhido e o problema real que o app resolve."),
    ("Demonstração do app", 3, "Fluxo completo: login, cadastro, lista, alteração, exclusão e a funcionalidade diferencial. Tenha um vídeo de reserva."),
    ("A ferramenta: Expo e React Native", 2, "O que é React Native e o que o Expo acrescenta (Expo Go, Expo Router, rodar no celular e no navegador). Por que usar."),
    ("Firebase: Authentication e Firestore", 2, "Como funciona o login por e-mail/senha, coleções e subcoleções, e as regras de segurança. Mostre o console."),
    ("Arquitetura do projeto", 2, "Organização de pastas, componentes, hooks (ex.: `use-alunos`) e o caminho de um dado: tela → hook → Firestore → tela."),
    ("Desafios com o framework", 2, "Problemas com React Native/Expo/Expo Router e como foram resolvidos (veja as sugestões do seu tema)."),
    ("Desafios com a tecnologia", 2, "Problemas com Firebase/Firestore/TypeScript e como foram resolvidos (veja as sugestões do seu tema)."),
    ("Aprendizados e próximos passos", 1, "O que o grupo aprendeu, o que faria diferente e o que melhoraria no app."),
]

CRITERIOS_APRESENTACAO = [
    ("Conteúdo técnico (ferramenta e arquitetura corretas)", 5),
    ("Desafios enfrentados e soluções (framework e tecnologia)", 4),
    ("Demonstração funcionando", 3),
    ("Clareza, divisão da fala e respeito ao tempo", 3),
]

CRONOGRAMA = [
    ("Semana 1", "Atividades 1 e 2"),
    ("Semana 2", "Atividades 3 e 4"),
    ("Semana 3", "Atividades 5 e 6"),
    ("Semana 4", "Atividade 7"),
    ("Semana 5", "Atividades 8 e 9 (documentação e apresentações)"),
]


from conteudo_livre import *  # noqa: E402

TEMAS.append(TEMA_LIVRE)
ATIVIDADES_LIVRE = atividades_livre(ATIVIDADES)
