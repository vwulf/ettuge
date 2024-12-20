import Data.Typeable
import Control.Monad
import Data.List
import qualified Data.Map as Map

type Step = Int
type Path = [Step]
type Paths = [Path]
type PathsFrom = (Step, Paths)
--type PathsTable = [PathsFrom]
type PathsTable = Map.Map Step Paths
type PathsTables = [PathsTable]
data CatInput = CatInput {begin :: Step, end :: Step, jump :: Step}
data JCtxt = JCtxt { currSj :: Step, nextSj :: Step, endSj :: Step}
data Ctxt = Ctxt { signC :: Step, curC :: Step, prevC :: Step, pathC :: Path, pathsT :: PathsTable}

prepend :: Step -> Paths -> Paths
prepend step paths = do
  path <- paths
  return (step : path)
  
prependPF :: Step -> PathsFrom -> PathsFrom
prependPF step pf = (step, prepend step (snd pf))

{--
addStep :: Step -> PathsTable -> PathsTable
addStep step pt = do
  pathsFrom <- pt
  let (nextStep, paths) = pathsFrom
  return (step, prepend step paths)
--}
  
merge :: PathsTables -> PathsTable
merge pts =
  foldl mergePT [] pts

mergePT :: PathsTable -> PathsTable -> PathsTable
mergePT x y = Map.unionWithKey mergePaths x y

mergePaths :: Step -> Paths -> Paths -> Paths
mergePaths s x y = x ++ y

mergePF :: PathsFrom -> PathsFrom -> PathsFrom
mergePF x y = (fst x, (snd x) ++ (snd y))

pickNZ :: a -> Maybe a -> a
pickNZ z mx = case mx of
  (Just x) -> x
  Nothing -> z

mergePTPF :: PathsTable -> PathsFrom -> PathsTable
mergePTPF pt pf = ptNew
  where
    upM = Map.update (fst pf) pt 
    foundPF = find (\x -> (fst x) == (fst pf)) pt
    pfNewM = (mergePF pf) <$> foundPF
    pfNew = pickNZ pf pfNewM
    ptNew = pt ++ [pfNew]

safe :: JCtxt -> Bool
safe sj =
  let
    step = currSj sj
    jump = nextSj sj
    maxStep = endSj sj
    goingright = ((signum jump) == 1)
    goingleft = not goingright
    lessthanorequal = ((step + jump) <= maxStep)
    greaterthanorequal = ((step + jump) >= maxStep)
    leftwithin = goingright && lessthanorequal
    rightwithin = goingleft && greaterthanorequal
    inside = leftwithin || rightwithin
  in
    inside
        
cath :: CatInput -> Ctxt -> PathsTable
cath i c
  | curStep == maxStep = finalPathT
  | True = res
  where
    beginStep = begin i
    maxStep = end i
    maxJump = jump i
    sign = signC c
    curStep = curC c
    path = pathC c
    pathsTable = pathsT c
    endPath = reverse path
    endPF = (curStep, [endPath])
    --prevPF = prependPF (prevC c) endPF
    --endPathT = if path == [] then [endPF] else [prevPF, endPF]
    finalPathT = mergePTPF pathsTable endPF
    
    explore :: PathsTable -> Step -> PathsTable
    explore p j = safeEx
      where
        newStep = curStep + j
        newPath = (newStep : path)
        newPT = mergePTPF p (curStep, [reverse path])
        sj = JCtxt curStep j maxStep
        cNew = Ctxt sign newStep curStep newPath newPT
        --done = (\s -> if pathsTable == [] then [] else endPathT)
        --done = (\s -> [])
        safeEx = if (safe sj) then (cath i cNew) else p
    
    explore1 :: PathsTable -> Step -> PathsTable
    explore1 p j = newPt
      where
        newStep = curStep + j
        foundPF = find (\x -> (fst x) == newStep) p
        exPTM = (mergePTPF p) <$> (prependPF curStep) <$> foundPF
        expt = pickNZ p exPTM
        newEx = explore expt j
        newPt = if expt == Map.empty then newEx else expt
    
    {--
    sc1s = explore 1
    sc2s = explore 2
    sc1n = addStep n sc1s
    sc2n = addStep n sc2s
    res = merge $ [sc1n, sc2n]
    --}
    
    --res = merge $ map ((addStep n) . explore) [1..2]
    
    jTbl = map (* sign) $ take (abs maxJump) [1..]
    --res = merge $ map explore jTbl
    --res = (explore pathsTable) =<< jTbl
    --res = foldM ex (0,[]) jTbl
    --res = (explore1 pathsTable) =<< jTbl
    res = foldl explore1 pathsTable jTbl

cat :: CatInput -> PathsTable
cat i
  | j == 0 = Map.empty
  | dir /= jdir = Map.empty
  | True = do
    let ctxt = Ctxt dir b b [b] $ Map.empty
    pt <- cath i ctxt
    --path <- snd pt
    return pt
  where
    b = begin i
    e = end i
    j = jump i
    dir = signum (e - b)
    jdir = signum j

pcat b e j = do
  print $ "begin: " ++ show b ++ " end: " ++ show e ++ " maxJump: " ++ show j
  let i = CatInput b e j
  print $ cat i

main = do
  putStrLn "Hello, World!"
  nStr <- getLine -- Reading 20 from input
  let n = read nStr
  mStr <- getLine -- Reading 30
  let m = read mStr
  print (typeOf m)
  print . take m $ map (foo) [15..]
  print . take n $ map (foo) [0..]
  print $ take 2 [2..5]
  print $ take 2 $ map (foo) [1..10]
  pf 3
  plafoo [1..5]
  yStr <- getLine
  let y = read yStr
  print $ sqr y
  pcat 0 5 2
  pcat (-2) 5 2
  pcat (-2) 5 7
  pcat (-2) (-5) 7 -- not ok
  pcat (-2) 5 (-7) -- not ok
  pcat (-2) (-5) (-7) -- ok
  pcat 2 (-5) (-7) -- ok
  pcat (-2) 0 7 -- ok
  pcat 2 5 0 -- not ok
  pcat 2 0 3 -- not ok
  pcat 5 0 (-2)

