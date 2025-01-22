{-# LANGUAGE ScopedTypeVariables #-}
module Main where

import Control.Monad ( forM_, foldM )
import Lib (greet)
import Qsortof(qsort)

main :: IO ()
main = do
  greet
  let t1 = unless 0 (==) 10 (+) 1 id -- [0,1,2,3,4,5,6,7,8,9,10]
  let t2 = unless 0 (==) 10 (+) 1 (*2) -- [0,2,4,6,8,10]
  let t3 = unless 10 (>=) 0 (-) 1 (*2) -- []
  let t4 = unless 10 (<) 0 (-) 1 (*2) -- [20,18,16,14,12,10,8,6,4,2,0]
  let t5 = unless (10.0^^20) (<) (sqrtFloat 2.0) (\x _ -> sqrtFloat x) 1 (*1) -- [1.4330126,2.053525,4.2169647,17.782793,316.22775,100000.0,1.0e10,1.0e20]
  let t6 = unless (10.0^^20) (<) 1.1 (\x _ -> sqrtFloat x) 1 (*1) -- [1.197085,1.4330126,2.053525,4.2169647,17.782793,316.22775,100000.0,1.0e10,1.0e20]

  forM_ [t1, t2, t3, t4, t5, t6] $ \t -> do
    putStrLn $ "Sort of " ++ show t ++ " is " ++ show (qsort t)

  putStrLn "Enter List of integers in [p,q,r,] format"
  inputs <- getContents
  forM_ (lines inputs) $ \aline -> do
    let input = aline
    let y :: [Int] = read input
    putStrLn $ "Sort of " ++ input ++ " is " ++ show (qsort y)
