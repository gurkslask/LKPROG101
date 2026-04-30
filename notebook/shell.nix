let
  nixpkgs = fetchTarball "https://github.com/NixOS/nixpkgs/tarball/nixos-24.05";
  pkgs = import nixpkgs { config = {}; overlays = []; };

in

pkgs.mkShellNoCC {
  packages = with pkgs; [
    cowsay
    lolcat
    uv
    python3
    jupyter
  ];
  # Automatically run jupyter when entering the shell.
  shellHook = ''
  # 1. Skapa en virtuell miljö om den inte finns
    if [ ! -d ".venv" ]; then
      uv venv
    fi
    
    # 2. Aktivera miljön
    source .venv/bin/activate

    # 3. Installera dina paket blixtsnabbt (uv sköter detta)
    echo "Ser till att jupyturtle och jupyter är installerade..." | lolcat
    uv pip install jupyter jupyturtle

    echo "Startar Jupyter..."
    jupyter notebook --allow-root
  '';
}
