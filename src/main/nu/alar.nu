'''
Input file => .txt with random assorted lines, desired lines with some in order, some out of order.
----------------
LinkChecker 10.4.0
...
Start checking at 2024-04-17 22:28:30-007

URL        `https://alar.ink/glossary/kannada/english/%E0%B2%85'
Real URL   https://alar.ink/glossary/kannada/english/%E0%B2%85
Check time 0.373 seconds
D/L time   0.001 seconds
Size       20.72KB
Result     Valid: 200 OK

URL        `/static/search.svg'
Name       `Search'
Parent URL https://alar.ink/glossary/kannada/english/%E0%B2%85, line 39, col 37
Real URL   https://alar.ink/static/search.svg
Info       The URL is outside of the domain filter, checked only
           syntax.
Result     Valid: filtered

URL        `/dictionary/kannada/english'
Parent URL https://alar.ink/glossary/kannada/english/%E0%B2%85, line 36, col 11
Real URL   https://alar.ink/dictionary/kannada/english
Info       The URL is outside of the domain filter, checked only
           syntax.
Result     Valid: filtered

-------
Output file : Neatly formatted object level accessible json

[
  {
    "Url": "/static/search.svg",
    "Name": "Search",
    "Rurl": "https://alar.ink/static/search.svg",
    "phttp": "https://alar.ink/glossary/kannada/english/%E0%B2%85",
    "pline": "39",
    "pcol": "37"
  },
..



---------
Command to do it in nushell lang // after hours of wrangling with regular expressions:
'''
open alar.txt | parse -r '(((URL *\x60(?P<Url>[^\x27]*)\x27)\n)|((Name *\x60(?P<Name>.*)\x27)\n)|(Parent URL *(?P<Purl>(?P<phttp>[^,]*), line (?P<pline>[^,]*), col (?P<pcol>[^\n]*))\n)|((Real URL *(?P<Rurl>.*))\n)){4}' | select Url Name Rurl phttp pline pcol| to json | save -f "alar-url.txt"

