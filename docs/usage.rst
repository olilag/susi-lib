Používanie
==========

Inštalácia
----------

Pred prvým použitím si treba knižnicu nainštalovať.

Windows
^^^^^^^
.. code-block:: console

   $ py -m pip install susi-lib

Linux
^^^^^
.. code-block:: console

   $ python -m pip install susi-lib

Niektoré linuxy (napr. Arch) vedia mať problém s globálnym inštalovaním python balíčkov.
Treba vtedy skúsiť user inštaláciu.
Ak ani to nepomôže, tak treba použiť virtual environment (napríklad builtin venv) - verím, že ak máš linux, tak vieš čo to je a nebudem to tu vysvetľovať.

V kóde
------

Na použitie v kóde treba balíček importovať.
To sa robí kľúčovým slovom ``import`` a po ňom napísať názov balíčka ``import susi_lib``.
Ďalej v kóde sa dajú jednotlivé triedy/funkcie použiť ako ``susi_lib.<podbalíček>.<vec>``,
kde vec je väčšinou nejaká funkcia/trieda a podbalíček je "cesta" k danej veci.
Štruktúra balíčka je nižšie.
Alebo sa dá daná vec importnúť aj nasledovne ``from susi_lib.<podbalíček> import <vec>``, vo zvyšku kódu potom viete danú vec používať aj iba napísaním vec bez "cesty".

Štruktúra importov
^^^^^^^^^^^^^^^^^^

| susi_lib
| ├─ functions (podbalíček)
| │   └─ obsahuje nejaké funkcie
| ├─ types (podbalíček)
| │   └─ obsahuje triedy na reprezentáciu slov v kódovaniach
| ├─ Finder (vec) - trieda na hľadanie slov pomocou aplikácie zadanej funkcie na každé slovo,
| │      táto funkcia urči, či dané slovo chceme alebo nie
| ├─ RegEx (vec) - trieda na hľadanie pomocou regulárnych výrazov
| ├─ create_regex (vec) - funkcia, ktorá vytvorí regulárny výraz z postupnosti zadaných písmen
| ├─ Selection (vec) - pomocný enum pre funkciu create_regex
| └─ Dictionary (vec) - trieda, ktorá automaticky stiahne požadovaný slovník a vráti cestu k nemu
