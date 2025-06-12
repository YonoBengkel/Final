#!/bin/bash

echo "Menghitung suhu maksimum:"
awk 'NR > 1 { if ($2 > max) max = $2 } END { print "Suhu maksimum: " max }' data.txt

echo ""
echo "Menghitung rata-rata kelembaban:"
awk 'NR > 1 { total += $3; count++ } END { print "Rata-rata kelembaban: " total/count }' data.txt
