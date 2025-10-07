import  wikipedia

wikipedia.set_lang("pt")

def wiki(): #Função principal que faz a pesquisa na wiki
    assunto = wikipedia.search(input("Assunto da wiki:"))
    print(assunto)
    print("...")
    pagina = wikipedia.page(assunto[0])
    print("Conteudo Completo:"); completo = pagina.content; print(completo)
    print()
    print("*#*" * 30)
    print()
    print("Conteudo resumido:"); resumido = pagina.summary; print(resumido)
    nova_pesquisa = input("Deseja pesquisar novamente? S/n ")
    if nova_pesquisa == "n":
        exit()
    else:
        return

while True:
    wiki()
