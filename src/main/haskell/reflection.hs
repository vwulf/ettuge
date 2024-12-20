import Control.Monad
import Control.Arrow
import Data.Typeable
import Language.Haskell.TH
--import System.Eval.Haskell

cmd = "Command> "
cmt = "Vish> "
inte = "Haskell> "

prompt :: String -> String -> String
prompt p s = p ++ s

cmdp = prompt cmd
cmdೱ = putStr . cmdp
cmdLnೱ = putStrLn . cmdp
cmtp = prompt cmt
cmtೱ = putStr . cmtp
cmtLnೱ msg = (putStrLn . cmtp) $ msg ++ "\n"
intp = prompt inte
intೱ = putStr . intp
intLnೱ = putStrLn . intp

data Expl = English | Symbolic

expValೱ :: (Show a) => String -> String -> a -> Expl -> IO ()
expValೱ  expr term typ expl = do 
  let y = case expl of English -> do
                         intೱ $ "Value of " ++ term ++ " is:\n" ++ show(typ) ++ "\n\n"
                       Symbolic -> do
                         intೱ $ term ++ " = " ++ show (typ) ++ "\n\n"
  y


expTypೱ :: (Typeable a, Show a) => String -> String -> a -> Expl -> IO ()
expTypೱ expr term typ expl = do
  cmdLnೱ expr
  let x = case expl of English -> do
                         intೱ $ "Type of " ++ term ++ " is:\n"
                         print $ (typeOf typ)
                       Symbolic -> do
                         intೱ $ term ++ " :: " 
                         print $ (typeOf typ)
  let y = expValೱ  expr term typ expl
  x
  y
  
--f :: ()

expExpೱ :: String -> String -> Expl -> IO()
expExpೱ expr expExpr expl = do
  let x = case expl of English ->
                         intೱ $ "Type of " ++ expr ++ " is:\n" ++ expExpr ++ "\n"
                       Symbolic ->
                         intೱ $ expr ++ " :: " ++ expExpr ++ "\n"
  x

main = do
  cmtLnೱ "Haskell defines types and enforces them strictly. It has a nice interpreter for exploration and compiled into an executable file."
  expTypೱ "'A'" "'A'" 'A' English
  
  cmtLnೱ "\"Type of\" in English is written in Haskell as \"::\""
  cmtLnೱ "\"Value of\" in English is written in Haskell as \"=\""
  
  expTypೱ "'ಅ'" "'ಅ'" 'ಅ' Symbolic
  
  cmtLnೱ "\"let\" is used to introduce newer symbols. Haskell typically infers the type. \"::\" can be used to disambiguate."
  let x = 0::Int
  expTypೱ "let x = 0::Int" "x" x Symbolic
  
  cmtLnೱ "What if I skip specifying the type here?"
  let x1 = 0
  cmdLnೱ "let x1 = 0"
  expExpೱ "x1" "Num p => p" Symbolic
  
  putStrLn ""
  cmtLnೱ "Haskell says \"x1\" is of numeric \"type\"  \"Num\" rather than \"Int\". \"Num\" is a \"kind\", like a higher order type or metatype."
  cmtLnೱ "Kinds specify type constraints for the input type parameter. Int satisfies the Num type constraint."
  cmtLnೱ "If your logic applies to different types that belong to some kind, you are doing \"Generic Programming\"."
  
  let x2 = 0 + 1
  cmdLnೱ "let x2 = 0 + 1"

  expExpೱ "x2" "Num a => a" Symbolic
  expValೱ "let x2 = 0 + 1" "x2" x2 Symbolic
  
  cmtLnೱ "How does this work? Lets look at what is \"+\"?" 
  expExpೱ "(+)" "Num a => a -> a -> a" Symbolic

  putStrLn ""
  cmtLnೱ "Haskell says (+) takes 2 inputs of some type \"a\" and returns an \"a\" as long as \"a\" satisffies the \"Num\" type constraint."
  cmtLnೱ "So => is a type constraint, What is this strange \"->\"?"
  cmtLnೱ "In Haskell, A function f(x,y,z) i.e. f x y z is treated as ((f x) y) z). ((f x) y) takes 1 parameter less than (f x) since y is bound and so on. This is called currying."
  cmtLnೱ "-> is right associative and represents 1 currying operation which is read right to left. All functions in haskell take exactly 1 argument, with currying doing the reduction of mutiple arguments to 1. "
  
  cmtLnೱ "Its easier to read the function signature directly, instead of in curried form. (+) takes 2 \"a\" i.e. a -> a and finally returns an a i.e. -> a, giving the type signature a -> a -> a. The last -> is the return value. The rest are arguments."
  
  cmtLnೱ "Why all this complexity? It reduces special cases and lets you create new functions on the fly."
  
  let plus5 = (5 +)
  cmdLnೱ "let plus5 = (5 +)"
  expExpೱ "plus5" "Num a => a -> a" Symbolic
  cmtLnೱ "\"a\" is an arbitrary type but if it's mentioned multiple times, it indicates that they are the same type. If the fn e.g. takes another argument or returns a different type \"b\", \"c\" etc are used."
  
  cmtLnೱ "Let's move on. Read lc as list of characters, llc as list of list of characters."

  let lc1 = "T"
  expTypೱ "let lc1 = \"T\"" "lc1" lc1 Symbolic

  cmtLnೱ "lc1 is the same as [\'T\']. A list of characters is a string."

  let lc2 = ['T']
  expTypೱ "let lc2 = ['T']" "lc2" lc2 Symbolic

  let llc1 = ["T","a","k"]
  expTypೱ "let llc1 = [\"T\",\"a\",\"k\"]" "llc1" llc1 Symbolic
  
  let llc2 = ["Y","u"," "]
  let llc3 = ["h","s",""]
  let lllc1 = [llc1,llc2,llc3]
  putStrLn $ "lllc1 = " ++ (show lllc1)
  let b = [["h","n"," "],["o"," ","S"],["a","!",""]]
  putStrLn $ "b = " ++ (show b)
  
  expExpೱ "(++)" "[a] -> [a] -> [a]" Symbolic
  let f = zipWith (++)
  --print $ (typeOf +)
  expExpೱ "zipWith" "(a -> b -> c) -> [a] -> [b] -> [c]" Symbolic
  
  let sf = "zipWith (++)"
  putStrLn $ "f = " ++ sf
  let g = zipWith f
  let sg = "zipWith f"
  putStrLn $ "g = " ++ sg
  let i = g lllc1 b
  let si = "g a b"
  putStrLn $ "i = " ++ si
  putStrLn $ "Running i gives " ++ (show i)
  let j = join $ i
  let sj = "join $ i or join (i)"
  putStrLn $ "j = " ++ sj
  putStrLn $ "Running j gives " ++ (show j)
  let k = join $ j
  let sk = "join $ j"
  putStrLn $ "k = " ++ sk
  putStrLn $ "Running k gives " ++ (show k)
  putStrLn $ "join => Monad. While currying freely, you learnt about .."
  print "..Just a monoid in the category of endofunctors. So what's the problem?"
  print "Just another mapping to Kleisli.."
  print "Happy B'day again!"
