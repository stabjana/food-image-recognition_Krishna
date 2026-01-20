from glob import glob
import os
from PIL import Image, ImageEnhance

# Zielordner
os.makedirs('jpg_darker', exist_ok=True)

# Alle JPG-Dateien sammeln
jpg_files = (
    glob('*.jpg') +
    glob('*.JPG') +
    glob('*.jpeg') +
    glob('*.JPEG')
)

for img in jpg_files:
    try:
        im = Image.open(img).convert('RGB')

        # Helligkeit um 50 % reduzieren
        enhancer = ImageEnhance.Brightness(im)
        darker = enhancer.enhance(0.5)

        base, _ = os.path.splitext(img)
        out_name = f"{base}-darker.jpg"

        darker.save(f'jpg_darker/{out_name}', 'JPEG')

    except Exception as e:
        print(f"Fehler bei {img}: {e}")

print(f"{len(jpg_files)} Bilder wurden abgedunkelt.")

