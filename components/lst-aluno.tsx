import { useFocusRefresh } from "@/hooks/use-focus-refresh";
import { useAlunos } from "@/hooks/use-alunos";

import Toast from "react-native-toast-message";
import { router } from "expo-router";
import { db } from "@/firebase";
import { deleteDoc, doc } from 'firebase/firestore';

import {View, FlatList, StyleSheet, Text, StatusBar, TouchableOpacity} from 'react-native';
import {SafeAreaView, SafeAreaProvider} from 'react-native-safe-area-context';

export default function LstAlunos(){

  const { alunos, carregarAlunos } = useAlunos();

  async function excluirAluno(id: string){
    try{
      await deleteDoc(doc(db, "alunos", id));
      Toast.show({
        type: "success",
        text1: "Deletado!",
        text2: "Registro deletado com Sucesso!"
      });
      carregarAlunos();
    }catch(error: any){
      Toast.show({
        type: "error",
        text1: "Erro!",
        text2: "Erro ao deletar o Registro!"
      })
    }
  }

  function editarAluno(id: string){
    router.push({ pathname: "/(tabs)/aluno",params:{id}})
  }

  useFocusRefresh(carregarAlunos);

  return (
   <SafeAreaProvider>
    <SafeAreaView style={styles.container}>
      <FlatList
        data={alunos}
        keyExtractor={item => item.id}
        renderItem={({item}) => (
          <View style={styles.card}>
            <Text style={styles.nome}>{item.nome}</Text>
            <Text style={styles.info}>Idade: {item.idade}</Text>
            <Text style={styles.info}>Matrícula: {item.matricula}</Text>

            <View style={styles.acoes}>
              <TouchableOpacity style={[styles.botao, styles.botaoAlterar]} onPress={
                ()=>editarAluno(item.id)
              }>
                <Text style={styles.botaoTexto}>Alterar</Text>
              </TouchableOpacity>

              <TouchableOpacity style={[styles.botao, styles.botaoExcluir]} onPress={
                ()=>excluirAluno(item.id)
              }>
                <Text style={styles.botaoTexto}>Excluir</Text>
              </TouchableOpacity>
            </View>
          </View>
        )}
      />
    </SafeAreaView>
  </SafeAreaProvider>
  );
};

const styles = StyleSheet.create({
  container: {
    flex: 1,
    marginTop: StatusBar.currentHeight || 0,
    backgroundColor: '#f5f7fc',
  },
  card: {
    backgroundColor: '#ffffff',
    borderRadius: 12,
    borderLeftWidth: 4,
    borderLeftColor: '#F7941D',
    padding: 16,
    marginVertical: 8,
    marginHorizontal: 16,
  },
  nome: {
    fontSize: 18,
    fontWeight: 'bold',
    color: '#1a3a8f',
  },
  info: {
    fontSize: 14,
    color: '#002d66',
    marginTop: 2,
  },
  acoes: {
    flexDirection: 'row',
    gap: 8,
    marginTop: 12,
  },
  botao: {
    flex: 1,
    alignItems: 'center',
    borderRadius: 8,
    padding: 10,
  },
  botaoAlterar: {
    backgroundColor: '#1a3a8f',
  },
  botaoExcluir: {
    backgroundColor: '#e85d04',
  },
  botaoTexto: {
    color: '#ffffff',
    fontWeight: 'bold',
  },
});
