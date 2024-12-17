"" | save -f ott.txt
(for $i in [ಕ,ಖ,ಗ,ಘ,ಙ,ಚ,ಛ,ಜ,ಝ,ಞ,ಟ,ಠ,ಡ,ಢ,ಣ,ತ,ಥ,ದ,ಧ,ನ,ಪ,ಫ,ಬ,ಭ,ಮ,ಯ,ರ,ಱ,ಲ,ಳ,ವ,ಶ,ಷ,ಸ,ಹ,ೞ]
#(for $i in [ಕ,ಖ,ಗ]
{
    (for $j in [ಕ,ಖ,ಗ,ಘ,ಙ,ಚ,ಛ,ಜ,ಝ,ಞ,ಟ,ಠ,ಡ,ಢ,ಣ,ತ,ಥ,ದ,ಧ,ನ,ಪ,ಫ,ಬ,ಭ,ಮ,ಯ,ರ,ಱ,ಲ,ಳ,ವ,ಶ,ಷ,ಸ,ಹ,ೞ]
    #(for $j in [ಕ,ಖ,ಗ]
    {
        let k = "alar-212-sorted-uniq-2.txt-" + $"($i)" + ".txt" ;
        let l =  $"($i)್($j)" ;
        let m = $"s/($l)/~/g";
        $l | save --append -f ott.txt;
        cat $k | sed $"($m)" | grep "~" | wc -l | save --append -f ott.txt;
        print -n $"($l)";
    };
    )
})
