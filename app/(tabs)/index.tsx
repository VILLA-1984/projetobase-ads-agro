import { auth } from '@/firebase';
import { router } from 'expo-router';
import { signOut } from 'firebase/auth';
import { StyleSheet, Text, TouchableOpacity, View } from 'react-native';
import { SafeAreaView } from 'react-native-safe-area-context';

export default function HomeScreen() {
  async function sair() {
    await signOut(auth);
    router.replace('/(auth)');
  }

  return (
    <SafeAreaView style={styles.container}>
      <TouchableOpacity style={styles.sair} onPress={sair}>
        <Text style={styles.sairTexto}>Sair</Text>
      </TouchableOpacity>

      <View style={styles.header}>
        <Text style={styles.brand}>
          Uni<Text style={styles.brandAccent}>Senai</Text>
        </Text>
        <Text style={styles.subtitle}>Gestão de Alunos</Text>
      </View>

      <View style={styles.content}>
        <Text style={styles.title}>Bem-vindo!</Text>
        <Text style={styles.text}>Cadastre novos alunos ou consulte, altere e exclua os já cadastrados.</Text>

        <TouchableOpacity style={styles.button} onPress={() => router.push('/(tabs)/aluno')}>
          <Text style={styles.buttonText}>Cadastrar aluno</Text>
        </TouchableOpacity>
        <TouchableOpacity
          style={[styles.button, styles.buttonSecondary]}
          onPress={() => router.push('/(tabs)/lstAlunos')}>
          <Text style={styles.buttonText}>Ver alunos</Text>
        </TouchableOpacity>
      </View>
    </SafeAreaView>
  );
}

const styles = StyleSheet.create({
  container: {
    flex: 1,
    backgroundColor: '#1a3a8f',
  },
  sair: {
    alignSelf: 'flex-end',
    marginTop: 12,
    marginRight: 16,
    paddingVertical: 6,
    paddingHorizontal: 14,
    borderRadius: 8,
    borderWidth: 1,
    borderColor: '#ffffffb3',
  },
  sairTexto: {
    color: '#ffffff',
    fontWeight: 'bold',
  },
  header: {
    alignItems: 'center',
    paddingVertical: 32,
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
  content: {
    flex: 1,
    backgroundColor: '#f5f7fc',
    borderTopLeftRadius: 24,
    borderTopRightRadius: 24,
    padding: 24,
    gap: 12,
  },
  title: {
    fontSize: 24,
    fontWeight: 'bold',
    color: '#002d66',
  },
  text: {
    fontSize: 16,
    color: '#002d66',
    marginBottom: 12,
  },
  button: {
    alignItems: 'center',
    backgroundColor: '#F7941D',
    borderRadius: 8,
    padding: 14,
  },
  buttonSecondary: {
    backgroundColor: '#1a3a8f',
  },
  buttonText: {
    color: '#ffffff',
    fontWeight: 'bold',
    fontSize: 16,
  },
});
