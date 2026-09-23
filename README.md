# Générateur de feedback LEPL1401

Ce script génère un document unique et imprimable contenant le feedback d'une
mission LEPL1401.

## Fonctionnalités

- Résume les résultats des étudiants dans une liste sur quatre colonnes.
- Affiche le score de chaque étudiant sous la forme d'un symbole facile à lire.
- Présente les exemples de code Python communs dans des blocs mis en forme.
- Ajoute les remarques générales destinées à l'ensemble du groupe.
- Indique la mission, le correcteur et la date de génération dans l'en-tête.
- Produit un fichier source Typst modifiable ainsi qu'un PDF prêt à partager.

## Prérequis

- Python 3
- [Typst](https://typst.app/) accessible avec la commande `typst`

## Télécharger les soumissions

Lors du téléchargement des soumissions, sélectionner les options suivantes :

- « Uniquement les soumissions pour évaluation » ;
- « Arborescence simplifiée » ;
- « Identifiant d'exercice/nom d'utilisateur ».

Le dossier téléchargé doit être nommé `mission_X_REAL`.

## Préparer le dossier des soumissions

Dans `mission_X_REAL`, renommer chaque dossier étudiant afin que son nom se
termine par un underscore suivi d'un score compris entre `1` et `4` :

```text
mission_X_REAL/
├── alice_4/
├── bob_3/
├── charlie_2/
└── feedback.md
```

Le score détermine le symbole affiché à côté du nom de l'étudiant :

| Score | Signification |
| --- | --- |
| `1` | Non remis |
| `2` | À clarifier |
| `3` | Bien, avec une petite erreur |
| `4` | Parfait |

Créer ensuite un fichier `feedback.md` dans `mission_X_REAL`. Séparer les
exemples de code Python par `---`. Le contenu placé après le dernier séparateur
devient le feedback général :

````markdown
def premier_exemple():
    pass

---

def deuxieme_exemple():
    pass

---

La plupart des soumissions étaient bien structurées. Pensez à documenter les
cas limites.
````

## Générer le rapport

Depuis le dossier de ce dépôt, exécuter :

```bash
python3 generate.py mission_X_REAL <NOM_DE_LA_MISSION> <NOM_DU_CORRECTEUR>
```

Mettre entre guillemets les arguments qui contiennent des espaces. Par exemple :

```bash
python3 generate.py mission_X_REAL "Mission 2" "Ada Lovelace"
```

La commande crée deux fichiers dans `mission_X_REAL` :

- `output.typst` — le document Typst généré et modifiable ;
- `output.pdf` — le rapport compilé, prêt à être partagé ou imprimé.
