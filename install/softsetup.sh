echo "PIP Install:"
apt install -y python-pip

echo "Install Text To Speech:"
pip install pyttsx

echo "Install Speech Recognition:"
pip install SpeechRecognition

echo "Install Chatterbot:"
pip install chatterbot

echo "Install CMU Sphinx:"
echo "Step 1, dependencies:"
apt install -y gcc automake autoconf libtool bison swig python-dev libpulse-dev

echo "Step 2, sphinxbase:"
git clone https://github.com/cmusphinx/sphinxbase.git
cd sphinxbase/
./autogen.sh
make
make install
echo "/usr/local/lib" >> /etc/ld.so.conf
ldconfig

echo "Step 3, pocketsphinx:"
cd ..
git clone https://github.com/cmusphinx/pocketsphinx.git
cd pocketsphinx/
./autogen.sh
make
make install
ldconfig

echo "Step 4, sphinxtrain:"
cd ..
git clone https://github.com/cmusphinx/sphinxtrain.git
cd sphinxtrain/
./autogen.sh
make
make install
ldconfig


echo "Step 5, cmusphinx:" 
cd ..                                                                                       svn checkout svn://svn.code.sf.net/p/cmusphinx/code/trunk cmusphinx-code
cd cmusphinx-code/
cd cmuclmtk/
./autogen.sh
make
make install

echo "Install PortAudio:"
cd ..
cd ..
wget http://portaudio.com/archives/pa_stable_v190600_20161030.tgz
tar -zxvf pa_stable_v190600_20161030.tgz
cd portaudio/
./configure
make 
make install
pip install pyaudio







