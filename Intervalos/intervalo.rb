f=gets.to_f;puts (f<0||f>100)?"Fora de intervalo":"Intervalo #{["[0,25","(25,50","(50,75","(75,100"][[f>25,f>50,f>75].count(true)]}]"
