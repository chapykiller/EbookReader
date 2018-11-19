#!/bin/bash
echo "Preparando RNNQuote environment:"
cd RNNQuoteAttribution
wget --no-check-cert https://www.dropbox.com/s/8bx96i6mo7kkw2k/glove.6B.100d.word2vec.txt?dl=0 -O glove.6B.100d.word2vec.txt
wget --no-check-cert https://www.dropbox.com/s/nwcanpx8xnb0j9j/weights.tar.gz?dl=0 -O weights.tar.gz
tar -xzf weights.tar.gz
rm -f weights.tar.gz
conda create -yn quote python=2.7
source activate quote
conda install -y scikit-learn
conda install -y tensorflow
conda install -y gensim
conda install -y matplotlib
source deactivate quote
cd ..
echo "Preparando Deepvoice3 environment:"
cd deepvoice3_pytorch
wget --no-check-cert https://www.dropbox.com/s/c7xtniw4lh3ljhe/20171222_deepvoice3_vctk108_checkpoint_step000300000.pth?dl=0 -O 20171222_deepvoice3_vctk108_checkpoint_step000300000.pth
conda create -yn deepvoice python=3.6.6
source activate deepvoice
pip install scikit-learn==0.19.1
pip install torch==0.3.1
pip install torchvision
pip install --upgrade tensorflow
pip install tensorboard-pytorch
pip install nnmnkwii==0.0.9
pip install matplotlib
pip install IPython
pip install -e ".[train]"
mkdir out
source deactivate deepvoice
cd ..
