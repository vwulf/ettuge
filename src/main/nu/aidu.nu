# print 5 letter kannada words from alar
$env.vowel = "[ಅ|ಆ|ಇ|ಈ|ಉ|ಊ|ಋ|ಎ|ಏ|ಐ|ಒ|ಓ|ಔ]"
$env.vowelend = "[ಂ|಼|ಃ]"
$env.cons = "[ಕ|ಖ|ಗ|ಘ|ಙ|ಚ|ಛ|ಜ|ಝ|ಞ|ಟ|ಠ|ಡ|ಢ|ಣ|ತ|ಥ|ದ|ಧ|ನ|ಪ|ಫ|ಬ|ಭ|ಮ|ಯ|ರ|ಱ|ಲ|ಳ|ವ|ಶ|ಷ|ಸ|ಹ|ೞ]"
$env.consend = "[ಾ|ಿ|ೀ|ು|ೂ|ೃ|ೆ|ೇ|ೈ|ೊ|ೋ|ೌ|ಂ|ಃ|಼|ೱ]?"
$env.hal = "[್]"
$env.vowelfull = $env.vowel + $env.vowelend
$env.consnooth = $env.cons + $env.consend
$env.consotth1 = $env.cons + $env.hal + $env.cons + $env.consend
$env.consotth2 = $env.cons + $env.hal + $env.cons + $env.hal + $env.cons + $env.consend
$env.block = $"\(\(($env.vowelfull)\)|\(($env.consnooth)\)|\(($env.consotth1)\)|\(($env.consotth2)\)\)"
egrep $"\^($env.block){5}[್]?\$" ~/alar-212-sorted-uniq-2.txt 
