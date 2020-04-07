# -*- coding: utf-8 -*-
"""
Created on Mon Apr  6 23:29:42 2020

@author: papico
"""
import imageio 
import numpy 
import numpy as np
import matplotlib.image as mpimg



## Image Processing
class Picture:
    '''
    Creer une image à partir d'un fichier en utilisant la fonction imread() de matplotlig.image ou plus généralement la 
    librairie Pillow
    '''
    def __init__(self,nomFichier = None,H = None, W = None):
        if nomFichier == None:
                
            '''
            Creer une image blanche de hauteur H et de largeur W
            '''
            self.H = H
            self.W = W
            self.img = np.zeros((H,W,3))
        else:
                
            '''
            Creer une image à partir d'un fichier
            '''
            self.img = mpimg.imread(nomFichier)
            self.H = self.img.shape[1]
            self.W = self.img.shape[0]
        
    
    '''
    Retourne la hauteur H
    '''
    def getH(self):
        return self.H
    '''
    Retourne la largeur W
    '''
    def getW(self):
        return self.W
    '''
    Retourne le tableau numpy constituant l'image
    '''
    def getImg(self):
        return self.img
    '''
    Retourne les couleurs R,G, B sous forme de liste du pixel à la ligne row et la colonne col
    '''
    def getCouleur(self,row, col):
        return self.img[row,col]
         
    '''
    Modifie les couleurs R,G,B du pixel à la ligne row et la colonne col
    '''
    def setCouleur(self,row, col,couleur):
        self.img[row,col]=couleur
        
        
    '''
    Affiche une image
    '''
    def affiche(self):
        plt.imshow(self.img)
        plt.show()
    '''
    Sauve  une image dans un fichier png
    '''
    def save(self, nomFichier):
        
        plt.imsave(nomFichier, self.img, format = 'png')
    
    
   #########programme principal#####################

   # on Cree une image à partir d'un fichier babouin.png en utilisant la fonction imread() de matplotlig.image 

p1=Picture("babouin.png",100,100)

 # On Retourne la hauteur H
print("la hauteur du fichier est",p1.getH())

 
# Retourne la largeur W
print("la largeur est ",p1.getW())

#    Retourne le tableau numpy constituant l'image
print("Retourne le tableau numpy constituant l'image")
p1.getImg

#On  Retourne les couleurs R,G, B sous forme de liste du pixel à la ligne 100 et la colonne 120
p1.img[100,120]

#Affichage del'image
p1.affiche()

#    Sauvegarder l'image  dans un fichier babouin2 png
p1.save("babouin2")


rouge = p1.img[:,:,0] 
vert = p1.img[:,:,1] 
bleu = p1.img[:,:,2]
print(rouge[100,120]) 
#La fonction matplotlib.pyplot.imshow permet d’aﬃcher un tableau sous forme d’une image :

figure(figsize=(4,4)) 
imshow(rouge,cmap="gray")


#Le pixel de coordonnées (i,j) est l’élément rouge[j,i]. L’argument cmap=’gray’ permet de représenter les valeurs en niveaux de gris. La fonctionmatplotlib.pyplot.imshowainsiutiliséeconvertitlaplagedevaleurs[min,max] du tableau en valeurs dans l’intervalle [0,255] pour l’aﬃchage en image. Il peut être intéressant de représenter l’image en niveaux de gris avec une échelle de couleurs, car nous identiﬁons plus facilement une couleur qu’un niveau de gris :

figure(figsize=(5,5)) 
imshow(rouge) 
colorbar()

#Une partie rectangulaire d’une image peut être extraite de la manière suivante, en faisant attention à indiquer les lignes sélectionnées en premier :

partie = rouge[0:60,60:160] 
figure(figsize=(4,4)) 
imshow(partie,cmap="gray")


#Une opération courante est la sélection d’une seule ligne (ou d’une seule colonne) :
ligne20 = rouge[20,:] 
figure(figsize=(8,4)) 
plot(ligne20)

# Modiﬁcation des niveaux de gris 

def seuillage(image,seuil): 
    resultat = image.copy() 
    s = image.shape 
    for j in range(s[0]): 
        for i in range(s[1]): 
            if image[j,i] > seuil: 
                resultat[j,i] = 1 
            else: 
                resultat[j,i] = 0 
        return resultat
im4 = seuillage(rouge,0.5) 
figure(figsize=(4,4)) 
imshow(im4,cmap="gray",vmin=0,vmax=1)


#Enregistrement d’une image 
#L’image précédente peut être enregistrée avec la fonction imageio.imwrite :

imageio.imwrite("imA.png",rouge)


#On peut aussi reconstituer une image en couleur à partir de ses trois couches. Pour obtenir une image diﬀérente de l’image initiale, on réduit les valeurs de la couche rouge. On doit tout d’abord créer un tableau à trois dimensions et le remplir avec les couches.

s = rouge.shape 
couleur = numpy.zeros((s[0],s[1],3),dtype=numpy.float32) 
couleur[:,:,0] = rouge*0.5
couleur[:,:,1] = vert 
couleur[:,:,2] = bleu 
imsave("imB.png",couleur)
imshow(couleur)
