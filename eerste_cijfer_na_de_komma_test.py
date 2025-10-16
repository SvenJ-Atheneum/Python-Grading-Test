import eerste_cijfer_na_de_komma

def test():
  assert eerste_cijfer_na_de_komma.eerste_cijfer_na_de_komma(1.724586) == 7
  assert eerste_cijfer_na_de_komma.eerste_cijfer_na_de_komma(845.92841) == 9
  assert eerste_cijfer_na_de_komma.eerste_cijfer_na_de_komma(409.9168) == 9
  assert eerste_cijfer_na_de_komma.eerste_cijfer_na_de_komma(29.042629) == 0
