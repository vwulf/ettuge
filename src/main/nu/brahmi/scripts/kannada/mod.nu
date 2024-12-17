const internal_ref = '''
│   0 │ 0xC80   │ ಀ    │  32 │ 0xCA0   │ ಠ    │	 64 │ 0xCC0   │ ೀ   │  96 │ 0xCE0   │ ೠ    │ 
│   1 │ 0xC81   │ ಁ     │  33 │ 0xCA1   │ ಡ    │  65 │ 0xCC1   │ ು    |  97 │ 0xCE1   │ ೡ    │
│   2 │ 0xC82   │ ಂ   |  34 │ 0xCA2   │ ಢ    │  66 │ 0xCC2   │ ೂ    │  98 │ 0xCE2   │ ೢ     │
│   3 │ 0xC83   │ ಃ   |  35 │ 0xCA3   │ ಣ    │  67 │ 0xCC3   │ ೃ    │  99 │ 0xCE3   │ ೣ     │
│   4 │ 0xC84   │ ಄    │  36 │ 0xCA4   │ ತ    │  68 │ 0xCC4   │ ೄ    │ 100 │ 0xCE4   │ ೤    │
│   5 │ 0xC85   │ ಅ    │  37 │ 0xCA5   │ ಥ    │  69 │ 0xCC5   │ ೅     │ 101 │ 0xCE5   │ ೥    │
│   6 │ 0xC86   │ ಆ    │  38 │ 0xCA6   │ ದ    │  70 │ 0xCC6   │ ೆ      │ 102 │ 0xCE6   │ ೦    │
│   7 │ 0xC87   │ ಇ    │  39 │ 0xCA7   │ ಧ    │  71 │ 0xCC7   │ ೇ   │ 103 │ 0xCE7   │ ೧    │
│   8 │ 0xC88   │ ಈ    │  40 │ 0xCA8   │ ನ    │  72 │ 0xCC8   │ ೈ   │ 104 │ 0xCE8   │ ೨    │
│   9 │ 0xC89   │ ಉ    │  41 │ 0xCA9   │ ಩    │  73 │ 0xCC9   │ ೉     │ 105 │ 0xCE9   │ ೩    │
│  10 │ 0xC8A   │ ಊ    │  42 │ 0xCAA   │ ಪ    │  74 │ 0xCCA   │ ೊ   │ 106 │ 0xCEA   │ ೪    │
│  11 │ 0xC8B   │ ಋ    │  43 │ 0xCAB   │ ಫ    │  75 │ 0xCCB   │ ೋ  | 107 │ 0xCEB   │ ೫    │
│  12 │ 0xC8C   │ ಌ    │  44 │ 0xCAC   │ ಬ    │  76 │ 0xCCC   │ ೌ      │ 108 │ 0xCEC   │ ೬    │
│  13 │ 0xC8D   │ ಍    │  45 │ 0xCAD   │ ಭ    │  77 │ 0xCCD   │ ್      │ 109 │ 0xCED   │ ೭    │
│  14 │ 0xC8E   │ ಎ    │  46 │ 0xCAE   │ ಮ    │  78 │ 0xCCE   │ ೎     │ 110 │ 0xCEE   │ ೮    │
│  15 │ 0xC8F   │ ಏ    │  47 │ 0xCAF   │ ಯ    │  79 │ 0xCCF   │ ೏     │ 111 │ 0xCEF   │ ೯    │
│  16 │ 0xC90   │ ಐ    │  48 │ 0xCB0   │ ರ    │  80 │ 0xCD0   │ ೐     │ 112 │ 0xCF0   │ ೰    │
│  17 │ 0xC91   │ ಑    │  49 │ 0xCB1   │ ಱ    │  81 │ 0xCD1   │ ೑     │ 113 │ 0xCF1   │ ೱ    │
│  18 │ 0xC92   │ ಒ    │  50 │ 0xCB2   │ ಲ    │  82 │ 0xCD2   │ ೒     │ 114 │ 0xCF2   │ ೲ    │
│  19 │ 0xC93   │ ಓ    │  51 │ 0xCB3   │ ಳ    │  83 │ 0xCD3   │ ೓     │ 115 │ 0xCF3   │ ೳ    │
│  20 │ 0xC94   │ ಔ    │  52 │ 0xCB4   │ ಴    │  84 │ 0xCD4   │ ೔     │ 116 │ 0xCF4   │ ೴    │
│  21 │ 0xC95   │ ಕ    │  53 │ 0xCB5   │ ವ    │  85 │ 0xCD5   │ ೕ    │ 117 │ 0xCF5   │ ೵    │
│  22 │ 0xC96   │ ಖ    │  54 │ 0xCB6   │ ಶ    │  86 │ 0xCD6   │ ೖ    │ 118 │ 0xCF6   │ ೶    │
│  23 │ 0xC97   │ ಗ    │  55 │ 0xCB7   │ ಷ    │  87 │ 0xCD7   │ ೗     │ 119 │ 0xCF7   │ ೷    │
│  24 │ 0xC98   │ ಘ    │  56 │ 0xCB8   │ ಸ    │  88 │ 0xCD8   │ ೘     │ 120 │ 0xCF8   │ ೸    │
│  25 │ 0xC99   │ ಙ    │  57 │ 0xCB9   │ ಹ    │  89 │ 0xCD9   │ ೙     │ 121 │ 0xCF9   │ ೹    │
│  26 │ 0xC9A   │ ಚ    │  58 │ 0xCBA   │ ಺    │  90 │ 0xCDA   │ ೚     │ 122 │ 0xCFA   │ ೺    │
│  27 │ 0xC9B   │ ಛ    │  59 │ 0xCBB   │ ಻    │  91 │ 0xCDB   │ ೛     │ 123 │ 0xCFB   │ ೻    │
│  28 │ 0xC9C   │ ಜ    │  60 │ 0xCBC   │ ಼     │  92 │ 0xCDC   │ ೜     │ 124 │ 0xCFC   │ ೼    │
│  29 │ 0xC9D   │ ಝ    │  61 │ 0xCBD   │ ಽ    │  93 │ 0xCDD   │ ೝ     │ 125 │ 0xCFD   │ ೽    │
│  30 │ 0xC9E   │ ಞ    │  62 │ 0xCBE   │ ಾ   │  94 │ 0xCDE   │ ೞ     │ 126 │ 0xCFE   │ ೾    │
│  31 │ 0xC9F   │ ಟ    │  63 │ 0xCBF   │ ಿ     │  95 │ 0xCDF   │ ೟     │ 127 │ 0xCFF   │ ೿    │

'''

export const KANNADA_CONSONANTS = (
[{pos: "velar",         cons: [ಕ,ಖ,ಗ,ಘ,ಙ, ' '           ]},
 {pos: "palatal",       cons: [ಚ,ಛ,ಜ,ಝ,ಞ, ' '           ]},
 {pos: "retroflex",     cons: [ಟ,ಠ,ಡ,ಢ,ಣ,  ' '          ]},
 {pos: "dental",        cons: [ತ,ಥ,ದ,ಧ,ನ, ' '           ]},
 {pos: "labial",        cons: [ಪ,ಫ,ಬ,ಭ,ಮ,, ' '          ]},
 {pos: "unordered 1",   cons: [ಯ ,' ' ,ರ,ಱ,' ',' '      ]},
 {pos: "unordered 2",   cons: [ಲ,ಳ,ೞ,ವ, ' ' ,  ' '      ]},
 {pos: "unordered 3" ,  cons: [ಶ,ಷ,ಸ,ಹ, ' ' ,  ' '      ]},
 {pos: "unordered 4" ,  cons: [' ',' ',' ',' ',' ',' '  ]}
 ]
)

export const KANNADA_VOWELS = ([
{position:  0, name:  "a", 		char: "\u{0C85}", 		modifier:	""			}
{position:  1, name:  "A", 		char: "\u{0C86}",		modifier:	"\u{0CBE}"		}
{position:  2, name:  "act", 		char: "\u{0C85}\u{0CBC}",	modifier:	"\u{0CBC}"   		}
{position:  3, name:  "all", 		char: "\u{0C86}\u{0CBC}",      	modifier:	"\u{0CBC}\u{0CBE}"	}	
{position:  4, name:  "i", 		char: "\u{0C87}", 		modifier:	"\u{0CBF}" 		}
{position:  5, name:  "I", 		char: "\u{0C88}", 		modifier:	"\u{0CC0}"		}
{position:  6, name:  "u", 		char: "\u{0C89}", 		modifier:	"\u{0CC1}"		}
{position:  7, name:  "U", 		char: "\u{0C8A}", 		modifier:	"\u{0CC2}"		}
{position:  8, name:  "e", 		char: "\u{0C8E}", 		modifier:	"\u{0CC6}"		}
{position:  9, name:  "E", 		char: "\u{0C8F}", 		modifier:	"\u{0CC7}"		}
{position: 10, name:  "ay", 		char: "\u{0C90}", 		modifier:	"\u{0CC8}"		}	
{position: 11, name:  "o", 		char: "\u{0C92}", 		modifier:	"\u{0CCA}"		}
{position: 12, name:  "O", 		char: "\u{0C93}", 		modifier:	"\u{0CCB}"		}
{position: 13, name:  "av", 		char: "\u{0C94}", 		modifier:	"\u{0CCC}"		}
{position: 14, name:  "x", 		char: "\u{0C8B}", 		modifier:	"\u{0CC3}"		}
{position: 15, name:  "X", 		char: "\u{0CE0}", 		modifier:	"\u{0CC4}"		}
{position: 16, name:  "q", 		char: "\u{0C8C}", 		modifier:	"\u{0CE2}"		}
{position: 17, name:  "Q", 		char: "\u{0CE1}", 		modifier:	"\u{0CE3}"		}
{position: 18, name:  "anusvAra", 	char: "\u{0C85}\u{0C82}", 	modifier:	"\u{0C82}"		}
{position: 19, name:  "visarga", 	char: "\u{0C85}\u{0C83}",	modifier:	"\u{0C83}"		}
{position: 20, name:  "virAma", 	char: "",  			modifier:	"\u{0CCD}"		}
{position: 21, name:  "chandrabindu", 	char: "",  			modifier:	"\u{0C8D}"		}
{position: 22, name:  "avagraha", 	char: "", 	      		modifier:	"\u{0CBD}"		}
{position: 23, name:  "nuktha", 	char: "",  			modifier:  	"\u{0CBC}"		}
])

