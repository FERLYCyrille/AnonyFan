from PIL import Image
import os

# taille recommandée pour OG/Twitter
width, height = 1200, 630
color = (255, 236, 210)  # #ffecd2 en RGB

# créer l'image
img = Image.new('RGB', (width, height), color)

# chemin vers ton dossier static
output_path = os.path.join('core', 'static', 'core', 'preview.png')
os.makedirs(os.path.dirname(output_path), exist_ok=True)

img.save(output_path)
print(f"Preview image créée : {output_path}")
