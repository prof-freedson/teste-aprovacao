class Aprovacao:
    # Essa classe irá definir
    # a aprovação de um(a) aluno(a)
    # para a cálculo de uma média
    # aritmética de 4 notas

    # 1º Passo: método de cálculo
    # da média para 4 notas
    def calculoMedia(n1, n2, n3, n4):
       media = (n1 + n2 + n3 + n4)/4
       return media
    
    # 2º Passo: método que determina
    # a aprovação, recuperação ou
    # reprovação de um(a) aluno(a)
    def aprova_ou_reprova(media):
        if media >= 7:
            return "Aluno(a) aprovado(a)"
        if media >= 5 and media < 7:
            return "Aluno(a) de recuperação"
        else:
            return "Aluno(a) reprovado(a)"

# Atribuindo valores de notas:
""" aluno = Aprovacao()
media_aluno = aluno.calculoMedia(6,7,8,9)
situacao_aluno = aluno.aprova_ou_reprova(media_aluno)
print(situacao_aluno) """



