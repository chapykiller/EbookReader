echo "Running Quote Attribution:"
source activate quote
cd RNNQuoteAttribution
python teste.py
cd ..
source deactivate

echo "Running Deepvoice3"
source activate deepvoice
cd deepvoice3_pytorch
python gerar.py -t "Test"
cd ..
source deactivate
