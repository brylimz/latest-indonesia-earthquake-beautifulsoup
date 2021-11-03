import bs4


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
    soup = bs4.BeautifulSoup("<p>Some<b>bad<i>HTML")
    print(soup.prettify())



    hasil = dict()
    hasil['tanggal'] = '03 November 2021'
    hasil['waktu'] = '09:04:20'
    hasil['magnitudo'] = 2.7
    hasil['kedalaman'] = "10 Km"
    hasil['lokasi'] = {'ls': 3.72, 'bt': 128.10}
    hasil['pusat gempa'] = "Pusat gempa berada di laut 9 km Barat Ambon, SBB"
    hasil['dirasakan'] = "(Skala MMI: II Ambon)"

    return hasil


def tampilkan_data(result):
    print('Gempa terakhir berdasarkan BMKG')
    print(f"Tanggal {result['tanggal']}")
    print(f"Magnitudo {result['magnitudo']}")
    print(f"kedalaman {result['kedalaman']}")
    print(f"lokasi ls={result['lokasi']['ls']},bt={result['lokasi']['bt']}")
    print(f"pusat gempa {result['pusat gempa']}")
    print(f"dirasakan {result['dirasakan']}")
    pass