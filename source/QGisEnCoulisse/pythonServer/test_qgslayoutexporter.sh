#!/bin/sh

rm ./utilities.py
wget https://raw.githubusercontent.com/qgis/QGIS/master/tests/src/python/utilities.py ./utilities.py

rm ./test_qgslayoutexporter.py
wget https://raw.githubusercontent.com/qgis/QGIS/master/tests/src/python/test_qgslayoutexporter.py ./test_qgslayoutexporter.py
chmod +x ./test_qgslayoutexporter.py

python3 ./test_qgslayoutexporter.py
