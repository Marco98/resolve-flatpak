#!/bin/sh
set -eu

cd x264
./configure --enable-shared
make
cd ..

cp -r "/app/Developer/CodecPlugin/Examples/x264_encoder_plugin" "x264_encoder_plugin"
patch -s -p0 < libx264_ioplugin.patch
cd x264_encoder_plugin
make clean
make
make install
