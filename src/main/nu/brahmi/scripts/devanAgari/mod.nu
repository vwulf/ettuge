const internal_ref = '''
│ 0 │ 0x900 │ ऀ 	    │ 32 │ 0x920 │ ठ    │  64 │ 0x940  │ ी   │ 	96 │ 0x960   │ ॠ    │
│ 1 │ 0x901 │ ँ      │ 33 │ 0x921 │ ड    │  65 │ 0x941  │ ु     │  97 │ 0x961   │ ॡ    │
│ 2 │ 0x902 │ ं      │ 34 │ 0x922 │ ढ    │  66 │ 0x942  │ ू     │  98 │ 0x962   │ ॢ     │
│ 3 │ 0x903 │ ः    │ 35 │ 0x923 │ ण    │  67 │ 0x943  │ ृ     │  99 │ 0x963   │ ॣ     │
│ 4 │ 0x904 │ ऄ     │ 36 │ 0x924 │ त    │  68 │ 0x944  │ ॄ     │ 100 │ 0x964   │ ।    │
│ 5 │ 0x905 │ अ     │ 37 │ 0x925 │ थ    │  69 │ 0x945  │ ॅ     │ 101 │ 0x965   │ ॥    │
│ 6 │ 0x906 │ आ     │ 38 │ 0x926 │ द    │  70 │ 0x946  │ ॆ     │ 102 │ 0x966   │ ०    │
│ 7 │ 0x907 │ इ     │ 39 │ 0x927 │ ध    │  71 │ 0x947  │ े     │ 103 │ 0x967   │ १    │
│ 8 │ 0x908 │ ई     │ 40 │ 0x928 │ न    │  72 │ 0x948  │ ै     │ 104 │ 0x968   │ २    │
│ 9 │ 0x909 │ उ     │ 41 │ 0x929 │ ऩ    │  73 │ 0x949  │ ॉ   │ 105 │ 0x969   │ ३    │
│10 │ 0x90A │ ऊ     │ 42 │ 0x92A │ प    │  74 │ 0x94A  │ ॊ   │ 106 │ 0x96A   │ ४    │
│11 │ 0x90B │ ऋ     │ 43 │ 0x92B │ फ    │  75 │ 0x94B  │ ो   │ 107 │ 0x96B   │ ५    │
│12 │ 0x90C │ ऌ     │ 44 │ 0x92C │ ब    │  76 │ 0x94C  │ ौ   │ 108 │ 0x96C   │ ६    │
│13 │ 0x90D │ ऍ     │ 45 │ 0x92D │ भ    │  77 │ 0x94D  │ ्     │ 109 │ 0x96D   │ ७    │
│14 │ 0x90E │ ऎ     │ 46 │ 0x92E │ म    │  78 │ 0x94E  │ ॎ   │ 110 │ 0x96E   │ ८    │
│15 │ 0x90F │ ए     │ 47 │ 0x92F │ य    │  79 │ 0x94F  │ ॏ   │ 111 │ 0x96F   │ ९    │
│16 │ 0x910 │ ऐ     │ 48 │ 0x930 │ र    │  80 │ 0x950  │ ॐ    │ 112 │ 0x970   │ ॰    │
│17 │ 0x911 │ ऑ     │ 49 │ 0x931 │ ऱ    │  81 │ 0x951  │ ॑     │ 113 │ 0x971   │ ॱ    │
│18 │ 0x912 │ ऒ     │ 50 │ 0x932 │ ल    │  82 │ 0x952  │ ॒     │ 114 │ 0x972   │ ॲ    │
│19 │ 0x913 │ ओ     │ 51 │ 0x933 │ ळ    │  83 │ 0x953  │ ॓     │ 115 │ 0x973   │ ॳ    │
│20 │ 0x914 │ औ     │ 52 │ 0x934 │ ऴ    │  84 │ 0x954  │ ॔     │ 116 │ 0x974   │ ॴ    │
│21 │ 0x915 │ क     │ 53 │ 0x935 │ व    │  85 │ 0x955  │ ॕ     │ 117 │ 0x975   │ ॵ    │
│22 │ 0x916 │ ख     │ 54 │ 0x936 │ श    │  86 │ 0x956  │ ॖ     │ 118 │ 0x976   │ ॶ    │
│23 │ 0x917 │ ग     │ 55 │ 0x937 │ ष    │  87 │ 0x957  │ ॗ     │ 119 │ 0x977   │ ॷ    │
│24 │ 0x918 │ घ     │ 56 │ 0x938 │ स    │  88 │ 0x958  │ क़    │ 120 │ 0x978   │ ॸ    │
│25 │ 0x919 │ ङ     │ 57 │ 0x939 │ ह    │  89 │ 0x959  │ ख़    │ 121 │ 0x979   │ ॹ    │
│26 │ 0x91A │ च     │ 58 │ 0x93A │ ऺ     │  90 │ 0x95A  │ ग़    │ 122 │ 0x97A   │ ॺ    │
│27 │ 0x91B │ छ     │ 59 │ 0x93B │ ऻ   │  91 │ 0x95B  │ ज़    │ 123 │ 0x97B   │ ॻ    │
│28 │ 0x91C │ ज     │ 60 │ 0x93C │ ़     │  92 │ 0x95C  │ ड़    │ 124 │ 0x97C   │ ॼ    │
│29 │ 0x91D │ झ     │ 61 │ 0x93D │ ऽ    │  93 │ 0x95D  │ ढ़    │ 125 │ 0x97D   │ ॽ    │
│30 │ 0x91E │ ञ     │ 62 │ 0x93E │ ा   │  94 │ 0x95E  │ फ़    │ 126 │ 0x97E   │ ॾ    │
│31 │ 0x91F │ ट     │ 63 │ 0x93F │ ि   │  95 │ 0x95F  │ य़    │ 127 │ 0x97F   │ ॿ    │

'''

export const DEVANAGARI_CONSONANTS = (
[{pos: "velar",         cons: [क,ख,ग,घ,ङ,' '            ]},
 {pos: "palatal",       cons: [च,छ,ज,झ,ञ,' '            ]},
 {pos: "retroflex",     cons: [ट,ठ,ड,ढ,ण,' '            ]},
 {pos: "dental",        cons: [त,थ,द,ध,न,' '            ]},
 {pos: "labial",        cons: [प,फ,ब,भ,म,' '            ]},
 {pos: "unordered 1",   cons: [य,य़,र,ऱ,' ', ' '         ]},
 {pos: "unordered 2",   cons: [ल,ळ,ऴ,व,' ', ' '         ]},
 {pos: "unordered 3" ,  cons: [श,ष,स,ह,' ', ' '         ]},
 {pos: "unordered 4" ,  cons: [क्ष,' ',' ',' ',' ',' '    ]}
 ]
)

export const DEVANAGARI_VOWELS = ([
{position:  0, name:  "a", 		char: "\u{0905}", 		modifier:	""			}
{position:  1, name:  "A", 		char: "\u{0906}",		modifier:	"\u{093E}"		}
{position:  2, name:  "act", 		char: "\u{0904}",		modifier:	"\u{0945}"   		}
{position:  3, name:  "all", 		char: "\u{0912}",      		modifier:	"\u{0949}"		}	
{position:  4, name:  "i", 		char: "\u{0907}", 		modifier:	"\u{093F}" 		}
{position:  5, name:  "I", 		char: "\u{0908}", 		modifier:	"\u{0940}"		}
{position:  6, name:  "u", 		char: "\u{0909}", 		modifier:	"\u{0941}"		}
{position:  7, name:  "U", 		char: "\u{090A}", 		modifier:	"\u{0942}"		}
{position:  8, name:  "e", 		char: "\u{090D}", 		modifier:	"\u{0946}"		}
{position:  9, name:  "E", 		char: "\u{090E}", 		modifier:	"\u{0947}"		}
{position: 10, name:  "ay", 		char: "\u{0910}", 		modifier:	"\u{0948}"		}	
{position: 11, name:  "o", 		char: "\u{0912}", 		modifier:	"\u{094A}"		}
{position: 12, name:  "O", 		char: "\u{0913}", 		modifier:	"\u{094B}"		}
{position: 13, name:  "av", 		char: "\u{0914}", 		modifier:	"\u{094C}"		}
{position: 14, name:  "x", 		char: "\u{090B}", 		modifier:	"\u{0943}"		}
{position: 15, name:  "X", 		char: "\u{0960}", 		modifier:	"\u{0944}"		}
{position: 16, name:  "q", 		char: "\u{090C}", 		modifier:	"\u{0962}"		}
{position: 17, name:  "Q", 		char: "\u{0961}", 		modifier:	"\u{0963}"		}
{position: 18, name:  "anusvAra", 	char: "\u{0905}\u{0902}", 	modifier:	"\u{0902}"		}
{position: 19, name:  "visarga", 	char: "\u{0905}\u{0903}",	modifier:	"\u{0903}"		}
{position: 20, name:  "virAma", 	char: "",  			modifier:	"\u{094D}"		}
{position: 21, name:  "chandrabindu", 	char: "",  			modifier:	"\u{0901}"		}
{position: 22, name:  "avagraha", 	char: "", 	      		modifier:	"\u{093D}"		}
{position: 23, name:  "nuktha", 	char: "",  			modifier:  	"\u{093C}"		}
])


