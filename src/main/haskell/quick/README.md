my-simple-project/
├── app/
│   └── Main.hs        # Entry point for the executable
├── src/
│   └── Lib.hs         # Library source code
├── test/
│   └── Spec.hs        # Test source code
├── package.yaml       # Project configuration
├── stack.yaml         # Stack configuration
└── README.md          # Optional README

cd ~/code/ettuge/src/main/haskell/quick/

Build and Run

Build the project:
stack build

Run the executable:
stack exec quick-exe

Run tests:
stack test

For doc, see:
<https://github.com/vwulf/ettuge/blob/master/src/main/md/haskell/qsortof.md>
