# Guia do projeto-base

Este guia explica o projeto de **cadastro de alunos** que serve de modelo para os três temas.

## Como rodar

```bash
npm install
npx expo start
```

Pressione `w` para abrir no navegador ou leia o QR Code com o app **Expo Go** no celular.

## Mapa dos arquivos

| Arquivo | O que faz |
|---|---|
| `firebase.ts` | Inicializa o Firebase e exporta `auth` e `db`. |
| `components/frm-login.tsx` | Tela de login com `signInWithEmailAndPassword`. |
| `components/frm-cad-aluno.tsx` | Formulário que cadastra (`addDoc`) e altera (`updateDoc`) conforme o parâmetro `id`. |
| `components/lst-aluno.tsx` | Lista (`FlatList`) com botões Alterar e Excluir (`deleteDoc`). |
| `hooks/use-alunos.ts` | Hook que consulta a coleção (`getDocs`) e um documento (`getDoc`). |
| `hooks/use-focus-refresh.ts` | Recarrega os dados toda vez que a tela recebe foco. |
| `app/(tabs)/_layout.tsx` | Barra de abas com as cores do tema. |
| `app/(tabs)/index.tsx` | Tela inicial com botão Sair (`signOut`). |

## Fluxo de dados

1. `frm-login.tsx` autentica com `signInWithEmailAndPassword` e vai para as abas.
2. `frm-cad-aluno.tsx` grava com `addDoc` (cadastro) ou `updateDoc` (quando recebe `id`).
3. `use-alunos.ts` lê do Firestore (`getDocs`/`getDoc`) e devolve os dados para a tela.
4. `lst-aluno.tsx` mostra os cartões; **Alterar** navega com `router.push` passando o `id`; **Excluir** usa `deleteDoc`.
5. `use-focus-refresh.ts` recarrega a lista ao voltar para a tela.
6. O botão **Sair** da tela inicial chama `signOut` e volta ao login.

## Atenção: rotas com o mesmo caminho

A tela de login (`app/(auth)/index.tsx`) e a tela inicial (`app/(tabs)/index.tsx`) têm ambas a rota `/`. Para voltar ao login use `router.replace('/(auth)')`, e não `router.replace('/')`.

## Como adaptar para o seu tema

1. Copie `use-alunos.ts` para `use-<seu-tema>.ts` e troque a coleção e os campos.
2. Copie o formulário e a lista trocando os campos e os textos.
3. Ajuste as abas em `app/(tabs)/_layout.tsx`.
4. Troque a configuração em `firebase.ts` pelo **seu** projeto Firebase.

## Referências

### Expo

- [Documentação do Expo SDK 54 (versão do projeto)](https://docs.expo.dev/versions/v54.0.0/)
- [Expo Router – introdução](https://docs.expo.dev/router/introduction/)
- [Expo Router – abas (Tabs)](https://docs.expo.dev/router/advanced/tabs/)
- [Usando Firebase com Expo](https://docs.expo.dev/guides/using-firebase/)

### Firebase

- [Firestore – visão geral](https://firebase.google.com/docs/firestore)
- [Firestore – adicionar dados (addDoc, setDoc, updateDoc)](https://firebase.google.com/docs/firestore/manage-data/add-data)
- [Firestore – ler dados (getDoc, getDocs)](https://firebase.google.com/docs/firestore/query-data/get-data)
- [Firestore – excluir dados (deleteDoc)](https://firebase.google.com/docs/firestore/manage-data/delete-data)
- [Firestore – consultas simples e compostas (where, orderBy)](https://firebase.google.com/docs/firestore/query-data/queries)
- [Firestore – subcoleções e modelo de dados](https://firebase.google.com/docs/firestore/data-model)
- [Firestore – regras de segurança](https://firebase.google.com/docs/firestore/security/get-started)
- [Authentication – e-mail e senha na Web](https://firebase.google.com/docs/auth/web/password-auth)

### React e React Native

- [React – useState](https://react.dev/reference/react/useState)
- [React – useCallback](https://react.dev/reference/react/useCallback)
- [React – criando seus próprios Hooks](https://react.dev/learn/reusing-logic-with-custom-hooks)
- [React Native – FlatList](https://reactnative.dev/docs/flatlist)
- [React Native – TextInput](https://reactnative.dev/docs/textinput)
- [React Native – StyleSheet](https://reactnative.dev/docs/stylesheet)
- [react-native-toast-message](https://github.com/calintamas/react-native-toast-message)

### TypeScript

- [TypeScript Handbook](https://www.typescriptlang.org/docs/handbook/intro.html)
