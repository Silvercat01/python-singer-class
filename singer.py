class Singer:

    def __init__(self,nev,mufaj,helydatum):
        if not isinstance(nev,str):
            raise TypeError("a névnek stringnek kell lennie")
        if not nev.strip():
            raise ValueError("a név nem lehet üres vagy space")
        
        if not isinstance(mufaj,str):
            raise TypeError("a műfajnak stringnek kell lennie")
        if not mufaj.strip():
            raise ValueError("a műfaj nem lehet üres vagy space")
        
        if not isinstance(helydatum,list):
            raise TypeError("a koncertek helyszínének és dátumának listában kell lennie")
        for elem in helydatum:
            if not isinstance(elem,tuple) or len(elem)!=2:
                raise TypeError("kételemű tupleben kell lennie a helyszínnek és dátumnak")
            if not elem[0].strip() or not elem[1].strip():
                raise ValueError("a helyszín és dátum nem lehet üres vagy space")
            
        self._nev = nev
        self._mufaj = mufaj
        self._helyszindatum = helydatum

    @property
    def nev(self):
        return self._nev
    @nev.setter
    def nev(self,nev):
        if not isinstance(nev,str):
            raise TypeError("a névnek stringnek kell lennie")
        if not nev.strip():
            raise ValueError("a név nem lehet üres vagy space")
        self._nev = nev

    @property
    def mufaj(self):
        return self._mufaj
    @mufaj.setter
    def mufaj(self,mufaj):
        if not isinstance(mufaj,str):
            raise TypeError("a műfajnak stringnek kell lennie")
        if not mufaj.strip():
            raise ValueError("a műfaj nem lehet üres vagy space")
        self._mufaj = mufaj

    @property
    def helyszindatum(self):
        return self._helyszindatum
    
    def __str__(self):
        tuple_str = ";".join(helyszin + "," + datum for helyszin, datum in self._helyszindatum)
        return str(self._nev)+","+str(self._mufaj)+":"+tuple_str
    def __add__(self,ujkoncert):
        if not isinstance(ujkoncert,tuple) or len(ujkoncert)!=2:
            raise TypeError("kételemű tupleben kell lennie a helyszínnek és dátumnak")
        if not ujkoncert[0].strip() or not ujkoncert[1].strip():
            raise ValueError("a helyszín és dátum nem lehet üres vagy space")
        helyszindatum = self._helyszindatum + [ujkoncert]
        #vagy:
        #helyszindatum = self._helyszindatum [:]
        #   helyszindatum.append(ujkoncert)
        return Singer(self._nev,self._mufaj,helyszindatum)
    def __sub__(self,koncert):
        helyszindatum = self._helyszindatum [:]
        if not isinstance(koncert,tuple) or len(koncert)!=2:
            raise TypeError("kételemű tupleben kell lennie a helyszínnek és dátumnak")
        if not koncert[0].strip() or not koncert[1].strip():
            raise ValueError("a helyszín és dátum nem lehet üres vagy space")
        if koncert in helyszindatum:
            helyszindatum.remove(koncert)
        else:
            raise ValueError("nem található ilyen elem a listában")
        return Singer(self._nev,self._mufaj,helyszindatum)
    def __lt__ (self,masik):
        if not isinstance(masik,Singer):
            raise TypeError("nem Singer típusú a megadott elem")
        return len(self._helyszindatum) < len(masik._helyszindatum)
    def __gt__(self,masik):
        if not isinstance(masik,Singer):
            raise TypeError("nem Singer típusú a megadott elem")
        return len(self._helyszindatum) > len(masik._helyszindatum)
    
class ConcertOrganizer:

    def __init__(self,enekesek = None):
        if enekesek is None:
            self._enekesek = []
        else:
            if not isinstance(enekesek,list):
                raise TypeError("az énekeseknek listéban kell lenniük")
            if not all(isinstance(enekes,Singer) for enekes in enekesek):
                raise TypeError("minden énekesnek Singer típusúnak kell lenni")
            self._enekesek = list(enekesek)

    @property
    def enekesek(self):
        return list(self._enekesek)
    
    def __str__(self):
        return "\n".join(str(enekes) for enekes in self._enekesek)
    def add_singer(self,masik):
        if not isinstance(masik,Singer):
            raise TypeError("az énekesnek Singer típusúnak kell lennie")
        if masik not in self._enekesek:
            self._enekesek.append(masik)
    def legtobbkoncert(self):
        if not self._enekesek:
            return None
        maxert = max(len(enekes._helyszindatum) for enekes in self._enekesek)
        legtobb = [enekes.nev for enekes in self._enekesek if len(enekes._helyszindatum) == maxert]
        return legtobb if len(legtobb) > 1 else legtobb[0]