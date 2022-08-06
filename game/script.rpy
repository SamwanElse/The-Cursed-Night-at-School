# Kamu dapat taruh script game mu di file ini.

# Deklarasikan gambar di bawah line ini, menggunakan pernyataan image.
# cnth. image eileen happy = "eileen_happy.png"

#transform
transform shake:
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
image kevin = "images/kevin/Kevin.png"
#yeri
image yericharm = "images/yeri/YeriCharm.png"
image yerismile = "images/yeri/YeriSmile.png"
image yerifullsmile = "images/yeri/YeriFullSmile.png"
image yerinormal = "images/yeri/YeriNormal.png"

#citra
image citra = "images/citra/Citra.png"

# Deklarasikan karakter yang digunakan di game.
# All chara
#YERI
define ye = Character('Yeri')
define ye_shout = Character("Yeri", what_size=50)
define ye_whisper = Character("Yeri", what_size=18)
#ZAKY
define zk = Character('Zaky')
define zk_shout = Character("Zaky", what_size=34)
define zk_whisper = Character("Zaky", what_size=18)
#KEVIN
define kv = Character('Kevin')
define kv_shout = Character("Kevin", what_size=34)
define kv_whisper = Character("Kevin", what_size=18)
#CITRA
define ct = Character('Citra')
define ct_shout = Character("Citra", what_size=34)
define ct_whisper = Character("Citra", what_size=18)
#MC
define en = Character('???')
define cr = Character('[name]')
define cr_shout = Character("[name]", what_size=34)
define cr_whisper = Character("[name]", what_size=18)
#Mix
define kyc = Character("Kevin, Yeri, dan [name]")


 
# Game dimulai disini.

 
label start:

    scene bg its
    with dissolve

    stop music fadeout 1.0

    "Pagi hari ini terasa sangat cerah tidak seperti biasa."
    "Dengan semangat pagi yang membara aku pergi menuju sekolahku."
    "Dari kejauhan aku melihat Kevin sedang berjalan dipinggir jalan."

    show kevin with dissolve

    en 'Hello Kevin. Bagaimana kabarmu?'
    kv 'Hai...'

    #field name
    python:
        name = renpy.input("Siapa namamu: ")

        name = name.strip() or "You"

    kv 'Hai [name], baik kok! bagaimana denganmu?'
    cr 'Baik seperti biasa kok ahahahaha...'
    kv 'Kamu mau menuju sekolah?'
    cr 'Iyalah! Aku sudah memakai pakaian kek gini.'
    cr 'Masak ga pergi sekolah.'
    kv 'Ahahaha... Maaf aku cuma bercanda tadi.'

    hide kevin with dissolve

    scene bg outs with dissolve

    "Kami berdua berjalan menuju sekolah."
    "Sesampainya disekolah, Kevin mengingatkanku tentang rapat OSIS sehabis pulang sekolah nanti."

    show kevin with dissolve

    kv 'Hei... Jangan lupa nanti ya! Sehabis pulang sekolah buat rapat untuk acara Ulang Tahun sekolah kita.'
    cr 'Okay... Pasti aku datang kok.'
    cr 'Aku kan anak rajin.'
    kv 'Heleh ahahahaha.'

    hide kevin with dissolve

    scene bg insc with dissolve

    "Aku menuju ke ruang kelasku."
    "Saat di pertengahan perjalanan aku bertemu Yeri lalu menyapanya."

    show yerinormal with dissolve

    cr 'Hai Yeri. Bagaimana kabarmu?'
    hide yerinormal 
    show yericharm 
    ye 'Hai [name], baik kok. Bagaimana denganmu?'
    cr 'Baik kok. Aku ke kelas duluan dulu ya!'
    ye 'Okei!'
    hide yericharm with dissolve
    #-------
    #bedascene
    scene bg incl with dissolve

    "Sesampainya dikelas, aku langsung menuju ke tempat dudukku."
    "Saat aku sedang melamun. Tiba-tiba Zaky datang untuk menyapaku."
    
    show zaky with dissolve

    zk 'Woi [name]. Kamu kenapa melamun saja? Apa ada masalah dengan dirimu?'
    cr 'Tidak kok. Aku cuma bersantai aja.'
    zk 'Hadeh... Jangan lupa untuk ikut rapat nanti sepulang sekolah ya! Ingat.'
    cr 'Iya... Santai aja. Aku inget kok.'

    hide zaky with dissolve

    "Setelah kejadian itu guru pun masuk kedalam ruangan untuk memulai pelajaran di pagi yang cerah ini."

    scene bg insc with dissolve

    "Bel istirahat pun berbunyi."
    "Lalu beberapa saat kemudian Zaky, Yeri, dan Kevin menghampiriku didepan kelasku."

    show kevin at left with dissolve:
            xalign 0.1
            yalign 1.0
    show yerismile at center with dissolve:
             
    show zaky at right with dissolve:
            xalign 0.9
            yalign 1.0

    zk 'Hei [name], yuk ke kantin. Mau ga?' 
    ye 'Iya nih... mau ga?'
    
    cr 'Boleh saja sih... Tapi...'
    kv 'Ga usah pake tapi-tapian. Ayo gas berangkat.'
    cr 'Tapi aku tu males banget coy...'
    hide yerismile
    show yerinormal at center:
    ye 'Sudahlah ikut saja...'

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

        cr 'Iya deh aku ikut. Yuk ke kantin.'
        hide yerinormal
        show yerismile
        kv 'Nah gitu donk... Lama bet mikirnya dah ni anak.' 
        ye 'Yokkk berangkat!' 

        # 3 chara hilang bersamaan
        hide kevin 
        hide yerismile 
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

                cr "Aku sangat-" 

                
                jump choice2_done

                label choice2_no:

                $ menu_flag = False

                cr "Aku kurang-" 
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
        ye 'Kamu tadi mengapa melamun?' 
        ye 'Apa yang sedang kamu pikirkan?' 
        cr 'Ga ada apa-apa sih.' 
        ye 'Ah boong kamu.'
        cr 'Beneran kok.'

        #hide yerinormal
        #show yerikesal
        "Yeri menatapku dengan tatapan serius dicampur kesal."
        "Akhirnya aku pun menyerah dan memberitahunya apa alasanku melamun tadi."

        cr 'Sebenernya tadi aku merasa.'

        menu:
            "Sangat antusias dengan rapat nanti.":
                jump choice4_done
            "Kurang tertarik dengan rapat nanti.":
                jump choice4_done
                

                label choice4_done:
        #hideyerikesal
        hide yerinormal#hilangkan!
        show yerismile
        ye 'Ya ampun kukira kamu mikirin apaan.' 
        ye 'Ternyata mikirin hal kayak gitu aja.' 
        cr 'Ahahaha... Maaf ya...' 
        hide yerismile
        show yerifullsmile
        ye 'Ga apa-apa.' 
        ye 'Kamu harus ikut rapat itu walaupun suka atau engga.'
        hide yerifullsmile
        show yerismile
        ye 'Karena rapat itu untuk membahas perayaan ulang tahun sekolah kita.' 
        cr 'Iya aku tau kok.' 

        hide yerismile with dissolve
         
        "Tak lama kemudian Kevin datang ke tempat dudukku dengan Citra." 

        show kevin with dissolve

        kv 'Kalian lagi membahas apa nih?' 

        show kevin with move:
            xalign 0.3
            yalign 1.0 
        show yerismile at right with dissolve:
            xalign 0.8
            yalign 1.0

        ye "Ga ada apa-apa sih."
        cr "Iya, ga ada apa-apa."
        kv "Yang bener?"
        
        hide yerismile
        show yerinormal at right:
            xalign 0.8
            yalign 1.0

        ye "Ga ada Kevin..."
        kv "Iya deh iya."
        hide yerinormal
        hide kevin 
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
        
        ct "Hai semua..."

        hide citra
        hide zaky 
        with dissolve

        show kevin with dissolve:
            xalign 0.3
            yalign 1.0 
        show yerismile at right with dissolve:
            xalign 0.8
            yalign 1.0

        kyc "Hai Citra..."
        hide kevin
        hide yerismile
        with dissolve

        show citra with dissolve
        ct "Halo..."

        hide citra with dissolve
        show yerismile
        ye "Bagaimana kabarmu Cit?"
        show yerismile with move:
            xalign 0.3
            yalign 1.0 
        show citra at right with dissolve:
            xalign 0.8
            yalign 1.0

        ct "Baik kok!"
        hide yerismile
        show yerifullsmile:
            xalign 0.3
            yalign 1.0 
        ye "Sini kalian berdua ikut duduk!"
        ct "Okeiiii!"

        hide yerifullsmile
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
        cr 'Ga dulu deh. Aku mau ke kamar mandi aja.' 
        kv 'Yah ga asik lu!' 
        ye 'Iya nih... Ga asik.' 
        cr 'Aku bilang ngga ya ngga anjir!' 
        zk 'Sudah deh biarin aja dia...' 
        kv 'Yaudah deh... Yuk Yeri Zaky. Kita ke kantin.' 

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

        en '"Halo..."'

        show citra with dissolve

        "Ternyata itu Citra." 

        cr 'Ahhh Citra. Ada apa?' 
        ct 'Aku boleh minta tolong ga?' 
        cr 'Minta tolong apa?'
        ct 'Tolong ambilin buku itu donk.' 

        "Citra menunjuk buku diatas pojok kanan."

        menu:
            "Kan kamu bisa ambil sendiri.":
                jump choice5_done
            "Engga ah.":
                jump choice5_done
                

                label choice5_done:

        ct 'Ya ampun... Itu tinggi banget. Ambilin donk.' 
        cr 'Iya deh iya.'

        hide citra with dissolve

        "Aku mengambilkan buku tersebut."
        "Ternyata buku itu adalah buku novel romance yang akhir-akhir ini terkenal dikalangan remaja."
        "Saat aku memberikan buku tersebut kepada Citra."
        "Dirinya agak malu-malu."

        show citra with dissolve

        ct 'Makasih ya!' 
        cr 'Iya okay...'
        ct 'Btw... kamu ikut rapat nanti sore ngga?'
        cr 'Mungkin iya sih... Kan itu wajib untuk anggota OSIS.'
        cr 'Emang kamu ga mau ikut?'
        ct 'Bukan begitu.'

        ct 'Aku hanya bertanya saja.'
        cr 'Baiklah... Btw buku yang kamu baca itu lumayan terkenal ya.'
        ct 'Iya sih bener... Aku mau baca dulu ya...'
        cr 'Oke deh...'

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

        en 'Hei...[name].'

        show citra with dissolve

        "Ah... ternyata itu Citra."
        cr 'Ada apa Cit?'
        ct 'Kamu mau ikut ke kantin ga?'
        cr 'Eh...'

        hide citra with dissolve

        "Ternyata Citra mengajak diriku ke kantin."
        "Aku bingung ingin ikut atau tidak."
        "Padahal beberapa waktu lalu aku menolak ajakan Kevin, Zaky, dan Yeri."
        
        show citra with dissolve
        ct 'Gimana? Mau ikut?'

        menu:
            "Aduh gimana yah...":
                jump choice6_done
            "Bentar kupikir dulu...":
                jump choice6_done
                

                label choice6_done:

       
        ct 'Ayo donk ikut... Jangan lama-lama mikirnya.'
        cr 'Tapi tuh, beberapa waktu yang lalu aku diajak ke kantin sama Kevin, Zaky, dan Yeri.'
        cr 'Tapi aku menolaknya' 
        ct 'Kok gitu? Kenapa kamu menolaknya?'
        cr 'Ya... karena aku males buat ikut.'
        ct 'Nah... Yok ikut sekalian.'
        ct 'Nanti sekalian juga untuk membahas masalah rapat nanti sore.' 

        hide citra with dissolve

        "Aku kebingungan ingin mengikutinya atau tidak."
        "Ya... mungkin ikut bukan sesuatu yang buruk."

        show citra with dissolve

        ct 'Gimana?'
        cr 'Iya deh iya...'
        ct 'Nah gitu donk...'

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

        cr "Hai Yeri... Kamu lagi ngapain?"
        ye "Eh [name]... Kenapa kamu kesini?"
        ye "Katanya ngga mau ikut ke kantin?"
        cr "Aku ikut Citra tadi." 
        cr "Dipaksa tadi sih."
        hide yerinormal 
        show yerismile
        ye "Ahahahhahaha... Dipaksa."
        cr "Ya mau gimana lagi."
        hide yerismile with dissolve
        "Saat kita berdua sedang mengobrol datang Kevin, Zaky, dan Citra."
        show kevin at left with dissolve:
            xalign 0.1
            yalign 1.0
        show citra at center with dissolve:
             
        show zaky at right with dissolve:
            xalign 0.9
            yalign 1.0
        kv "Hai... Eh... Ada [name], katanya kamu ga mau ikut ke kantin sama kita."
        zk "Iya... Kenapa tadi ga mau ikut?"
        ct "Tadi [name] bareng sama aku dari perpustakaan."
        zk "Jadi gitu ya."
        zk "Katanya tadi kamu mau ke kamar mandi."
        cr "Iya tadi aku ke kamar mandi sih."
        cr "(Sebenarnya diriku berbohong.)"
        kv "Begitu ya... Baiklah."
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

    kv "Jangan lupa ya rapat sore nanti."
    cr "Memangnya kita mau membahas apa saja di rapat nanti?"
    kv "Rencananya nanti sore pas sepulang sekolah mau ngumpulin semua anggota pengurus OSIS."

    hide kevin with dissolve

    show yeriangry at shake, center

    ye_shout "AH ANJIRLAH"
    ye "sebenarnya aku males banget buat ikut rapat"

    show kevin with dissolve at left

    kv "Bentarlah Yeri, belum selesai ni aku ngomongnya.."

    show citra with dissolve at right

    ct "Hahaha, sabar Yeri.."

    ct "Emang resikonya ikut organisasi tu ya gini"

    ct "Pulangnya telat mulu"

    
    
return