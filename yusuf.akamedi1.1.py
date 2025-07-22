import random

profil = {}
rozet = ""

# 📚 Ders, Konu ve Sorular
soru_bankası = {
    "3. sınıf": {
        "matematik": {
            "toplama": [
                {"soru": "5 + 8?", "cevap": "13"},
                {"soru": "12 + 9?", "cevap": "21"},
                {"soru": "23 + 17?", "cevap": "40"}
            ],
            "çıkarma": [
                {"soru": "15 - 7?", "cevap": "8"},
                {"soru": "30 - 10?", "cevap": "20"},
                {"soru": "50 - 25?", "cevap": "25"}
            ]
        },
        "fen": {
            "canlılar": [
                {"soru": "İnsan bir canlı mıdır?", "cevap": "evet"},
                {"soru": "Ağaç canlı mı?", "cevap": "evet"},
                {"soru": "Kaya canlı mı?", "cevap": "hayır"}
            ]
        }
    },
    "4. sınıf": {
        "matematik": {
            "kesirler": [
                {"soru": "1/2 + 1/4?", "cevap": "3/4"},
                {"soru": "1/3 + 1/3?", "cevap": "2/3"},
                {"soru": "3/4 - 1/4?", "cevap": "1/2"}
            ],
            "uzunluk": [
                {"soru": "1 metre kaç cm?", "cevap": "100"},
                {"soru": "50 cm kaç metredir?", "cevap": "0.5"},
                {"soru": "2.5 m kaç cm?", "cevap": "250"}
            ]
        },
        "fen": {
            "elektrik": [
                {"soru": "Ampul neyle çalışır?", "cevap": "elektrik"},
                {"soru": "Pil ne tür enerji sağlar?", "cevap": "kimyasal"},
                {"soru": "Anahtar açıkken ampul yanar mı?", "cevap": "hayır"}
            ]
        }
    },
    "5. sınıf": {
        "türkçe": {
            "fiiller": [
                {"soru": "\"Koşmak\" hangi tür fiildir?", "cevap": "eylem"},
                {"soru": "Fiil nedir?", "cevap": "iş oluş hareket bildirir"},
                {"soru": "“Okumak” kelimesi nedir?", "cevap": "fiil"}
            ],
            "cümle": [
                {"soru": "Tam cümlede ne bulunur?", "cevap": "özne yüklem"},
                {"soru": "\"Okula gittim.\" cümlesinde özne kim?", "cevap": "ben"},
                {"soru": "“Kitap okuyor.” cümlesinde yüklem nedir?", "cevap": "okuyor"}
            ]
        }
    }
}

print("📘 Test Uygulamasına Hoş Geldin!")
profil["Ad"] = input("👤 Adını gir: ")

# 🔍 Sınıf seçimi
sınıflar = list(soru_bankası.keys())
print("\n📚 Sınıf Seç:")
for i, s in enumerate(sınıflar, 1):
    print(f"{i}. {s}")
sınıf = sınıflar[int(input("Seçimin: ")) - 1]
profil["Sınıf"] = sınıf

# 📖 Ders seçimi
dersler = list(soru_bankası[sınıf].keys())
print("\n📘 Ders Seç:")
for i, d in enumerate(dersler, 1):
    print(f"{i}. {d}")
ders = dersler[int(input("Seçimin: ")) - 1]

# 📌 Konu seçimi
konular = list(soru_bankası[sınıf][ders].keys())
print(f"\n📎 {ders} dersinden konu seç:")
for i, k in enumerate(konular, 1):
    print(f"{i}. {k}")
konu = konular[int(input("Seçimin: ")) - 1]

# ✅ Soru seçimi
sorular = soru_bankası[sınıf][ders][konu]
if len(sorular) < 50:
    sorular *= (50 // len(sorular)) + 1  # kopyalayarak arttır
secilen_sorular = random.sample(sorular, 50)

dogru = 0

print(f"\n🧪 {sınıf} - {ders} - {konu} testine başlıyoruz!")

for i, soru in enumerate(secilen_sorular, 1):
    print(f"\nSoru {i}: {soru['soru']}")
    cevap = input("Cevabın: ").strip().lower()
    if cevap == soru["cevap"].lower():
        print("✅ Doğru!")
        dogru += 1
    else:
        print(f"❌ Yanlış. Doğru cevap: {soru['cevap']}")

# 🎯 Sonuç
yanlis = 50 - dogru
yuzde = round((dogru / 50) * 100)

print(f"\n📝 Test Bitti! Doğru: {dogru}, Yanlış: {yanlis}, Başarı: %{yuzde}")

if dogru >= 45:
    rozet = "🏆 Altın Beyin"
elif dogru >= 30:
    rozet = "🥈 Gümüş Zeka"
elif dogru >= 15:
    rozet = "🥉 Bronz Çaba"
else:
    rozet = "🔍 Deneme Aşaması"

profil["Doğru"] = dogru
profil["Yanlış"] = yanlis
profil["Başarı"] = f"%{yuzde}"
profil["Rozet"] = rozet

# 📋 Profil Özeti
print("\n📊 Profil Bilgilerin:")
for k, v in profil.items():
    print(f"{k}: {v}")

