import Data.Typeable

ಎಡಬಲ ಕ = scanl ಕ
ಕಡೆ ಕ = last ಕ
ಉಲ್ಟ ಕ = reverse ಕ
ತಲೆ ಕ = head ಕ
ಎಡಮಡ್ಇಸ್ಉ ಕ = foldl ಕ
ಮ್ಉದ್ರ್ಇಸ್ಉ ಕ = print ಕ

-- 🔦 🌞 🔋  -> 🌞 🔦 
ಟ್ಆರ್ಚ್ :: (Num ಅ) => ಅ -> (ಅ -> ಅ) -> ಅ
ಟ್ಆರ್ಚ್ ಸ್ಊರ್ಯ ಬ಼್ಆಟ್ರ್ಇ = ಬ಼್ಆಟ್ರ್ಇ ಸ್ಊರ್ಯ

-- ⏳ 🕰 -> 🏃‍♀️🛑 -> ⌛️ 
ಓಡ್ಇಸ್ಉ :: (Num ಅ) => [ಅ -> ಅ] -> ಅ -> ಅ
ಓಡ್ಇಸ್ಉ ಕ್ರ್ಇಯ್ಎ ಚರ =
  let ಉತ್ತರ = ಕಡೆ $ ಎಡಬಲ (ಟ್ಆರ್ಚ್) ಚರ ಕ್ರ್ಇಯ್ಎ in
  ಉತ್ತರ

-- 📼 🧠 💎? -> 💎 ✅
ಹಿನ್ದ್ಎ :: (Num ಅ) => [(ಅ -> ಅ)] -> [ಅ] -> [ಅ] 
ಹಿನ್ದ್ಎ ಕಳ್ಳನಬ್ಉದ್ದ್ಇ ವಜ್ರಗಳ್ಉ =
  ಉತ್ತರ
  where
  ಆಕಳ್ಳನವಜ್ರಗಳ್ಉ = ತಲೆ ವಜ್ರಗಳ್ಉ
  ಈಕಳ್ಳನವಜ್ರಗಳ್ಉ = ಕಳ್ಳನಬ್ಉದ್ದ್ಇ `ಓಡ್ಇಸ್ಉ` ಆಕಳ್ಳನವಜ್ರಗಳ್ಉ
  ಉತ್ತರ = ಈಕಳ್ಳನವಜ್ರಗಳ್ಉ : ವಜ್ರಗಳ್ಉ

-- ⌨️ 📺 👩‍🍳 -> 🍲 
ಮ್ಉಖ್ಯ :: IO ()
ಮ್ಉಖ್ಯ = do
  let ಕಳ್ಳರಸ್ಅಮ್ಖ್ಯ್ಎ = 5
  let ಕ್ಒನ್ಎಕಳ್ಳನವಜ್ರಗಳ್ಉ = 1
  let ಕಳ್ಳನಬ್ಉದ್ದ್ಇ = ಉಲ್ಟ [(*2),(+2)]
  let ಒನ್ದ್ಉಸಲ = (ಹಿನ್ದ್ಎ ಕಳ್ಳನಬ್ಉದ್ದ್ಇ)
  let ಕಳ್ಳನವಜ್ರಗಳ್ಉ ಚರ _ = ಒನ್ದ್ಉಸಲ ಚರ
  let ಖಜ಼್ಆನ್ಎ = ಎಡಮಡ್ಇಸ್ಉ ಕಳ್ಳನವಜ್ರಗಳ್ಉ [ಕ್ಒನ್ಎಕಳ್ಳನವಜ್ರಗಳ್ಉ] [1..(ಕಳ್ಳರಸ್ಅಮ್ಖ್ಯ್ಎ -1)]
  ಮ್ಉದ್ರ್ಇಸ್ಉ $ ತಲೆ ಖಜ಼್ಆನ್ಎ
  ಮ್ಉದ್ರ್ಇಸ್ಉ $ ಖಜ಼್ಆನ್ಎ
  
main = ಮ್ಉಖ್ಯ
