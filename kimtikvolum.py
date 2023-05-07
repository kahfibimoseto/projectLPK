import streamlit as st

st.title(':green[KIMIA ANALITIK : VOLUMETRI]')
st.markdown("Ini adalah Aplikasi Percepatan Perhitungan Untuk Analis Kimia")
st.write('''Aplikasi ini dibuat oleh Kelompok X dari kelas IB Analis Kimia beranggotakan
1. Ika Septiana (2219083)
2. Kahfi Akmal J.B.S (2219089)
3. Nabila Azzahra K. (2219120)
4. Retno Dwi A. (2219120)
''')

tab1, tab2, tab3, tab4, tab5, tab6, tab7 = st.tabs(['Halaman Utama', 'Molaritas', 'Normalitas', 'ppm', 'Persen Berat', 'Persen Volume', 'Informasi Titrasi'])

with tab1:
    st.header("Selamat Datang")
    st.markdown("Gunakan tabel berat molekul dibawah ini untuk bahan yang anda gunakan")
    st.image('tabelBM.PNG')
    st.caption('_gunakan literatur bila data yang anda butuhkan tidak ada di tabel_')
     
with tab2:
    st.header("Molaritas")
    st.markdown("DATA BAHAN")
    namabahan=st.text_input("Nama Bahan Molaritas")
    jmlbahan=st.number_input("Jumlah Bahan(g) Molaritas")
    bmmolar=st.number_input("Masukkan BM/Ar Bahan")
    volumbahan=st.number_input("Volume Larutan(mL) Molaritas")
    if st.button('Molaritas'):
        molaritas=((jmlbahan)/(bmmolar))/(volumbahan)
        st.info(f'Molaritas dari {namabahan}: {molaritas}')
    
with tab3:
    st.header("Normalitas")
    st.markdown("DATA BAHAN")
    namabahan=st.text_input("Nama Bahan Normalitas")
    jmlbahan=st.number_input("Jumlah Bahan(g) Normalitas")
    benormal=st.number_input("Masukkan BE Bahan")
    volumbahan=st.number_input("Volume Larutan(mL) Normalitas")
    if st.button('Normalitas'):
        normalitas=((jmlbahan)/(benormal))/(volumbahan)
        st.info(f'Molaritas dari {namabahan}: {normalitas}')
    
with tab4:
    st.header("ppm")
    st.markdown("DATA BAHAN")
    namabahan=st.text_input("Nama Bahan ppm")
    jmlbahan=st.number_input("Jumlah Bahan(g) ppm")
    vbahan=st.number_input("Volume Larutan(L)")
    if st.button('ppm'):
        ppm=((jmlbahan)*1000)/(vbahan)
        st.info(f'ppm dari {namabahan}: {ppm}')

with tab5:
    st.header("Persen Berat")
    st.markdown("DATA BAHAN")
    namabahan=st.text_input("Nama Bahan Persen Berat")
    beratbahan=st.number_input("Berat Bahan(g)")
    beratlar=st.number_input("Berat Larutan(g)")
    if st.button('Persen Berat'):
        pberat=((beratbahan)/(beratlar)*100)
        st.info(f'Persen Berat dari {namabahan}: {pberat}')

with tab6:
    st.header("Persen Volume")
    st.markdown("DATA BAHAN")
    namabahan=st.text_input("Nama Bahan Persen Volume")
    volumebahan=st.number_input("Volume Bahan(mL)")
    volumebahan=st.number_input("VolumeLarutan(L)")
    if st.button('Persen Volume'):
        pvolume=((volumebahan)/(volumebahan)*100)
        st.info(f'Persen Volume dari {namabahan}: {pvolume}')
        
with tab7:
    import streamlit as st
    
    st.header("TITRASI KONVENSIONAL")
    option=st.selectbox(
            'metode titrasi',
            ('Asam Basa', 'Argentometri', 'Permanganometri', 'Iodometri', 'Kompleksometri'))
#Asam Basa
    if option=='Asam Basa':
        st.header("Asam Basa")
        st.write('''
        :violet[_Informasi Prosedur_]
    
        Sejumlah larutan bahan standar primer dititrasi dengan larutan standar baku sekunder dengan indikator hingga TA. Pada saat TA, TE kedua bahan sama dan konsentrasi bahan dapat dihitung.
        
        Baku Primer : Asam Oksalat atau Boraks
        
        Baku Sekunder : HCl atau NaOH
        
        Indikator : Metil Merah untuk HCl, Phenolpthalein untuk NaOH
        ''')
        st.divider()
    
        st.write('''
        :violet[_Informasi Penggunaan Bahan Primer_]
        ''')
        namaprimerab=st.text_input("Bahan Standar Baku Primer Asam Basa")
        massaprimerab=st.number_input("Massa Standar Baku Primer(g)")
        bmbeprimerab=st.number_input("BM(untuk molaritas)/BE(untuk normalitas) Standar Baku Primer")
        volumeprimerab=st.number_input("Volume Labu Takar(L)")
        cprimerab=((massaprimerab)/(bmbeprimerab))/(volumeprimerab)
        if st.button('Konsentrasi Standar Primer'):
            cprimerab=((massaprimerab)/(bmbeprimerab))/(volumeprimerab)
            st.info(f'Konsentrasi dari {namaprimerab}: {cprimerab}')
        st.divider()
    
        st.write('''
        :violet[_Informasi Titrasi_]
        ''')
        volumetitranab=st.number_input("Volume Titran(mL)")
        volumepipetab=st.number_input("Volume Standar Yang Dipipet(mL)")
        f'konsentrasi larutan baku primer {namaprimerab} : {cprimerab}'
        if st.button('hasil titrasi'):
            csampelab=(cprimerab*volumepipetab)/(volumetitranab)
            st.info(f'Kadar Hasil Titrasi : {csampelab}')
#Iodometri    
    elif option=='Iodometri':
            st.header("Iodometri")
            st.write('''
            :violet[_Informasi Prosedur_]
    
        Sejumlah larutan sampel/larutan bahan standar primer ditambahkan iod dalam KI dan pengasam kemudian langsung dititrasi dengan larutan natrium tiosulfat jelang TA (kekuningan) ditambahkan kanji kemudian titrasi dilanjut hingga TA berwarna hijau terang. Pada saat TA, TE kedua bahan sama dan konsentrasi bahan dapat dihitung.
        
        Baku Primer : kalium dikromat
        
        Baku Sekunder : natrium tiosulfat
        
        Indikator : amylum/kanji
        ''')
            st.divider()
    
            st.write(':violet[_Informasi Penggunaan Bahan Primer_]')
            namaprimerio=st.text_input("Bahan Standar Baku Primer Iodometri")
            massaprimerio=st.number_input("Massa Standar Baku Primer(g) Iodometri")
            bmbeprimerio=st.number_input("BM(untuk molaritas)/BE(untuk normalitas) Standar Baku Primer Iodometri")
            volumeprimerio=st.number_input("Volume Labu Takar(L) Iodometri")
       
            cprimerio=((massaprimerio)/(bmbeprimerio))/(volumeprimerio)
        
            if st.button(f'Konsentrasi Standar Primer {namaprimerio}'):
                    cprimerio=((massaprimerio)/(bmbeprimerio))/(volumeprimerio)
                    st.info(f'Konsentrasi dari {namaprimerio}: {cprimerio}')
            st.divider()
    
            st.write('''
                :violet[_Informasi Titrasi_]
                ''')
            volumetitranio=st.number_input("Volume Titran Iodometri(mL)")
            volumepipetio=st.number_input(f"Volume {namaprimerio} Yang Dipipet(mL)")
            f'konsentrasi larutan baku primer {namaprimerio} : {cprimerio}'
            if st.button('hasil titrasi iodo'):
                csampelio=(cprimerio*volumepipetio)/(volumetitranio)
                st.info(f'Kadar Hasil Titrasi : {csampelio}')
#Permanganometri                
    elif option=='Permanganometri':
            st.header("Permanganometri")
            st.write('''
            :violet[_Informasi Prosedur_]
        
            Sejumlah larutan sampel/larutan bahan standar primer ditambahkan pengasam dan dipanaskan hingga 70 derajat celcius kemudian dititrasi dengan larutan kalium permanganat kemudian dititrasi hingga TA berwarna merah muda seulas. Pada saat TA, TE kedua bahan sama dan konsentrasi bahan dapat dihitung.
            
            Baku Primer : asam oksalat
            
            Baku Sekunder : kalium permanganat
            
            Indikator : autoindikator
            ''')
            st.divider()
            
            st.write('''
            :violet[_Informasi Penggunaan Bahan Primer_]
            ''')
            namaprimermn=st.text_input("Bahan Standar Baku Primer Permanganometri")
            massaprimermn=st.number_input("Massa Standar Baku Primer Permanganometri(g)")
            bmbeprimermn=st.number_input("BM(untuk molaritas)/BE(untuk normalitas) Standar Baku Primer Permanganometri")
            volumeprimermn=st.number_input("Volume Labu Takar(L) Permanganometri")
            
            cprimermn=((massaprimermn)/(bmbeprimermn))/(volumeprimermn)
        
            if st.button(f'Konsentrasi Standar Primer {namaprimermn}'):
                cprimermn=((massaprimermn)/(bmbeprimermn))/(volumeprimermn)
                st.info(f'Konsentrasi dari {namaprimermn}: {cprimermn}')
            st.divider()
        
            st.write('''
            :violet[_Informasi Titrasi_]
            ''')
            volumetitranmn=st.number_input("Volume Titran(mL)")
            volumepipetmn=st.number_input("Volume Standar Yang Dipipet(mL)")
            f'konsentrasi larutan baku primer {namaprimermn} : {cprimermn}'
            if st.button('hasil titrasi permangano'):
                csampelmn=(cprimermn*volumepipetmn)/(volumetitranmn)
                st.info(f'Kadar Hasil Titrasi : {csampelmn}')
#Argentometri            
    elif option=='Argentometri':
            st.header("Argentometri")
            st.write('''
            :violet[_Informasi Prosedur_]
            Sejumlah larutan standar/sampel dititrasi dengan perak I nitrat dengan indikator tertentu hingga terbentuk endapan putih dan warna TA (merah bata untuk ind. kromat, merah muda seulas untuk ind. flourescence). Saat TA, TE bahan sama sehingga konsentrasi dapat dihitung.
        
            Baku Primer : natrium klorida
        
            Baku Sekunder : perak I nitrat
        
            Indikator : kromat, fluorescence
            ''')
            st.divider()
        
            st.write('''
            :violet[_Informasi Penggunaan Bahan Primer_]
            ''')
            namaprimerag=st.text_input("Bahan Standar Baku Primer Argentometri")
            massaprimerag=st.number_input("Massa Standar Baku Primer(g) Argentometri")
            bmbeprimerag=st.number_input("BM(untuk molaritas)/BE(untuk normalitas) Standar Baku Primer Argentometri")
            volumeprimerag=st.number_input("Volume Labu Takar(L) Argentometri")
        
            cprimerag=((massaprimerag)/(bmbeprimerag))/(volumeprimerag)
        
            if st.button('Konsentrasi Standar Primer'):
                cprimer=((massaprimerag)/(bmbeprimerag))/(volumeprimerag)
                st.info(f'Konsentrasi dari {namaprimerag}: {cprimerag}')
            st.divider()
        
            st.write('''
            :violet[_Informasi Titrasi_]
            ''')
            volumetitranag=st.number_input("Volume Titran(mL)")
            volumepipetag=st.number_input("Volume Standar Yang Dipipet(mL)")
            f'konsentrasi larutan baku primer {namaprimerag} : {cprimerag}'
            if st.button('hasil titrasi'):
                csampelag=(cprimerag*volumepipetag)/(volumetitranag)
                st.info(f'Kadar Hasil Titrasi : {csampelag}')
#Kompleksometri        
    elif option=='Kompleksometri':
            st.header("Kompleksometri")
            st.write('''
            :violet[_Informasi Prosedur_]
            Sejumlah sampel/standar ditambahkan buffer sesuai kondisi dan kebutuhan kemudian diberikan indikator dan dititrasi hingga TA. Pada TA, TE antar bahan sama sehingga konsentrasi dapat dihitung.
        
            Baku Primer : kalsium karbonat
            
            Baku Sekunder : EDTA
        
            Indikator : EBT, Murexide
            ''')
            st.divider()
            
            st.write('''
            :violet[_Informasi Penggunaan Bahan Primer_]
            ''')
            namaprimerko=st.text_input("Bahan Standar Baku Primer Kompleksometri")
            massaprimerko=st.number_input("Massa Standar Baku Primer(g) Kompleksometri")
            bmbeprimerko=st.number_input("BM(untuk molaritas)/BE(untuk normalitas) Standar Baku Primer Kompleksometri")
            volumeprimerko=st.number_input("Volume Labu Takar(L)Kompleksometri")
        
            cprimerko=((massaprimerko)/(bmbeprimerko))/(volumeprimerko)
        
            if st.button('Konsentrasi Standar Primer'):
                cprimerko=((massaprimerko)/(bmbeprimerko))/(volumeprimerko)
                st.info(f'Konsentrasi dari {namaprimerko}: {cprimerko}')
            st.divider()
        
            st.write('''
            :violet[_Informasi Titrasi_]
            ''')
            volumetitranko=st.number_input("Volume Titran(mL)")
            volumepipetko=st.number_input("Volume Standar Yang Dipipet(mL)")
            f'konsentrasi larutan baku primer {namaprimerko} : {cprimerko}'
            if st.button('hasil titrasi'):
                csampelko=(cprimerko*volumepipetko)/(volumetitranko)
                st.info(f'Kadar Hasil Titrasi : {csampelko}')
        
    else:
          print("batal")