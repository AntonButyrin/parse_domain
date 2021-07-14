import whois_alt
import subprocess


while True:
    try:
        for number_file in range(0, 10290):
            with open(f'fileNo{number_file}.txt', 'r') as open_file:
                print(f'fileNo{number_file}')
                save_lines = open_file.readlines()
                counter = 0
                for str_dom in save_lines:
                    counter += 1
                    domain = whois_alt.get_whois(f'{str_dom}')
                    print(counter)
                    if domain['nameservers']:
                        if 'NS1.DIGITALOCEAN.COM' in domain['nameservers'] \
                                or 'NS2.DIGITALOCEAN.COM' in domain['nameservers'] \
                                or 'NS3.DIGITALOCEAN.COM' in domain['nameservers']:
                            com_line = subprocess.check_output(f'nslookup -ls -d {str_dom}')
                            string_byte = str(com_line)
                            if 'SERVFAIL' in string_byte:
                                with open('success_ocean.txt', 'a') as ocean:
                                    ocean.write(str_dom)
                    cut = save_lines[counter:]
                    with open(f'fileNo{number_file}.txt', 'w') as open_file:
                        m = open_file.writelines(cut)
    except Exception:
        cut = save_lines[counter:]
        with open(f'fileNo{number_file}.txt', 'w') as open_file:
            m = open_file.writelines(cut)
