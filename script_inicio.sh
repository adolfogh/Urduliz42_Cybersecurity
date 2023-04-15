MYPATH="/goinfre/$USER/miniconda3"

$MYPATH/bin/conda init zsh
$MYPATH/bin/conda config --set auto_activate_base false
source ~/.zshrc


# No se requiere una vez se inicializa el entorno.
conda create --name 42AI-$USER python=3.7 jupyter pandas pycodestyle numpy


 # Conexion con los entornos
 conda info --envs
 conda activate 42AI-adogarci