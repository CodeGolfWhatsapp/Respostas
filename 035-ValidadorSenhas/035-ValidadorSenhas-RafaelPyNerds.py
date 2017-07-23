import re;print('SENHA '+(''if re.match(r'[A-Za-z0-9\d][^\W_]{6,32}',input())else'IN')+'VALIDA')
