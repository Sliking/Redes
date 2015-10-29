from tld import get_tld

def get_domain(url):
    print("[DEBUG] Getting domain name")
    domain_name = get_tld(url)
    print("[DEBUG] Domain name -> DONE!")
    return domain_name
