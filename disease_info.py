"""معلومات مبسطة عن كل حالة (للأغراض التعليمية فقط)."""

DISEASES = {
    "glioma": {
        "ar": {
            "name": "ورم دبقي (Glioma)",
            "what": "ورم بيبدأ في الخلايا الدبقية، وهي الخلايا اللي بتدعم وتحمي الخلايا العصبية في المخ. ممكن يكون بطيء النمو أو سريعه حسب درجته.",
            "symptoms": ["صداع مستمر أو بيزيد مع الوقت", "نوبات تشنج", "غثيان وقيء", "تغيّر في الذاكرة أو الشخصية", "ضعف في جزء من الجسم أو صعوبة في الكلام", "مشاكل في النظر"],
            "treatment": "العلاج بيعتمد على درجة الورم ومكانه، وممكن يشمل الجراحة والعلاج الإشعاعي والعلاج الكيميائي. الفريق الطبي هو اللي بيحدد الخطة المناسبة.",
        },
        "en": {
            "name": "Glioma",
            "what": "A tumor that starts in glial cells, the cells that support and protect nerve cells in the brain. It can grow slowly or quickly depending on its grade.",
            "symptoms": ["Headaches that persist or get worse", "Seizures", "Nausea and vomiting", "Changes in memory or personality", "Weakness in part of the body or difficulty speaking", "Vision problems"],
            "treatment": "Treatment depends on the grade and location of the tumor and may include surgery, radiotherapy, and chemotherapy. The medical team decides the right plan.",
        },
    },
    "meningioma": {
        "ar": {
            "name": "ورم سحائي (Meningioma)",
            "what": "ورم بيبدأ في السحايا، وهي الأغشية اللي بتغلّف المخ والحبل الشوكي. في الغالب بيكون حميد وبطيء النمو.",
            "symptoms": ["صداع", "ضعف أو تغيّر في النظر", "طنين أو ضعف في السمع", "نوبات تشنج", "فقدان في الذاكرة", "ضعف في الأطراف"],
            "treatment": "ممكن يكتفي الطبيب بالمتابعة الدورية لو الورم صغير وبدون أعراض، أو يتم التدخل بالجراحة أو العلاج الإشعاعي حسب الحالة.",
        },
        "en": {
            "name": "Meningioma",
            "what": "A tumor that starts in the meninges, the membranes that cover the brain and spinal cord. It is most often benign and slow-growing.",
            "symptoms": ["Headaches", "Vision changes or blurring", "Ringing in the ears or hearing loss", "Seizures", "Memory loss", "Weakness in the limbs"],
            "treatment": "If the tumor is small and causes no symptoms, the doctor may only monitor it regularly. Otherwise surgery or radiotherapy may be used, depending on the case.",
        },
    },
    "pituitary": {
        "ar": {
            "name": "ورم الغدة النخامية (Pituitary Tumor)",
            "what": "ورم بيظهر في الغدة النخامية، وهي غدة صغيرة في قاعدة المخ بتتحكم في هرمونات كتير في الجسم. أغلبها أورام حميدة.",
            "symptoms": ["صداع", "ضعف في النظر خصوصًا الرؤية الجانبية", "اضطراب في الهرمونات (إرهاق، تغيّر في الدورة الشهرية، تغيّر في الوزن)", "تغيّر في الشكل أو حجم اليدين والقدمين في بعض الأنواع"],
            "treatment": "حسب نوع الورم: أدوية لتنظيم الهرمونات، أو جراحة (غالبًا من خلال الأنف)، أو علاج إشعاعي.",
        },
        "en": {
            "name": "Pituitary Tumor",
            "what": "A tumor in the pituitary gland, a small gland at the base of the brain that controls many hormones in the body. Most of these tumors are benign.",
            "symptoms": ["Headaches", "Vision problems, especially loss of side vision", "Hormone imbalance (tiredness, menstrual changes, weight changes)", "Changes in the size of hands and feet in some types"],
            "treatment": "Depends on the type: medicines to balance hormones, surgery (often through the nose), or radiotherapy.",
        },
    },
    "notumor": {
        "ar": {
            "name": "لا يوجد ورم (No Tumor)",
            "what": "الموديل ما لقاش علامات ورم من الأنواع التلاتة اللي اتدرب عليها في الصورة دي.",
            "symptoms": [],
            "treatment": "",
            "note": "ده لا يعني بالضرورة إن المخ سليم تمامًا. لو عندك أعراض مستمرة (زي صداع مزمن أو نوبات تشنج أو تغيّر مفاجئ في النظر) اعرض نفسك على الطبيب حتى لو النتيجة سليمة.",
        },
        "en": {
            "name": "No Tumor",
            "what": "The model did not find signs of any of the three tumor types it was trained on in this image.",
            "symptoms": [],
            "treatment": "",
            "note": "This does not necessarily mean the brain is completely healthy. If you have persistent symptoms (such as chronic headaches, seizures, or sudden vision changes), see a doctor even if the result is normal.",
        },
    },
}
