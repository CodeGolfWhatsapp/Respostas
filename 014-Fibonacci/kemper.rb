f=->(x){x<2?x:f[x-2]+f[x-1]};p f[gets.to_i]
