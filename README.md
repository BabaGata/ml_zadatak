# ml_zadatak
Tu se nalazi api aplikacija sa templateom, Dockerfileom, requirements.txt i sa ordinal_encoder.pkl.<br>
Za normalno funkcioniranje aplikacije potreban je jos file random_forest_model.pkl koji se moze skinuti sa drive-a<br>
https://drive.google.com/file/d/17ckASaujKpy_bQnYkHaqeyBnogAsgM7p/view?usp=sharing<br>
ili pokretanjem .ipynb datoteke ML_Model_Vehicles.ipynb.<br>
https://github.com/BabaGata/ipynb_datoteke_zadatak/blob/main/ML_Model_Vehicles.ipynb<br>
File je potrebno spremiti u glavni direktorj, tj. onaj u kojemu se nalazi main.py.<br><br>
Aplikaciji je postavljen port na 8000.<br>
Funkcija:
Prima podatke o vozilu u obliku HTML forme, i potom racuna predvidenu cijenu vozila, te ju ispisuje.<br><br>

U ovom repozitoriju se NE nalaze datoteke s kojima je pripremljen dataset i napravljen model. To se nalazi u repozitoriju:<br>
https://github.com/BabaGata/ipynb_datoteke_zadatak<br>
Datoteke sljedeceg repozitorija:<br>
Ciscenje.ipynb  -  Ucitava datoteku vehicles.scv, koja se mora unaprijed skinuti sa Kaggle-a,<br>
https://www.kaggle.com/datasets/austinreese/craigslist-carstrucks-data?resource=download<br>
i spremiti u isti direktorij gdje se nalazi Ciscenje.ipynb. 
Ostale datoteke koje notebook koristi, se nalaze unutar repositorija. U ovoj datoteci se podatci pripremaju i spremaju u tri razlicite verzije, 
od kojih se jedna kasnije koristi u ostalim noteboocima.<br>
ML_Model_Vehicles.csv  -  Ucitava datoteku vehicles_1.csv, koja se nalazi u repozitoriju. Ovaj notebook transformira string stupce, trenira modele, i
sprema ih u datoteke. Ovaj notebook se treba pokrenuti za genriranje datoteke random_forest_model.pkl koja se koristi pri generiranju predvidanja 
u apiju.<br>
DeepL_Model_Vehicles.ipynb  -  Isprobavanje deep learning neuralnih mreza za predvidanje cijene. Nije koristeno dalje.<br>
Izvjestaj.ipynb  - Izvjestaj o rjesavanju zadatka.
<br><br>
Exportani docker container: https://drive.google.com/file/d/1iprs2o8kHmUjFJvMAUAxDgU-y9u_oYDW/view?usp=sharing
