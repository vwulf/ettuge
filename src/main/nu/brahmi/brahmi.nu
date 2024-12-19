use table/emitters e_table_outer
use scripts/Eke EKE_CONSONANTS
use scripts/Eke EKE_VOWELS
use scripts/Ekeek EKEEK_CONSONANTS
use scripts/Ekeek EKEEK_VOWELS
use scripts/kannada KANNADA_CONSONANTS
use scripts/kannada KANNADA_VOWELS
use scripts/iso ISO_CONSONANTS
use scripts/ek EK_CONSONANTS
use scripts/ek EK_VOWELS
use scripts/brahmi BRAHMI_CONSONANTS
use scripts/brahmi BRAHMI_VOWELS
use scripts/devanAgari DEVANAGARI_CONSONANTS
use scripts/devanAgari DEVANAGARI_VOWELS
use scripts/grantha GRANTHA_CONSONANTS
#use scripts/grantha GRANTHA_VOWELS


let $positions = ([
	"velar", 
	"palatal",
	"retroflex",
	"dental",
	"labial",
	"unordered 1",
	"unordered 2",
	"unordered 3",
	"unordered 4"
])

let $scrnames = ([
	"Eke",
	"ISO",
	"kannaDa",
	"ellara kannaDa",
	"Eke(ek)",
	"brAhmi",
	"devanAgari",
	"grantha"
])



let $scrs = ([
    {name: "Eke", hal: "", rows: $EKE_CONSONANTS}, 
    {name: "ISO", hal: "", rows: $ISO_CONSONANTS}, 
    {name: "kannaDa", hal: "\u{0CCD}", rows: $KANNADA_CONSONANTS},
    {name: "ellara kannaDa", hal: "\u{0CCD}",
            hal1: "\u{200D}" , hal1c:"ರ",
            hal2cs: [ಙ, ಞ],
            hal2csby: { velar:          {before:    'ಂ',   after: {ಙ:'ನ್ಗ', ಞ: 'ನ್ಯ'}}
                        palatal:        {before:    'ಂ',   after: {ಙ:'ನ್ಗ', ಞ: 'ನ್ಯ'}}
                        retroflex:      {before:    'ಂ',   after: {ಙ:'ನ್ಗ', ಞ: 'ನ್ಯ'}}
                        dental:         {before:    'ಂ',   after: {ಙ:'ನ್ಗ', ಞ: 'ನ್ಯ'}}
                        labial:         {before:    'ಂ',   after: {ಙ:'ನ್ಗ', ಞ: 'ನ್ಯ'}}
                        "unordered 1":  {before:    'ಂ',   after: {ಙ:'ನ್ಗ', ಞ: 'ನ್ಯ'}}
                        "unordered 2":  {before:    'ಂ',   after: {ಙ:'ನ್ಗ', ಞ: 'ನ್ಯ'}}
                        "unordered 3":  {before:    'ಂ',   after: {ಙ:'ನ್ಗ', ಞ: 'ನ್ಯ'}}
                        "unordered 4":  {before:    'ಂ',   after: {ಙ:'ನ್ಗ', ಞ: 'ನ್ಯ'}}
                        },
            rows: $EK_CONSONANTS},
    {name: "Eke(ek)", hal: "", 
            hal2cs: [G, Y],
            hal2csby: { velar:          { before:  'n', after: { G: 'ng',  Y: 'ny' }}
                        palatal:        { before:  'n', after: { G: 'ng',  Y: 'ny' }}
                        retroflex:      { before:  'n', after: { G: 'ng',  Y: 'ny' }}
                        dental:         { before:  'n', after: { G: 'ng',  Y: 'ny' }}
                        labial:         { before:  'm', after: { G: 'ng',  Y: 'ny' }}
                        "unordered 1":  { before:  'm', after: { G: 'ng',  Y: 'ny' }}
                        "unordered 2":  { before:  'n', after: { G: 'ng',  Y: 'ny' }}
                        "unordered 3":  { before:  'm', after: { G: 'ng',  Y: 'ny' }}
                        "unordered 4":  { before:  'n', after: { G: 'ng',  Y: 'ny' }}
                        },
            rows: $EKEEK_CONSONANTS}, 
    {name: "brAhmi", hal: "\u{11046}", rows: $BRAHMI_CONSONANTS},
    {name: "devanAgari", hal: "\u{094D}", rows: $DEVANAGARI_CONSONANTS},
    {name: "grantha", hal: "\u{1134D}", rows: $GRANTHA_CONSONANTS}
])

mut t1 = []
(for p in $positions
{
    mut t2 = []
    #print $p
    (for rc in 0..5
    {
        mut t3 = []
        (for scrn in $scrnames
        {
            mut t4 = []
            #print $scrn
            let scr = ($scrs |
			where {|x| $x.name == $scrn} |
                        get 0)
            let row = ($scr.rows |
			where {|x| $x.pos == $p} |
			get 0)
            let consonant = ($row.cons |
			      get $rc)
            #print $consonant
            let consonantname = if ($consonant == ' ') {
                ""
            } else {
                $"($consonant)($scr.hal)"
            }
            (for r in $scr.rows
            {
                mut t5 = []
                (for c in $r.cons
                {
                   if (($consonant != ' ') and
			($c != ' ')) {
                        let hal1 = ($scr |
				     default "" hal1).hal1
                        let hal1c = ($scr |
				      default "" hal1c).hal1c
                        let hal2cs = ($scr |
			 	       default [] hal2cs).hal2cs
                        let hal2csby = ($scr |
 					 default {} hal2csby).hal2csby
                        let halfind = ($hal2cs |
					any {|e| (
					 ($e == $consonant) or
					 ($e == $c)
                                        )})
                        #print $"hal2cs ($halfind) ($consonant) ($c) ($hal2cs)"

                        let l = if (($hal2cs != []) and ($halfind)) {
                            #print $"hal2cs ($hal2cs)"
                            let pos = $r.pos
                            let morn = (($hal2csby | default "" ($pos)) | get ($pos))

                            #print $"hal2cs cochl: ($consonant)($scr.hal)($c)($scr.hal) pos: ($pos) morn: ($morn) comh: ($consonant)($morn.before)($scr.hal) mcoh: ($morn.before)($consonant)($scr.hal) chm: ($c)($scr.hal)($morn.before) mch: ($morn.before)($c)($scr.hal)"

                            if (($hal2cs | any {|e| ($e == ($c))}) and 
				($rc == 4) and 
				($hal2cs | any {|e| ($e == ($consonant))})) {
                            #    print $"($morn.before)($morn.after | get ($c))($scr.hal)"
                            #    $"($morn.before)   "
                                 $"($morn.before)($morn.after | get ($c))($scr.hal)"
                            } else if ($hal2cs | any {|e| ($e == ($consonant))}) {
                                $"($morn.before)($c)($scr.hal)"
                            } else if (($hal1 != "") and
					($hal1c == $consonant)) {
                                $"($consonant)($scr.hal)($hal1)($morn.after | get ($c))($scr.hal)"
                            } else {
                                #print $"hal2cs after: ($morn.after | get ($c)) "
                                $"($consonant)($scr.hal)($morn.after | get ($c))($scr.hal)"
                            }
                        } else if (($hal1 != "") and
				   ($hal1c == $consonant)) {
                            $"($consonant)($scr.hal)($hal1)($c)($scr.hal)   "
                        } else {
                            $"($consonant)($scr.hal)($c)($scr.hal)   "
                        }
                        #print -n $"($l)"
                        $t5 = ($t5 | append $l)
                    } else {
                        $t5 = ($t5 | append ' ') 
                    }
                })
                #print t5 $t5
                $t4 = ($t4 | append {name: "t4",
				     span: ($t5 | length),
                                     t5: $t5})
                #print t4 $t4
            })
            $t3 = ($t3 | append {name: "t3",
				 span: ($t4 | length), 
				 script: ($scr.name),
				 consonant: $consonantname,
				 t4: $t4})
            #print t3 $t3 
        })
        $t2 = ($t2 | append {name: "t2",
			     span: ($t3 | length),
                             rc: $rc,
                             t3: $t3})
        #print $t2
    })
    $t1 = ($t1 | append {name: "t1",
			 span: ($t2 | length), 
			 p: $p, t2: $t2})
    #print -r $t1
    #print ($t1 | to md)
})



let scrnamesv = (["Eke",
# "ISO",
 "kannaDa",
 "ellara kannaDa",
 "Eke(ek)",
 "brAhmi",
 "devanAgari",
# "grantha" 
])


let scrvs = ([
    {name: "Eke", rows: $EKE_VOWELS}, 
#    {name: "ISO", rows: $ISO_VOWELS}, 
    {name: "kannaDa", rows: $KANNADA_VOWELS},
    {name: "ellara kannaDa", rows: $EK_VOWELS},
    {name: "Eke(ek)", rows: $EKEEK_VOWELS}, 
    {name: "brAhmi", rows: $BRAHMI_VOWELS},
    {name: "devanAgari", hal: "\u{094D}", rows: $DEVANAGARI_VOWELS},
#    {name: "grantha", hal: "\u{1134D}", rows: $GRANTHA_VOWELS}
])

mut v1 = []
(for p in $positions
{
    mut v2 = []
    #print $p
    (for rc in 0..5
    {
        mut v3 = []
        (for scrn in ($scrnamesv)
        {
            mut v41 = []
            mut v42 = []
            #print $scrn
            let scr = ($scrs |
		        where {|x| $x.name == $scrn} |
			get 0)
            let row = ($scr.rows |
			where {|x| $x.pos == $p} |
			get 0)
	    let a = $row.cons | get $rc
	    let hal2cs = ($scr |
			   default [] hal2cs).hal2cs
	    let hal2csby = ($scr |
			   default {} hal2csby).hal2csby
	    let halfind = ($hal2cs | any {|e| (($e == $a))})
            let morn = (($hal2csby |
			  default "" ($row.pos)) |
			 get ($row.pos))
            let akSara = if ($halfind) {
           	$"($morn.after | get ($a))"
	    } else {
		($a)
            }

            #print $akSara
            (for s in ($scrvs |
			filter {|i| ($i.name == $scrn)})
            {
            	mut v5 = []

		(for v in $s.rows
		{
		    if (($akSara != "") and ($v.char != "")) {
			 let l = $"($v.char)"
			 # print -n $"($l)"
			 $v5 = ($v5 | append $l)
		    } else if ($v.modifier != "" ) {
			 $v5 = ($v5 | append ($v.modifier)) 
		    } else {
			 $v5 = ($v5 | append ($v.name)) 
		    }
		})
                $v41 = ($v41 | append {name: "v4",
				       span: ($v5 | length),
                                       v5: $v5})
		#print v5 $v5
            	mut v6 = []

		(for v in $s.rows
		{
		    if (($akSara != ' ') and ($v != ' ')) {
			 let l = $"($akSara)($v.modifier) "
			 # print -n $"($l)"
			 $v6 = ($v6 | append $l)
		    } else {
			 $v6 = ($v6 | append ' ') 
		    }
		})
		#print v6 $v6
                $v42 = ($v42 | append {name: "v4",
				       span: ($v6 | length),
                                       v6: $v6})
            })
            #print v4 $v4
            $v3 = ($v3 | append {name: "v3",
			 	 span: ($v41 | length),
				 script: ($scr.name),
				 akSara: "Vowel",
				 v41: $v41})
            $v3 = ($v3 | append {name: "v3",
				 span: ($v42 | length),
				 script: ($scr.name),
				 akSara: $akSara,
				 v42: $v42})
        })
        #print v3 $v3 
        $v2 = ($v2 | append {name: "v2",
 			     span: ($v3 | length),
			     rc: $rc,
			     v3: $v3})
    })
    #print $v2
    $v1 = ($v1 | append {name: "v1",
 			 span: ($v2 | length),
			 p: $p,
			 v2: $v2})
})

let corv = "c"

if ($corv == "c") {
    '''
    Consonant cluster tables
    '''
    print "== Consonant Clusters / ottakSaragaLu =="
    e_table_outer $t1
} else {
    '''
    Consonant vowel combination tables
    '''
    print "== Consonant Vowel combinations / akSaragaLu =="
    e_table_outer $v1
}
