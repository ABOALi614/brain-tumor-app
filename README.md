---
title: Brain Tumor MRI Classifier
emoji: 🧠
colorFrom: purple
colorTo: blue
sdk: streamlit
sdk_version: 1.44.1
python_version: "3.11"
app_file: app.py
pinned: false
---

# 🧠 كاشف أورام المخ بالذكاء الاصطناعي | AI Brain Tumor Classifier

موقع يستقبل صورة أشعة رنين مغناطيسي (MRI) للمخ، ويصنّفها إلى: **Glioma / Meningioma / Pituitary / No Tumor**، ويعرض معلومات مبسطة عن الحالة (بالعربي والإنجليزي).

> ⚠️ مشروع تعليمي فقط، النتيجة ليست تشخيصًا طبيًا.

---

## 📁 محتويات المشروع

| الملف | وظيفته |
|---|---|
| `app.py` | الموقع نفسه (Streamlit) |
| `config.py` | **اسمك وروابطك** (عدّلها من هنا) |
| `translations.py` | كل نصوص الموقع عربي/إنجليزي |
| `disease_info.py` | معلومات الأمراض المبسطة |
| `model_utils.py` | تحميل الموديل وتحليل الصورة |
| `training/train_model_colab.ipynb` | نوتبوك تدريب الموديل (يتشغّل على Google Colab) |
| `model/` | هنا بتحط ملف الموديل بعد التدريب |
| `requirements.txt` | المكتبات المطلوبة |

---

## 🚀 الخطوات (من الصفر)

### الخطوة 1: تدريب الموديل على Google Colab (مجاني)

1. ادخل على https://colab.research.google.com بحساب Google.
2. من **File ← Upload notebook** ارفع الملف `training/train_model_colab.ipynb`.
3. من **Runtime ← Change runtime type** اختار **T4 GPU** ثم **Save**.
4. من **Runtime ← Run all**. الخلية التالتة ممكن تطلب تسجيل دخول Kaggle:
   - اعمل حساب مجاني على https://www.kaggle.com
   - من **Settings ← API ← Create New Token** (أو انسخ الـ username و key) وحطهم في المربع اللي بيظهر.
5. استنى 15–30 دقيقة. في الآخر هينزل لك ملف `brain_tumor_results.zip` تلقائيًا (لو المتصفح منعه، اسمح بالتنزيل).
6. فك الضغط. هتلاقي:
   - `brain_tumor_model.keras` و `class_names.json` ← **انسخهم داخل فولدر `model/`** في المشروع.
   - `results.json` و `confusion_matrix.png` و `training_curves.png` ← للتقرير (فيهم دقة الموديل).

### الخطوة 2 (اختيارية): تجربة الموقع على جهازك

```bash
pip install -r requirements.txt
streamlit run app.py
```
(محتاج Python 3.10 أو 3.11 أو 3.12)

### الخطوة 3: الرفع على Hugging Face Spaces (مجاني بالكامل)

1. اعمل حساب مجاني على https://huggingface.co
2. اضغط **New ← Space**.
3. اكتب اسم للموقع، واختار **SDK: Streamlit**، و **Hardware: CPU basic (Free)**، و **Public** ← **Create Space**.
4. ادخل على تبويب **Files** ← **Add file ← Upload files**.
5. اسحب **كل محتويات** فولدر المشروع (بما فيها فولدر `model` وفيه الموديل، وملف `README.md` و `.streamlit`) وارفعها ← **Commit changes**.
   - ملف الموديل أكبر من 10MB: الموقع بيرفعه تلقائيًا بنظام LFS، متقلقش.
6. استنى كام دقيقة لحد ما الحالة تبقى **Running**، وبعدها الموقع يشتغل على رابط زي:
   `https://huggingface.co/spaces/اسم-حسابك/اسم-الموقع`

> الاستضافة المجانية بتنام لو محدش استخدم الموقع فترة، وبتصحى لما حد يفتحه (بياخد دقيقة).

---

## ✏️ تعديل الاسم والروابط
افتح `config.py` وعدّل `AUTHOR_NAME_AR` و `AUTHOR_NAME_EN` و `LINKS`.

## 🛠️ مشاكل شائعة

| المشكلة | الحل |
|---|---|
| الموقع بيقول "ملف الموديل غير موجود" | تأكد إن `brain_tumor_model.keras` و `class_names.json` جوه فولدر `model` |
| خطأ أثناء تحميل الموديل بعد الرفع | غالبًا اختلاف إصدار TensorFlow. افتح `results.json` وشوف `tensorflow_version`، وفي `requirements.txt` غيّر السطر لـ `tensorflow-cpu==<نفس الإصدار>` |
| رفع الصورة بيفشل على Hugging Face | تأكد إن `.streamlit/config.toml` اترفع |
| Colab وقف قبل ما يخلص | اعمل Run all تاني (ممكن تقلل `epochs` في خلايا التدريب) |
| نسبة الثقة قليلة | طبيعي لو الصورة مش MRI للمخ أو مش واضحة |

## ⚠️ حدود المشروع
نسخة أولية (MVP) بـ 4 تصنيفات. الموديل ما بيتأكدش إن الصورة أشعة مخ أصلًا. مش بديل عن الطبيب.

---
**تم بواسطة | Built by:** أحمد عبدالجيد (Ahmed Abd-Algayed)
