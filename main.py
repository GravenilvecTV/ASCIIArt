from PIL import Image
import requests

ascii_char = ' .:-=+*#%@'  # du plus foncé au plus clair
while True:
    # On dit à l'utilisateur d'entrer un lien:
    link = input("Entrez un lien d'une image: ")
    r = requests.get(link)
    # SI l'utilisateur a entré un faux lien:
    if r.status_code == 404:
        print("Le lien n'est pas disponible!")

    # EN REVANCHE si l'utiulisateur en entre un bon: 
    elif r.status_code == 200:
        file = open("image.jpg", "wb")
        file.write(r.content)
        file.close()

    with Image.open("image.jpg") as image:
        image = image.resize((500, 500))

        for y in range(image.height):
            line = ""
            for x in range(image.width):
                # on récupère le pixel sous format RGB
                rgb = image.getpixel((x, y))
                # on fait la moyenne de chaque channel pour faire une nuance de gris
                grey = sum(rgb) // len(rgb)
                # on fait un produit en croix pour récupérer l'index
                index = grey * 9 // 255
                # on rajoute 2 espaces, car en console la hauteur d'un char est plus grande que sa largeur
                line += ascii_char[index] + "  "
            print(line)


# On met le tout dans une boucle while au cas où il y a une erreur.
