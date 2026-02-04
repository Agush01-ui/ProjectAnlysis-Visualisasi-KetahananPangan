#!/usr/bin/env python
# coding: utf-8

# In[1]:


import matplotlib.pyplot as plt
import matplotlib.patches as mpatches

# Buat peta skematik sederhana Indonesia
fig, ax = plt.subplots(figsize=(10, 6))

# Titik koordinat kasar representasi pulau
pulau = {
    'Sumatra': (1, 5),
    'Jawa': (2.5, 4),
    'Kalimantan': (4, 6),
    'Sulawesi': (6, 5.5),
    'Maluku': (7.5, 4.5),
    'Papua': (9, 5)
}

# Tampilkan pulau-pulau sebagai titik
for nama, (x, y) in pulau.items():
    ax.plot(x, y, 'o', markersize=10)
    ax.text(x, y+0.3, nama, ha='center', fontsize=10)

# Panah untuk distribusi luar Sulampua ke dalam Sulampua
ax.annotate("", xy=pulau['Sulawesi'], xytext=pulau['Jawa'],
            arrowprops=dict(arrowstyle="->", color='red', lw=2))
ax.annotate("", xy=pulau['Maluku'], xytext=pulau['Jawa'],
            arrowprops=dict(arrowstyle="->", color='red', lw=2))
ax.annotate("", xy=pulau['Papua'], xytext=pulau['Jawa'],
            arrowprops=dict(arrowstyle="->", color='red', lw=2))

# Panah distribusi intra-Sulampua
ax.annotate("", xy=pulau['Maluku'], xytext=pulau['Sulawesi'],
            arrowprops=dict(arrowstyle="->", color='green', lw=2))
ax.annotate("", xy=pulau['Papua'], xytext=pulau['Maluku'],
            arrowprops=dict(arrowstyle="->", color='green', lw=2))
ax.annotate("", xy=pulau['Papua'], xytext=pulau['Sulawesi'],
            arrowprops=dict(arrowstyle="->", color='green', lw=2))

# Keterangan
red_patch = mpatches.Patch(color='red', label='Distribusi dari Luar Sulampua')
green_patch = mpatches.Patch(color='green', label='Distribusi Intra Sulampua')
ax.legend(handles=[red_patch, green_patch], loc='upper left')

# Pengaturan visual
ax.set_xlim(0, 11)
ax.set_ylim(3, 7)
ax.set_xticks([])
ax.set_yticks([])
ax.set_title("Visualisasi Skematik Distribusi Pangan: Intra vs Luar Sulampua", fontsize=12)
ax.set_facecolor('lightblue')
plt.grid(False)
plt.tight_layout()
plt.show()


# In[4]:


import matplotlib.pyplot as plt
import seaborn as sns
import pandas as pd
import numpy as np

# Data dummy
provinces = ['NTT', 'NTB', 'Papua', 'Papua Barat', 'Maluku', 'Maluku Utara', 'Sulsel', 'Sulbar', 'Sulut']
beras_consumption = [101, 97, 3, 5, 4, 2, 4.5, 5.1, 4.7]
non_beras = [60, 80, 95, 90, 92, 96, 93, 91, 92]

df_heatmap = pd.DataFrame({
    'Provinsi': provinces,
    'Konsumsi Beras': beras_consumption
}).set_index('Provinsi')

# Tren konsumsi pangan lokal
years = list(range(2010, 2025))
sagu = np.random.uniform(10, 20, len(years)).round(2)
jagung = np.random.uniform(8, 18, len(years)).round(2)
ubi = np.random.uniform(7, 17, len(years)).round(2)

# Radar chart
labels = ['Ketersediaan', 'Akses', 'Pemanfaatan', 'Stabilitas', 'Kelembagaan']
NTT_scores = [3, 4, 3.5, 3, 2.5]
Papua_scores = [2, 2.5, 3, 2, 2]
Maluku_scores = [3, 3.5, 4, 3.5, 3]

# Pie chart
labels_pie = ['Pangan Lokal', 'Pangan dari Luar Sulampua']
sizes_pie = [35, 65]

# Buat subplot
fig, axs = plt.subplots(3, 2, figsize=(14, 12))
plt.subplots_adjust(hspace=0.5)

# 1. Heatmap Konsumsi Beras
sns.heatmap(df_heatmap, cmap='Reds', annot=True, fmt=".1f", ax=axs[0, 0])
axs[0, 0].set_title('Heatmap Konsumsi Beras per Kapita (kg/tahun)')

# 2. Tren Konsumsi Pangan Alternatif
axs[0, 1].plot(years, sagu, label='Sagu', marker='o')
axs[0, 1].plot(years, jagung, label='Jagung', marker='o')
axs[0, 1].plot(years, ubi, label='Ubi', marker='o')
axs[0, 1].set_title('Tren Konsumsi Pangan Lokal Alternatif (2010–2024)')
axs[0, 1].legend()
axs[0, 1].set_xlabel('Tahun')
axs[0, 1].set_ylabel('kg/kapita')

# 3. Radar Chart
def make_radar_chart(ax, values, label, color):
    angles = np.linspace(0, 2 * np.pi, len(labels), endpoint=False).tolist()
    values += values[:1]
    angles += angles[:1]
    ax.plot(angles, values, label=label, color=color)
    ax.fill(angles, values, alpha=0.25, color=color)
    ax.set_xticks(angles[:-1])
    ax.set_xticklabels(labels)
    ax.set_yticklabels([])
    ax.set_title("Radar Ketahanan Pangan Daerah")

radar_ax = fig.add_subplot(3, 2, 3, polar=True)
make_radar_chart(radar_ax, NTT_scores.copy(), 'NTT', 'blue')
make_radar_chart(radar_ax, Papua_scores.copy(), 'Papua', 'green')
make_radar_chart(radar_ax, Maluku_scores.copy(), 'Maluku', 'orange')
radar_ax.legend(loc='upper right', bbox_to_anchor=(1.3, 1.1))

# 4. Pie Chart
axs[1, 1].pie(sizes_pie, labels=labels_pie, autopct='%1.1f%%', startangle=140, colors=['green', 'red'])
axs[1, 1].axis('equal')
axs[1, 1].set_title('Kontribusi Pangan Lokal vs Luar Sulampua')

# 5. Placeholder Rantai Pasok
axs[2, 0].axis('off')
axs[2, 0].text(0.5, 0.5, 'Diagram Alir Rantai Pasok\n(digambar manual atau pakai Graphviz)', 
              ha='center', va='center', fontsize=12, bbox=dict(boxstyle="round,pad=1", edgecolor='black', facecolor='lightgray'))

# Kosongkan slot terakhir
axs[2, 1].axis('off')

# Judul besar
plt.suptitle("Visualisasi Strategis Ketahanan Pangan Indonesia Timur", fontsize=16)
plt.show()


# In[ ]:





# In[ ]:




