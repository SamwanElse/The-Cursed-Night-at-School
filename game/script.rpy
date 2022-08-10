# Kamu dapat taruh script game mu di file ini.

# Deklarasikan gambar di bawah line ini, menggunakan pernyataan image.
# cnth. image eileen happy = "eileen_happy.png"

#transform
transform long_shake:
    ease .06 yoffset 24
    ease .06 yoffset -24
    ease .05 yoffset 20
    ease .05 yoffset -20
    ease .04 yoffset 16
    ease .04 yoffset -16
    ease .03 yoffset 12
    ease .03 yoffset -12
    ease .02 yoffset 8
    ease .02 yoffset -8
    ease .01 yoffset 4
    ease .01 yoffset -4
    ease .01 yoffset 0

transform short_shake:
    ease .03 yoffset 12
    ease .03 yoffset -12
    ease .02 yoffset 8
    ease .02 yoffset -8
    ease .01 yoffset 4
    ease .01 yoffset -4
    ease .01 yoffset 0

#allbg
image bg club = "images/bg club.png"
image bg blck = "images/bg black.png"
image bg its = "images/scene.jpg"
image bg outs = "images/outschool.jpg"
image bg insc = "images/corridor.jpg"
image bg incl = "images/inclass.jpg"
image bg prps = "images/perpus.png"
image bg cntn = "images/canteen.jpg"
#-----------

#image chara
#zaky
image zaky = "images/zaky/Zaky.png"
#kevin
image kevincheerful = "images/kevin/KevinCheerful.png"
image kevinhappy = "images/kevin/KevinHappy.png"
image kevinserious = "images/kevin/KevinSerious.png"
image kevinsmile = "images/kevin/KevinSmile.png"
image kevintalk = "images/kevin/KevinTalk.png"
#yeri
image yeriangry1 = "images/yeri/YeriAngry.png"
image yeriangry2 = "images/yeri/YeriAngry2.png"
image yericheerful = "images/yeri/YeriCheerful.png"
image yerihappy = "images/yeri/YeriHappy.png"
image yerinormal = "images/yeri/YeriNormal.png"
image yerisad = "images/yeri/YeriSad.png"
image yeriscared = "images/yeri/YeriScared.png"
image yerishy = "images/yeri/YeriShy.png"
image yerismile = "images/yeri/YeriSmile.png"
image yerisurprised = "images/yeri/YeriSurprised.png"
image yeritalk = "images/yeri/YeriTalk.png"
image yeritsundere1 = "images/yeri/YeriTsundere1.png"
image yeritsundere2 = "images/yeri/YeriTsundere2.png"
#citra
image citra = "images/citra/Citra.png"

# Deklarasikan karakter yang digunakan di game.
# All chara
#YERI
define y = Character('Yeri')
define y_shout = Character("Yeri", what_size=50)
define y_whisper = Character("Yeri", what_size=18)
#ZAKY
define z = Character('Zaky')
define z_shout = Character("Zaky", what_size=50)
define z_whisper = Character("Zaky", what_size=18)
#KEVIN
define k = Character('Kevin')
define k_shout = Character("Kevin", what_size=50)
define k_whisper = Character("Kevin", what_size=18)
#CITRA
define c = Character('Citra')
define c_shout = Character("Citra", what_size=50)
define c_whisper = Character("Citra", what_size=18)
#MC
define u = Character('???')
define p = Character('[name]')
define c_shout = Character("[name]", what_size=50)
define c_whisper = Character("[name]", what_size=18)
#Mix
define kyc = Character("Kevin, Yeri, dan [name]")


 
# Game dimulai disini.

 
label start:

    scene bg black
    with dissolve

    #field name
    python:
        name = renpy.input("Siapa namamu: ")

        name = name.strip() or "You"

    scene bg its
    with dissolve

    stop music fadeout 1.0

    "Pagi hari ini terasa sangat cerah tidak seperti biasa."
    "Dengan semangat pagi yang membara aku pergi menuju sekolahku."
    "Dari kejauhan aku melihat Kevin sedang berjalan dipinggir jalan."

    show kevinserious with dissolve

    u 'Hello Kevin. Bagaimana kabarmu?'

    hide kevinserious
    show kevincheerful at short_shake, center

    k 'Hai [name], baik kok! bagaimana denganmu?'
    p 'Baik seperti biasa kok ahahahaha...'
    k 'Kamu mau menuju sekolah?'
    p 'Iyalah! Aku sudah memakai pakaian kek gini.'
    p 'Masak ga pergi sekolah.'

    show kevinhappy at short_shake,center

    k 'Ahahaha... Maaf aku cuma bercanda tadi.'

    hide kevin 
    scene bg outs with dissolve

    "Kami berdua berjalan menuju sekolah."
    "Sesampainya disekolah, Kevin mengingatkanku tentang rapat OSIS sehabis pulang sekolah nanti."

    show kevintalk with dissolve

    k 'Eh... Jangan lupa nanti ya! Sehabis pulang sekolah buat rapat untuk acara Ulang Tahun sekolah kita.'
    p 'Okay... Pasti aku datang kok.'
    p 'Aku kan anak rajin.'

    hide kevintalk
    show kevinhappy at short_shake, center

    k 'Heleh ahahahaha.'

    hide kevin
    scene bg insc with dissolve

    "Aku menuju ke ruang kelasku."
    "Saat di pertengahan perjalanan aku bertemu Yeri lalu menyapanya."

    show yerinormal with dissolve

    p 'Hai Yeri. Bagaimana kabarmu?'
 
    hide yerinormal
    show yerihappy at short_shake, center

    y 'Hai [name], baik kok. Bagaimana denganmu?'
    p 'Baik kok. Aku ke kelas duluan dulu ya!'
    y 'Okei!'

    hide yeri with dissolve
    #-------
    #bedascene
    scene bg incl with dissolve

    "Sesampainya dikelas, aku langsung menuju ke tempat dudukku."
    "Saat aku sedang melamun. Tiba-tiba Zaky datang untuk menyapaku."
    
    show zaky with dissolve

    z 'Woi [name]. Kamu kenapa melamun saja? Apa ada masalah dengan dirimu?'
    p 'Tidak kok. Aku cuma bersantai aja.'
    z 'Hadeh... Jangan lupa untuk ikut rapat nanti sepulang sekolah ya! Ingat.'
    p 'Iya... Santai aja. Aku inget kok.'

    hide zaky with dissolve

    "Setelah kejadian itu guru pun masuk kedalam ruangan untuk memulai pelajaran di pagi yang cerah ini."

    scene bg insc with dissolve

    "Bel istirahat pun berbunyi."
    "Lalu beberapa saat kemudian Zaky, Yeri, dan Kevin menghampiriku didepan kelasku."

    show kevinsmile with dissolve:
            xalign 0.0
            yalign 1.0

    show zaky with dissolve:
            xalign 0.9
            yalign 1.0

    show yerismile with dissolve

    z 'Hei [name], yuk ke kantin. Mau ga?' 
    y 'Iya nih... mau ga?'
    
    p 'Boleh saja sih... Tapi...'

    hide kevinsmile
    show kevintalk at short_shake:
        xalign 0.0
        yalign 1.0

    k 'Ga usah pake tapi-tapian. Ayo gas berangkat.'

    hide kevintalk
    show kevinserious:
        xalign 0.0
        yalign 1.0

    p 'Tapi aku tu males banget coy...'

    hide yerismile
    show yericheerful at short_shake, center
    
    y 'Sudahlah ikut saja...'

    hide yericheerful
    show yerihappy at center

    menu:
        "Aku akan ikut.":
            jump kantin_yes

        "Aku tidak ingin ikut.":
            jump kantin_no

#--------------------
#KE KANTIN(setuju)
#-------------------
    label kantin_yes:

        $ menu_flag = True

        p 'Iya deh aku ikut. Yuk ke kantin.'
        
        hide kevinserious
        show kevincheerful at short_shake:
            xalign 0.0
            yalign 1.0

        k 'Nah gitu donk... Lama bet mikirnya dah ni anak.' 

        hide yerihappy
        show yericheerful at short_shake, center

        y "Hahaha"
        y 'Yaudah yokkk berangkat!' 

        # 3 chara hilang bersamaan
        hide kevincheerful
        hide yericheerful
        hide zaky 
        with dissolve

        "Kami berempat pergi menuju kantin bersama."
        "Dalam perjalanan menuju kantin, mereka bertiga membicarakan tentang rapat OSIS yang akan diadakan sore ini."
        "Aku terdiam sejenak, dan berpikir." 
        "Sejujurnya..." 
        menu:

            "Aku sangat antusias dengan rapat nanti.":
                jump choice2_yes
        
       
            "Aku kurang tertarik dengan rapat kali ini.":
                jump choice2_no

                label choice2_yes:

                $ menu_flag = True

                p "Aku sangat-" 

                
                jump choice2_done

                label choice2_no:

                $ menu_flag = False

                p "Aku kurang-" 
                jump choice2_done

                label choice2_done:
                
        "Tiba-tiba Kevin memanggilku dengan keras dan itu membuatku terkejut." 
        "Ternyata aku tertinggal jauh dari mereka. Lalu, aku menyusul mereka dengan cepat." 

        scene bg cntn with dissolve

        "Kami berempat telah tiba dikantin."
        "Kevin dan Zaky lalu menuju tempat makanan, sedangkan aku dan Yeri mencari tempat duduk." 
        "Kami berdua berhasil mendapatkan tempat duduk." 
        "Lalu kami mendudukinya untuk menunggu Kevin dan Zaky." 
        

        show yerinormal with dissolve
        y 'Kamu tadi mengapa melamun?' 
        y 'Apa yang sedang kamu pikirkan?' 
        p 'Ga ada apa-apa sih.' 
        y 'Ah boong kamu.'
        p 'Beneran kok.'

        #hide yerinormal
        #show yerikesal
        "Yeri menatapku dengan tatapan serius dicampur kesal."
        "Akhirnya aku pun menyerah dan memberitahunya apa alasanku melamun tadi."

        p 'Sebenernya tadi aku merasa.'

        menu:
            "Sangat antusias dengan rapat nanti.":
                jump choice4_done
            "Kurang tertarik dengan rapat nanti.":
                jump choice4_done
                

                label choice4_done:
        #hideyerikesal
        hide yerinormal#hilangkan!
        show yerismile
        y 'Ya ampun kukira kamu mikirin apaan.' 
        y 'Ternyata mikirin hal kayak gitu aja.' 
        p 'Ahahaha... Maaf ya...' 
        hide yerismile
        show yericheerful at short_shake, center
        y 'Ga apa-apa.' 
        y 'Kamu harus ikut rapat itu walaupun suka atau engga.'
        hide yericheerful
        show yerismile
        y 'Karena rapat itu untuk membahas perayaan ulang tahun sekolah kita.' 
        p 'Iya aku tau kok.' 

        hide yerismile with dissolve
         
        "Tak lama kemudian Kevin datang ke tempat dudukku dengan Citra." 

        show kevincheerful with dissolve

        k 'Kalian lagi membahas apa nih?' 

        show kevincheerful with move:
            xalign 0.3
            yalign 1.0 
        show yericheerful at right with dissolve:
            xalign 0.8
            yalign 1.0

        y "Ga ada apa-apa sih."
        p "Iya, ga ada apa-apa."
        k "Yang bener?"
        
        hide yericheerful
        show yeriangry2 at short_shake, right:
            xalign 0.8
            yalign 1.0

        y "Ga ada Kevin..."

        hide kevincheerful
        show kevinhappy at short_shake:
            xalign 0.3
            yalign 1.0


        k "Iya deh iya."
        hide yeriangry2
        hide kevinhappy
        with dissolve

        "Kevin mulai duduk di kursi meja kantin yang aku duduki."
        "Saat Kevin telah duduk."
        "Datanglah Citra dan Zaky."

        show citra with dissolve:
            xalign 0.3
            yalign 1.0 
        show zaky at right with dissolve:
            xalign 0.8
            yalign 1.0
        
        c "Hai semua..."

        hide citra
        hide zaky 
        with dissolve

        show kevinsmile with dissolve:
            xalign 0.3
            yalign 1.0 
        show yerismile at right with dissolve:
            xalign 0.8
            yalign 1.0

        kyc "Hai Citra..."
        hide kevinsmile
        hide yerismile
        with dissolve

        show citra with dissolve
        c "Halo..."

        hide citra with dissolve
        show yerismile
        y "Bagaimana kabarmu Cit?"
        show yerismile with move:
            xalign 0.3
            yalign 1.0 
        show citra at right with dissolve:
            xalign 0.8
            yalign 1.0

        c "Baik kok!"
        hide yerismile
        show yericheerful:
            xalign 0.3
            yalign 1.0 
        y "Sini kalian berdua ikut duduk!"
        c "Okeiiii!"

        hide yericheerful
        hide citra
        with dissolve

        "Citra dan Zaky mulai duduk di kursi meja kantin yang kutempati."
        "Saat mereka berempat sedang berbincang."
           

        jump kantin_done
#---------------
#INI KE PERPUS(ga setuju)
#--------------
    label kantin_no:

        $ menu_flag = False
        p 'Ga dulu deh. Aku mau ke kamar mandi aja.' 
        k 'Yah ga asik lu!' 
        y 'Iya nih... Ga asik.' 
        p 'Aku bilang ngga ya ngga anjir!' 
        z 'Sudah deh biarin aja dia...' 
        k 'Yaudah deh... Yuk Yeri Zaky. Kita ke kantin.' 

        hide kevin with dissolve
        hide yeri with dissolve
        hide zaky with dissolve

        "Mereka bertiga mulai berjalan menjauhiku." 
        "Sejujurnya aku tidak ingin pergi kekamar mandi." 
        "Tetapi, aku ingin ke Perpustakaan untuk menenangkan diri sebelum menghadapi rapat nanti." 
        "Karena perpustakaan adalah tempat yang tenang dan sunyi." 
        "Karena hal itulah aku ingin pergi ke perpustakaan." 

        scene bg prps with dissolve

        "Sesampainya di perpustakaan."
        "Hawa ketenangan mulai dirasakan oleh benakku."
        "Aku berpikir ini merupakan pilihan terbaik daripada pergi kekantin yang tempatnya sangat ramai."
        "Aku ingin mengambil salah satu buku di rak buku." 
        "Saat aku ingin mengambil buku tersebut. Tiba-tiba ada seseorang yang menepuk pundakku dan menyapaku." 

        u '"Halo..."'

        show citra with dissolve

        "Ternyata itu Citra." 

        p 'Ahhh Citra. Ada apa?' 
        c 'Aku boleh minta tolong ga?' 
        p 'Minta tolong apa?'
        c 'Tolong ambilin buku itu donk.' 

        "Citra menunjuk buku diatas pojok kanan."

        menu:
            "Kan kamu bisa ambil sendiri.":
                jump choice5_done
            "Engga ah.":
                jump choice5_done
                

                label choice5_done:

        c 'Ya ampun... Itu tinggi banget. Ambilin donk.' 
        p 'Iya deh iya.'

        hide citra with dissolve

        "Aku mengambilkan buku tersebut."
        "Ternyata buku itu adalah buku novel romance yang akhir-akhir ini terkenal dikalangan remaja."
        "Saat aku memberikan buku tersebut kepada Citra."
        "Dirinya agak malu-malu."

        show citra with dissolve

        c 'Makasih ya!' 
        p 'Iya okay...'
        c 'Btw... kamu ikut rapat nanti sore ngga?'
        p 'Mungkin iya sih... Kan itu wajib untuk anggota OSIS.'
        p 'Emang kamu ga mau ikut?'
        c 'Bukan begitu.'

        c 'Aku hanya bertanya saja.'
        p 'Baiklah... Btw buku yang kamu baca itu lumayan terkenal ya.'
        c 'Iya sih bener... Aku mau baca dulu ya...'
        p 'Oke deh...'

        hide citra with dissolve
        
        "Citra pergi meninggalkanku untuk mencari tempat duduk yang nyaman."
        "Aku mulai mencari buku untuk dibaca."
        "Aku telah menemukan buku yang ingin kubaca."
        "Saat aku ingin mengambil buku tersebut."
        "Ada satu buku yang terjatuh karena aku mengambil buku tersebut."
        "Buakkkk!!!!"
        "Buku tersebut terjatuh dilantai."
        "Cover buku itu sangat menarik perhatianku."
        "Aku mengambil buku itu dari lantai."
        "Saat aku ingin mengambil buku tersebut ada seseorang yang menepuk pundakku."

        u 'Hei...[name].'

        show citra with dissolve

        "Ah... ternyata itu Citra."
        p 'Ada apa Cit?'
        c 'Kamu mau ikut ke kantin ga?'
        p 'Eh...'

        hide citra with dissolve

        "Ternyata Citra mengajak diriku ke kantin."
        "Aku bingung ingin ikut atau tidak."
        "Padahal beberapa waktu lalu aku menolak ajakan Kevin, Zaky, dan Yeri."
        
        show citra with dissolve
        c 'Gimana? Mau ikut?'

        menu:
            "Aduh gimana yah...":
                jump choice6_done
            "Bentar kupikir dulu...":
                jump choice6_done
                

                label choice6_done:

       
        c 'Ayo donk ikut... Jangan lama-lama mikirnya.'
        p 'Tapi tuh, beberapa waktu yang lalu aku diajak ke kantin sama Kevin, Zaky, dan Yeri.'
        p 'Tapi aku menolaknya' 
        c 'Kok gitu? Kenapa kamu menolaknya?'
        p 'Ya... karena aku males buat ikut.'
        c 'Nah... Yok ikut sekalian.'
        c 'Nanti sekalian juga untuk membahas masalah rapat nanti sore.' 

        hide citra with dissolve

        "Aku kebingungan ingin mengikutinya atau tidak."
        "Ya... mungkin ikut bukan sesuatu yang buruk."

        show citra with dissolve

        c 'Gimana?'
        p 'Iya deh iya...'
        c 'Nah gitu donk...'

        hide citra with dissolve

        "Aku mengembalikan buku yang kuambil dari ke rak buku."
        "Citra mulai meninggalkan ruangan perpustakaan."
        "Lalu, aku ikut meninggalkan ruangan perpustakaan dan mengikuti Citra."
#---------------
#INI KE PERPUS(ga setuju) to kantin
#--------------

        scene bg cntn with dissolve

        "Sesampainya disana Citra langsung menuju ke tempat pembelian."
        "Disana aku melihat Yeri sedang sendirian."
        "Aku menghampirinya dan menyapanya."

        show yerinormal with dissolve

        p "Hai Yeri... Kamu lagi ngapain?"
        y "Eh [name]... Kenapa kamu kesini?"
        y "Katanya ngga mau ikut ke kantin?"
        p "Aku ikut Citra tadi." 
        p "Dipaksa tadi sih."
        hide yerinormal 
        show yerismile
        y "Ahahahhahaha... Dipaksa."
        p "Ya mau gimana lagi."
        hide yerismile with dissolve
        "Saat kita berdua sedang mengobrol datang Kevin, Zaky, dan Citra."
        show kevin at left with dissolve:
            xalign 0.1
            yalign 1.0
        show citra at center with dissolve:
             
        show zaky at right with dissolve:
            xalign 0.9
            yalign 1.0
        k "Hai... Eh... Ada [name], katanya kamu ga mau ikut ke kantin sama kita."
        z "Iya... Kenapa tadi ga mau ikut?"
        c "Tadi [name] bareng sama aku dari perpustakaan."
        z "Jadi gitu ya."
        z "Katanya tadi kamu mau ke kamar mandi."
        p "Iya tadi aku ke kamar mandi sih."
        p "(Sebenarnya diriku berbohong.)"
        k "Begitu ya... Baiklah."
        hide kevin 
        hide citra 
        hide zaky 
        with dissolve
        "Kevin, Citra, dan Zaky mulai duduk di kursi meja kantin yang aku duduki."

        

        jump kantin_done


label kantin_done:

    "Aku mulai ingat rapat pada sore nanti."

    jump chapter1_start

label chapter1_start:

    show kevin with dissolve

    k "Jangan lupa ya rapat sore nanti."
    p "Memangnya kita mau membahas apa saja di rapat nanti?"
    k "Rencananya nanti sore pas sepulang sekolah mau ngumpulin semua anggota pengurus OSIS."

    hide kevin with dissolve

    show yeriangry at shake, center

    y_shout "AH ANJIRLAH"
    y "sebenarnya aku males banget buat ikut rapat"

    show kevin with dissolve:
        xalign 0.1
        yalign 1.0

    k "Bentarlah Yeri, belum selesai ni aku ngomongnya.."

    show citra with dissolve:
        xalign 0.9
        yalign 1.0

    c "Hahaha, sabar Yeri.."
    c "Emang resikonya ikut organisasi tu ya gini"
    c "Pulangnya telat mulu"
    y "Iyadeh iya, Silahkan kalau mau dilanjut Vin.."

    hide yeriangry 
    hide citra 
    with dissolve

    show kevin with move:
        xalign 0.5
        yalign 1.0

    k "Jadi rapat kali ini itu mau membahas tentang acara ulang tahun sekolah kita..."

    "Lalu Kevin menjelaskan sedikit tentang rapat nanti"

    p "Ouu, lalu kenapa di jadwal itu lama sekali rapatnya?"

    hide kevin with dissolve

    show citra with dissolve:
        xalign 0.8
        yalign 1.0

    show yerinormal with dissolve:
        xalign 0.2
        yalign 1.0

    y "Itulah kenapa aku malas ikut rapatnya"
    c "Iya nih, dari jam 4 sore sampai jam 8 malam itu lama banget"

    hide citra
    hide yerinormal 
    with dissolve

    show zaky with dissolve

    z "Gini, karena waktunya sudah mepet, maka rapat diadakan selama 4 jam"
    z "Jadi rencana Kevin tu mau rapat sekali jalan aja"

    show zaky with move:
        xalign 0.2
        yalign 1.0

    show kevin with dissolve

    k "Iya karena kita dapat dana dari sekolahnya juga baru kemaren malam"
    k "Jujur aku juga agak jengkel sama guru Kesiswaannya karena dia nganggep acara ini sepele"
    k "Tapi mau gimana lagi, daripada ngeluh terus mending fokus sama event besar ini."

    hide kevin with dissolve

    y "Hahaha..."
    y "Apa yang kamu harapkan dari sekolah ini"
    y "Memang sih, dari fasilitas dan muridnya itu sangat bergengsi"
    y "Tapi guru guru disini beberapa ada yang tidak niat untuk menjadi guru dan hanya ingin gajinya saja"
    c "Heh Yeri, jangan keras keras nanti kedengeran guru lain gimana?"
    z "Iya nih Yeri kalo ngomong kadang ga dipikir dulu dua kali"
    y "Halah gapapa, gaada guru disini"
    y "Toh kalau memang ada guru yang dengar biar dia tersinggung aja"
    k "Ckckck"
    k "Yaa beginilah Yeri, emang dari dulu sudah begini"
    y "Lagipula kita disini cukup ramai juga gaada yang dengar sama pembicaraan kita"
    y "Kecuali hantu yang bergentayangan disini hahaha.."
    z "Eh kamu jangan bilang gitu di sekolah ini.."
    z "Nanti kamu didatengin hantu beneran lo"
    y "Dih.. mana ada hantu di sekolah ini.." 
    y "lagipula aku ga percaya sama hal hal begituan"
    z "Kamu belum pernah dengar rumor ada hantu di sekolah ini?"
    y "Heee"
    y "Gimana tuh rumorya??"
    y "Paling paling cuma pohon keramat atau kamar mandi terkutuk kan.."
    z "Bukan.."
    z "Jadi katanya sekolah ini sangat menyeramkan kalau di malam hari"
    k "Hahaha, bukannya semua sekolah itu memang kesannya menyeramkan kalau di malam hari?"
    z "Ngga, jadi aku pernah dengar kalau kita itu gaboleh di sekolah sampai malam hari.."
    z "Katanya sih jika kita berada di sini hingga malam hari nanti akan menghilang dan tidak pernah ditemukan kembali.."
    z "Makanya jika sekolah ada kegiatan kemah biasanya diadakan diluar sekolah"
    c "Menurutku yang dikatakan Zaki masuk akal sih.."
    k "Memangnya pernah ada kasus murid menghilang disini?"
    z "Belum tau sih, tapi aku denger denger ada orang yang sempat hilang lalu ditemukan kembali.."
    y_shout "HAHAHAHAHAHA"
    y "Mana ada murid yang menghilang dan bisa kembali lagi disini.."
    z "Iya denger denger sih begitu.."
    z "Kalau beneran ada apa ngga ya aku gatau"
    p "Memangnya kamu dapat rumor itu darimana Zaki? Kok kamu bisa tau rumor itu"
    z "Kemarin jam 6 sore, aku baru keluar sekolah karena tugas piket dan sekalian nyelesaiin tugas"
    z "Lalu saat di gerbang aku gak sengaja denger dua satpam sedang membicarakan tentang sekolah ini saat malam hari"
    z "Jadi kata salah satu satpam itu.."
    z "Kalau bisa jangan masuk di sekolah ini pada malam hari"
    z "Dan jika masi ngeyel kamu bakal menyesal"
    k "Hahaha, mana mungkin.."
    z "Iya beneran, aku denger dari telinga ku sendiri, rill no fek"
    y "Halah, mungkin itu satpamnya yang penakut"
    k "Mana mungkin.."
    k "Satpam kan sudah dilatih buat berani"
    z "Iya bener si.."
    z "Tapi karena kedua satpam itu membahas itu jadinya aku heran"
    c "Tapi memangnya kalau disekolah saat malam hari ada hantunya yah?"
    c "Kan hantu itu tidak nyata"
    p "Jaman sekarang masi percaya hantu?"
    y "Bener juga yak, hantu itu tidak nyata.."
    y "Jadi buat apa takut sama hantu?"
    z "Kalian semua pemberani ya.."
    z "Aku nonton film horror, 3 hari gabisa tidur dengan tenang"
    c "Kalo nonton begituan ma aku juga takut sebenarnya.."
    c "Tapi yang namanya film itu kan belum tentu nyata"
    c "Jadi aku masi tetep ga percaya yang namanya hantu.."
    y "Iyep.. betulll"
    y "Hantu itu tidak nyata, kayak husbuku aja..."
    p "Hahahaha"
    p "Bisa aja kamu, Teri"
    y_shout "JANGAN PANGGIL AKU TERI, DASAR BODOH!!!"
    p "kan cuma bercanda Yeri, hahaha"
    y "Dih, bodolah"
    c "Udah, sabar Yeri..."
    c "[name] kan cuma bercanda"
    z "Hahaha, bercandanya"
    k "Btw.."
    k "Perasaan tadi kita lagi membahas rapat osis dah.."
    k "Kenapa pembahasannya jadi kemana-mana?"
    p "Iya juga.."
    p "Jadi gimana? Rapatnya jadi jam 4 sore nanti?"
    z "Iya, jangan sampe lupa.. apalagi cabut"
    p "Gaakan cabut aku.."
    p "Tah aku kan anaknya si paling rajin hehe"
    y "Iyadeh si paling rajin.."
    c "Hahaha"
    c "Eh Yer, sebelum rapat nanti kita ketemuan dulu di depan perpus yaa"
    c "Aku ada urusan, jadi tolong temani aku.."
    y "Oke gas"
    y "Kebetulan aku juga mau meminjam beberapa buku buat ulangan besok"
    c "Eh mapel apa?"
    y "Bahasa Jepang"
    c "Mapel yang cukup sulit yaa"
    c "Kemarin aku sudah ulangannya"
    y "Lo kamu sudah ulangan?"
    c "Iya, kemarin di jam ke tujuh"
    y "Kok enak sih.. kelasku baru besok loh"
    y "Oiya.. boleh kali"
    y "Bocoran soalnya"
    c "Aduh maaf Yer.."
    c "Karena ulangannya susah pas aku sudah selesai seketika langsung lupa semua.."
    y "Ah kamu gaasik"
    z "Udah-udah daritadi ngerumpi sendiri"
    p "Iyanih.. women"
    #bel
    k "Udah bel tuh, mending kita masuk kelas aja.."
    k "Ayo [name] kita ke kelas"
    p "Okeoke"
    z "Weh, tungguin napa.."
    z "Aku juga mau bareng ke kelasnya"
    p "Halah, manja banget lu"
    z "Bodoamat lah"

    #ch1 selesai(?) (hore(?))
    
return