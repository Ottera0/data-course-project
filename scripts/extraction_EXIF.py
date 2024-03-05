import os
import json
from PIL import Image
from PIL.ExifTags import TAGS

def get_exif_data(image):
    exif_data = {}
    info = image._getexif()
    if info:
        for tag, value in info.items():
            decoded = TAGS.get(tag, tag)
            exif_data[decoded] = value
    return exif_data

def get_orientation(width, height):
    if width > height:
        return "Paysage"
    elif width < height:
        return "Portrait"
    else:
        return "Carré"

# Chemin vers le dossier contenant vos images
directory = "../data/images/"

# Créer un dictionnaire pour stocker les métadonnées
metadata = {}

# Parcourir le dossier des images et extraire les métadonnées
for filename in os.listdir(directory):
    file_path = os.path.join(directory, filename)
    with Image.open(file_path) as img:
        metadata[filename] = {
            "Taille": img.size,
            "Format": img.format,
            "Orientation": get_orientation(*img.size),
            "EXIF": get_exif_data(img)
        }

# Enregistrer les métadonnées dans un fichier JSON
with open('image_metadata.json', 'w') as f:
    json.dump(metadata, f, indent=4)
