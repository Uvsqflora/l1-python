def tempsEnSeconde(temps1):
    """ Renvoie la valeur en seconde de temps donné comme jour, heure, minute, seconde."""
    print((temps1[0]*86400) + (temps1[1]*3600) + (temps1[2]*60) + temps1[3])


def secondeEnTemps(seconde_tot):
    """Renvoie le temps (jour, heure, minute, seconde) qui correspond au nombre de seconde passé en argument"""

    jour = seconde_tot // 86400
    heure = (seconde_tot - (jour * 86400)) // 3600
    minute = (seconde_tot - (jour * 86400) - (heure * 3600)) // 60
    seconde = (seconde_tot - (jour * 86400) - (heure * 3600) - (minute * 60))

    print("jour =", jour, ", heure =", heure, ", minute =", minute, ", seconde =", seconde)


tempsEnSeconde((1, 3, 46, 40))
secondeEnTemps(100000)
