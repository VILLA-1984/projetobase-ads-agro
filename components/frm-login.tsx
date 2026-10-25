import {
    StyleSheet,
    Text, TextInput, TouchableOpacity,
    View
} from 'react-native';

import { auth } from "@/firebase";
import { router } from "expo-router";
import { signInWithEmailAndPassword } from "firebase/auth";
import { useState } from 'react';
import Toast from "react-native-toast-message";

export default function Login() {

    const [usuario, setUsuario] = useState('');
    const [senha, setSenha] = useState('');

    async function onPress() {
        try{
            await signInWithEmailAndPassword(auth, usuario, senha);
            router.replace("/(tabs)");
        }catch(error: any){
            Toast.show({
                type: "error",
                text1: 'Erro!',
                text2: 'Usuário ou Senha inválidos!'
            })
        }
    }

    return (
        <View style={styles.container}>
            <View style={styles.header}>
                <Text style={styles.brand}>Uni<Text style={styles.brandAccent}>Senai</Text></Text>
                <Text style={styles.subtitle}>Gestão de Alunos</Text>
            </View>

            <View style={styles.card}>
                <Text style={styles.title}>Acesse sua conta</Text>
                <TextInput
                    style={styles.input}
                    onChangeText={setUsuario}
                    value={usuario}
                    placeholder="Usuário"
                    placeholderTextColor="#7a89b0"
                    autoCapitalize="none"
                />
                <TextInput
                    style={styles.input}
                    onChangeText={setSenha}
                    value={senha}
                    placeholder="Senha"
                    placeholderTextColor="#7a89b0"
                    secureTextEntry={true}
                />

                <TouchableOpacity style={styles.button} onPress={onPress}>
                    <Text style={styles.buttonText}>Entrar</Text>
                </TouchableOpacity>
            </View>

            <Toast />

        </View>
    )
}

const styles = StyleSheet.create({
    container: {
        flex: 1,
        justifyContent: 'center',
        backgroundColor: '#1a3a8f',
        padding: 24,
    },
    header: {
        alignItems: 'center',
        marginBottom: 32,
    },
    brand: {
        fontSize: 40,
        fontWeight: 'bold',
        color: '#ffffff',
    },
    brandAccent: {
        color: '#F7941D',
    },
    subtitle: {
        fontSize: 16,
        color: '#ffffffb3',
        marginTop: 4,
    },
    card: {
        backgroundColor: '#ffffff',
        borderRadius: 16,
        padding: 20,
    },
    title: {
        fontSize: 20,
        fontWeight: 'bold',
        color: '#002d66',
        marginBottom: 8,
        marginHorizontal: 12,
    },
    input: {
        height: 44,
        margin: 12,
        borderWidth: 1,
        borderColor: '#d4ddf0',
        backgroundColor: '#f5f7fc',
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
