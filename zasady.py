def litery(orto):
    orto = orto.lower()

    for letter in orto:
        if letter not in "aąbcćdeęfghijklłmnńoóprsśtuwxyzźż":
            return False

    return True

#-----------------------------------------------------------------

def wyjatek(wyjatek):

    wyjatek = wyjatek.replace("godzilla", "goƷ′i•la")
    wyjatek = wyjatek.replace("cito", "c′ito")
    wyjatek = wyjatek.replace("sinus", "s′inus")
    wyjatek = wyjatek.replace("nimfa", "n’imfa")

    return wyjatek

def alfabet_fonetyczny(slowo):
    # "dz", "Ʒ"Ʒ’
    slowo = slowo.replace("dz", "Ʒ")
    # "dź", "Ʒ’"
    slowo = slowo.replace("dź", "Ʒ’")
    # "dż", "Ǯ"
    slowo = slowo.replace("dż", "Ǯ")
    # "cz", "č"
    slowo = slowo.replace("cz", "č")
    # "rz", "ž"
    slowo = slowo.replace("rz", "ž")
    # "sz", "š"
    slowo = slowo.replace("sz", "š")
    # "h", "ᶍ"
    slowo = slowo.replace("ch", "ᶍ")
    # "ch", "ᶍ"
    slowo = slowo.replace("h", "ᶍ")
    # "ó", "u"
    slowo = slowo.replace("ó", "u")
    # "w", "v"
    slowo = slowo.replace("w", "v")

    return slowo

#-----------------------------------------------------------------
#dź
def litery_plus_i_plus_samogloska_dz(slowo_dz):
    slowo_dz = slowo_dz.replace("Ʒia", "Ʒ’a")
    slowo_dz = slowo_dz.replace("Ʒie", "Ʒ’e")
    slowo_dz = slowo_dz.replace("Ʒio", "Ʒ’o")
    slowo_dz = slowo_dz.replace("Ʒiu", "Ʒ’u")
    slowo_dz = slowo_dz.replace("Ʒiy", "Ʒ’y")
    slowo_dz = slowo_dz.replace("Ʒią", "Ʒ’ą")
    slowo_dz = slowo_dz.replace("Ʒię", "Ʒ’ę")

    return slowo_dz

#ģ
def litery_plus_i_plus_samogloska_g(slowo_g):
    slowo_g = slowo_g.replace("gia", "ģa")
    slowo_g = slowo_g.replace("gie", "ģe")
    slowo_g = slowo_g.replace("gio", "ģo")
    slowo_g = slowo_g.replace("giu", "ģu")
    slowo_g = slowo_g.replace("giy", "ģy")
    slowo_g = slowo_g.replace("gią", "ģą")
    slowo_g = slowo_g.replace("gię", "ģę")

    return slowo_g
#ḱ
def litery_plus_i_plus_samogloska_k(slowo_k):

    slowo_k = slowo_k.replace("kia", "ḱa")
    slowo_k = slowo_k.replace("kie", "ḱe")
    slowo_k = slowo_k.replace("kio", "ḱo")
    slowo_k = slowo_k.replace("kiu", "ḱu")
    slowo_k = slowo_k.replace("kiy", "ḱy")
    slowo_k = slowo_k.replace("kią", "ḱą")
    slowo_k = slowo_k.replace("kię", "ḱę")

    return slowo_k

#ć
def litery_plus_i_plus_samogloska_c(slowo_c):
    slowo_c = slowo_c.replace("cia", "ća")
    slowo_c = slowo_c.replace("cie", "će")
    slowo_c = slowo_c.replace("cio", "ćo")
    slowo_c = slowo_c.replace("ciu", "ću")
    slowo_c = slowo_c.replace("ciy", "ćy")
    slowo_c = slowo_c.replace("cią", "ćą")
    slowo_c = slowo_c.replace("cię", "ćę")

    return slowo_c

#ź
def litery_plus_i_plus_samogloska_z(slowo_z):
    slowo_z = slowo_z.replace("zia", "źa")
    slowo_z = slowo_z.replace("zie", "źe")
    slowo_z = slowo_z.replace("zio", "źo")
    slowo_z = slowo_z.replace("ziu", "źu")
    slowo_z = slowo_z.replace("ziy", "źy")
    slowo_z = slowo_z.replace("zią", "źą")
    slowo_z = slowo_z.replace("zię", "źę")

    return slowo_z

#ś
def litery_plus_i_plus_samogloska_s(slowo_s):

    slowo_s = slowo_s.replace("sia", "śa")
    slowo_s = slowo_s.replace("sie", "śe")
    slowo_s = slowo_s.replace("sio", "śo")
    slowo_s = slowo_s.replace("siu", "śu")
    slowo_s = slowo_s.replace("siy", "śy")
    slowo_s = slowo_s.replace("sią", "śą")
    slowo_s = slowo_s.replace("się", "śę")

    return slowo_s

#ń
def litery_plus_i_plus_samogloska_n(slowo_n):
    slowo_n = slowo_n.replace("nia", "ńa")
    slowo_n = slowo_n.replace("nie", "ńe")
    slowo_n = slowo_n.replace("nio", "ńo")
    slowo_n = slowo_n.replace("niu", "ńu")
    slowo_n = slowo_n.replace("niy", "ńy")
    slowo_n = slowo_n.replace("nią", "ńą")
    slowo_n = slowo_n.replace("nię", "ńę")

    return slowo_n
#-----------------------------------------------------------------
#dz
def litery_plus_i_plus_spolgloska_dz(slowo_dz):

     slowo_dz = slowo_dz.replace("Ʒi", "Ʒ’i")

     return slowo_dz

#ģ
def litery_plus_i_plus_spolgloska_g(slowo_g):

     slowo_g = slowo_g.replace("gi", "ģi")
     return slowo_g

#ḱ
def litery_plus_i_plus_spolgloska_k(slowo_k):

    slowo_k = slowo_k.replace("ki", "ḱi")
    return slowo_k

#ć
def litery_plus_i_plus_spolgloska_c(slowo_c):
    slowo_c = slowo_c.replace("ci", "ći")
    return slowo_c

#ź
def litery_plus_i_plus_spolgloska_z(slowo_z):

    slowo_z = slowo_z.replace("zi", "źi")
    return slowo_z

#ś
def litery_plus_i_plus_spolgloska_s(slowo_s):

    slowo_s = slowo_s.replace("si", "śi")
    return slowo_s

#ń
def litery_plus_i_plus_spolgloska_n(slowo_n):

    slowo_n = slowo_n.replace("ni", "ńi")
    return slowo_n
#-----------------------------------------------------------------
def spolgloska_plus_i_plus_samogloska_pj(slowo_pj):
    slowo_pj = slowo_pj.replace("pia", "p'ja")
    slowo_pj = slowo_pj.replace("pie", "p'je")
    slowo_pj = slowo_pj.replace("pio", "p'jo")
    slowo_pj = slowo_pj.replace("piu", "p'ju")
    slowo_pj = slowo_pj.replace("piy", "p'jy")
    slowo_pj = slowo_pj.replace("pią", "p'ją")
    slowo_pj = slowo_pj.replace("pię", "p'ję")

    return slowo_pj

def spolgloska_plus_i_plus_samogloska_bj(slowo_bj):
    slowo_bj = slowo_bj.replace("bia", "b'ja")
    slowo_bj = slowo_bj.replace("bie", "b'je")
    slowo_bj = slowo_bj.replace("bio", "b'jo")
    slowo_bj = slowo_bj.replace("biu", "b'ju")
    slowo_bj = slowo_bj.replace("biy", "b'jy")
    slowo_bj = slowo_bj.replace("bią", "b'ją")
    slowo_bj = slowo_bj.replace("bię", "b'ję")

    return slowo_bj

def spolgloska_plus_i_plus_samogloska_fj(slowo_fj):
    slowo_fj = slowo_fj.replace("fia", "f'ja")
    slowo_fj = slowo_fj.replace("fie", "f'je")
    slowo_fj = slowo_fj.replace("fio", "f'jo")
    slowo_fj = slowo_fj.replace("fiu", "f'ju")
    slowo_fj = slowo_fj.replace("fiy", "f'jy")
    slowo_fj = slowo_fj.replace("fią", "f'ją")
    slowo_fj = slowo_fj.replace("fię", "f'ję")

    return slowo_fj

def spolgloska_plus_i_plus_samogloska_wj(slowo_wj):
    slowo_wj = slowo_wj.replace("via", "v'ja")
    slowo_wj = slowo_wj.replace("vie", "v'je")
    slowo_wj = slowo_wj.replace("vio", "v'jo")
    slowo_wj = slowo_wj.replace("viu", "v'ju")
    slowo_wj = slowo_wj.replace("viy", "v'jy")
    slowo_wj = slowo_wj.replace("vią", "v'ją")
    slowo_wj = slowo_wj.replace("vię", "v'ję")

    return slowo_wj

def spolgloska_plus_i_plus_samogloska_mj(slowo_mj):
    slowo_mj = slowo_mj.replace("mia", "m'ja")
    slowo_mj = slowo_mj.replace("mie", "m'je")
    slowo_mj = slowo_mj.replace("mio", "m'jo")
    slowo_mj = slowo_mj.replace("miu", "m'ju")
    slowo_mj = slowo_mj.replace("miy", "m'jy")
    slowo_mj = slowo_mj.replace("mią", "m'ją")
    slowo_mj = slowo_mj.replace("mię", "m'ję")

    return slowo_mj
#-----------------------------------------------------------------
def geminata_w_slowie(geminata):
    geminata = geminata.replace("aa", "•a")
    geminata = geminata.replace("ąą", "•ą")
    geminata = geminata.replace("bb", "•b")
    geminata = geminata.replace("cc", "•c")
    geminata = geminata.replace("ćć", "•ć")
    geminata = geminata.replace("dd", "•d")
    geminata = geminata.replace("ee", "•e")
    geminata = geminata.replace("ęę", "•ę")
    geminata = geminata.replace("ff", "•f")
    geminata = geminata.replace("gg", "•g")
    geminata = geminata.replace("ii", "•i")
    geminata = geminata.replace("jj", "•j")
    geminata = geminata.replace("kk", "•k")
    geminata = geminata.replace("ll", "•l")
    geminata = geminata.replace("łł", "•ł")
    geminata = geminata.replace("mm", "•m")
    geminata = geminata.replace("nn", "•n")
    geminata = geminata.replace("ńń", "•ń")
    geminata = geminata.replace("oo", "•o")
    geminata = geminata.replace("pp", "•p")
    geminata = geminata.replace("qq", "•q")
    geminata = geminata.replace("rr", "•r")
    geminata = geminata.replace("ss", "•s")
    geminata = geminata.replace("śś", "•ś")
    geminata = geminata.replace("tt", "•t")
    geminata = geminata.replace("uu", "•u")
    geminata = geminata.replace("vv", "•v")
    geminata = geminata.replace("xx", "•x")
    geminata = geminata.replace("yy", "•y")
    geminata = geminata.replace("zz", "•z")
    geminata = geminata.replace("źź", "•ź")
    geminata = geminata.replace("żż", "•ż")
    geminata = geminata.replace("ƷƷ", "•Ʒ")
    geminata = geminata.replace("ǮǮ", "•Ǯ")
    geminata = geminata.replace("čč", "•č")
    geminata = geminata.replace("žž", "•ž")
    geminata = geminata.replace("šš", "•š")
    geminata = geminata.replace("ᶍᶍ", "•ᶍ")
    geminata = geminata.replace("Ʒ’Ʒ’", "•Ʒ’")

    return geminata


#-----------------------------------------------------------------
def transkrypca_fonetyczna(slowo):

    slowo=slowo.lower()

    if slowo == "godzilla" or slowo == "cito" or slowo == "sinus" or slowo == "nimfa":
        slowo = wyjatek(slowo)
        return slowo

    #---------------------------------------
    slowo = alfabet_fonetyczny(slowo)

    #---------------------------------------
    if "Ʒi" in slowo:
        if "Ʒia" or "Ʒie" or "Ʒio" or "Ʒiu" or "Ʒiy" or "Ʒią" or "Ʒię" in slowo:
            slowo = litery_plus_i_plus_samogloska_dz(slowo)

    if "gi" in slowo:
        if "gia" or "gie" or "gio" or "giu" or "giy" or "gią" or "gię" in slowo:
            slowo = litery_plus_i_plus_samogloska_g(slowo)
    if "ki" in slowo:
        if "kia" or "kie" or "kio" or "kiu" or "kiy" or "kią" or "kię" in slowo:
            slowo = litery_plus_i_plus_samogloska_k(slowo)

    if "ci" in slowo:
        if "cia" or "cie" or "cio" or "ciu" or "ciy" or "cią" or "cię" in slowo:
            slowo = litery_plus_i_plus_samogloska_c(slowo)

    if "zi" in slowo:
        if "zia" or "zie" or "zio" or "ziu" or "ziy" or "zią" or "zię" in slowo:
            slowo = litery_plus_i_plus_samogloska_z(slowo)

    if "si" in slowo:
        if "sia" or "sie" or "sio" or "siu" or "siy" or "sią" or "się" in slowo:
            slowo = litery_plus_i_plus_samogloska_s(slowo)

    if "ni" in slowo:
        if "nia" or "nie" or "nio" or "niu" or "niy" or "nią" or "nię" in slowo:
            slowo = litery_plus_i_plus_samogloska_n(slowo)

     #---------------------------------------
    slowo = litery_plus_i_plus_spolgloska_dz(slowo)

    slowo = litery_plus_i_plus_spolgloska_g(slowo)

    slowo = litery_plus_i_plus_spolgloska_k(slowo)

    slowo = litery_plus_i_plus_spolgloska_c(slowo)

    slowo = litery_plus_i_plus_spolgloska_z(slowo)

    slowo = litery_plus_i_plus_spolgloska_s(slowo)

    slowo = litery_plus_i_plus_spolgloska_n(slowo)

    #---------------------------------------
    if "pi" in slowo:
        if "pia" or "pie" or "pio" or "piu" or "piy" or "pią" or "pię" in slowo:
            slowo = spolgloska_plus_i_plus_samogloska_pj(slowo)

    if "bi" in slowo:
        if "bia" or "bie" or "bio" or "biu" or "biy" or "bią" or "bię" in slowo:
            slowo = spolgloska_plus_i_plus_samogloska_bj(slowo)

    if "fi" in slowo:
        if "fia" or "fie" or "fio" or "fiu" or "fiy" or "fią" or "fię" in slowo:
            slowo = spolgloska_plus_i_plus_samogloska_fj(slowo)

    if "mi" in slowo:
        if "mia" or "mie" or "mio" or "miu" or "miy" or "mią" or "mię" in slowo:
            slowo = spolgloska_plus_i_plus_samogloska_mj(slowo)

    if "vi" in slowo:
        if "via" or "vie" or "vio" or "viu" or "viy" or "vią" or "vię" in slowo:
            slowo = spolgloska_plus_i_plus_samogloska_wj(slowo)

    # ---------------------------------------
    if "aa" or "ąą" or "bb" or "cc" or "ćć" or "dd" or "ee" or "ęę" or "ff" or "gg" or "ii" or "jj" or "kk" or "ll" or "łł" or "mm" or "nn" or "ńń" or "oo" or "pp" or "qq" or "rr" or "ss" or "śś" or "tt" or "uu" or "vv" or "xx" or "yy" or "zz" or "źź" or "żż" or "ƷƷ" or "ǮǮ" or "čč" or "žž" or "šš" or "ᶍᶍ" or "Ʒ’Ʒ’" in slowo:
        slowo = geminata_w_slowie(slowo)

    return slowo

#-----------------------------------------------------------------
"""test1 = "dzban dżdżownica czekam rzeka szampan herbata chaber król woda dźwignia"
print(test1)
print(transkrypca_fonetyczna(test1))
print("\n")
test2 = "giełda kiedy ciotka ziemia się Ania nie lubi niani"
print(test2)
print(transkrypca_fonetyczna(test2))
print("\n")
test3 = "gil kirkor ci zima siny nic"
print(test3)
print(transkrypca_fonetyczna(test3))
print("\n")
test4 = "piec biel fiat wiosna miasto"
print(test4)
print(transkrypca_fonetyczna(test4))
print("\n")
test5 = "manna gamma ssak"
print(test5)
print(transkrypca_fonetyczna(test5))
test6 = "cito Ʒ’Ʒ’Ʒ’Ʒ’Ʒ’"
print(test6)
print(transkrypca_fonetyczna(test6))
"""