module Main where

import Test.Hspec
import Lib (greet)

main :: IO ()
main = hspec $ do
  describe "greet" $ do
    it "prints a greeting" $ do
      True `shouldBe` True -- Replace with real tests!
