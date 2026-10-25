import { useCallback, useState } from "react";
import Toast from "react-native-toast-message";
import { db } from "@/firebase";
import { collection, doc, getDoc, getDocs } from "firebase/firestore";

export interface Aluno {
  id: string;
  nome: string;
  idade: string;
  email: string;
  matricula: string;
}

export function useAlunos() {
  const [alunos, setAlunos] = useState<Aluno[]>([]);

  const carregarAlunos = useCallback(async () => {
    try {
      const dados = await getDocs(collection(db, "alunos"));
      setAlunos(dados.docs.map((d) => ({ id: d.id, ...d.data() }) as Aluno));
    } catch (error: any) {
      Toast.show({
        type: "error",
        text1: "Erro",
        text2: "ERRO AO CONSULTAR DADOS: " + (error.code ?? error.message),
      });
    }
  }, []);

  const carregarAluno = useCallback(async (id: string) => {
    try {
      const d = await getDoc(doc(db, "alunos", id));
      if (!d.exists()) throw new Error("Aluno não encontrado");
      return { id: d.id, ...d.data() } as Aluno;
    } catch (error: any) {
      Toast.show({
        type: "error",
        text1: "Erro",
        text2: "ERRO AO CONSULTAR ALUNO: " + (error.code ?? error.message),
      });
      return null;
    }
  }, []);

  return { alunos, carregarAlunos, carregarAluno };
}
