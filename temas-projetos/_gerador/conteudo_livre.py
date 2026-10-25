# -*- coding: utf-8 -*-
"""Conteúdo do tema livre (4º tema). Importado por conteudo.py."""

LIVRE_CARDAPIO = [
    ("Subcoleção relacionada", "Registros filhos de outro (ex.: itens de um pedido, comentários de uma tarefa) em `colecao/{id}/sub`."),
    ("Dados por usuário", "Cada usuário vê apenas os **seus** registros (campo `uid` gravado com `auth.currentUser.uid` + regra de segurança correspondente)."),
    ("Busca e filtros", "Busca por texto e filtro por categoria/status na lista, usando `where` ou filtro no app."),
    ("Ordenação e agrupamento", "Lista ordenada (`orderBy`) e/ou agrupada por categoria, data ou status."),
    ("Painel de resumo", "Tela inicial com contadores/totais calculados a partir do Firestore (ex.: itens por status, soma de valores)."),
    ("Mudança de status com um toque", "Alternar o estado de um registro (ex.: pendente ↔ concluído) direto na lista."),
    ("Cadastro de usuário", "Tela de criar conta (`createUserWithEmailAndPassword`) e recuperação de senha."),
    ("Perfil do usuário", "Tela com os dados do usuário logado e edição de um documento `perfis/{uid}`."),
    ("Recurso nativo do Expo", "Usar um módulo do Expo SDK 54 (ex.: localização, câmera ou seletor de imagem) integrado ao app."),
    ("Atualização em tempo real", "Usar `onSnapshot` para a lista atualizar sozinha, sem recarregar a tela."),
]

LIVRE_IDEIAS = [
    "Agenda de consultas ou compromissos", "Controle de gastos pessoais", "Lista de compras compartilhada",
    "Diário de estudos ou de treinos", "Biblioteca de livros, filmes ou jogos", "Livro de receitas",
    "Cadastro de pets para adoção", "Organizador de eventos e convidados", "Controle de tarefas de uma equipe",
    "Catálogo de produtos de um pequeno comércio",
]

LIVRE_PROPOSTA = [
    ("Nome do app", "Um nome curto e a ideia em uma frase"),
    ("Problema", "Que problema resolve e para quem"),
    ("Funcionalidades", "Lista das principais funcionalidades"),
    ("Dados", "Coleções e subcoleções, com os campos e tipos de cada uma"),
    ("Telas", "Lista das telas (mínimo 5) e como o usuário navega entre elas"),
    ("Diferenciais", "Os 3 (ou mais) itens do cardápio que pretende fazer"),
    ("Integrantes", "Nomes e quem faz o quê"),
]

LIVRE_REQUISITOS = [
    "Login e logout com Firebase Authentication.",
    "**Pelo menos 2 coleções** no Firestore (ou 1 coleção + 1 subcoleção) com relação clara entre elas.",
    "**CRUD completo** (cadastrar, listar, alterar e excluir) em pelo menos uma coleção.",
    "Um **hook próprio** para consultar o Firestore, seguindo o modelo `use-alunos.ts`.",
    "Mínimo de **5 telas** (contando o login) com navegação por abas.",
    "Validação dos campos e mensagens de erro/sucesso com `Toast`.",
    "**Regras de segurança** do Firestore que exijam usuário autenticado.",
    "Identidade visual própria e **sem nenhuma tela de exemplo** do template.",
    "Código em repositório Git, com `README.md`.",
]

LIVRE_PROIBIDO = [
    "Repetir o próprio projeto-base (cadastro de alunos) ou os temas 1, 2 e 3 só com outro nome.",
    "Guardar dados sensíveis reais de pessoas (CPF, endereço, saúde). Use dados fictícios.",
    "Publicar chaves ou senhas pessoais em repositório público.",
]

TEMA_LIVRE = {
    "livre": True,
    "pasta": "04-tema-livre",
    "titulo": "Tema Livre",
    "slug": "livre",
    "colecao": "(definida pelo grupo)",
    "diferencial": {"nome": "Escolhidos pelo grupo no cardápio de diferenciais"},
    "desafios_fw": ["Decidir como dividir o app em telas e abas e navegar entre elas passando parâmetros (Expo Router)",
                    "Manter as telas atualizadas ao voltar para elas sem causar loop de renderização"],
    "desafios_tec": ["Modelar os dados no Firestore (o que vira coleção, o que vira subcoleção)",
                     "Escrever regras de segurança que combinem com o modelo escolhido"],
    "extras": ["Modo escuro respeitando o tema do sistema", "Publicar a versão web e apresentar o link"],
}


def atividades_livre(atividades):
    """Mesma numeração e pontuação dos demais temas; 8 e 9 são reaproveitadas de `atividades`."""
    return [
        (1, "Proposta e preparação do ambiente", [
            "Escrever a **proposta do projeto** (1 página, modelo na seção 7): problema, público, funcionalidades, dados e telas.",
            "Entregar a proposta ao professor e **aguardar a aprovação** antes de seguir para as demais atividades.",
            "Criar o **seu** projeto no console do Firebase, ativar **Authentication (e-mail/senha)** e **Firestore**.",
            "Trocar a configuração em `firebase.ts` e cadastrar um usuário de teste.",
            "Definir regras do Firestore que aceitem apenas usuários autenticados (`request.auth != null`).",
        ], "Proposta aprovada + print do app rodando e do console do Firebase.",
         "Proposta completa e viável; Firebase é o do grupo; regras não estão abertas para qualquer pessoa."),
        (2, "Autenticação (login e logout)", [
            "Adaptar a tela de login do modelo à identidade do seu app.",
            "Mostrar mensagem de erro com `Toast` quando usuário/senha forem inválidos.",
            "Implementar o botão **Sair** que encerra a sessão e volta ao login (`router.replace('/(auth)')`).",
        ], "Vídeo curto (até 1 min) ou prints: login correto, login errado, logout.",
         "Login/erro/logout funcionam; o Sair volta para a tela de login."),
        (3, "Cadastro da entidade principal", [
            "Criar o formulário com todos os campos definidos na proposta, validando obrigatórios e tipos.",
            "Gravar com `addDoc` e mostrar `Toast` de sucesso ou erro.",
            "Limpar o formulário após salvar.",
        ], "Prints do formulário preenchido e do documento criado no Firestore.",
         "Dados chegam ao Firestore com os tipos certos (números como `number`)."),
        (4, "Listagem", [
            "Criar um **hook próprio** (`hooks/use-<seu-tema>.ts`) seguindo o modelo `use-alunos.ts`.",
            "Listar com `FlatList` em cartões e recarregar ao voltar para a tela (`useFocusRefresh`).",
            "Mostrar mensagem amigável quando a lista estiver vazia.",
        ], "Print da lista com pelo menos 5 registros.",
         "A lista atualiza sozinha após cadastrar/alterar/excluir."),
        (5, "Alteração e exclusão", [
            "Botão **Alterar** abre o formulário com os dados carregados (`getDoc` + parâmetro `id`).",
            "No modo edição, o botão muda para **Alterar** e grava com `updateDoc`.",
            "Botão **Excluir** com confirmação (`Alert`) antes de `deleteDoc`.",
        ], "Vídeo curto ou prints do fluxo: alterar um registro e excluir outro.",
         "Edição não cria registro duplicado; exclusão pede confirmação."),
        (6, "Identidade visual", [
            "Definir (e justificar na documentação) a paleta de cores e o nome do app.",
            "Usar nomes de abas claros e ícones coerentes.",
            "Remover do app todo conteúdo de exemplo do template do Expo.",
        ], "Prints de todas as telas.",
         "Visual consistente entre telas; nenhuma tela de template sobrando."),
        (7, "Diferenciais escolhidos (cardápio)", [
            "Escolher **no mínimo 3 itens** do cardápio de diferenciais e implementá-los (seção 5).",
            "Pelo menos **1 item** deve envolver uma **segunda coleção ou subcoleção**.",
            "Registrar na documentação quais itens foram escolhidos e por quê.",
        ], "Vídeo curto (até 2 min) mostrando cada diferencial e prints do Firestore.",
         "Os itens funcionam e os dados ficam consistentes entre as coleções."),
        atividades[7],
        atividades[8],
    ]
