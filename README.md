School of Adventures (better name coming)

Installation:
   virtualenv env
   source env/bin/activate
   pip install -r requirements.txt
   (Will look into options to package as .exe etc. later)

Playing:
   python SoA

Running dedicated server:
   python SoAServer [-l] [portnumber]
     (-l specifies localhost only; portnumber defaults to 8192)

Testing:
   python -m unittest discover   
