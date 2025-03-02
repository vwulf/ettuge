{-# LANGUAGE ScopedTypeVariables #-}
{-# LANGUAGE LambdaCase #-}
module Main where

import GHC.Float (sqrtDouble, sqrtFloat)
import Control.Monad ( forM_, foldM )
import Lib (greet)
import Qsortof(qsort, unless, qsel)

import Data.Functor.Foldable (refold)
import qualified Data.Foldable as List
import qualified Data.Foldable as Int
import qualified Data.List as List
import Debug.Trace (traceShow, trace)
import GHC.Natural
import Data.Fixed (Nano)
import Control.Monad.Fix (fix)
import Control.Concurrent


f :: Int -> Int -> Int
f x sum =
  let
    m = x `mod` 10
    sum' = sum + m
    x' = x `div` 10
  in
    if x' == 0
      then sum'
      else f x' sum'

g :: Int -> [Int]
g x =
  let
    m = x `mod` 10
    x' = x `div` 10
  in
    if x' == 0
      then [m]
      else m : g x'

h :: Natural -> [Natural]
h x
  | x == 0 = [m]
  | otherwise = m : h (x `div` 10)
  where
    m = x `mod` 10

s :: Natural -> Natural
s = refold List.sum h

i :: Natural -> [Natural]
i = fix (\f x ->
      let m = (x `mod` 10) in
      case x of
        0 ->
          traceShow ("m", m)
          []
        _ ->
          traceShow (m, x `div` 10)
          m : f (x `div` 10))

j :: Natural -> Maybe (Natural, Natural)
j x = case x of
   0 -> Nothing
   x -> Just (x `mod` 10, x `div` 10)
{--
sumd :: Natural -> Natural
sumd = refold List.sum $ fix (\f x ->
    let m = (x `mod` 10) in
      case x of
        0 -> 
          traceShow ("m", m) 
          []
        _ ->
          traceShow (m, x `div` 10) 
          m : f (x `div` 10))
--}

l1 :: Maybe (Natural, Natural) -> Maybe Natural
l1 = fmap fst

l = l1 . j

sum1 = sum . fst

sumd :: Natural -> Natural
sumd = refold sum1 (\case
  0 -> [] 
  x ->
    let x' = x `mod` 10 in
      traceShow ("x: ", x)
      [(x', x `div` 10)])

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
