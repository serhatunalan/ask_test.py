# -*- coding: utf-8 -*-
"""
Created on Sat May 10 20:47:12 2025

@author: SERHAT
"""

import streamlit as st

st.set_page_config(page_title="Aşk & Hayat Tarzı Testi", page_icon="💘")
st.title("💘 Aşk & Hayat Tarzı Testi")

st.write("""
Bu test, aşk anlayışını, sevgi tarzını ve hayata bakış açını ölçer.
10 soruda seni en iyi tanımlayan kişiliği bul!
""")

questions = [
    ("Aşka bakış açın nedir?", 
     ["Aşk her şeydir", "Aşk güzeldir ama tek başına yetmez", "Önce kariyer, sonra aşk", "Aşksız da olur"]),
    
    ("Partnerinde ne ararsın?", 
     ["Romantizm ve ilgi", "Denge ve anlayış", "Stabil yaşam ve vizyon", "Kısıtlamayan biri"]),
    
    ("Bir ilişkide en korktuğun şey nedir?", 
     ["Sevilmemek", "Anlaşamamak", "Maddi sorunlar", "Özgürlüğümü kaybetmek"]),
    
    ("Bir gün piyango kazansan ilk ne yaparsın?", 
     ["Partnerime sürpriz bir tatil", "Ev alırım", "Yatırıma yönelirim", "Tek başıma dünyayı gezerim"]),
    
    ("Sana göre ideal buluşma:", 
     ["Mum ışığında akşam yemeği", "Sakin bir yürüyüş ve sohbet", "Birlikte plan/proje yapmak", "Sürpriz bir kaçamak"]),
    
    ("Partnerinin maaşı senden düşük, ne hissedersin?", 
     ["Hiç sorun değil, aşk yeter", "Zamanla toparlarız", "Zorlanırım", "Kimseye bağımlı olmam"]),
    
    ("Yalnız kalmak senin için:", 
     ["Korkutucu", "Bazen iyi gelir", "Gerekli bir mola", "Özgürlük!"]),
    
    ("Hayat planların arasında hangisi var?", 
     ["Mutlu bir evlilik", "Kariyer & aile dengesi", "Başarılı bir iş hayatı", "Dünyayı keşfetmek"]),
    
    ("Partnerin seni çok seviyor ama ekonomik olarak yetersiz, ne yaparsın?", 
     ["Sevgi yeter, destek olurum", "Beraber çözüm buluruz", "Zamanla yıpranırım", "İlişkiyi gözden geçiririm"]),
    
    ("Aşağıdakilerden hangisi sana daha yakın?", 
     ["Duygusallık", "Empati", "Gerçekçilik", "Bağımsızlık"])
]

# Puan tablosu
scores = {'A': 0, 'B': 0, 'C': 0, 'D': 0}
options_map = ['A', 'B', 'C', 'D']

# Soruları döngüyle göster
for i, (q, opts) in enumerate(questions):
    answer = st.radio(f"{i+1}. {q}", opts, key=f"q{i}")
    if answer:
        index = opts.index(answer)
        scores[options_map[index]] += 1

# Sonuç butonu
if st.button("🔍 Sonucumu Göster"):
    result = max(scores, key=scores.get)
    
    profiles = {
        'A': {
            "title": "💓 Tutkulu Romantik",
            "desc": "Aşk senin için hayatın merkezinde. Sevgiyle bağlanır, kalpten seversin. Partnerin için elinden geleni yaparsın."
        },
        'B': {
            "title": "⚖️ Dengeli Aşık",
            "desc": "Sen hem kalbinle hem aklınla seversin. Aşk senin için önemli ama ayakların yere sağlam basar."
        },
        'C': {
            "title": "💼 Pratik Hayatçı",
            "desc": "Gerçekçi ve planlısın. Aşk önemli ama maddi güvenlik ve düzen olmazsa olmazın."
        },
        'D': {
            "title": "🕊️ Bağımsız Ruh",
            "desc": "Sen özgürlüğüne düşkünsün. Aşk senin için bir seçenek ama tek seçenek değil."
        }
    }

    st.subheader(profiles[result]["title"])
    st.write(profiles[result]["desc"])

    st.markdown("---")
    st.markdown("🔗 Bu sonucu arkadaşlarınla paylaş!")
    st.code("https://seninkisisayfan.com/test?sonuc=" + result)
