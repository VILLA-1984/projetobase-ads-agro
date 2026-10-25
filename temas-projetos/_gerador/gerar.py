# -*- coding: utf-8 -*-
"""Gera, a partir de conteudo.py, os arquivos de cada tema:
   <tema>.md  |  <tema>-moodle.html (colar no Moodle)  |  <tema>.pdf
Uso:  python _gerador/gerar.py      (precisa do pacote `markdown` e do Microsoft Edge ou Chrome)
"""
import os
import re
import shutil
import subprocess
import sys
import tempfile
import markdown

sys.path.insert(0, os.path.dirname(__file__))
from conteudo import *  # noqa

RAIZ = os.path.abspath(os.path.join(os.path.dirname(__file__), ".."))
NAVEGADORES = [
    r"C:\Program Files (x86)\Microsoft\Edge\Application\msedge.exe",
    r"C:\Program Files\Microsoft\Edge\Application\msedge.exe",
    r"C:\Program Files\Google\Chrome\Application\chrome.exe",
]
AZUL, AZUL_ESC, LARANJA, FUNDO = "#1a3a8f", "#002d66", "#F7941D", "#f5f7fc"


# ----------------------------------------------------------------- markdown
def tabela(cab, linhas):
    out = ["| " + " | ".join(cab) + " |", "|" + "---|" * len(cab)]
    out += ["| " + " | ".join(str(c) for c in l) + " |" for l in linhas]
    return "\n".join(out)


def md_referencias(nivel="##"):
    out = []
    for grupo, links in REFERENCIAS:
        out.append(f"{nivel} {grupo}\n")
        out += [f"- [{t}]({u})" for t, u in links]
        out.append("")
    return "\n".join(out)


def md_tema_livre(t, numero):
    p = [f"# Projeto {numero}: {t['titulo']}\n",
         "> Material para os alunos · React Native (Expo SDK 54) + Firebase · derivado do projeto-base de cadastro de alunos\n",
         "## 1. Ideia do tema livre\n",
         "Aqui **você escolhe o assunto**. Pode ser um app útil para o seu dia a dia, para um pequeno negócio, "
         "para a escola ou para a família. O que não é livre são os **requisitos técnicos**: o app precisa usar "
         "o que aprendemos com o projeto-base (login, Firestore, hooks, abas) e cumprir o mínimo descrito abaixo.\n",
         "> **Antes de começar**, entregue a proposta (Atividade 1) e espere a aprovação do professor.\n",
         "## 2. Requisitos mínimos obrigatórios\n"]
    p += ["- " + r for r in LIVRE_REQUISITOS]
    p += ["", "## 3. O que não pode\n"]
    p += ["- " + r for r in LIVRE_PROIBIDO]
    p += ["", "## 4. O que você vai reaproveitar do projeto-base\n",
          tabela(["Arquivo", "O que faz"], [(f"`{a}`", b) for a, b in BASE]) + "\n",
          "## 5. Cardápio de diferenciais (escolha no mínimo 3)\n",
          tabela(["Diferencial", "O que precisa ter"], [(f"**{a}**", b) for a, b in LIVRE_CARDAPIO]) + "\n",
          "## 6. Ideias de inspiração (opcional)\n",
          "Se não souber por onde começar:\n"]
    p += [f"- {i}" for i in LIVRE_IDEIAS]
    p += ["", "## 7. Modelo da proposta (1 página)\n", tabela(["Item", "O que escrever"], LIVRE_PROPOSTA) + "\n",
          "## 8. Atividades\n", "As atividades são sequenciais. Total: **100 pontos**.\n"]
    for n, titulo, itens, entregavel, criterio in ATIVIDADES_LIVRE:
        p.append(f"### Atividade {n} – {titulo} ({PONTOS[n]} pontos)\n")
        p.append("**O que fazer**\n")
        p += ["- " + i.format(colecao="sua coleção", slug="seu-tema") for i in itens]
        p.append(f"\n**Entregável:** {entregavel}\n")
        p.append(f"**Critério principal:** {criterio}\n")
    p += ["### Desafios extras (opcionais, +5 pontos cada, até 10)\n"]
    p += [f"- {e}" for e in t["extras"]]
    p += ["", "## 9. Cronograma sugerido\n",
          "**Antes da semana 1:** entregar a proposta e aguardar a aprovação.\n",
          tabela(["Período", "Atividades"], CRONOGRAMA) + "\n",
          "## 10. Avaliação\n",
          tabela(["Atividade", "Pontos"], [(f"{n} – {tt}", PONTOS[n]) for n, tt, *_ in ATIVIDADES_LIVRE] + [("**Total**", "**100**")]) + "\n",
          "O que descontamos: projeto sem aprovação da proposta, requisitos mínimos faltando, chaves/senhas pessoais "
          "no repositório público, código copiado sem entender, telas do template sobrando, app que não abre.\n",
          "## 11. Dicas importantes\n",
          "- **Leia a documentação da versão certa**: este projeto usa Expo SDK 54 (`https://docs.expo.dev/versions/v54.0.0/`).",
          "- Comece pequeno: faça o CRUD de uma coleção funcionando antes de pensar nos diferenciais.",
          "- Faça commits pequenos e frequentes: um por atividade, no mínimo.",
          "- Se o Firestore recusar a gravação, veja o código do erro no `Toast` e revise as regras de segurança.",
          "- Paleta de cores do projeto-base (use ou troque): " + ", ".join(f"`{c}` {n}" for c, n in CORES) + ".\n"]
    ap = md_apresentacao(t)
    ap[0] = ap[0].replace("## 10.", "## 12.")
    p += ap
    p += ["## 13. Referências\n", md_referencias("###")]
    return "\n".join(p)


def md_tema(t, numero):
    if t.get("livre"):
        return md_tema_livre(t, numero)
    p = [f"# Projeto {numero}: {t['titulo']}\n",
         "> Material para os alunos · React Native (Expo SDK 54) + Firebase · parte do projeto-base de cadastro de alunos\n",
         "## 1. Contexto\n", t["contexto"] + "\n",
         "## 2. Objetivo\n",
         f"Construir um aplicativo mobile (rodando também no navegador) que faça o controle de **{t['entidade']}s**, "
         "com login, cadastro, listagem, alteração, exclusão e uma funcionalidade diferencial do tema. "
         "Você vai **partir do projeto-base** (cadastro de alunos) e adaptá-lo ao seu tema.\n",
         "## 3. O que você vai reaproveitar do projeto-base\n",
         tabela(["Arquivo", "O que faz"], [(f"`{a}`", b) for a, b in BASE]) + "\n",
         "## 4. Modelo de dados (Firestore)\n",
         f"### Coleção `{t['colecao']}`\n",
         tabela(["Campo", "Tipo", "Obrigatório", "Descrição"], [(f"`{a}`", b, c, d) for a, b, c, d in t["campos"]]) + "\n",
         f"### Subcoleção `{t['sub'][1]}`\n",
         tabela(["Campo", "Tipo", "Descrição"], [(f"`{a}`", b, c) for a, b, c in t["sub"][2]]) + "\n",
         "> Datas são guardadas como texto `AAAA-MM-DD`; números (peso, quantidade, horas…) devem ser gravados como `number`, "
         "não como texto.\n",
         "## 5. Telas do aplicativo\n"]
    p += [f"{i}. {x}" for i, x in enumerate(t["telas"], 1)]
    p += ["", "## 6. Atividades\n",
          "As atividades são sequenciais: cada uma depende da anterior. Total: **100 pontos**.\n"]
    for n, titulo, itens, entregavel, criterio in ATIVIDADES:
        dif = t["diferencial"]
        if n == 7:
            titulo = titulo.format(dif_nome=dif["nome"])
            itens = dif["itens"]
            entregavel = "Vídeo curto (até 2 min) mostrando a funcionalidade e prints do Firestore."
            criterio = "Todos os itens funcionam e os dados ficam consistentes entre as coleções."
        titulo = titulo.format(entidade=t["entidade"])
        p.append(f"### Atividade {n} – {titulo} ({PONTOS[n]} pontos)\n")
        p.append("**O que fazer**\n")
        p += ["- " + i.format(colecao=t["colecao"], slug=t["slug"]) for i in itens]
        p.append(f"\n**Entregável:** {entregavel}\n")
        p.append(f"**Critério principal:** {criterio}\n")
    p += ["### Desafios extras (opcionais, +5 pontos cada, até 10)\n"]
    p += [f"- {e}" for e in t["extras"]]
    p += ["", "## 7. Cronograma sugerido\n", tabela(["Período", "Atividades"], CRONOGRAMA) + "\n",
          "## 8. Avaliação\n",
          tabela(["Atividade", "Pontos"], [(f"{n} – {tt.format(entidade=t['entidade'], dif_nome=t['diferencial']['nome'])}", PONTOS[n])
                                           for n, tt, *_ in ATIVIDADES] + [("**Total**", "**100**")]) + "\n",
          "O que descontamos: chaves/senhas pessoais no repositório público, código copiado sem entender, "
          "telas do template do Expo sobrando, app que não abre.\n",
          "## 9. Dicas importantes\n",
          "- **Leia a documentação da versão certa**: este projeto usa Expo SDK 54 (`https://docs.expo.dev/versions/v54.0.0/`). "
          "Tutoriais antigos podem ensinar APIs que mudaram.",
          "- Faça commits pequenos e frequentes: um por atividade, no mínimo.",
          "- Teste no navegador (`w` no terminal do Expo) e no celular (Expo Go) quando puder.",
          "- Se o Firestore recusar a gravação, veja o código do erro no `Toast` e revise as regras de segurança.",
          "- Paleta de cores sugerida (inspirada no UniSenai): " + ", ".join(f"`{c}` {n}" for c, n in CORES) + ".\n",
          ]
    p += md_apresentacao(t)
    p += ["## 11. Referências\n", md_referencias("###")]
    return "\n".join(p)


def md_apresentacao(t):
    total = sum(m for _, m, _ in ROTEIRO)
    out = ["## 10. Apresentação final e roteiro (até 15 minutos por grupo)\n",
           "Cada grupo apresentará o projeto para a turma. A apresentação vale **15 pontos** (Atividade 9). "
           "Todos os integrantes devem falar e responder perguntas.\n",
           "### Roteiro sugerido\n",
           tabela(["#", "Tópico", "Tempo", "O que abordar"],
                  [(i, a, f"{m} min", c) for i, (a, m, c) in enumerate(ROTEIRO, 1)] + [("", "**Total**", f"**{total} min**", "")]) + "\n",
           "### Desafios sugeridos para o seu tema\n",
           "Escolha os que o seu grupo realmente enfrentou e conte **o problema, o que tentaram e a solução**.\n",
           "**Framework (React Native / Expo / Expo Router)**\n"]
    out += ["- " + x for x in t["desafios_fw"]]
    out += ["", "**Tecnologia (Firebase / Firestore / TypeScript)**\n"]
    out += ["- " + x for x in t["desafios_tec"]]
    out += ["", "> Além dos sugeridos, vale citar os desafios comuns: rotas com o mesmo caminho (`/` do login e da tela inicial), "
            "loop de renderização por callback não memorizado e números gravados como texto.\n",
            "### Checklist antes de apresentar\n",
            "- Slides prontos (cerca de 1 por minuto) e enviados em PDF.",
            "- App rodando, com dados de exemplo já cadastrados.",
            "- Vídeo de reserva caso a internet ou o Firebase falhe.",
            "- Falas divididas entre todos os integrantes; tempo ensaiado.",
            "- Chaves e senhas pessoais **fora** dos slides.\n",
            "### Avaliação da apresentação\n",
            tabela(["Critério", "Pontos"], CRITERIOS_APRESENTACAO + [("**Total**", "**15**")]) + "\n"]
    return out


def md_guia():
    p = ["# Guia do projeto-base\n",
         "Este guia explica o projeto de **cadastro de alunos** que serve de modelo para os três temas.\n",
         "## Como rodar\n",
         "```bash\nnpm install\nnpx expo start\n```\n",
         "Pressione `w` para abrir no navegador ou leia o QR Code com o app **Expo Go** no celular.\n",
         "## Mapa dos arquivos\n",
         tabela(["Arquivo", "O que faz"], [(f"`{a}`", b) for a, b in BASE]) + "\n",
         "## Fluxo de dados\n",
         "1. `frm-login.tsx` autentica com `signInWithEmailAndPassword` e vai para as abas.",
         "2. `frm-cad-aluno.tsx` grava com `addDoc` (cadastro) ou `updateDoc` (quando recebe `id`).",
         "3. `use-alunos.ts` lê do Firestore (`getDocs`/`getDoc`) e devolve os dados para a tela.",
         "4. `lst-aluno.tsx` mostra os cartões; **Alterar** navega com `router.push` passando o `id`; **Excluir** usa `deleteDoc`.",
         "5. `use-focus-refresh.ts` recarrega a lista ao voltar para a tela.",
         "6. O botão **Sair** da tela inicial chama `signOut` e volta ao login.\n",
         "## Atenção: rotas com o mesmo caminho\n",
         "A tela de login (`app/(auth)/index.tsx`) e a tela inicial (`app/(tabs)/index.tsx`) têm ambas a rota `/`. "
         "Para voltar ao login use `router.replace('/(auth)')`, e não `router.replace('/')`.\n",
         "## Como adaptar para o seu tema\n",
         "1. Copie `use-alunos.ts` para `use-<seu-tema>.ts` e troque a coleção e os campos.",
         "2. Copie o formulário e a lista trocando os campos e os textos.",
         "3. Ajuste as abas em `app/(tabs)/_layout.tsx`.",
         "4. Troque a configuração em `firebase.ts` pelo **seu** projeto Firebase.\n",
         "## Referências\n", md_referencias("###")]
    return "\n".join(p)


def md_readme(temas):
    p = ["# Temas de projeto – React (Expo) + Firebase\n",
         "Pasta de distribuição dos projetos finais. Cada aluno (ou dupla) recebe **um** tema e parte do "
         "projeto-base de cadastro de alunos. *Material para o professor; os documentos de cada tema são escritos para os alunos.*\n",
         "O **tema livre** (`04-tema-livre/`) não tem assunto fixo: o grupo propõe o app, o professor aprova a proposta "
         "e o grupo cumpre requisitos mínimos e escolhe diferenciais de um cardápio.\n",
         "## Temas\n",
         tabela(["Tema", "Pasta", "Coleção principal", "Diferencial"],
                [(t["titulo"], f"`{t['pasta']}/`", f"`{t['colecao']}`", t["diferencial"]["nome"]) for t in temas]) + "\n",
         "## Conteúdo de cada pasta\n",
         tabela(["Arquivo", "Uso"], [("`tema.md`", "Fonte em Markdown (GitHub/VS Code)"),
                                     ("`tema-moodle.html`", "HTML com estilos embutidos para colar no Moodle"),
                                     ("`tema.pdf`", "Versão para impressão/anexo")]) + "\n",
         "## Arquivos comuns\n",
         "- `guia-projeto-base.*` – como o projeto-base funciona e como adaptá-lo.",
         "- `referencias.*` – links da documentação oficial.",
         "- `_gerador/` – scripts que geram HTML e PDF a partir do conteúdo (`python _gerador/gerar.py`).\n",
         "## Estrutura comum das atividades (100 pontos)\n",
         tabela(["Atividade", "Pontos"], [(f"{n} – {tt.format(entidade='registro', dif_nome='Diferencial do tema')}", PONTOS[n]) for n, tt, *_ in ATIVIDADES]) + "\n",
         "## Como usar no Moodle\n",
         "1. Crie um recurso **Página** (ou uma descrição de **Tarefa**) e abra o editor.",
         "2. No editor (Atto ou TinyMCE), clique no botão `<>` (**Editar código-fonte / HTML**).",
         "3. Cole todo o conteúdo de `tema-moodle.html` e salve.",
         "4. Anexe o `tema.pdf` como arquivo complementar.\n",
         "## Distribuição sugerida\n",
         "Sorteie ou deixe os alunos escolherem, limitando o número de duplas por tema. "
         "Peça que **cada um crie o seu projeto Firebase** para não compartilharem credenciais.\n",
         "## Observação sobre os links\n",
         "As referências apontam para a documentação oficial. Confira se continuam válidos a cada semestre."]
    return "\n".join(p)


# --------------------------------------------------------------- HTML / PDF
ESTILOS = {
    "h1": f"color:{AZUL};border-bottom:4px solid {LARANJA};padding-bottom:6px;margin:0 0 12px",
    "h2": f"color:{AZUL};margin:28px 0 8px;border-left:6px solid {LARANJA};padding-left:10px",
    "h3": f"color:{AZUL_ESC};margin:20px 0 6px",
    "p": "line-height:1.5;margin:6px 0",
    "ul": "line-height:1.5;margin:6px 0 6px 20px",
    "ol": "line-height:1.5;margin:6px 0 6px 20px",
    "table": "border-collapse:collapse;width:100%;margin:10px 0;font-size:14px",
    "th": f"background:{AZUL};color:#ffffff;text-align:left;padding:6px 8px;border:1px solid #d4ddf0",
    "td": "padding:6px 8px;border:1px solid #d4ddf0;vertical-align:top",
    "blockquote": f"background:{FUNDO};border-left:4px solid {AZUL};margin:10px 0;padding:6px 12px;color:{AZUL_ESC}",
    "pre": f"background:{FUNDO};padding:10px;border:1px solid #d4ddf0;border-radius:6px;overflow:auto",
    "a": f"color:{AZUL}",
}
CODE_INLINE = "background:#eef2f9;padding:1px 5px;border-radius:4px;font-family:Consolas,monospace;font-size:90%"


def para_html(md_texto):
    return markdown.markdown(md_texto, extensions=["tables", "fenced_code", "sane_lists"])


def moodle(md_texto):
    """Fragmento com estilos inline (o Moodle costuma remover <style>)."""
    html = para_html(md_texto)
    html = re.sub(r"<pre>\s*<code>", "<pre><code>", html)

    def estilizar(m):
        tag, resto = m.group(1), m.group(2)
        return f'<{tag} style="{ESTILOS[tag]}"{resto}>' if tag in ESTILOS else m.group(0)

    html = re.sub(r"<(h1|h2|h3|p|ul|ol|table|th|td|blockquote|pre|a)(\b[^>]*)>", estilizar, html)
    html = re.sub(r"<code>", f'<code style="{CODE_INLINE}">', html)
    return f'<div style="font-family:Arial,Helvetica,sans-serif;color:{AZUL_ESC};max-width:900px">\n{html}\n</div>\n'


def pagina_pdf(md_texto, titulo):
    css = "".join(f"{k}{{{v}}}" for k, v in ESTILOS.items())
    return (f'<!doctype html><html lang="pt-BR"><head><meta charset="utf-8"><title>{titulo}</title>'
            f'<style>@page{{margin:16mm}}body{{font-family:Arial,Helvetica,sans-serif;color:{AZUL_ESC};font-size:13px}}'
            f'{css}code{{{CODE_INLINE}}}h2,h3,tr{{break-inside:avoid}}</style></head><body>{para_html(md_texto)}</body></html>')


def navegador():
    for n in NAVEGADORES:
        if os.path.exists(n):
            return n
    raise SystemExit("Edge/Chrome não encontrado para gerar o PDF.")


def gerar_pdf(md_texto, titulo, destino):
    with tempfile.TemporaryDirectory() as d:
        arq = os.path.join(d, "p.html")
        with open(arq, "w", encoding="utf-8") as f:
            f.write(pagina_pdf(md_texto, titulo))
        subprocess.run([navegador(), "--headless", "--disable-gpu", "--no-pdf-header-footer",
                        f"--user-data-dir={os.path.join(d, 'perfil')}",
                        f"--print-to-pdf={destino}", "file:///" + arq.replace("\\", "/")],
                       check=True, capture_output=True, timeout=120)


def salvar(pasta, base, md_texto, titulo):
    os.makedirs(pasta, exist_ok=True)
    with open(os.path.join(pasta, base + ".md"), "w", encoding="utf-8", newline="\n") as f:
        f.write(md_texto)
    with open(os.path.join(pasta, base + "-moodle.html"), "w", encoding="utf-8", newline="\n") as f:
        f.write(moodle(md_texto))
    gerar_pdf(md_texto, titulo, os.path.join(pasta, base + ".pdf"))
    print("ok:", os.path.relpath(os.path.join(pasta, base), RAIZ))


if __name__ == "__main__":
    for i, t in enumerate(TEMAS, 1):
        salvar(os.path.join(RAIZ, t["pasta"]), "tema", md_tema(t, i), f"Projeto {i} - {t['titulo']}")
    salvar(RAIZ, "guia-projeto-base", md_guia(), "Guia do projeto-base")
    salvar(RAIZ, "referencias", "# Referências\n\nDocumentação oficial usada nos projetos.\n\n" + md_referencias("##"), "Referências")
    with open(os.path.join(RAIZ, "README.md"), "w", encoding="utf-8", newline="\n") as f:
        f.write(md_readme(TEMAS))
    print("README.md do professor gerado")
