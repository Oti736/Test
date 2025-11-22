#Exercitiul de reverse la un sir dintr-un fisier given.txt

input_file = "given.txt"
output_file = "expected.txt"


def reverse_file(input_file, output_file):
  #Citim fisierul given.txt
  with open(input_file, "r") as infile:
      content = infile.read()

  #Reverse la ce este scris in interior
  reverse = content[::-1]

  #Scriem ce am inversat in fisierul expected.txt
  with open(output_file, "w") as outfile:
      outfile.write(reverse)

  print(f"Fisierul '{output_file}' a fost editat!")

reverse_file(input_file, output_file)


