{-# LANGUAGE ScopedTypeVariables #-}

import Control.Monad
import Data.Typeable

qsort :: (Ord a) => [a] -> [a]
qsort [] = []
qsort ns = (qsort s) ++ m ++ (qsort l) where
  x = head ns
  (s, m, l) = foldl (\(s, m, l) e ->
                  if e < x then (e:s, m, l)
                  else if e == x then (s, e:m, l) 
                  else (s, m, e:l)) ([],[],[]) ns

main = do
  putStrLn $ "Enter List of integers in [p,q,r,] format"
  inputs <- getContents
  forM_ (lines inputs) $ \aline -> do
    let input = aline
    let y :: [Int] = read input
    putStrLn $ "Sort of " ++ input ++ " is " ++ show(qsort y)
