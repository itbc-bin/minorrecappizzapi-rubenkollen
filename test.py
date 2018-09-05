def hoi(functie):

    def wrapper(functie2):
        print("derp")
        return functie(functie2)

    return wrapper


def checkDNA(functie):
    def wrapper(dna):

        print("test")
        if dna.count('t') + dna.count('c') + dna.count('g') + dna.count('a') != len(dna):
            print("REEEEEEEEEE")

        return functie(dna)

    return wrapper


@hoi
@checkDNA
def dna_to_rna(dna):

    dna = dna.replace('t','u').replace('T','U')
    return dna


print(dna_to_rna('aaatttcccggg'))