const span = 6
const nested = false 

const e_name_list = ([
	"t2",
	"t3",
 	"v2",
	"v3"
])

def e_rec_beg [colspan x] {
    print ""
    print "|-"
    print -n $"| colspan = \"($span)\" | "
    #print -n $"| colspan = \"($x)\" | "
}

def e_rec_bef_field [] {
    print -n " || "
}

def e_rec_aft_field [] {
}

def e_rec_end [] {
    print ""
}

def e_record [r1 outer] {
    let r1t = ($r1 | describe)
    let x = ($r1 | default "1" span).span
    let nm = ($r1 | default "" name).name 
    if ($nested or
	$outer or
 	($e_name_list |
	 any {|e| $e == $nm})) {
        e_rec_beg $span $x
    }
    ($r1 |
      reject -i span |
      reject -i name |
      values |
      each {|field|
        e_rec_bef_field
        e_field $field false
        e_rec_aft_field
      })
    if ($nested or
	$outer or
        ($e_name_list |
          any {|e| $e == $nm})) {
        e_rec_end
    }
}

def e_list [l1] {
    let l1t = $l1 | describe
    if ($nested) {
        print ""
        print "|-"
        print -n "| "
    }
    ($l1 |
      each {|field|
        e_field $field false
        print -n " || "
      })
    if ($nested) {
        print ""
    }
}

def e_table [t1 outer] {
    let t1t = $t1 | describe
    if ($nested or $outer) {
        print ""
        print "|-"
        print -n "| "
    }
    $t1 | each {|row|
        if ($outer and not $nested) {
            print ""
            print "|-"
            print -n "| "
        }
        e_field $row $outer
        if ($nested or $outer) {
            print ""
        }
    }
    if ($nested or $outer) {
        print ""
    }
}

def e_field [f1 outer] {
    let f1t = ($f1 | describe)
    let e_fieldtype = ($f1t | split row '<' | get 0) 
    #print "FIELD: " $f1t $e_fieldtype
    match ($e_fieldtype) {
        "list" => {e_list $f1}
        "record" => {e_record $f1 $outer}
        "table" => {e_table $f1 $outer}
        _ => {print -n $f1}
    }
}

export def e_table_outer [tbl] {
    let outer = true
    print "{| class=\"wikitable Unicode\" style=\"text-align:center; font-size:100%;\""
    print "|-"
    print -n "| "
    e_table $tbl $outer 
    print "|}"
}
