
######################################################################################## Correction de l'exercice 4 BAC 2020 ##########################################################################
########################################################################################          Colonne Dominante          ##########################################################################
########################################################################################        Correction proposée par       ##########################################################################
########################################################################################            TUNISIA TUTO             ##########################################################################     
def Remplir(F,M,n):
    fichier=open(F,"a+")
    Vmax=-999999
    nc=0
    for i in range(n):
        for j in range(n):
            if M[i][j]>Vmax:
                Vmax=M[i][j]
                nc=j
        fichier.write("Vmax={}, NL={} et NC={}\n".format(Vmax,i+1,nc+1))
        Vmax=-999999
        nc=0
    fichier.close()
    
def Saisir(M,n):
    for i in range(n):
        M.append([0]*n)
        for j in range(n):
            M[i][j]=int(input("M[{}][{}]=".format(i,j)))
    return M
        

def Frequence(F,NC):
    file=open(F,"r")
    occ=0
    for ligne in file:
        nm=int(ligne[len(ligne)-2])
        if NC==nm:
            occ=occ+1
    file.close()
    return occ
        


def col_dominante(F):
    file=open(F,"r")
    text=file.readlines()
    lignes=len(text)
    file.close()
    nb_occ=-99999
    cd=0
    for i in range(lignes):
        if Frequence(F,i+1)>nb_occ:
            nb_occ=Frequence(F,i+1)
            cd=i+1
    return cd
    

def main():
    M=[]
    F="F_Max.dat"
    n=int(input("Donnez la dimension de la matrice M:"))
    N=Saisir(M,n)
    Remplir(F,M,n)
    CD=col_dominante(F)
    print("La colonne dominante est {}".format(CD))
    
    


if __name__=="__main__":
    main()