Word Finder
===========

Tento program slúži na hľadania slov v nejakom slovníku, ak máme nejaké obmedzenia na písmená na konkrétnych pozíciach.

Otvor si príkazový riadok (na windowse radšej PowerShell):

.. code-block:: console

    $ susi-word-finder -h   # zobrazí nápovedu
    $ susi-word-finder -i sample_file.txt -w abcde  # nájde všetky slová dlhé 5 obsahujúce iba abcde, ktoré sú v súbore sample_file.txt

Možnosti
--------

Program vie meniť svoje správanie podľa toho, čo napíšeš za ``susi-word-finder``. Nižšie je popis všetkých možností:

.. list-table::
    :widths: 50 50
    :header-rows: 1

    * - Možnosť
      - Popis
    * - ``-h/--help``
      - zobrazí nápovedu
    * - ``-i/--input-file``
      - tu nasleduje cesta k textovému súboru, v ktorom chceme hľadať alebo skratku slovníku :py:class:`Dictionary`
    * - ``-w/--word-length``
      - nasleduje číslo, aké dlhé slová má hľadať alebo rozpätie ``x-y``, ktoré znamená, že vyhľadá všetky slová dlhé ``x`` až ``y``

Číslo pri ``-w/--word-length`` sa použije hlavne vtedy, ak nasleduje iba
jeden argument. Ak sa ``-w/--word-length`` nepoužije, dĺžka slova sa určí
podľa počtu argumentov. Pri použití rozpätia musí nasledovať iba jedna skupina písmen.

Argumenty
---------

Po možnostiach nasledujú argumenty. Ak sa určí dĺžka hľadaného slova cez
``-w/--word-length``, stačí ako ďalší argument napísať množinu písmen,
ktoré chceme aby heslo obsahovalo. Program potom nájde všetky slová v
zdrojovom súbore, ktoré sú tvorené iba zadanými písmenami.

Ak dĺžku slova neurčíme, tak sa dĺžka slova určí podľa počtu argumentov.
Každý argument reprezentuje písmená, ktoré majú v hľadanom slove na
danom mieste. argumenty sú oddelené medzerou.

.. list-table::
    :widths: 50 50
    :header-rows: 1

    * - Znak
      - Popis
    * - ``^``
      - ak použijeme tento znak, tak programu povieme, že nemá použiť zadanú množinu písmen
    * - ``a-z``
      - skrátený zápis množiny tvorenej písmenami a až z, môžeme použiť iné písmená ako a a z
    * - ``.``
      - reprezentuje ľubovoľný znak

Príklady
--------

.. code-block:: console

    $ susi-word-finder -i podstatne_mena_ascii.txt -w 5 abc . . ^a-f .


Zo súboru ``podstatne_mena_ascii.txt`` vyberie všetky ``5`` písmenové slová,
ktoré majú na prvej pozícii niektoré z písmen ``abc``, na druhej a tretej
pozícii môžu byť ľubovoľné znaku, na štvrtej pozícii nemôžu byť písmená
``a-f`` (a až f) a na poslednej pozícii môže byť ľubovoľné písmeno.

.. code-block:: console

    $ susi-word-finder -i PM_a -w 7 abcde


Zo súboru ``podstatne_mena_ascii.txt`` vyberie všetky ``7`` písmenové slová,
ktoré sú tvorené iba písmenami ``abcde``.
