import Control.Monad

{- https://twitter.com/fermatslibrary/status/1089519916049485824?s=21 -}

{-
https://math.stackexchange.com/questions/296102/fastest-square-root-algorithm
-}

-- Helper function that does all the work
sqrh :: (Floating a, Ord a) => a -> a -> a -> a
sqrh y p x =
  let d = y - x^2 in
    if (abs d) < p then
      x
    else
      let g' = x + d / (2*x) in
        sqrh y p g'

-- Catch corner cases
sqrp :: (Floating a, Ord a) => a -> a -> (Maybe a)
sqrp y p =
  if (y < 0 || p == 0.0) then Nothing
  else 
    Just $ sqrh y (abs p) (y/2)

-- Fix precision to avoid repeating
sqr y = sqrp y 0.00000000001

{- 
https://stackoverflow.com/questions/13426417/how-do-i-re-write-a-haskell-function-of-two-argument-to-point-free-style
https://stackoverflow.com/questions/12409572/pointfree-composition-with-multiple-variables
using a closure, the param y can be implied.
sqrp = \y -> sqrp y 0.01
-}

main = do
  inputs <- getContents
  forM_ (lines inputs) $ \aline -> do
  let input = aline
  let y = read input
  putStrLn $ "Sqrt of " ++ input ++ " is " ++ show(sqr y)
