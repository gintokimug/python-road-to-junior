def DNA_strand(dna):
    pairs = {"A" : "T", "T" : "A", "C" : "G", "G" : "C"}
    return "".join([pairs[x] for x in dna if x in pairs])


def DNA_strand(dna):
    new_dna = ""
    for x in dna:
        if x == "A":
            new_dna += "T"
        if x == "T":
            new_dna += "A"
        if x == "G":
            new_dna += "C"
        if x == "C":
            new_dna += "G"
    return new_dna
        


   


example = "AAGGCCF"
print(DNA_strand(example))