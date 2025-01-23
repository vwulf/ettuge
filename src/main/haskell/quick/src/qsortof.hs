{-# LANGUAGE InstanceSigs #-}
{-# LANGUAGE FlexibleContexts #-}
{-# LANGUAGE ScopedTypeVariables #-}
{-# LANGUAGE OverloadedRecordDot #-}
module Qsortof where
import Data.Monoid ()
import Data.Typeable ()
import Data.List ( foldl', unfoldr )
import Data.Bifunctor (Bifunctor(first), Bifunctor(second), Bifunctor (bimap))
import Data.Biapplicative (Biapplicative (bipure), Biapplicative ((<<*>>)))
import Debug.Trace (traceShow)
import Data.Maybe (listToMaybe, fromMaybe)


qsort :: (Ord a) => [a] -> [a]
qsort [] = []
qsort elems = qsort lt ++ eq ++ qsort gt where
  pivot = head elems
  emptysml = (mempty, mempty, mempty)
  (lt, eq, gt) = foldl' (\ (lt, eq, gt) elem ->
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

qsort1 :: (Show a, Ord a, Show b, Ord b, Num b) => [a] -> b -> [a]
qsort1 elems k = qsort1' elems k 0 where
  qsort1' :: (Show a, Ord a, Show b, Ord b, Num b) => [a] -> b -> b -> [a]
  qsort1' [] k off = []
  qsort1' elems k off =
    --traceShow("pivot: ", pivot, "k: ", k, "off: ", off, "ltc: ", ltc, "eqc: ", eqc, "gtc: ", gtc)
    (if k < ltc then
       qsort1' ltl k off
    else ltl) ++
     eql ++
     (if k >= ltc + eqc then
        qsort1' gtl k (off + ltc + eqc)
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

data H a b = H {
  h_lst :: [a],
  h_cnt :: b,
  h_min :: Maybe a,
  h_max :: Maybe a,
  h_wmid :: Maybe a,
  h_sum :: Maybe a
} deriving (Ord, Eq, Show)

instance (Ord a, Integral a, Num b, Ord b) => Semigroup (H a b) where
  (<>) :: H a b -> H a b -> H a b
  h1 <> h2 = let
    h_min_ = maybeOp min h1.h_min h2.h_min
    h_max_ = maybeOp max h1.h_max h2.h_max
    in H {
      h_lst = h1.h_lst ++ h2.h_lst,
      h_cnt = h1.h_cnt + h2.h_cnt,
      h_min = h_min_,
      h_max = h_max_,
      h_wmid = calcWmid h_min_ h_max_ h1.h_wmid h2.h_wmid,
      h_sum = fmap (+) h1.h_sum <*> h2.h_sum
    }

instance (Integral a, Num b, Ord b) => Monoid (H a b) where
  mempty = H {
    h_lst = mempty,
    h_cnt = 0,
    h_min = Nothing,
    h_max = Nothing,
    h_wmid = Nothing,
    h_sum = Nothing
  }

instance Functor (H a) where
  fmap :: (b -> c) -> H a b -> H a c
  fmap f h = H {
    h_lst = h.h_lst,
    h_cnt = f h.h_cnt,
    h_min = h.h_min,
    h_max = h.h_max,
    h_wmid = h.h_wmid,
    h_sum = h.h_sum
  }

instance Bifunctor H where
  bimap :: (a -> c) -> (b -> d) -> H a b -> H c d
  bimap f g h = H {
    h_lst = map f h.h_lst,
    h_cnt = g h.h_cnt,
    h_min = fmap f h.h_min,
    h_max = fmap f h.h_max,
    h_wmid = fmap f h.h_wmid,
    h_sum = fmap f h.h_sum
  }

instance Biapplicative H where
  bipure :: a -> b -> H a b
  bipure x y = H {
    h_lst = [x],
    h_cnt = y,
    h_min = Just x,
    h_max = Just x,
    h_wmid = Just x,
    h_sum = Just x
  }

  (<<*>>) :: H (a -> c) (b -> d) -> H a b -> H c d
  (<<*>>) h1 h2 = let
    h_min_ = h1.h_min <*> h2.h_min
    h_max_ = h1.h_max <*> h2.h_max
    h_wmid_ = h1.h_wmid <*> h2.h_wmid
    in H {
      h_lst = zipWith ($) h1.h_lst h2.h_lst,
      h_cnt = h1.h_cnt h2.h_cnt,
      h_min = h_min_,
      h_max = h_max_,
      h_wmid = h_wmid_,
      h_sum = h1.h_sum <*> h2.h_sum
    }

maybeOp :: (a -> a -> a) -> Maybe a -> Maybe a -> Maybe a
maybeOp f Nothing Nothing = Nothing
maybeOp f (Just x) Nothing = Just x
maybeOp f Nothing (Just y) = Just y
maybeOp f (Just x) (Just y) = Just (f x y)

maybeOp' :: (a -> b -> c) -> Maybe a -> Maybe b -> Maybe c
maybeOp' f Nothing Nothing = Nothing
maybeOp' f Nothing x = Nothing
maybeOp' f x Nothing = Nothing
maybeOp' f (Just x) (Just y) = Just (f x y)

fromMaybeOp :: (a -> a -> a) -> Maybe a -> a -> a
fromMaybeOp f Nothing x = x
fromMaybeOp f (Just y) x = f y x

calcWmid :: (Num a, Ord a, Integral a) =>
  Maybe a -> Maybe a -> Maybe a -> Maybe a -> Maybe a
calcWmid hmin hmax hwmid elem = let
  calcWmid' :: (Num a, Ord a, Integral a) => a -> a -> a -> a -> a
  calcWmid' min' max' wmid' elem = let
    mid = (min' + max') `div` 2
    elemmiddiff = abs (elem - mid)
    wmidmiddiff = abs (wmid' - mid)
    in if elemmiddiff <= wmidmiddiff then elem else wmid'
  in
  do
    min' <- hmin
    max' <- hmax
    let calcWmid'' = calcWmid' min' max'
    maybeOp calcWmid'' hwmid elem

calcH :: (Num a, Ord a, Integral a, Num b) => a -> H a b -> H a b
calcH elem h = let
  h_min_ = maybeOp min h.h_min $ Just elem
  h_max_ = maybeOp max h.h_max $ Just elem
  in H {
    h_lst = elem : h.h_lst,
    h_cnt = 1 + h.h_cnt,
    h_min = h_min_,
    h_max = h_max_,
    h_wmid = calcWmid h_min_ h_max_ h.h_wmid $ Just elem,
    h_sum = maybeOp (+) (Just elem) h.h_sum
  }

pivotnk :: (Integral a) => 
            H a a ->
            a ->
            a ->
            a ->
            (a -> a -> a -> a -> a -> a) ->
            Maybe a
pivotnk h k off defp form =
  do
    min' <- h.h_min
    max' <- h.h_max
    let cnt' = h.h_cnt
    let pivot' = form min' max' cnt' k off
    if pivot' == defp then
      listToMaybe h.h_lst
    else
      return pivot'
 

qsel :: (Show a, Ord a, Integral a) =>
  [a] -> a -> Maybe (a, [a])
qsel elems k = ret where
  ret
    | k < 1 = Nothing
    | k >= fromIntegral (length elems) = Just (maximum elems, elems)
    | otherwise = do
            mink <- qsel' elems k 0 (listToMaybe elems)
            let minkelems = take
                  (fromIntegral k)
                  $ filter (<= fromIntegral mink)
                  elems
            return (mink, minkelems)

  accf :: (Ord a, Integral a) =>
   a -> a -> (H a a, H a a, H a a)
   -> (H a a, H a a, H a a)
  accf pivot elem acc = let (lt, eq, gt) = acc
    in
      if elem < pivot then
        (calcH elem lt, eq, gt)
      else
         if elem == pivot then
           (lt, calcH elem eq, gt)
         else
           (lt, eq, calcH elem gt)
 
  emptysml :: (Integral a) => (H a a, H a a, H a a)
  emptysml = (mempty, mempty, mempty)

  qsel' :: (Show a, Ord a, Integral a) =>
    [a] -> a -> a -> Maybe a -> Maybe a
  qsel' [] k off pivot =
     traceShow (concat ["pivot: ", show pivot, " k: ", show k,
                ", off: ", show off, " el: ", show (k + off)])
     Nothing
  qsel' (x:xs) k off pivot
    | k <= off + lt.h_cnt =
      traceShow (concat ["pivot: ", show pivot, " x: ", show x,
                 ", pivotl: ", show pivotl, ", k: ", show k,
                 ", off: ", show off, ", lt.h_cnt: ", show lt.h_cnt,
                 ", eq.h_cnt: ", show eq.h_cnt,
                 ", gt.h_cnt: ", show gt.h_cnt])
      qsel' lt.h_lst k off pivotl
    | k > off + lt.h_cnt + eq.h_cnt =
      traceShow (concat ["pivot: ", show pivot, " x: ", show x,
                 ", pivotg: ", show pivotg, ", k: ", show k,
                 ", off: ", show off, ", lt.h_cnt: ", show lt.h_cnt,
                 ", eq.h_cnt: ", show eq.h_cnt,
                 ", gt.h_cnt: ", show gt.h_cnt])
      qsel' gt.h_lst k (off + lt.h_cnt + eq.h_cnt) pivotg
    |
      traceShow (concat ["pivot: ", show pivot, ", x: ", show x,
                  ", k:", show k, ", off: ", show off,
                  ", lt.h_cnt: ", show lt.h_cnt,
                  ", eq.h_cnt: ", show eq.h_cnt,
                  ", gt.h_cnt: ", show gt.h_cnt])
      otherwise = maybeOp const pivot (Just x)
    where
      pivota = fromMaybeOp const pivot x
      (lt, eq, gt) = foldr (accf pivota) emptysml (x:xs)
      --pivotl = maybeOp const lt.h_wmid (listToMaybe lt.h_lst)
      --pivotg = maybeOp const gt.h_wmid (listToMaybe gt.h_lst)
      --lm = maybeOp' div lt.h_sum $ Just lt.h_cnt
      --rm = maybeOp' div gt.h_sum $ Just gt.h_cnt
      --pivotl = maybeOp const lm (listToMaybe lt.h_lst)
      --pivotg = maybeOp const rm (listToMaybe gt.h_lst)
      pivotl = pivotnk lt k off pivota
                (\min' max' cnt' k off ->
                  min' + (k * (max' - min')) `div` cnt')
      pivotg = pivotnk gt k off pivota
                (\min' max' cnt' k off ->
                  min' + ((k - off) * (max' - min')) `div` cnt')






