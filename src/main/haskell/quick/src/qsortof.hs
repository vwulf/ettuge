{-# LANGUAGE InstanceSigs #-}
{-# LANGUAGE FlexibleContexts #-}
{-# LANGUAGE ScopedTypeVariables #-}
module Qsortof where
import Data.Monoid ()
import Data.Typeable ()
import Data.List ( foldl', unfoldr )
import Data.Bifunctor (Bifunctor(first), Bifunctor(second), Bifunctor (bimap))
import Data.Biapplicative (Biapplicative (bipure), Biapplicative ((<<*>>)))
import Debug.Trace (traceShow)
import Data.Maybe (listToMaybe, fromMaybe)
import Data.Bifunctor.Biff (Biff)


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
} deriving (Show, Eq, Ord)

instance (Ord a, Integral a, Num b, Ord b) => Semigroup (H a b) where
  (<>) :: H a b -> H a b -> H a b
  h1 <> h2 = let
    h_min_ = maybeOp min (h_min h1) (h_min h2)
    h_max_ = maybeOp max (h_max h1) (h_max h2)
    in H {
      h_lst = h_lst h1 ++ h_lst h2,
      h_cnt = h_cnt h1 + h_cnt h2,
      h_min = h_min_,
      h_max = h_max_,
      h_wmid = calcWmid h_min_ h_max_ (h_wmid h1) (h_wmid h2),
      h_sum = fmap (+) (h_sum h1) <*> h_sum h2
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
    h_lst = h_lst h,
    h_cnt = f (h_cnt h),
    h_min = h_min h,
    h_max = h_max h,
    h_wmid = h_wmid h,
    h_sum = h_sum h
  }

instance Bifunctor H where
  bimap :: (a -> c) -> (b -> d) -> H a b -> H c d
  bimap f g h = H {
    h_lst = map f (h_lst h),
    h_cnt = g (h_cnt h),
    h_min = fmap f (h_min h),
    h_max = fmap f (h_max h),
    h_wmid = fmap f (h_wmid h),
    h_sum = fmap f (h_sum h)
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
    h_min_ = h_min h1 <*> h_min h2
    h_max_ = h_max h1 <*> h_max h2
    h_wmid_ = h_wmid h1 <*> h_wmid h2
    in H {
      h_lst = zipWith ($) (h_lst h1) (h_lst h2),
      h_cnt = h_cnt h1 (h_cnt h2),
      h_min = h_min_,
      h_max = h_max_,
      h_wmid = h_wmid_,
      h_sum = h_sum h1 <*> h_sum h2
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

calcWmid :: (Num a, Ord a, Integral a) => Maybe a -> Maybe a -> Maybe a -> Maybe a -> Maybe a
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
  h_min_ = maybeOp min (h_min h) (Just elem)
  h_max_ = maybeOp max (h_max h) (Just elem)
  in H {
  h_lst = elem : h_lst h,
  h_cnt = 1 + h_cnt h,
  h_min = h_min_,
  h_max = h_max_,
  h_wmid = calcWmid h_min_ h_max_ (h_wmid h) (Just elem),
  h_sum = fmap (+ elem) (h_sum h)
}

qsel :: (Show a, Ord a, Integral a) =>
  [a] -> a -> a
qsel elems k = qsel' elems k 0 (head elems) where
  qsel' :: (Show a, Ord a, Integral a) =>
    [a] -> a -> a -> a -> a
  qsel' [] k off pivot = pivot
  qsel' (x:xs) k off pivot
    | k < off + ltc =
      traceShow (concat ["pivot: ", show pivot, ", pivotl: ", show pivotl, ", k: ", show k, ", off: ", show off, ", ltc: ", show ltc, ", eqc: ", show eqc, ", gtc: ", show gtc])
      qsel' ltl k off pivotl
    | k > off + ltc + eqc =
      traceShow (concat ["pivot: ", show pivot,", pivotg: ", show pivotg, ", k: ", show k, ", off: ", show off, ", ltc: ", show ltc, ", eqc: ", show eqc, ", gtc: ", show gtc])
      qsel' gtl k (off + ltc + eqc) pivotg
    |
      traceShow (concat ["pivot: ", show pivot, ", k: ", show k, ", off: ", show off, ", ltc: ", show ltc, ", eqc: ", show eqc, ", gtc: ", show gtc])
      otherwise = pivota
    where
      pivota = pivot
      emptysml = (mempty, mempty, mempty)
      (lt, eq, gt) =
        foldl'
          ( \(lt, eq, gt) elem ->
               if elem < pivot then
                 (calcH elem lt, eq, gt)
               else
                  if elem == pivot then
                    (lt, calcH elem eq, gt)
                  else
                    (lt, eq, calcH elem gt)
          ) emptysml (x : xs)
      (ltl, eql, gtl) = (h_lst lt, h_lst eq, h_lst gt)
      (ltc, eqc, gtc) = (h_cnt lt, h_cnt eq, h_cnt gt)
      --pivotl = fromMaybeOp const (h_wmid lt) (head ltl)
      --pivotg = fromMaybeOp const (h_wmid gt) (head gtl)
      --lm = fmap (div (h_cnt lt)) (h_sum lt) 
      lm = maybeOp' div (h_sum lt) $ Just (h_cnt lt)
      rm = maybeOp' div (h_sum gt) $ Just (h_cnt gt)
      pivotl = fromMaybeOp const lm (head ltl)
      pivotg = fromMaybeOp const rm (head gtl)





