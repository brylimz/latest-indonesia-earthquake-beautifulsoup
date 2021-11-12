import requests
from bs4 import BeautifulSoup

#testing connection
def ekstraksi_data():
    """
    Tanggal: 03 November 2021
    Waktu: 09:04:20 WIB
    Magnitudo: 2.7
    Kedalaman: 10 km
    Lokasi: LS= 3.72 BT= 128.10
    Pusat Gempa: Pusat gempa berada di laut 9 km Barat Ambon, SBB
    Dirasakan: (Skala MMI): II Ambon
    :return:
    """
    try:
        content = requests.get('https://bmkg.go.id')
    except Exception:
        return None
    if content.status_code == 200:
        soup = BeautifulSoup(content.text,'html.parser')

        result = soup.find('span', {'class': 'waktu'})
        result = result.text.split(', ')
        tanggal = result[0]
        waktu = result[1]

        result = soup.find('div', {'class': 'col-md-6 col-xs-6 gempabumi-detail no-padding'})
        result = result.findChildren('li')
        i = 0
        magnitudo = None
        ls = None
        bt = None
        pusat = None
        dirasakan = None
        kedalaman = None
        lokasi = None

        for res in result:
            print(i, res)
            if i == 1:
                magnitudo = res.text
            elif i == 2:
                kedalaman = res.text
            elif i == 3:
                koordinat = res.text.split(' - ')
                ls = koordinat[0]
                bt = koordinat[1]
            elif i == 4:
                lokasi = res.text
            elif i == 5:
                dirasakan = res.text
            i = i + 1


        hasil = dict()
        hasil['tanggal'] = tanggal #'03 November 2021'
        hasil['waktu'] = waktu
        hasil['magnitudo'] = magnitudo
        hasil['kedalaman'] = kedalaman
        hasil['koordinat'] = {'ls': koordinat[0], 'bt': koordinat[1]}
        hasil['lokasi'] = lokasi
        hasil['pusat gempa'] = "Pusat gempa berada di laut 9 km Barat Ambon, SBB"
        hasil['dirasakan'] = dirasakan
        return hasil
    else:
        return None


def tampilkan_data(result):
    if result is None:
        return
        print ("tidak bisa menemukan data terkini")
    print('Gempa terakhir berdasarkan BMKG')
    print(f"Tanggal {result['tanggal']}")
    print(f"Waktu {result['waktu']}")
    print(f"Magnitudo {result['magnitudo']}")
    print(f"kedalaman {result['kedalaman']}")
    print(f"lokasi {result['lokasi']}")
    print(f"koordinat ls = {result['koordinat']['ls']},bt = {result['koordinat']['bt']}")
    print(f"pusat gempa {result['pusat gempa']}")
    print(f"dirasakan {result['dirasakan']}")
    pass