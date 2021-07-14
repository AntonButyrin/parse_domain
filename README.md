## Domains parser
A simple and convenient solution for enumerating the base of domains and finding valid ones.
The parser is convenient in that it is fully automated, if the domain is crooked, it will continue to work, just as invalid domains are simply deleted from the file that is parsed.
##instructions for install:
1. Downloading the repository:
>![alt](https://skr.sh/i/140721/kG13xFgw.jpg?download=1&name=%D0%A1%D0%BA%D1%80%D0%B8%D0%BD%D1%88%D0%BE%D1%82%2014-07-2021%2013:07:28.jpg)
2. Install the whois alt package:
>pip install whois-alt
3. Done

## About main.py
* If you have a large TXT file (in my case 190 million lines) then just specify "text.txt" instead and run the script. Then your file will be split into convenient files of 15,000 lines. This will allow you to sort out even on a weak gland.

## About parse.py

1. Сhange the range from which to which file to pass the parser
2. Change to DNS addresses required by us
>![alt2](https://skr.sh/i/140721/IhRkA8bI.jpg?download=1&name=%D0%A1%D0%BA%D1%80%D0%B8%D0%BD%D1%88%D0%BE%D1%82%2014-07-2021%2013:08:10.jpg)
3. The required domains will appear in the success_ocean.txt file
