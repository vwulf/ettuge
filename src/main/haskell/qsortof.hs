{-# LANGUAGE ScopedTypeVariables #-}

import Control.Monad
import Data.Typeable

qsort :: (Ord a) => [a] -> [a]
qsort [] = []
qsort ns = (qsort s) ++ m ++ (qsort l) where
  x = head ns
  s = [n | n <- ns, n < x]
  l = [n | n <- ns, n > x]
  m = [n | n <- ns, n == x]

main = do
  inputs <- getContents
  forM_ (lines inputs) $ \aline -> do
  let input = aline
  let y :: [Int] = read input
  putStrLn $ "Sort of " ++ input ++ " is " ++ show(qsort y)
