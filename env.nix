with import <nixpkgs> {};
stdenv.mkDerivation {
  name = "env-reveal-js";
  buildInputs = [
    nodejs
  ];
}