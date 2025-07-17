import os
import shutil

# 👉 Chemin vers ton dossier “breast”
base_dir = r"C:\Users\boudi\OneDrive\Desktop\histologyDL\datasetC\BreaKHis_v1\BreaKHis_v1\histology_slides\breast"

# Extensions d'image à garder
keep_folders = ["40X", "100X"]

def clean_directory(path):
    for root, dirs, files in os.walk(path, topdown=False):
        # Supprimer les fichiers inutiles
        for f in files:
            # garde uniquement les fichiers d'images, supprime les autres
            if not (f.lower().endswith(".png") or f.lower().endswith(".jpg") or f.lower().endswith(".jpeg") or f.lower().endswith(".tif")):
                file_path = os.path.join(root, f)
                try:
                    os.remove(file_path)
                    print(f"Supprimé fichier: {file_path}")
                except Exception as e:
                    print(f"Erreur suppression fichier {file_path}: {e}")

        # Vérifier les sous-dossiers
        for d in dirs:
            folder_path = os.path.join(root, d)
            # Si ce n'est pas un dossier 40X ou 100X et que ce dossier contient directement des images,
            # ou si c'est un dossier comme 200X ou 400X → on supprime
            if d not in keep_folders:
                # Si ce dossier est un des niveaux de grossissement indésiré
                if d.endswith("X"):
                    try:
                        shutil.rmtree(folder_path)
                        print(f"Supprimé dossier: {folder_path}")
                    except Exception as e:
                        print(f"Erreur suppression dossier {folder_path}: {e}")
                # sinon, on garde les autres dossiers de structure (patients, types)

# Nettoyer benign et malignant
clean_directory(os.path.join(base_dir, "benign"))
clean_directory(os.path.join(base_dir, "malignant"))

print("✅ Nettoyage terminé !")