{-# LANGUAGE ScopedTypeVariables #-}

import Control.Monad ( forM_ )
import Data.Monoid ()
import Data.Typeable ()
import Data.List ( foldl', unfoldr )
import GHC.Float (sqrtDouble, sqrtFloat)
import qualified Data.Bifunctor (first, second)
import Data.Bifunctor (Bifunctor(first), Bifunctor(second), Bifunctor (bimap))
import Debug.Trace (traceShow)

qsort :: (Ord a) => [a] -> [a]
qsort [] = []
qsort elems = qsort lt ++ eq ++ qsort gt where
  pivot = head elems
  emptysml = (mempty, mempty, mempty)
  (lt, eq, gt) = foldr (\ elem (lt, eq, gt) ->
                  if elem < pivot
                    then (elem:lt, eq, gt)
                  else if elem == pivot
                    then (lt, elem:eq, gt)
                  else
                    (lt, eq, elem:gt)
                  ) emptysml elems

unless :: (Ord b) => b ->
                     (b -> b -> Bool) ->
                     b ->
                     (b -> b -> b) ->
                     b ->
                     (b -> a) ->
                     [a]
unless counter reaches end step init f =
  unfoldr (tillcount reaches end step init f) counter where
  tillcount :: (b -> b -> Bool) ->
               b ->
               (b -> b -> b) ->
               b ->
               (b -> a) ->
               b ->
               Maybe (a, b)
  tillcount reaches end step init f counter =
    if counter `reaches` end
    then Nothing
    else Just (f counter, counter `step` init)

qsel :: (Show a, Ord a, Show b, Ord b, Num b) => [a] -> b -> [a]
qsel elems k = qsel' elems k 0 where
  qsel' :: (Show a, Ord a, Show b, Ord b, Num b) => [a] -> b -> b -> [a]
  qsel' [] k off = []
  qsel' elems k off = 
    --traceShow("pivot: ", pivot, "k: ", k, "off: ", off, "ltc: ", ltc, "eqc: ", eqc, "gtc: ", gtc)
    (if k < ltc then
       qsel' ltl k off
    else ltl) ++
     eql ++
     (if k >= ltc + eqc then
        qsel' gtl k (off + ltc + eqc)
     else []) where
    pivot = head elems
    emptysml = ((mempty, 0), (mempty, 0), (mempty, 0))
    filt x po =
       if k >= off + po then x else ([], 0)
    (lt, eq, gt) =
       foldr (\elem (lt, eq, gt) ->
          let (ltl, eql, gtl) = (fst lt, fst eq, fst gt)
              (ltc, eqc, gtc) = (snd lt, snd eq, snd gt) in
          if elem < pivot
            then
              let ltc' = ltc + 1
                  eqpo = ltc'
                  gtpo = ltc' + eqc
                  in
              (filt (elem:ltl, ltc') 0,
               filt eq eqpo,
               filt gt gtpo)
          else if elem == pivot
            then
              let eqc' = eqc + 1
                  eqpo = ltc
                  gtpo = ltc + eqc' in
              (filt lt 0,
               filt (elem:eql, eqc') eqpo,
               filt gt gtpo)
          else
            let gtc' = gtc + 1
                eqpo = ltc
                gtpo = ltc + eqc in
            (filt lt 0,
             filt eq eqpo,
             filt (elem:gtl, gtc') gtpo)
          ) emptysml elems
    (ltl, eql, gtl) = (fst lt, fst eq, fst gt)
    (ltc, eqc, gtc) = (snd lt, snd eq, snd gt)



main :: IO ()
main = do
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
