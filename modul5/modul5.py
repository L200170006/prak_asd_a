##Nama  : Bagus Nuril Anam
##NIM   : L200170006
##Kelas : A
##Modul : 5

class Mahasiswa(object):
    """Class Manusia yang dibangun dari class manusia"""
    def __init__(self,nama,NIM,kota,us):
        """Metode inisiasi ini menutupi metode inisiasi di class Manusia"""
        self.nama = nama
        self.NIM = NIM
        self.kotaTinggal = kota
        self.uangSaku = us

class MhsTIF (Mahasiswa):  
    """Class MhsTIF yang dibangun dari class Mahasiswa"""
    def katakanPy(self):
        print('Python is cool.')
        
Daftar = [MhsTIF ('Masimah',20,'Jakarta',540000),
MhsTIF('Muslihat',31,'Bekasi',130000),
MhsTIF('Kang Bahar',12,'Surakarta',550000),
MhsTIF('Chandra',18,'Surakarta', 230000),
MhsTIF('Komar',33,'Tangerang',245000),
MhsTIF('Fandi',31,'Salatiga', 250000),
MhsTIF('Deni',13,'Klaten', 245000),
MhsTIF('Galuh',5,'Wonogiri', 245000),
MhsTIF('Janto',23,'Klaten', 245000),
MhsTIF('Hasan',64,'Karanganyar', 270000),
MhsTIF('Justin',49,'Skandanavia',125000)]

#1
def ceknim (d):
    for i in d :
        print (i.NIM)

def swap (a, p, q) :
    tmp = a[p]
    a[p] = a[q]
    a[q] = tmp

def urutnim(d):
    n = len(d)
    for i in range (n -1) :
        for k in range (n-i-1) :
            if d[k].NIM > d[k+1].NIM :
                swap(d,k,k+1)
##cara menampilkan
##urutnim(Daftar)
##ceknim(Daftar)
#2
a = [2,6,7,9,4]
b = [5,8,10,3,1]
c = a + b
 
def swap (a, p, q) :
    tmp = a[p]
    a[p] = a[q]
    a[q] = tmp

def urut(d):
    n = len (d)
    for i in range (n -1) :
        for k in range (n-i-1) :
            if d[k] > d[k+1] :
                swap(d,k,k+1)

urut(c)
print(c)

#3
from time import time as detak
from random import shuffle as kocok
def swap(A,p,q):
    tmp = A[p]
    A[p]= A[q]
    A[q]= tmp

def bubbleSort(A):
    n = len(A)
    for i in range(n-1):
        for j in range(n-i-1):
            if A[j] > A[j+1]:
                swap(A,j,j+1)

def selectionSort(A):
    n = len(A)
    for i in range(n-1):
        indexKecil = cariPosisiYangTerkecil(A, i, n)
        if indexKecil != i :
            swap(A, i, indexKecil)

def insertionSort(A):
    n = len(A)
    for i in range(1,n):
        nilai = A[i]
        pos = i
        while pos > 0 and nilai < A[pos - 1]:
            A[pos] = A[pos -1]
            pos = pos -1
        A[pos] = nilai
        
def cariPosisiYangTerkecil(A,darisini, sampaisini):
    posisiYangTerkecil = darisini
    for i in range (darisini+1, sampaisini):
        if A[i] < A[posisiYangTerkecil]:
