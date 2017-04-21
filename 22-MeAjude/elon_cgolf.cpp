#include <iostream>



main(){
	unsigned a,b,c,d;
	cin>>a>>b>>c>>d;
	
	cout<<((a*b>c*d)?"primeiro":(a*b<c*d)?"segundo":"empate");
	
	if(a*b>c*d)
		cout<<"maior ="<<a*b;
	else
		cout<<"maior = "<<c*d;
  		
}
