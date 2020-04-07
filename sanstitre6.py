# -*- coding: utf-8 -*-
"""
Created on Mon Apr  6 23:37:16 2020

@author: papico
"""

import imageio 
import numpy 
from matplotlib.pyplot import * 
img = imread("babouin.png")
#Voici les dimensions du tableau et le type de données :
print(img.shape) 

print(img.dtype) 

rouge = img[:,:,0] 
vert = img[:,:,1] 
bleu = img[:,:,2]
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


## Image processing
class ImageProcessing:
    
    def __init__(self,image):
        self.image = image
    '''
    Helper function
    '''
    def __calGray__(listePixel):
        A = math.floor(0.299*listePixel[0] + 0.587*listePixel[1] + 0.114*listePixel[2])
        return np.ndarray([A,A,A])
        
    '''
     Transformer en grayscale et visualiser l'image et sa transformée
     Appliquer les fonctions map, reduce ou filter pour reduire la complexite
    '''
    def transformGrayscaleMap(self):
        grayPicture = Picture(None,self.image.W,self.image.H)
        grayPicture.image = map(self.__calGray__,self.image[:,:])
        return grayPicture
        
    '''
     Transformer en grayscale et visualiser l'image et sa transformée
     Une classe gloutonne avec des boucles for
    '''
    def transformGrayscaleGlouton(self):
        pass
                 
        
    '''
     Creer une image en inversant les proportions de l'image source. Afficher les deux images
    '''
    def transformScale(self):
        pass
    '''
    Separer les couleurs d'une image et visualiser les trois couleurs
    '''
    def separerCouleur(self):
        pass
    '''
    Filtre de glace: Affecter à chaque pixel p la couleur d'un pixel voisin choisi alétoirement
    (Les coordonnées du pixel et de p doivent différer d'au plus 5).
    Afficher les deux images 
    '''
    def filtreGlass(self):
        pass