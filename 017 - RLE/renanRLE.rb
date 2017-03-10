gets.gsub(/(.)\1{0,8}/){$><<$&.size.to_s+$1}
