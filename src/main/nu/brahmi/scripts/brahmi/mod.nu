const internal_ref = '''
Brahmi[1][2]
Official Unicode Consortium code chart (PDF)
         0  1  2  3  4  5  6  7  8  9  A  B  C  D  E  F
U+1100x  𑀀 	𑀁  𑀂   𑀃    𑀄   𑀅  𑀆  𑀇  𑀈  𑀉  𑀊  𑀋  𑀌  𑀍  𑀎  𑀏
U+1101x  𑀐  𑀑  𑀒  𑀓  𑀔  𑀕  𑀖  𑀗  𑀘  𑀙  𑀚  𑀛  𑀜  𑀝  𑀞  𑀟
U+1102x  𑀠  𑀡  𑀢  𑀣  𑀤  𑀥  𑀦  𑀧  𑀨  𑀩  𑀪  𑀫  𑀬  𑀭  𑀮  𑀯
U+1103x  𑀰  𑀱  𑀲  𑀳  𑀴  𑀵  𑀶  𑀷 	𑀸 	𑀹 	𑀺 	𑀻 	𑀼 	𑀽 	𑀾 	𑀿
U+1104x 	𑁀 	𑁁 	𑁂 	𑁃 	𑁄 	𑁅 	𑁆  𑁇  𑁈  𑁉  𑁊  𑁋  𑁌  𑁍   
U+1105x  𑁒  𑁓  𑁔  𑁕  𑁖  𑁗  𑁘  𑁙  𑁚  𑁛  𑁜  𑁝  𑁞  𑁟
U+1106x  𑁠  𑁡  𑁢  𑁣  𑁤  𑁥  𑁦  𑁧  𑁨  𑁩  𑁪  𑁫  𑁬  𑁭  𑁮  𑁯
U+1107x 	𑁰  𑁱  𑁲 	𑁳 	𑁴  𑁵            BNJ '''

export const BRAHMI_CONSONANTS = (
[{pos: "velar",         cons: [𑀓,𑀔,𑀕,𑀖,𑀗, ' '           ]},
 {pos: "palatal",       cons: [𑀘,𑀙,𑀚,𑀛,𑀜,' '            ]},
 {pos: "retroflex",     cons: [𑀝,𑀞,𑀟,𑀠,𑀡, ' '           ]},
 {pos: "dental",        cons: [𑀢,𑀣,𑀤,𑀥,𑀦,'𑀷'	        ]},
 {pos: "labial",        cons: [𑀧,𑀨,𑀩,𑀪,𑀫, ' '           ]},
 {pos: "unordered 1",   cons: [𑀬,' ',𑀭,'𑀶',' ',' '      ]},
 {pos: "unordered 2",   cons: [𑀮,𑀴,,'𑀵',𑀯, ' ' ,  ' '  ]},
 {pos: "unordered 3" ,  cons: [𑀰,𑀱,𑀲,𑀳,  ' ' ,  ' '     ]},
 {pos: "unordered 4" ,  cons: [' ',' ',' ',' ',' ',' '  ]}
 ]
)

export const BRAHMI_VOWELS = ([
{position:  0, name:  "a", 		char: "\u{11005}", 		modifier:	""			}
{position:  1, name:  "A", 		char: "\u{11006}",		modifier:	"\u{11038}"		}
{position:  2, name:  "act", 		char: "\u{11005}",		modifier:	"\u{11038}"   		}
{position:  3, name:  "all", 		char: "\u{11005}",     		modifier:	"\u{11038}"		}	
{position:  4, name:  "i", 		char: "\u{11007}", 		modifier:	"\u{1103A}" 		}
{position:  5, name:  "I", 		char: "\u{11008}", 		modifier:	"\u{1103B}"		}
{position:  6, name:  "u", 		char: "\u{11009}", 		modifier:	"\u{1103C}"		}
{position:  7, name:  "U", 		char: "\u{1100A}", 		modifier:	"\u{1103D}"		}
{position:  8, name:  "e", 		char: "\u{11071}", 		modifier:	"\u{11073}"		}
{position:  9, name:  "E", 		char: "\u{1100F}", 		modifier:	"\u{11042}"		}
{position: 10, name:  "ay", 		char: "\u{11010}", 		modifier:	"\u{11043}"		}	
{position: 11, name:  "o", 		char: "\u{11072}",		modifier:	"\u{11074}"		}
{position: 12, name:  "O", 		char: "\u{11011}", 		modifier:	"\u{11044}"		}
{position: 13, name:  "av", 		char: "\u{11012}", 		modifier:	"\u{11045}"		}
{position: 14, name:  "x", 		char: "\u{1100B}", 		modifier:	"\u{1103E}"		}
{position: 15, name:  "X", 		char: "\u{1100C}", 		modifier:	"\u{1103F}"		}
{position: 16, name:  "q", 		char: "\u{1100D}", 		modifier:	"\u{11040}"		}
{position: 17, name:  "Q", 		char: "\u{1100E}", 		modifier:	"\u{11041}"		}
{position: 18, name:  "anusvAra", 	char: "\u{11005}\u{11001}", 	modifier:	"\u{11001}"		}
{position: 19, name:  "visarga", 	char: "\u{11005}\u{11002}",	modifier:	"\u{11002}"		}
{position: 20, name:  "virAma", 	char: "",  			modifier:	"\u{11046}"		}
{position: 21, name:  "chandrabindu", 	char: "",  			modifier:	"\u{11000}"		}
{position: 22, name:  "avagraha", 	char: "", 	      		modifier:	""			}
{position: 23, name:  "nuktha", 	char: "",  			modifier:  	""			}
])


