candidatos = [
    {"nome": "Candidato 1", "resultado": "e3_t5_p7_s9"},
    {"nome": "Candidato 2", "resultado": "e4_t6_p8_s10"},
    {"nome": "Candidato 3", "resultado": "e2_t4_p6_s8"},
    {"nome": "Candidato 4", "resultado": "e5_t7_p9_s11"},
    {"nome": "Candidato 5", "resultado": "e4_t4_p8_s8"}
]

opcao_escolhida = -1

def adicionar_candidato():
    nome = input("Digite o nome do candidato: ")
    resultado_entrevista = int(input("Digite a nota do candidato na entrevista: "))
    resultado_teste_teórico = int(input("Digite a nota do candidato no teste teórico: "))
    resultado_teste_prático = int(input("Digite a nota do candidato no teste prático: "))
    resultado_soft_skills = int(input("Digite a nota do candidato na avaliação de soft skills: "))
    
    resultado = "e{}_t{}_p{}_s{}".format(resultado_entrevista, resultado_teste_teórico, resultado_teste_prático, resultado_soft_skills)
    candidatos.append({"nome": nome, "resultado": resultado})
    

def buscar_candidatos(candidatos, e_min, t_min, p_min, s_min):
    candidatos_selecionados = []
    for candidato in candidatos:
        resultado = candidato["resultado"].split('_')
        e = int(resultado[0][1:])
        t = int(resultado[1][1:])
        p = int(resultado[2][1:])
        s = int(resultado[3][1:])
        if e >= e_min and t >= t_min and p >= p_min and s >= s_min:
            candidatos_selecionados.append(candidato["nome"])
    return candidatos_selecionados

while opcao_escolhida != 0:
    opcao_escolhida = int(input(f'''
    ===========  O QUE DESEJA FAZER?  ============
            [1] - ADICIONAR CADIDATOS
            [2] - BUSCAR CANDIDATOS                  
            [0] - SAIR
    ==============================================                            
    '''))
    match opcao_escolhida:
        case 1:
            adicionar_candidato()
            print("Adicionado com Sucesso!")
        case 2:
            e_min = int(input("Digite a nota mínima na entrevista: "))
            t_min = int(input("Digite a nota mínima no teste teórico: "))
            p_min = int(input("Digite a nota mínima no teste prático: "))
            s_min = int(input("Digite a nota mínima na avaliação de soft skills: "))
            candidatos_selecionados = buscar_candidatos(candidatos, e_min, t_min, p_min, s_min)
            if candidatos_selecionados:
                print("Os candidatos que atendem aos critérios são:")
                for candidato in candidatos_selecionados:
                    print(candidato)
            else:
                print("Não há candidatos que atendam aos critérios informados.")
        case 0:
            print("Encerrando sistema... Volte Sempre!")
        case _:
            print("Opção inválida! Por favor tente umas das opções abaixo:")