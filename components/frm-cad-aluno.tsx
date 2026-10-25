import {
    View, Text, TextInput, TouchableOpacity,
    StyleSheet
} from 'react-native';

import { useCallback, useState } from 'react';
import Toast from "react-native-toast-message";
import { router, useLocalSearchParams } from "expo-router";
import { db } from "@/firebase";
import { addDoc, collection, doc, updateDoc } from 'firebase/firestore';
import { useFocusRefresh } from "@/hooks/use-focus-refresh";
import { useAlunos } from "@/hooks/use-alunos";

export default function CadAluno() {

    const { id } = useLocalSearchParams<{ id?: string }>();
    const { carregarAluno } = useAlunos();

    const [nome, setNome] = useState('');
    const [idade, setIdade] = useState('');
    const [email, setEmail] = useState('');
    const [matricula, setMatricula] = useState('');

    function limpar() {
        setNome('');
        setIdade('');
        setEmail('');
        setMatricula('');
    }

    // Com id: carrega o aluno para edição. Sem id: formulário em branco.
    const carregarFormulario = useCallback(async () => {
        if (!id) {
            limpar();
            return;
        }
        const aluno = await carregarAluno(id);
        if (aluno) {
            setNome(aluno.nome);
            setIdade(aluno.idade);
            setEmail(aluno.email ?? '');
            setMatricula(aluno.matricula);
        }
    }, [id, carregarAluno]);

    useFocusRefresh(carregarFormulario);

    async function onPress() {
        const dados = { nome, idade, email, matricula };
        try{
            if (id) {
                await updateDoc(doc(db, "alunos", id), dados);
            } else {
                await addDoc(collection(db, "alunos"), dados);
            }
            Toast.show({
                type: "success",
                text1: 'Sucesso!',
                text2: id ? 'Aluno Alterado!' : 'Usuário Cadastrado!'
            })
            if (id) router.setParams({ id: undefined });
            limpar();
        }catch(error: any){
            Toast.show({
                type: "error",
                text1: 'Erro!',
                text2: id ? 'Aluno Não Alterado!' : 'Usuário Não Cadastrado!'
            })
        }
    }

    return (
        <View style={styles.container}>
            <Text style={styles.title}>{id ? 'Alterar aluno' : 'Cadastrar aluno'}</Text>
            <TextInput
                style={styles.input}
                onChangeText={setNome}
                value={nome}
                placeholder="Nome do Aluno"
                placeholderTextColor="#7a89b0"
            />
            <TextInput
                style={styles.input}
                onChangeText={setIdade}
                value={idade}
                placeholder="Idade do aluno"
                placeholderTextColor="#7a89b0"
            />
            <TextInput
                style={styles.input}
                onChangeText={setEmail}
                value={email}
                placeholder="E-mail do aluno"
                placeholderTextColor="#7a89b0"
            />
            <TextInput
                style={styles.input}
                onChangeText={setMatricula}
                value={matricula}
                placeholder="Matricula do aluno"
                placeholderTextColor="#7a89b0"
            />

            <TouchableOpacity style={styles.button} onPress={onPress}>
                <Text style={styles.buttonText}>{id ? 'Alterar' : 'Cadastrar'}</Text>
            </TouchableOpacity>

            <Toast />

        </View>
    )
}

const styles = StyleSheet.create({
    container: {
        flex: 1,
        justifyContent: 'center',
        backgroundColor: '#f5f7fc',
        padding: 12,
    },
    title: {
        fontSize: 24,
        fontWeight: 'bold',
        color: '#1a3a8f',
        marginHorizontal: 12,
        marginBottom: 8,
    },
    input: {
        height: 44,
        margin: 12,
        borderWidth: 1,
        borderColor: '#d4ddf0',
        backgroundColor: '#ffffff',
        borderRadius: 8,
        paddingHorizontal: 12,
        color: '#002d66',
    },
    button: {
        alignItems: 'center',
        backgroundColor: '#F7941D',
        borderRadius: 8,
        padding: 12,
        margin: 12,
    },
    buttonText: {
        color: '#ffffff',
        fontWeight: 'bold',
        fontSize: 16,
    },
});
