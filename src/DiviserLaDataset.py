import os, shutil, random

# Chemins source
benign_source = r"C:\Users\boudi\OneDrive\Desktop\histologyDL\datasetC\BreaKHis_v1\BreaKHis_v1\histology_slides\breast\benign"
malignant_source = r"C:\Users\boudi\OneDrive\Desktop\histologyDL\datasetC\BreaKHis_v1\BreaKHis_v1\histology_slides\breast\malignant"

# Chemin destination
base_target = r"C:\Users\boudi\OneDrive\Desktop\histologyDL\data"
train_benign = os.path.join(base_target, "train", "benign")
train_malignant = os.path.join(base_target, "train", "malignant")
val_benign = os.path.join(base_target, "val", "benign")
val_malignant = os.path.join(base_target, "val", "malignant")

for p in [train_benign, train_malignant, val_benign, val_malignant]:
    os.makedirs(p, exist_ok=True)

def collect_and_split(src, train_dst, val_dst):
    all_imgs = []
    for root, dirs, files in os.walk(src):
        if root.endswith("40X") or root.endswith("100X"):
            for f in files:
                if f.lower().endswith((".png",".jpg",".jpeg",".tif")):
                    all_imgs.append(os.path.join(root,f))
    random.shuffle(all_imgs)
    split = int(0.8 * len(all_imgs))
    for img in all_imgs[:split]:
        shutil.copy(img, train_dst)
    for img in all_imgs[split:]:
        shutil.copy(img, val_dst)

collect_and_split(benign_source, train_benign, val_benign)
collect_and_split(malignant_source, train_malignant, val_malignant)

print("✅ Images copiées dans la structure train/val !")