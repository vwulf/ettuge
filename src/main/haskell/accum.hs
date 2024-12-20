app :: Char -> Char -> [Char]
app a b = a : [b]

--import Data.Maybe( Maybe(Nothing))
--data InvF = Maybe(Nothing)
--data NonNf a = Maybe a

--fn :: (Maybe a) -> Int
--fn x = 0

-- https://wiki.haskell.org/Fold
-- fold paper

type Res = [Char]
type Lft = [Char]
type Rgt = [Char]
data Accum = {res :: Res, lft :: Lft}

top :: Accum -> Rgt -> Accum
top acc rgt =
  let result = res acc
  let lft = lft acc
  next | next == LFT = {result:: (head lft), (tail lft), RGT}
       | next == RGT = {result:: (head rgt), lft, LFT}
  

main = do
  let r = zipWith app "2000" "2000"
  let s = foldl (++) "" r
  let merge = foldl . top
  let s1 = merge {"", "2000"} "2000"
  print s
