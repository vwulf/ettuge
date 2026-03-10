data Tree a = Branch (Tree a) a (Tree a) |
              Empty
    deriving (Read, Show, Eq)

instance Foldable Tree where
    foldMap :: Monoid m => (a -> m) -> t a -> m 

{--
 - ((), N, ())
 -  (, N, )
 -  ((), N, )
 -  (, N, ())
 --}
 {--
  - #x: #l, 10, #r
  - #l: #ll, 100,
  - #r: , 20, #rr
  - #rr: , 30 ,
  - #ll: , 40,
  -
  -

main 
    inputs <- getContents
