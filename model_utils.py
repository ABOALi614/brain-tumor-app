"""تحميل الموديل والتنبؤ بالصورة."""
import json
from pathlib import Path

import numpy as np
import streamlit as st
from PIL import Image, ImageOps

from config import IMG_SIZE

BASE_DIR = Path(__file__).parent
MODEL_PATH = BASE_DIR / "model" / "brain_tumor_model.keras"
CLASSES_PATH = BASE_DIR / "model" / "class_names.json"


def normalize_name(name: str) -> str:
    """glioma / Glioma Tumor / no_tumor ... -> مفتاح موحد."""
    n = name.lower().replace("_", "").replace(" ", "").replace("-", "")
    if n in ("notumor", "no", "normal", "healthy"):
        return "notumor"
    for key in ("glioma", "meningioma", "pituitary"):
        if key in n:
            return key
    return n


def model_files_exist() -> bool:
    return MODEL_PATH.exists() and CLASSES_PATH.exists()


@st.cache_resource(show_spinner=False)
def load_model_and_classes():
    """يتحمل مرة واحدة بس ويفضل في الذاكرة."""
    from tensorflow import keras  # استيراد متأخر عشان الصفحة تفتح أسرع

    model = keras.models.load_model(MODEL_PATH, compile=False)
    with open(CLASSES_PATH, encoding="utf-8") as f:
        class_names = json.load(f)
    return model, [normalize_name(c) for c in class_names]


def preprocess(image: Image.Image) -> np.ndarray:
    image = ImageOps.exif_transpose(image).convert("RGB").resize(IMG_SIZE)
    arr = np.asarray(image, dtype="float32")  # 0..255 (الموديل بيعمل التحجيم جواه)
    return np.expand_dims(arr, axis=0)


def predict_image(image: Image.Image):
    """يرجع (اسم الصنف الأعلى، ثقته، قاموس بكل الاحتمالات)."""
    model, classes = load_model_and_classes()
    probs = model.predict(preprocess(image), verbose=0)[0]
    probs = {c: float(p) for c, p in zip(classes, probs)}
    top = max(probs, key=probs.get)
    return top, probs[top], probs
