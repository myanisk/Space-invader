# Space-invader

Mohamed Yanis KOUFI - Robotique B3
---------------------------------------------------------------

# PRESENTATION DU PROJET :

Tout d'abord "Space-invader" est un jeu en deux dimensions où le joueur contrôle un vaisseau spatial et il doit détruire des vaisseaux ennemis se déplaçant latéralement et avançant vers le vaisseau du joueur jusqu'à arriver à une certaine limite qui annonce la perte de la partie de jeu.
Durant ce projet nous devons developper en python un équivalent de ce jeu sur une STM32F407VG-DISC1 avec certaines directives à respecter :
- Déplacement à l'accéléromètre
- Tir au bouton poussoir bleu
- Affichage par UART
- Certaines choses seront contrôlées par timer   

    
---------------------------------------------------------------

# MODE D'EMPLOI :

Afin de jouer au jeu il faudra tout d'abord mettre python sur la carte, car ce n'est pas un langage prévu de base par la carte.
Il faudra alors suivre les étapes suivantes :

    Téléchargez le programme de flashage : https://github.com/micropython/micropython/blob/master/tools/pydfu.py
        Par exemple : https://github.com/micropython/micropython/blob/cdaec0dcaffbfcb58e190738cf6e9d34541464f0/tools/pydfu.py

    Créez un environnement virtuel, avec un shell
        cd  le_dossier_qui_va_bien
        python3.8 -m venv    venv
    Activez l'environnement virtuel
        source venv/bin/activate 
    (venv) est ajouté au début du promptpip  
        install pyusb==1.1.1
        
    Sur STM32F4 Discovery
        https://www.micropython.org/download#other  -> Prenez la dernière version stable
    
    Débranchez la STM32F4 Discovery et mettez un jumper entre VDD et BOOT0
    
    Branchez un câble mini-USB en haut de la STM32F4-Discovery
    Branchez un câble micro-USB en bas de la STM32F4-Discovery
    
    Rentrez les commandes suivantes :
       " python pydfu.py --list "
       " python pydfu.py --upload STM32F4DISC-20210222-v1.14.dfu "
    
    Ejectez la clé USB
    Retirez le Jumper
    Appuyez sur le bouton poussoir noir (Reset)
    
    Remplacez le contenu de la clé par les fichiers telecharger sur ce repertoire git 
    
    Ejectez la clé USB
    Appuyez sur le bouton poussoir noir (Reset)
    
    Lancer Putty, configutation :
    -> Serial line : Dépend du branchement 
    -> Speed : 115200
    -> Connection type : Serial
    
Touches : 
    - bouton bleu : tirer
    - orienter la carte : bouger le vaisseau

---------------------------------------------------------------

# DIFFICULTES RENCONTREES :

Les 3 plus grandes difficultés rencontrées :

    -> Le fait d'ejecter à chaque fois l'usb afin de tester le code, cela prenait beaucoup de temps tout en ayant des doutes sur le fait que le code soit bon.
        
    -> Le mouvement des vaisseaux ennemis qui doit être controlé par un timer

    -> le controle des missiles et de leur collisions  
        
  
---------------------------------------------------------------

# RETOUR GENERAL SUR LE PROJET :

Malgrés la frustration de ne pas avoir pu rendre un jeu fonctionnel et d'avoir été malade durant les deux dernieres semaines, l'idée de developper un jeu emblematique sur STM32F407VG-DISC1 est super interessant et m'a permis de m'améliorer en python (que j'avais déjà vu pour des applications purement mathématiques). Merci.   