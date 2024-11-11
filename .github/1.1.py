import gmpy2

# Fonction pour calculer l'exponentiation modulaire
def modular_pow(base, exponent, modulus):
    result = 1
    base = base % modulus  # Réduire la base modulo le modulateur
    while exponent > 0:
        # Vérifier si l'exposant est impair
        if (exponent % 2 == 1):
            result = (result * base) % modulus  # Multiplier la base actuelle au résultat
        exponent = exponent >> 1  # Diviser l'exposant par 2 (décalage à droite)
        base = (base * base) % modulus  # Mettre à jour la base
    return result

# Clé publique
N = 143516336909281815529104150147210248002789712761086900059705342103220782674046289232082435789563283739805745579873432846680889870107881916428241419520831648173912486431640350000860973935300056089286158737579357805977019329557985454934146282550582942463631245697702998511180787007029139561933433550242693047924440388550983498690080764882934101834908025314861468726253425554334760146923530403924523372477686668752567287060201407464630943218236132423772636675182977585707596016011556917504759131444160240252733282969534092869685338931241204785750519748505439039801119762049796085719106591562217115679236583
e = 3

# Cryptogramme
C = 1101510739796100601351050380607502904616643795400781908795311659278941419415375

try:
    # Calculer la racine e-ième de C avec précision arbitraire
    print("Calcul de la racine e-ième de C...")
    M, exact = gmpy2.iroot(C, e)  # Calculer la racine cubique de C
    if not exact:
        print("La racine n'est pas exacte, essayons de l'ajuster.")  # Informer si la racine n'est pas précise

    # Ajuster la valeur de M si nécessaire
    initial_M = M
    while modular_pow(M, e, N) != C and M > 0:
        M -= 1  # Essayer des valeurs plus petites jusqu'à obtenir un bon candidat
        print("Essai de M :", M)

    # Vérifier si le calcul est correct après ajustement
    if modular_pow(M, e, N) == C:
        print("Message clair (entier) trouvé :", M)
    else:
        print("Erreur lors du déchiffrement après ajustement")

    # Convertir l'entier M en chaîne de caractères UTF-8
    def int_to_str(M):
        # Convertir l'entier en binaire et le formater sur des blocs de 8 bits
        bits = bin(M)[2:]
        bits = bits.zfill(8 * ((len(bits) + 7) // 8))
        try:
            # Convertir chaque bloc de 8 bits en un caractère
            return ''.join(chr(int(bits[i:i+8], 2)) for i in range(0, len(bits), 8))
        except ValueError:
            return "Conversion en chaîne échouée : caractères non valides"

    # Afficher le message déchiffré
    message = int_to_str(M)
    print("Message déchiffré :", message)

except Exception as e:
    print("Une erreur s'est produite :", e)
