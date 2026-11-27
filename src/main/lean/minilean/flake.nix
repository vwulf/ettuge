{
  description = "No Magic: the sum formula proved in core Lean 4";

  inputs.nixpkgs.url = "github:NixOS/nixpkgs/nixpkgs-unstable";

  outputs = { self, nixpkgs }:
    let
      systems = [ "aarch64-darwin" "x86_64-darwin" "x86_64-linux" "aarch64-linux" ];
      forAllSystems = f: nixpkgs.lib.genAttrs systems
        (system: f nixpkgs.legacyPackages.${system});
    in {
      # Nix provides elan; elan installs the exact Lean version named in
      # ./lean-toolchain (the standard Lean setup). nixpkgs' own `lean4`
      # package usually trails the newest Lean release by a version or so.
      devShells = forAllSystems (pkgs: {
        default = pkgs.mkShell {
          packages = [ pkgs.elan pkgs.git ];
          shellHook = ''
            echo "Lean toolchain pinned to: $(cat lean-toolchain)"
            echo "Build with: lake build"
          '';
        };
      });
    };
}
