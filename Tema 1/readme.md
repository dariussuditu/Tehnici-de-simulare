__Jocul de barbut se joaca dupa urmatoarele reguli:__

	- jocul nu este influentat de ordinea in care jucatorii arunca zarul
	- daca jucatorii arunca aceeasi combinatie de zaruri, se reia aruncarea
	- daca unul din jucatori da dubla (1,1) acesta castiga automat indiferent de mana adversarului
	- daca unul din jucatori da dubla ( ex (x,x) ), acesta castiga daca celalalt jucătorul nu da o dubla mai mare (ex (x+1,x+1))
	-daca niciunul din jucatori nu da dubla, atunci castiga cel cu suma zarurilor maxima
	-daca suma zarurilor este egala se reia aruncarea dupa aceleasi reguli

Pentru a estima probabilitatea de castig, ne propunem sa simulam jocul pentru cat mai multe scenarii.
