from aiogram.types import ReplyKeyboardMarkup, ReplyKeyboardRemove, KeyboardButton,\
    InlineKeyboardButton, InlineKeyboardMarkup

# *Bosh menyu
b1 = KeyboardButton("📜E'lon berish")
b2 = KeyboardButton("📫Mening e'lonlarim")
b3 = KeyboardButton("Bizning kanallar")
b4 = KeyboardButton("📩Fikr bildirish")
b5 = KeyboardButton("📎Ma'lumot")
b6 = KeyboardButton("💬Takliflar")
b7 = KeyboardButton("⚙️Sozlamalar")

kb_bosh_menu = ReplyKeyboardMarkup(resize_keyboard=True)
kb_bosh_menu.add(b1, b2, b3, b4, b5, b6, b7)


# categories

ib1 = InlineKeyboardButton("Bolalar kiyimlari", callback_data="Bolalar kiyimlari")
ib2 = InlineKeyboardButton("Elektronika", callback_data="Elektronika")
ib3 = InlineKeyboardButton("Kitoblar", callback_data="Kitoblar")
ib4 = InlineKeyboardButton("Moda", callback_data="Moda")
ib5 = InlineKeyboardButton("Qurilish", callback_data="Qurilish")
ib6 = InlineKeyboardButton("Uy jihozlari", callback_data="Uy jihozlari")
ib7 = InlineKeyboardButton("Xayvonlar", callback_data="Xayvonlar")
ib8 = InlineKeyboardButton("Boshqa", callback_data="Boshqa")

last_kb1 = InlineKeyboardButton("⬅️ Orqaga", callback_data="last_kb1")
last_kb2 = InlineKeyboardButton("⬅️ Orqaga", callback_data="last_kb2")
last_kb3 = InlineKeyboardButton("⬅️ Orqaga", callback_data="last_kb3")


# Cancel and Discard
b_clear = InlineKeyboardButton("❌ Bekor qilish", callback_data="discard")

categories = InlineKeyboardMarkup().add(ib1, ib2, ib3, ib4, ib5, ib6, ib7, ib8)
categories.row(b_clear)


# Viloyatlar
vb1 = InlineKeyboardButton("Andijon", callback_data="Andijon")
vb2 = InlineKeyboardButton("Buxoro", callback_data="Buxoro")
vb3 = InlineKeyboardButton("Farg'ona", callback_data="Farg'ona")
vb4 = InlineKeyboardButton("Jizzax", callback_data="Jizzax")
vb5 = InlineKeyboardButton("Namangan", callback_data="Namangan")
vb6 = InlineKeyboardButton("Navoiy", callback_data="Navoiy")
vb7 = InlineKeyboardButton("Qashqadaryo", callback_data="Qashqadaryo")
vb8 = InlineKeyboardButton("Qoraqalpog'iston", callback_data="Qoraqalpog'iston")
vb9 = InlineKeyboardButton("Samarqand", callback_data="Samarqand")
vb10 = InlineKeyboardButton("Sirdaryo", callback_data="Sirdaryo")
vb11 = InlineKeyboardButton("Surxandaryo", callback_data="Surxandaryo")
vb12 = InlineKeyboardButton("Toshkent", callback_data="Toshkent")
vb13 = InlineKeyboardButton("Xorazm", callback_data="Xorazm")
vb14 = InlineKeyboardButton("Toshkent shaxar", callback_data="Toshkent_shaxar")

States_kb = InlineKeyboardMarkup()
States_kb.row(vb1, vb2)
States_kb.row(vb3, vb4)
States_kb.row(vb5, vb6)
States_kb.row(vb7, vb8)
States_kb.row(vb9, vb10)
States_kb.row(vb11, vb12)
States_kb.row(vb13, vb14)
States_kb.row(b_clear)

# ============Tumanlar========
# Andijon

anb1 = InlineKeyboardButton("Andijon", callback_data="Andijon")
anb2 = InlineKeyboardButton("Asaka", callback_data="Asaka")
anb3 = InlineKeyboardButton("Baliqchi", callback_data="Baliqchi")
anb4 = InlineKeyboardButton("Bo'z", callback_data="Bo'z")
anb5 = InlineKeyboardButton("Buloqboshi", callback_data="Buloqboshi")
anb6 = InlineKeyboardButton("Izbosgan", callback_data="Izbosgan")
anb7 = InlineKeyboardButton("Jalaquduq", callback_data="Jalaquduq")
anb8 = InlineKeyboardButton("Marhamat", callback_data="Marhamat")
anb9 = InlineKeyboardButton("Oltinko'l", callback_data="Oltinko'l")
anb10 = InlineKeyboardButton("Paxtaobod", callback_data="Paxtaobod")
anb11 = InlineKeyboardButton("Qo'rg'ontepa", callback_data="Qo'rg'ontepa")
anb12 = InlineKeyboardButton("Shaxrixon", callback_data="Shaxrixon")
anb13 = InlineKeyboardButton("Ulug'nor", callback_data="Ulug'nor")
anb14 = InlineKeyboardButton("Xo'jaobod", callback_data="Xo'jaobod")

Andijon_kb = InlineKeyboardMarkup()
Andijon_kb.row(anb1, anb2)
Andijon_kb.row(anb3, anb4)
Andijon_kb.row(anb5, anb6)
Andijon_kb.row(anb7, anb8)
Andijon_kb.row(anb9, anb10)
Andijon_kb.row(anb11, anb12)
Andijon_kb.row(anb13, anb14)
Andijon_kb.row(b_clear)


# Buxoro

bub1 = InlineKeyboardButton("Buxoro", callback_data="Buxoro")
bub2 = InlineKeyboardButton("Kogon", callback_data="Kogon")
bub3 = InlineKeyboardButton("G'ijduvon", callback_data="G'ijduvon")
bub4 = InlineKeyboardButton("Shofirkon", callback_data="Shofirkon")
bub5 = InlineKeyboardButton("Qorako'l", callback_data="Qorako'l")
bub6 = InlineKeyboardButton("Olot", callback_data="Olot")
bub7 = InlineKeyboardButton("Jondor", callback_data="Jondor")
bub8 = InlineKeyboardButton("Qorovulbozor", callback_data="Qorovulbozor")
bub9 = InlineKeyboardButton("Peshku", callback_data="Peshku")
bub10 = InlineKeyboardButton("Romitan", callback_data="Romitan")
bub11 = InlineKeyboardButton("Vobkent", callback_data="Vobkent")

Buxoro_kb = InlineKeyboardMarkup()
Buxoro_kb.row(bub1, bub2)
Buxoro_kb.row(bub3, bub4)
Buxoro_kb.row(bub5, bub6)
Buxoro_kb.row(bub7, bub8)
Buxoro_kb.row(bub9, bub10)
Buxoro_kb.row(bub11)
Buxoro_kb.row(b_clear)

# Farg'ona

fab1 = InlineKeyboardButton("Farg'ona", callback_data="Farg'ona")
fab2 = InlineKeyboardButton("So'x", callback_data="Sox")
fab3 = InlineKeyboardButton("Quva", callback_data="Quva")
fab4 = InlineKeyboardButton("Rishton", callback_data="Rishton")
fab5 = InlineKeyboardButton("Toshloq", callback_data="Toshloq")
fab6 = InlineKeyboardButton("Oltiariq", callback_data="Oltiariq")
fab7 = InlineKeyboardButton("Beshariq", callback_data="Beshariq")
fab8 = InlineKeyboardButton("Yaypan", callback_data="Yaypan")
fab9 = InlineKeyboardButton("Bag'dod", callback_data="Bag'dod")
fab10 = InlineKeyboardButton("Buvayda", callback_data="Buvayda")
fab11 = InlineKeyboardButton("Dang'ara", callback_data="Dang'ara")
fab12 = InlineKeyboardButton("Furqat", callback_data="Furqat")
fab13 = InlineKeyboardButton("Qo'shtepa", callback_data="Qo'shtepa")
fab14 = InlineKeyboardButton("Uchko'prik", callback_data="Uchko'prik")
fab15 = InlineKeyboardButton("Yozyovon", callback_data="Yozyovon")

Fargona_kb = InlineKeyboardMarkup()
Fargona_kb.row(fab1, fab2)
Fargona_kb.row(fab3, fab4)
Fargona_kb.row(fab5, fab6)
Fargona_kb.row(fab7, fab8)
Fargona_kb.row(fab9, fab10)
Fargona_kb.row(fab11, fab12)
Fargona_kb.row(fab13, fab14)
Fargona_kb.row(fab15)
Fargona_kb.row(b_clear)

# Jizzax

jib1 = InlineKeyboardButton("Arnasoy", callback_data="Arnasoy")
jib2 = InlineKeyboardButton("Zomin", callback_data="Zomin")
jib3 = InlineKeyboardButton("Mirzacho'l", callback_data="Mirzacho'l")
jib4 = InlineKeyboardButton("G'allaorol", callback_data="G'allaorol")
jib5 = InlineKeyboardButton("Paxtakor", callback_data="Paxtakor")
jib6 = InlineKeyboardButton("Baxmal", callback_data="Baxmal")
jib7 = InlineKeyboardButton("Do'stlik", callback_data="Do'stlik")
jib8 = InlineKeyboardButton("Forish", callback_data="Forish")
jib9 = InlineKeyboardButton("SharofRashidov", callback_data="SharofRashidov")
jib10 = InlineKeyboardButton("Yangiobod", callback_data="Yangiobod")
jib11 = InlineKeyboardButton("Zafarobod", callback_data="Zafarobod")
jib12 = InlineKeyboardButton("Zarbdor", callback_data="Zarbdor")


Jizzax_kb = InlineKeyboardMarkup()
Jizzax_kb.row(jib1, jib2)
Jizzax_kb.row(jib3, jib4)
Jizzax_kb.row(jib5, jib6)
Jizzax_kb.row(jib7, jib8)
Jizzax_kb.row(jib9, jib10)
Jizzax_kb.row(jib11, jib12)
Jizzax_kb.row(b_clear)

# Namangan

nab1 = InlineKeyboardButton("Namangan", callback_data="Namangan")
nab2 = InlineKeyboardButton("Chust", callback_data="Chust")
nab3 = InlineKeyboardButton("Chortoq", callback_data="Chortoq")
nab4 = InlineKeyboardButton("Kosonsoy", callback_data="Kosonsoy")
nab5 = InlineKeyboardButton("Uchqo'rg'on", callback_data="Uchqo'rg'on")
nab6 = InlineKeyboardButton("Uychi", callback_data="Uychi")
nab7 = InlineKeyboardButton("Nurota", callback_data="Nurota")
nab8 = InlineKeyboardButton("Toshbuloq", callback_data="Toshbuloq")
nab9 = InlineKeyboardButton("Yangiqo'rg'on", callback_data="Yangiqo'rg'on")
nab10 = InlineKeyboardButton("To'raqo'rg'on", callback_data="To'raqo'rg'on")
nab11 = InlineKeyboardButton("Pop", callback_data="Pop")

Namangan_kb = InlineKeyboardMarkup()
Namangan_kb.row(nab1, nab2)
Namangan_kb.row(nab3, nab4)
Namangan_kb.row(nab5, nab6)
Namangan_kb.row(nab7, nab8)
Namangan_kb.row(nab9, nab10)
Namangan_kb.row(nab11)
Namangan_kb.row(b_clear)

# Navoiy

navb1 = InlineKeyboardButton("Zarafshon", callback_data="Zarafshon")
navb2 = InlineKeyboardButton("Karama", callback_data="Karama")
navb3 = InlineKeyboardButton("Konimex", callback_data="Konimex")
navb4 = InlineKeyboardButton("Xatirchi", callback_data="Xatirchi")
navb5 = InlineKeyboardButton("Navbahor", callback_data="Navbahor")
navb6 = InlineKeyboardButton("Nurota", callback_data="Nurota")
navb7 = InlineKeyboardButton("Tomdibuloq", callback_data="Tomdibuloq")
navb8 = InlineKeyboardButton("Uchquduq", callback_data="Uchquduq")

Navoiy_kb = InlineKeyboardMarkup()
Navoiy_kb.row(navb1, navb2)
Navoiy_kb.row(navb3, navb4)
Navoiy_kb.row(navb5, navb6)
Navoiy_kb.row(navb7, navb8)
Navoiy_kb.row(b_clear)

# Qashqadaryo

qab1 = InlineKeyboardButton("Qarshi", callback_data="Qarshi")
qab2 = InlineKeyboardButton("Koson", callback_data="Koson")
qab3 = InlineKeyboardButton("Kitob", callback_data="Kitob")
qab4 = InlineKeyboardButton("Qamashi", callback_data="Qamashi")
qab5 = InlineKeyboardButton("Shaxrisabz", callback_data="Shaxrisabz")
qab6 = InlineKeyboardButton("Shayxali", callback_data="Shayxali")
qab7 = InlineKeyboardButton("G'uzor", callback_data="G'uzor")
qab8 = InlineKeyboardButton("Chiroqchi", callback_data="Chiroqchi")
qab9 = InlineKeyboardButton("Dehqonobod", callback_data="Dehqonobod")
qab10 = InlineKeyboardButton("Mirishkor", callback_data="Mirishkor")
qab11 = InlineKeyboardButton("Nishon", callback_data="Nishon")
qab12 = InlineKeyboardButton("Yakkabog'", callback_data="Yakkabog'")

Qashqadaryo_kb = InlineKeyboardMarkup()
Qashqadaryo_kb.row(qab1, qab2)
Qashqadaryo_kb.row(qab3, qab4)
Qashqadaryo_kb.row(qab5, qab6)
Qashqadaryo_kb.row(qab7, qab8)
Qashqadaryo_kb.row(qab9, qab10)
Qashqadaryo_kb.row(qab11, qab12)
Qashqadaryo_kb.row(b_clear)

# Qoraqalpog'iston

qob1 = InlineKeyboardButton("Amudaryo", callback_data="Amudaryo")
qob2 = InlineKeyboardButton("Nukus", callback_data="Nukus")
qob3 = InlineKeyboardButton("Xo'jayli", callback_data="Xo'jayli")
qob4 = InlineKeyboardButton("Qo'ng'irot", callback_data="Qo'ng'irot")
qob5 = InlineKeyboardButton("Beruniy", callback_data="Beruniy")
qob6 = InlineKeyboardButton("To'rtko'l", callback_data="To'rtko'l")
qob7 = InlineKeyboardButton("Chimboy", callback_data="Chimboy")
qob8 = InlineKeyboardButton("Qorao'zak", callback_data="Qorao'zak")
qob9 = InlineKeyboardButton("Ellikqala", callback_data="Ellikqala")
qob10 = InlineKeyboardButton("Kegeyli", callback_data="Kegeyli")
qob11 = InlineKeyboardButton("Mo'ynoq", callback_data="Mo'ynoq")
qob12 = InlineKeyboardButton("Qanliko'l", callback_data="Qanliko  'l")
qob13 = InlineKeyboardButton("Shumanay", callback_data="Shumanay")
qob14 = InlineKeyboardButton("Taxtako'pir", callback_data="Taxtako'pir")

Qoraqalpogiston_kb = InlineKeyboardMarkup()
Qoraqalpogiston_kb.row(qob1, qob2)
Qoraqalpogiston_kb.row(qob3, qob4)
Qoraqalpogiston_kb.row(qob5, qob6)
Qoraqalpogiston_kb.row(qob7, qob8)
Qoraqalpogiston_kb.row(qob9, qob10)
Qoraqalpogiston_kb.row(qob11, qob12)
Qoraqalpogiston_kb.row(qob13, qob14)
Qoraqalpogiston_kb.row(b_clear)

# Samarqand

sab1 = InlineKeyboardButton("Oqdaryo", callback_data="Oqdaryo")
sab2 = InlineKeyboardButton("Nurobod", callback_data="Nurobod")
sab3 = InlineKeyboardButton("Narpay", callback_data="Narpay")
sab4 = InlineKeyboardButton("Jomboy", callback_data="Jomboy")
sab5 = InlineKeyboardButton("Ishtixon", callback_data="Ishtixon")
sab6 = InlineKeyboardButton("Samarqand", callback_data="Samarqand")
sab7 = InlineKeyboardButton("Kattaqo'rg'on", callback_data="Kattaqo'rg'on")
sab8 = InlineKeyboardButton("Urgut", callback_data="Urgut")
sab9 = InlineKeyboardButton("Bulung'ur", callback_data="Bulung'ur")
sab10 = InlineKeyboardButton("Pastaqo'rg'on", callback_data="Pastaqo'rg'on")
sab11 = InlineKeyboardButton("Bulung'ur", callback_data="Bulung'ur")
sab12 = InlineKeyboardButton("Paxtachi", callback_data="Paxtachi")
sab13 = InlineKeyboardButton("Paxtachi", callback_data="Paxtachi")
sab14 = InlineKeyboardButton("Payariq", callback_data="Payariq")
sab15 = InlineKeyboardButton("Toyloq", callback_data="Toyloq")

Samarqand_kb = InlineKeyboardMarkup()
Samarqand_kb.row(sab1, sab2)
Samarqand_kb.row(sab3, sab4)
Samarqand_kb.row(sab5, sab6)
Samarqand_kb.row(sab7, sab8)
Samarqand_kb.row(sab9, sab10)
Samarqand_kb.row(sab11, sab12)
Samarqand_kb.row(sab13, sab14)
Samarqand_kb.row(sab15)
Samarqand_kb.row(b_clear)

# Sirdaryo

sib1 = InlineKeyboardButton("Guliston", callback_data="Guliston")
sib2 = InlineKeyboardButton("Sirdaryo", callback_data="Sirdaryo")
sib3 = InlineKeyboardButton("Sardoba", callback_data="Sardoba")
sib4 = InlineKeyboardButton("Oqoltin", callback_data="Oqoltin")
sib5 = InlineKeyboardButton("Boyovut", callback_data="Boyovut")
sib6 = InlineKeyboardButton("Xovos", callback_data="Xovos")
sib7 = InlineKeyboardButton("Mirzaobod", callback_data="Mirzaobod")
sib8 = InlineKeyboardButton("Sayxunobod", callback_data="Sayxunobod")

Sirdaryo_kb = InlineKeyboardMarkup()
Sirdaryo_kb.row(sib1, sib2)
Sirdaryo_kb.row(sib3, sib4)
Sirdaryo_kb.row(sib5, sib6)
Sirdaryo_kb.row(sib7, sib8)
Sirdaryo_kb.row(b_clear)

# Surxandaryo

sub1 = InlineKeyboardButton("Termiz", callback_data="Termiz")
sub2 = InlineKeyboardButton("Denov", callback_data="Denov")
sub3 = InlineKeyboardButton("Jarqo'rg'on", callback_data="Jarqo'rg'on")
sub4 = InlineKeyboardButton("Sherobod", callback_data="Sherobod")
sub5 = InlineKeyboardButton("Boysun", callback_data="Boysun")
sub6 = InlineKeyboardButton("Sho'rchi", callback_data="Sho'rchi")
sub7 = InlineKeyboardButton("Sariosiyo", callback_data="Sariosiyo")
sub8 = InlineKeyboardButton("Angor", callback_data="Angor")
sub9 = InlineKeyboardButton("Qiziriq", callback_data="Qiziriq")
sub10 = InlineKeyboardButton("Qumqo'rg'on", callback_data="Qumqo'rg'on")
sub11 = InlineKeyboardButton("Muzrabod", callback_data="Muzrabod")
sub12 = InlineKeyboardButton("Oltinsoy", callback_data="Oltinsoy")
sub13 = InlineKeyboardButton("Uzun", callback_data="Uzun")
sub14 = InlineKeyboardButton("Bandixon", callback_data="Bandixon")

Surxandaryo_kb = InlineKeyboardMarkup()
Surxandaryo_kb.row(sub1, sub2)
Surxandaryo_kb.row(sub3, sub4)
Surxandaryo_kb.row(sub5, sub6)
Surxandaryo_kb.row(sub7, sub8)
Surxandaryo_kb.row(sub9, sub10)
Surxandaryo_kb.row(sub11, sub12)
Surxandaryo_kb.row(sub13, sub14)
Surxandaryo_kb.row(b_clear)


# Toshkennt
tob1 = InlineKeyboardButton("Bo'stonliq", callback_data="Bo'stonliq")
tob2 = InlineKeyboardButton("Bekobod", callback_data="Bekobod")
tob3 = InlineKeyboardButton("Bo'ka", callback_data="Bo'ka")
tob4 = InlineKeyboardButton("Yangiyo'l", callback_data="Yangiyo'l")
tob5 = InlineKeyboardButton("Parkent", callback_data="Parkent")
tob6 = InlineKeyboardButton("Ohangaron", callback_data="Ohangaron")
tob7 = InlineKeyboardButton("Piskent", callback_data="Piskent")
tob8 = InlineKeyboardButton("Qibray", callback_data="Qibray")
tob9 = InlineKeyboardButton("Zomin", callback_data="Zomin")
tob10 = InlineKeyboardButton("Quyi-chirchiq", callback_data="Quyi-chirchiq")
tob11 = InlineKeyboardButton("Yuqori-chirchiq", callback_data="Yuqori-chirchiq")
tob12 = InlineKeyboardButton("O'rta-chirchiq", callback_data="O'rta-chirchiq")
tob13 = InlineKeyboardButton("Oqqo'rg'on", callback_data="Oqqo'rg'on")
tob14 = InlineKeyboardButton("Chinoz", callback_data="Chinoz")

Toshkent_kb = InlineKeyboardMarkup()
Toshkent_kb.row(tob1, tob2)
Toshkent_kb.row(tob3, tob4)
Toshkent_kb.row(tob5, tob6)
Toshkent_kb.row(tob7, tob8)
Toshkent_kb.row(tob9, tob10)
Toshkent_kb.row(tob11, tob12)
Toshkent_kb.row(tob13, tob14)
Toshkent_kb.row(b_clear)

# Xorazm

xob1 = InlineKeyboardButton("Urganch", callback_data="Urganch")
xob2 = InlineKeyboardButton("Xiva", callback_data="Xiva")
xob3 = InlineKeyboardButton("Xonqa", callback_data="Xonqa")
xob4 = InlineKeyboardButton("Gurlan", callback_data="Gurlan")
xob5 = InlineKeyboardButton("Shovot", callback_data="Shovot")
xob6 = InlineKeyboardButton("Bog'ot", callback_data="Bog'ot")
xob7 = InlineKeyboardButton("Hazorasp", callback_data="Hazorasp")
xob8 = InlineKeyboardButton("Qo'shko'prik", callback_data="Qo'shko'prik")
xob9 = InlineKeyboardButton("Yangiariq", callback_data="Yangiariq")
xob10 = InlineKeyboardButton("Yangibozor", callback_data="Yangibozor")
xob11 = InlineKeyboardButton("Tuproqqala", callback_data="Tuproqqala")

Xorazm_kb = InlineKeyboardMarkup()
Xorazm_kb.row(xob1, xob2)
Xorazm_kb.row(xob3, xob4)
Xorazm_kb.row(xob5, xob6)
Xorazm_kb.row(xob7, xob8)
Xorazm_kb.row(xob9, xob10)
Xorazm_kb.row(xob11)
Xorazm_kb.row(b_clear)


# Toshkent shaxri

toshb1 = InlineKeyboardButton("Bektemir", callback_data="Bektemir")
toshb2 = InlineKeyboardButton("Mirobod", callback_data="Mirobod")
toshb3 = InlineKeyboardButton("Mirzo-Ulug'bek", callback_data="Mirzo-Ulug'bek")
toshb4 = InlineKeyboardButton("Sergeli", callback_data="Sergeli")
toshb5 = InlineKeyboardButton("Olmazor", callback_data="Olmazor")
toshb6 = InlineKeyboardButton("Uchtepa", callback_data="Uchtepa")
toshb7 = InlineKeyboardButton("Shayxontoxur", callback_data="Shayxontoxur")
toshb8 = InlineKeyboardButton("Yashnobod", callback_data="Yashnobod")
toshb9 = InlineKeyboardButton("Chilonzor", callback_data="Chilonzor")
toshb10 = InlineKeyboardButton("Yunusobod", callback_data="Yunusobod")
toshb11 = InlineKeyboardButton("Yakkasaroy", callback_data="Yakkasaroy")

Toshkent_shkb = InlineKeyboardMarkup()
Toshkent_shkb.row(toshb1, toshb2)
Toshkent_shkb.row(toshb3, toshb4)
Toshkent_shkb.row(toshb5, toshb6)
Toshkent_shkb.row(toshb7, toshb8)
Toshkent_shkb.row(toshb9, toshb10)
Toshkent_shkb.row(toshb11)
Toshkent_shkb.row(b_clear)

# Send to admin
print_b = InlineKeyboardButton("✅ Yuborish", callback_data="print")
discard_b = InlineKeyboardButton("❌ Bekor qilish", callback_data="discard")
kb_send = InlineKeyboardMarkup()
kb_send.row(discard_b, print_b)


# Check
kb_check = InlineKeyboardMarkup()
kb_check.row(b_clear)

# Admin Print to Channel
print_to_channel_b = InlineKeyboardButton("✅ Kanalga chop etish", callback_data="printtochannel")
discard_b = InlineKeyboardButton("❌ Rad etish", callback_data="discardtouser")
kb_print_to_channel = InlineKeyboardMarkup()
kb_print_to_channel.row(discard_b)
kb_print_to_channel.row(print_to_channel_b)


# commands
advertisement = KeyboardButton('/elonlarim')
kb_ad = ReplyKeyboardMarkup(resize_keyboard=True)
kb_ad.add(advertisement)