import dns.resolver

adresa = input("Unesi adresu: ")
zapis = input("Unesi tip DNS zapisa: ")

# https://www.geeksforgeeks.org/network-programming-in-python-dns-look-up/

# geeksforgeeks.org
if(zapis == 'A') :
    result = dns.resolver.query(adresa, 'A')
    for ipval in result:
        print('IP: ', ipval.to_text())

# 116.62.218.34.in-addr.arpa
elif(zapis == 'PTR') :
    result = dns.resolver.query(adresa, 'PTR')
    for ipval in result:
        print('PTR Record: ', ipval.to_text())

# geeksforgeeks.org
elif(zapis == 'MX') : 
    result = dns.resolver.query(adresa, 'MX')
    for ipval in result:
        print ('MX Record: ' , ipval.to_text())