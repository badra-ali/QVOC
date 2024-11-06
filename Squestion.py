import streamlit as st
import pandas as pd

# Liste des dérivés du lait
dairy_products = ['262 mozzarella','263 cheddar','264 danbo','265 edam','266 gouda','267 havarti','268 samsoe','269 emmental','270 tilsiter','271 saint paulin','273 cottage cheese','274 coulommiers','276 camembert','277 brie','275 fromage crémeux','279 beurre', '243 lait fermenté', '283 fromage','221 fromage non affiné, y compris les fromages frais','208 fromage en saumure','288 crème et crèmes préparées','272 provolone']

# Fonction pour générer un sous-questionnaire structuré selon les rubriques
def generate_sub_questionnaire(dairy_product):

    if dairy_product == '262 mozzarella':
        return {
            "Matières premières": [
                "Lait de vache ou de bufflonne, ou leurs mélanges",
                "Produits obtenus à partir de ces laits"
            ],
            "Composition": [
                "Matière grasse laitière dans l'extrait sec : teneur minimale 20% (m/m), niveau de référence 40% à 50% (m/m)",
                "Faible teneur en humidité : teneur minimale 18% (m/m), niveau de référence 40% à 50% (m/m)"
            ],
            "Additifs alimentaires": {
                "Agents de conservation": [
                    "Acide sorbique",
                    "Sorbate de sodium",
                    "Sorbate de potassium",
                    "Nisine",
                    "Pimaricine",
                    "Acide propionique",
                    "Propionate de sodium",
                    "Propionate de calcium",
                    "Propionate de potassium"
                ],
                "Régulateurs de l’acidité": [
                    "Carbonate de calcium",
                    "Acide acétique",
                    "Acétate de potassium",
                    "Diacétate de potassium",
                    "Acétate de calcium",
                    "Acide lactique (L-, D- et DL)",
                    "Acide malique (DL)",
                    "Lactate de sodium",
                    "Lactate de potassium",
                    "Lactate de calcium",
                    "Acide citrique",
                    "Acide orthophosphorique",
                    "Malate acide de sodium",
                    "Malate de sodium",
                    "Malate acide de potassium",
                    "Malate de potassium",
                    "Malate de calcium (D, L)",
                    "Carbonate de sodium",
                    "Carbonate acide de sodium",
                    "Sesquicarbonate de sodium",
                    "Carbonate de potassium",
                    "Carbonate acide de potassium",
                    "Carbonate de magnésium",
                    "Carbonate acide de magnésium",
                    "Acide chlorhydrique",
                    "Glucono-delta-lactone",
                    "Gluconate de potassium",
                    "Gluconate de calcium",
                    "Citrate biacide de sodium",
                    "Citrate biacide de potassium",
                    "Citrates de calcium",
                    "Orthophosphate monosodique",
                    "Orthophosphate disodique",
                    "Orthophosphate trisodique",
                    "Orthophosphate monopotassique",
                    "Orthophosphate dipotassique",
                    "Orthophosphate tripotassique",
                    "Orthophosphate monocalcique",
                    "Orthophosphate dicalcique",
                    "Orthophosphate tricalcique",
                    "Orthophosphate monoammonié",
                    "Orthophosphate diammonié",
                    "Orthophosphate dimagnésien",
                    "Orthophosphate trimagnésien",
                    "Diphosphate disodique",
                    "Diphosphate tétrasodique",
                    "Diphosphate tétrapotassique",
                    "Diphosphate dicalcique",
                    "Triphosphate pentasodique",
                    "Triphosphate pentapotassique",
                    "Polyphosphate de sodium",
                    "Polyphosphate de potassium",
                    "Polyphosphate de calcium",
                    "Polyphosphate d’ammonium",
                    "Agar-agar",
                    "Carragenane",
                    "Algue euchema transformée",
                    "Gomme de caroube",
                    "Gomme guar",
                    "Gomme adragante",
                    "Gomme xanthane",
                    "Gomme Karaya",
                    "Gomme tara",
                    "Pectines",
                    "Carboxyméthyl-cellulose sodique"
                ],
                "Colorants": [
                    "Chlorophylle",
                    "Complexe chlorophylle cuivre",
                    "Complexe chlorophylle cuivre, sels de sodium et de potassium",
                    "Bioxyde de titane"
                ],
                "Antiagglomérants": [
                    "Cellulose microcristalline",
                    "Cellulose en poudre",
                    "Silice amorphe",
                    "Silicate de calcium",
                    "Silicate de magnésium"
                ]
            },
            "Nom du produit": [
                "Le nom du produit doit être 'Mozzarella' et doit être conforme aux normes d'étiquetage."
            ]
        }

    elif dairy_product == '263 cheddar':
        return {
            "Matières premières": [
                "Lait de vache ou de bufflonne, ou leurs mélanges",
                "Produits obtenus à partir de ces laits"
            ],
            "Substances nutritives autorisées": [
                "Les vitamines et minéraux ajoutés respectent-ils la législation nationale ?"
            ],
            "Composition": [
                "Matière grasse laitière dans l'extrait sec : teneur minimale 22% (m/m), sans restriction pour la teneur maximale, niveau de référence 48% à 60% (m/m)",
                "Teneur en matière grasse dans l'extrait sec égale ou supérieure à 22% mais inférieure à 30% : teneur minimale en matière sèche correspondante 49% (m/m)",
                "Teneur en matière grasse dans l'extrait sec égale ou supérieure à 30% mais inférieure à 40% : teneur minimale en matière sèche correspondante 53% (m/m)",
                "Teneur en matière grasse dans l'extrait sec égale ou supérieure à 40% mais inférieure à 48% : teneur minimale en matière sèche correspondante 57% (m/m)",
                "Teneur en matière grasse dans l'extrait sec égale ou supérieure à 48% mais inférieure à 60% : teneur minimale en matière sèche correspondante 61% (m/m)",
                "Teneur en matière grasse dans l'extrait sec égale ou supérieure à 60% : teneur minimale en matière sèche correspondante 66% (m/m)"
            ],
            "Additifs alimentaires": {
                "Colorants": [
                    "X (masse du fromage), traitement de la surface/croûte (–)"
                ],
                "Agents blanchissants": [
                    "Masse du fromage (–), traitement de la surface/croûte (–)"
                ],
                "Régulateurs de l’acidité": [
                    "X (masse du fromage), traitement de la surface/croûte (–)"
                ],
                "Stabilisants": [
                    "Masse du fromage (–), traitement de la surface/croûte (–)"
                ],
                "Épaississants": [
                    "Masse du fromage (–), traitement de la surface/croûte (–)"
                ],
                "Émulsifiants": [
                    "Masse du fromage (–), traitement de la surface/croûte (–)"
                ],
                "Antioxydants": [
                    "Masse du fromage (–), traitement de la surface/croûte (–)"
                ],
                "Conservateurs": [
                    "X (masse du fromage), traitement de la surface/croûte (X)"
                ],
                "Agents moussants": [
                    "Masse du fromage (–), traitement de la surface/croûte (–)"
                ],
                "Antiagglomérants": [
                    "Masse du fromage (–), traitement de la surface/croûte X(b)"
                ]
            },
            "Nom du produit": [
                "Le nom du produit doit être 'Cheddar' et doit être conforme aux normes d'étiquetage."
            ]
        }

    elif dairy_product == '264 danbo':
        return {
            "Matières premières": [
                "Lait de vache ou de bufflonne, ou leurs mélanges",
                "Produits obtenus à partir de ces laits"
            ],
            "Substances nutritives autorisées": [
                "Les vitamines et minéraux ajoutés respectent-ils la législation nationale ?"
            ],
            "Composition": [
                "Matière grasse laitière dans l'extrait sec : teneur minimale 20% (m/m), sans restriction pour la teneur maximale, niveau de référence 45% à 55% (m/m)",
                "Teneur en matière grasse dans l'extrait sec égale ou supérieure à 20% mais inférieure à 30% : teneur minimale en matière sèche correspondante 41% (m/m)"
            ],
            "Additifs alimentaires": {
                "Colorants": [
                    "X (masse du fromage), traitement de la surface/croûte (–)"
                ],
                "Agents blanchissants": [
                    "Masse du fromage (–), traitement de la surface/croûte (–)"
                ],
                "Régulateurs de l’acidité": [
                    "X (masse du fromage), traitement de la surface/croûte (–)"
                ],
                "Stabilisants": [
                    "Masse du fromage (–), traitement de la surface/croûte (–)"
                ],
                "Épaississants": [
                    "Masse du fromage (–), traitement de la surface/croûte (–)"
                ],
                "Émulsifiants": [
                    "Masse du fromage (–), traitement de la surface/croûte (–)"
                ],
                "Antioxydants": [
                    "Masse du fromage (–), traitement de la surface/croûte (–)"
                ],
                "Conservateurs": [
                    "X (masse du fromage), traitement de la surface/croûte (X)"
                ],
                "Agents moussants": [
                    "Masse du fromage (–), traitement de la surface/croûte (–)"
                ],
                "Antiagglomérants": [
                    "Masse du fromage (–), traitement de la surface/croûte X(b)"
                ]
            },
            "Nom du produit": [
                "Le nom du produit doit être 'Danbo' et doit être conforme aux normes d'étiquetage."
            ]
        }

    elif dairy_product == '265 edam':
        return {
            "Matières premières": [
                "Lait de vache ou de bufflonne, ou leurs mélanges",
                "Produits obtenus à partir de ces laits"
            ],
            "Substances nutritives autorisées": [
                "Les vitamines et minéraux ajoutés respectent-ils la législation nationale ?"
            ],
            "Composition": [
                "Matière grasse laitière dans l'extrait sec : teneur minimale 30% (m/m), sans restriction pour la teneur maximale, niveau de référence 40% à 50% (m/m)",
                "Teneur en matière grasse dans l'extrait sec égale ou supérieure à 30% mais inférieure à 40% : teneur minimale en matière sèche correspondante 47% (m/m)"
            ],
            "Additifs alimentaires": {
                "Colorants": [
                    "X (masse du fromage), traitement de la surface/croûte (–)",
                    "Béta-carotène, synthétique",
                    "Béta-carotène, Blakeslea trispora",
                    "Béta-apo-8’-caroténal",
                    "Acide béta",
                    "Extraits de rocou – base de norbixine"
                ],
                "Agents blanchissants": [
                    "Masse du fromage (–), traitement de la surface/croûte (–)"
                ],
                "Régulateurs de l’acidité": [
                    "X (masse du fromage), traitement de la surface/croûte (–)",
                    "Carbonate de calcium",
                    "Carbonate de magnésium",
                    "Glucono-delta-lactone"
                ],
                "Stabilisants": [
                    "Masse du fromage (–), traitement de la surface/croûte (–)"
                ],
                "Épaississants": [
                    "Masse du fromage (–), traitement de la surface/croûte (–)"
                ],
                "Émulsifiants": [
                    "Masse du fromage (–), traitement de la surface/croûte (–)"
                ],
                "Antioxydants": [
                    "Masse du fromage (–), traitement de la surface/croûte (–)"
                ],
                "Conservateurs": [
                    "X (masse du fromage), traitement de la surface/croûte (X)",
                    "Lysozyme",
                    "Acide sorbique",
                    "Sorbate de sodium",
                    "Sorbate de potassium",
                    "Sorbate de calcium",
                    "Nisine",
                    "Pimaricine (natamycine) - traitement de surface uniquement",
                    "Nitrate de sodium",
                    "Nitrate de potassium",
                    "Acide propionique",
                    "Propionate de sodium",
                    "Propionate de potassium"
                ],
                "Agents moussants": [
                    "Masse du fromage (–), traitement de la surface/croûte (–)"
                ],
                "Antiagglomérants": [
                    "Masse du fromage (–), traitement de la surface/croûte X(b)",
                    "Cellulose microcristalline",
                    "Cellulose en poudre",
                    "Silice amorphe",
                    "Silicate de calcium",
                    "Silicate de magnésium",
                    "Talc"
                ]
            },
            "Nom du produit": [
                "Le nom du produit doit être 'Edam' et doit être conforme aux normes d'étiquetage."
            ]
        }

    elif dairy_product == '266 gouda':
        return {
            "Matières premières": [
                "Lait de vache ou de bufflonne, ou leurs mélanges",
                "Produits obtenus à partir de ces laits"
            ],
            "Composition": [
                "Matière grasse laitière dans l'extrait sec : teneur minimale 30% (m/m), sans restriction pour la teneur maximale, niveau de référence 48% à 55% (m/m)",
                "Teneur en matière grasse dans l'extrait sec égale ou supérieure à 30% mais inférieure à 40% : teneur minimale en matière sèche correspondante 48% (m/m)"
            ],
            "Additifs alimentaires": {
                "Colorants": [
                    "X (masse du fromage), traitement de la surface/croûte (–)",
                    "Béta-carotène",
                    "Béta-carotène, Blakeslea trispora",
                    "Béta-apo-8’-caroténal",
                    "Acide béta-apo-8’-caroténique, ester méthylique ou éthylique",
                    "Extraits de rocou – base de norbixine"
                ],
                "Agents blanchissants": [
                    "Masse du fromage (–), traitement de la surface/croûte (–)"
                ],
                "Régulateurs de l’acidité": [
                    "X (masse du fromage), traitement de la surface/croûte (–)",
                    "Carbonate de calcium",
                    "Carbonate de magnésium",
                    "Glucono-delta-lactone"
                ],
                "Stabilisants": [
                    "Masse du fromage (–), traitement de la surface/croûte (–)"
                ],
                "Épaississants": [
                    "Masse du fromage (–), traitement de la surface/croûte (–)"
                ],
                "Émulsifiants": [
                    "Masse du fromage (–), traitement de la surface/croûte (–)"
                ],
                "Antioxydants": [
                    "Masse du fromage (–), traitement de la surface/croûte (–)"
                ],
                "Conservateurs": [
                    "X (masse du fromage), traitement de la surface/croûte (X)",
                    "Lysozyme",
                    "Acide sorbique",
                    "Sorbate de sodium",
                    "Sorbate de potassium",
                    "Sorbate de calcium",
                    "Nisine",
                    "Pimaricine (natamycine) - traitement de surface uniquement",
                    "Nitrate de sodium",
                    "Nitrate de potassium",
                    "Acide propionique",
                    "Propionate de sodium",
                    "Propionate de potassium"
                ],
                "Agents moussants": [
                    "Masse du fromage (–), traitement de la surface/croûte (–)"
                ],
                "Antiagglomérants": [
                    "Masse du fromage (–), traitement de la surface/croûte X(b)",
                    "Cellulose microcristalline",
                    "Cellulose en poudre",
                    "Silice amorphe",
                    "Silicate de calcium",
                    "Silicate de magnésium",
                    "Talc"
                ]
            },
            "Nom du produit": [
                "Le nom du produit doit être 'Gouda' et doit être conforme aux normes d'étiquetage."
            ]
        }

    elif dairy_product == '267 havarti':
        return {
            "Matières premières": [
                "Lait de vache ou de bufflonne, ou leurs mélanges",
                "Produits obtenus à partir de ces laits"
            ],
            "Composition": [
                "Matière grasse laitière dans l'extrait sec : teneur minimale 30% (m/m), sans restriction pour la teneur maximale, niveau de référence 45% à 55% (m/m)",
                "Teneur en matière grasse dans l'extrait sec égale ou supérieure à 30% mais inférieure à 40% : teneur minimale en matière sèche correspondante 46% (m/m)"
            ],
            "Additifs alimentaires": {
                "Colorants": [
                    "X (masse du fromage), traitement de la surface/croûte (–)",
                    "Béta-carotène",
                    "Béta-carotène, Blakeslea trispora",
                    "Béta-apo-8’-caroténal",
                    "Acide béta-apo-8’-caroténique, ester méthylique ou éthylique",
                    "Extraits de rocou"
                ],
                "Agents blanchissants": [
                    "Masse du fromage (–), traitement de la surface/croûte (–)"
                ],
                "Régulateurs de l’acidité": [
                    "X (masse du fromage), traitement de la surface/croûte (–)",
                    "Carbonate de calcium",
                    "Carbonate de magnésium",
                    "Glucono-delta-lactone"
                ],
                "Stabilisants": [
                    "Masse du fromage (–), traitement de la surface/croûte (–)"
                ],
                "Épaississants": [
                    "Masse du fromage (–), traitement de la surface/croûte (–)"
                ],
                "Émulsifiants": [
                    "Masse du fromage (–), traitement de la surface/croûte (–)"
                ],
                "Antioxydants": [
                    "Masse du fromage (–), traitement de la surface/croûte (–)"
                ],
                "Conservateurs": [
                    "X (masse du fromage), traitement de la surface/croûte (X)",
                    "Lysozyme",
                    "Acide sorbique",
                    "Sorbate de sodium",
                    "Sorbate de potassium",
                    "Sorbate de calcium",
                    "Nisine",
                    "Pimaricine (natamycine) - traitement de surface uniquement",
                    "Nitrate de sodium",
                    "Nitrate de potassium",
                    "Acide propionique",
                    "Propionate de sodium",
                    "Propionate de potassium"
                ],
                "Agents moussants": [
                    "Masse du fromage (–), traitement de la surface/croûte (–)"
                ],
                "Antiagglomérants": [
                    "Masse du fromage (–), traitement de la surface/croûte X(b)",
                    "Cellulose microcristalline",
                    "Cellulose en poudre",
                    "Silice amorphe",
                    "Silicate de calcium",
                    "Silicate de magnésium",
                    "Talc"
                ]
            },
            "Nom du produit": [
                "Le nom du produit doit être 'Havarti' et doit être conforme aux normes d'étiquetage."
            ]
        }

    elif dairy_product == '268 samsoe':
        return {
            "Matières premières": [
                "Lait de vache ou de bufflonne, ou leurs mélanges",
                "Produits obtenus à partir de ces laits"
            ],
            "Composition": [
                "Matière grasse laitière dans l'extrait sec : teneur minimale 30% (m/m), sans restriction pour la teneur maximale, niveau de référence 45% à 55% (m/m)",
                "Teneur en matière grasse dans l'extrait sec égale ou supérieure à 30% mais inférieure à 40% : teneur minimale en matière sèche correspondante 46% (m/m)"
            ],
            "Additifs alimentaires": {
                "Colorants": [
                    "X (masse du fromage), traitement de la surface/croûte (–)",
                    "Béta-carotène",
                    "Béta-carotène, Blakeslea trispora",
                    "Béta-apo-8’-caroténal",
                    "Acide béta-apo-8’-caroténique, ester méthylique ou éthylique",
                    "Extraits de rocou – base de norbixine"
                ],
                "Agents blanchissants": [
                    "Masse du fromage (–), traitement de la surface/croûte (–)"
                ],
                "Régulateurs de l’acidité": [
                    "X (masse du fromage), traitement de la surface/croûte (–)",
                    "Carbonate de calcium",
                    "Carbonate de magnésium",
                    "Glucono-delta-lactone"
                ],
                "Stabilisants": [
                    "Masse du fromage (–), traitement de la surface/croûte (–)"
                ],
                "Épaississants": [
                    "Masse du fromage (–), traitement de la surface/croûte (–)"
                ],
                "Émulsifiants": [
                    "Masse du fromage (–), traitement de la surface/croûte (–)"
                ],
                "Antioxydants": [
                    "Masse du fromage (–), traitement de la surface/croûte (–)"
                ],
                "Conservateurs": [
                    "X (masse du fromage), traitement de la surface/croûte (X)",
                    "Lysozyme",
                    "Acide sorbique",
                    "Sorbate de sodium",
                    "Sorbate de potassium",
                    "Sorbate de calcium",
                    "Nisine",
                    "Pimaricine - traitement de surface uniquement",
                    "Nitrate de sodium",
                    "Nitrate de potassium",
                    "Acide propionique",
                    "Propionate de sodium",
                    "Propionate de potassium"
                ],
                "Agents moussants": [
                    "Masse du fromage (–), traitement de la surface/croûte (–)"
                ],
                "Antiagglomérants": [
                    "Masse du fromage (–), traitement de la surface/croûte X(b)",
                    "Cellulose microcristalline",
                    "Cellulose en poudre",
                    "Silice amorphe",
                    "Silicate de calcium",
                    "Silicate de magnésium",
                    "Talc"
                ]
            },
            "Nom du produit": [
                "Le nom du produit doit être 'Samsoe' et doit être conforme aux normes d'étiquetage."
            ]
        }

    elif dairy_product == '269 emmental':
        return {
            "Matières premières": [
                "Lait de vache ou de bufflonne, ou leurs mélanges"
            ],
            "Composition": [
                "Matière grasse laitière dans l'extrait sec : teneur minimale 45% (m/m), sans restriction pour la teneur maximale, niveau de référence 45% à 55% (m/m)",
                "Teneur en matière grasse dans l'extrait sec égale ou supérieure à 45% mais inférieure à 50% : teneur minimale en matière sèche correspondante 60% (m/m)"
            ],
            "Additifs alimentaires": {
                "Colorants": [
                    "X (masse du fromage), traitement de la surface/croûte (–)",
                    "Béta-carotène",
                    "Béta-carotène, Blakeslea trispora",
                    "Béta-apo-8’-caroténal",
                    "Acide béta-apo-8’-caroténique",
                    "Extraits de rocou"
                ],
                "Agents blanchissants": [
                    "Masse du fromage (–), traitement de la surface/croûte (–)"
                ],
                "Régulateurs de l’acidité": [
                    "X (masse du fromage), traitement de la surface/croûte (–)",
                    "Carbonate de calcium",
                    "Carbonate de magnésium",
                    "Glucono-delta-lactone"
                ],
                "Stabilisants": [
                    "Masse du fromage (–), traitement de la surface/croûte (–)"
                ],
                "Épaississants": [
                    "Masse du fromage (–), traitement de la surface/croûte (–)"
                ],
                "Émulsifiants": [
                    "Masse du fromage (–), traitement de la surface/croûte (–)"
                ],
                "Antioxydants": [
                    "Masse du fromage (–), traitement de la surface/croûte (–)"
                ],
                "Conservateurs": [
                    "X (masse du fromage), traitement de la surface/croûte (X)",
                    "Lysozyme",
                    "Acide sorbique",
                    "Sorbate de sodium",
                    "Sorbate de potassium",
                    "Sorbate de calcium",
                    "Nisine",
                    "Pimaricine (natamycine)"
                ],
                "Agents moussants": [
                    "Masse du fromage (–), traitement de la surface/croûte (–)"
                ],
                "Antiagglomérants": [
                    "Masse du fromage (–), traitement de la surface/croûte X(b)",
                    "Cellulose microcristalline",
                    "Cellulose en poudre",
                    "Silice amorphe",
                    "Silicate de calcium",
                    "Silicate de magnésium",
                    "Talc"
                ]
            },
            "Nom du produit": [
                "Le nom du produit doit être 'Emmental' et doit être conforme aux normes d'étiquetage."
            ]
        }

    elif dairy_product == '270 tilsiter':
        return {
            "Matières premières": [
                "Lait de vache ou de bufflonne, ou leurs mélanges",
                "Produits obtenus à partir de ces laits"
            ],
            "Composition": [
                "Matière grasse laitière dans l'extrait sec : teneur minimale 45% (m/m), sans restriction pour la teneur maximale, niveau de référence 45% à 55% (m/m)",
                "Teneur en matière grasse dans l'extrait sec égale ou supérieure à 30% mais inférieure à 40% : teneur minimale en matière sèche correspondante 49% (m/m)"
            ],
            "Additifs alimentaires": {
                "Colorants": [
                    "X (masse du fromage), traitement de la surface/croûte (–)",
                    "Béta-carotène",
                    "Béta-apo-8’-caroténal",
                    "Acide béta-apo-8’-caroténique",
                    "Extraits de rocou"
                ],
                "Agents blanchissants": [
                    "Masse du fromage (–), traitement de la surface/croûte (–)"
                ],
                "Régulateurs de l’acidité": [
                    "X (masse du fromage), traitement de la surface/croûte (–)",
                    "Carbonate de calcium",
                    "Carbonate de magnésium",
                    "Glucono-delta-lactone"
                ],
                "Stabilisants": [
                    "Masse du fromage (–), traitement de la surface/croûte (–)"
                ],
                "Épaississants": [
                    "Masse du fromage (–), traitement de la surface/croûte (–)"
                ],
                "Émulsifiants": [
                    "Masse du fromage (–), traitement de la surface/croûte (–)"
                ],
                "Antioxydants": [
                    "Masse du fromage (–), traitement de la surface/croûte (–)"
                ],
                "Conservateurs": [
                    "X (masse du fromage), traitement de la surface/croûte (X)",
                    "Lysozyme",
                    "Acide sorbique",
                    "Sorbate de sodium",
                    "Sorbate de potassium",
                    "Sorbate de calcium",
                    "Nisine",
                    "Pimaricine"
                ],
                "Agents moussants": [
                    "Masse du fromage (–), traitement de la surface/croûte (–)"
                ],
                "Antiagglomérants": [
                    "Masse du fromage (–), traitement de la surface/croûte X(b)",
                    "Cellulose microcristalline",
                    "Cellulose en poudre",
                    "Silice amorphe",
                    "Silicate de calcium",
                    "Silicate de magnésium",
                    "Talc"
                ]
            },
            "Nom du produit": [
                "Le nom du produit doit être 'Tilsiter' et doit être conforme aux normes d'étiquetage."
            ]
        }

    elif dairy_product == '271 saint paulin':
        return {
            "Matières premières": [
                "Lait de vache ou de bufflonne, ou leurs mélanges",
                "Produits obtenus à partir de ces laits"
            ],
            "Composition": [
                "Matière grasse laitière dans l'extrait sec : teneur minimale 40% (m/m), sans restriction pour la teneur maximale, niveau de référence 40% à 50% (m/m)",
                "Teneur en matière grasse dans l'extrait sec égale ou supérieure à 40% mais inférieure à 60% : teneur minimale en matière sèche correspondante 44% (m/m)"
            ],
            "Additifs alimentaires": {
                "Colorants": [
                    "X (masse du fromage), traitement de la surface/croûte (–)",
                    "Béta-carotène",
                    "Béta-carotène, Blakeslea trispora",
                    "Béta-apo-8’-caroténal",
                    "Acide béta-apo-8’-caroténique, ester méthylique",
                    "Extraits de rocou"
                ],
                "Agents blanchissants": [
                    "Masse du fromage (–), traitement de la surface/croûte (–)"
                ],
                "Régulateurs de l’acidité": [
                    "X (masse du fromage), traitement de la surface/croûte (–)",
                    "Carbonate de calcium",
                    "Carbonate de magnésium",
                    "Glucono-delta-lactone"
                ],
                "Stabilisants": [
                    "Masse du fromage (–), traitement de la surface/croûte (–)"
                ],
                "Épaississants": [
                    "Masse du fromage (–), traitement de la surface/croûte (–)"
                ],
                "Émulsifiants": [
                    "Masse du fromage (–), traitement de la surface/croûte (–)"
                ],
                "Antioxydants": [
                    "Masse du fromage (–), traitement de la surface/croûte (–)"
                ],
                "Conservateurs": [
                    "X (masse du fromage), traitement de la surface/croûte (X)",
                    "Lysozyme",
                    "Acide sorbique",
                    "Sorbate de sodium",
                    "Sorbate de potassium",
                    "Sorbate de calcium",
                    "Nisine",
                    "Pimaricine"
                ],
                "Agents moussants": [
                    "Masse du fromage (–), traitement de la surface/croûte (–)"
                ],
                "Antiagglomérants": [
                    "Masse du fromage (–), traitement de la surface/croûte X(b)",
                    "Cellulose microcristalline",
                    "Cellulose en poudre",
                    "Silice amorphe",
                    "Silicate de calcium",
                    "Silicate de magnésium",
                    "Talc"
                ]
            },
            "Nom du produit": [
                "Le nom du produit doit être 'Saint Paulin' et doit être conforme aux normes d'étiquetage."
            ]
        }
    elif dairy_product == '272 provolone':
        return {
            "Matières premières": [
                "Lait de vache ou de bufflonne, ou leurs mélanges",
                "Produits obtenus à partir de ces laits"
            ],
            "Composition": [
                "Matière grasse laitière dans l'extrait sec : teneur minimale 45% (m/m), sans restriction pour la teneur maximale, niveau de référence 45% à 50% (m/m)",
                "Teneur en matière grasse dans l'extrait sec égale ou supérieure à 45% mais inférieure à 50% : teneur minimale en matière sèche correspondante 51% (m/m)"
            ],
            "Additifs alimentaires": {
                "Colorants": [
                    "Masse du fromage, traitement de la surface/croûte (–)",
                    "Béta-carotène",
                    "Béta-apo-8’-caroténal",
                    "Acide béta-apo-8’-caroténique, ester méthylique",
                    "Extraits de rocou – base de norbixine"
                ],
                "Agents blanchissants": [
                    "Masse du fromage (–), traitement de la surface/croûte (–)"
                ],
                "Régulateurs de l’acidité": [
                    "X (masse du fromage), traitement de la surface/croûte (–)",
                    "Carbonate de calcium",
                    "Glucono-delta-lactone"
                ],
                "Stabilisants": [
                    "Masse du fromage (–), traitement de la surface/croûte (–)"
                ],
                "Épaississants": [
                    "Masse du fromage (–), traitement de la surface/croûte (–)"
                ],
                "Émulsifiants": [
                    "Masse du fromage (–), traitement de la surface/croûte (–)"
                ],
                "Antioxydants": [
                    "Masse du fromage (–), traitement de la surface/croûte (–)"
                ],
                "Conservateurs": [
                    "X (masse du fromage), traitement de la surface/croûte (X)",
                    "Lysozyme",
                    "Acide sorbique",
                    "Sorbate de sodium",
                    "Sorbate de potassium",
                    "Sorbate de calcium",
                    "Nisine",
                    "Pimaricine (natamycine)",
                    "Hexaméthylène-tétramine - traitement de surface uniquement",
                    "Nitrate de sodium",
                    "Nitrate de potassium",
                    "Acide propionique",
                    "Propionate de sodium",
                    "Propionate de potassium"
                ],
                "Agents moussants": [
                    "Masse du fromage (–), traitement de la surface/croûte (–)"
                ],
                "Antiagglomérants": [
                    "Masse du fromage (–), traitement de la surface/croûte X(b)",
                    "Cellulose microcristalline",
                    "Cellulose en poudre",
                    "Silice amorphe",
                    "Silicate de calcium",
                    "Silicate de magnésium",
                    "Talc"
                ]
            },
            "Nom du produit": [
                "Le nom du produit doit être 'Provolone' et doit être conforme aux normes d'étiquetage."
            ]
        }
    

    elif dairy_product == '273 cottage cheese':
        return {
            "Matières premières": [
                "Lait de vache ou de bufflonne, ou leurs mélanges",
                "Produits obtenus à partir de ces laits"
            ],
            "Composition": [
                "Matière grasse laitière dans l'extrait sec : teneur minimale 0% (m/m), sans restriction pour la teneur maximale",
                "Matière sèche dégraissée : teneur minimale 18% (m/m), sans restriction pour la teneur maximale"
            ],
            "Additifs alimentaires": {
                "Agents de conservation": [
                    "Acide sorbique",
                    "Sorbate de sodium",
                    "Sorbate de potassium",
                    "Sorbate de calcium",
                    "Nisine",
                    "Acide propionique",
                    "Propionate de sodium",
                    "Propionate de calcium",
                    "Propionate de potassium"
                ],
                "Régulateurs de l’acidité": [
                    "Carbonate de calcium",
                    "Acide acétique",
                    "Acétate de potassium",
                    "Diacétate de potassium",
                    "Acétate de calcium",
                    "Acide lactique (L-, D- et DL)",
                    "Acide malique (DL)",
                    "Lactate de sodium",
                    "Lactate de potassium",
                    "Lactate de calcium",
                    "Acide citrique",
                    "Acide orthophosphorique",
                    "Malate acide de sodium",
                    "Malate de sodium",
                    "Malate acide de potassium",
                    "Malate de potassium",
                    "Malate de calcium (D, L)",
                    "Carbonate de sodium",
                    "Carbonate acide de sodium",
                    "Sesquicarbonate de sodium",
                    "Carbonate de potassium",
                    "Carbonate acide de potassium",
                    "Carbonate de magnésium",
                    "Carbonate acide de magnésium",
                    "Acide chlorhydrique",
                    "Glucono-delta-lactone",
                    "Gluconate de potassium",
                    "Gluconate de calcium"
                ],
                "Stabilisants": [
                    "Citrate biacide de sodium",
                    "Citrate biacide de potassium",
                    "Citrates de calcium",
                    "Orthophosphate monosodique",
                    "Orthophosphate disodique",
                    "Orthophosphate trisodique",
                    "Orthophosphate monopotassique",
                    "Orthophosphate dipotassique",
                    "Orthophosphate tripotassique",
                    "Orthophosphate monocalcique",
                    "Orthophosphate dicalcique",
                    "Orthophosphate tricalcique",
                    "Orthophosphate monoammonié",
                    "Orthophosphate diammonié",
                    "Orthophosphate trimagnésien",
                    "Diphosphate disodique",
                    "Diphosphate tétrasodique",
                    "Diphosphate tétrapotassique",
                    "Diphosphate dicalcique",
                    "Triphosphate pentasodique",
                    "Triphosphate pentapotassique",
                    "Polyphosphate de sodium",
                    "Polyphosphate de potassium",
                    "Polyphosphate de calcium",
                    "Polyphosphate d’ammonium",
                    "Acide alginique",
                    "Alginate de sodium",
                    "Alginate de potassium",
                    "Alginate d’ammonium",
                    "Alginate de calcium",
                    "Alginate de propylène glycol",
                    "Agar-agar",
                    "Carragenane",
                    "Algue euchema transformée",
                    "Gomme de caroube",
                    "Gomme guar",
                    "Gomme adragante",
                    "Gomme xanthane",
                    "Gomme karaya",
                    "Gomme tara",
                    "Pectines",
                    "Carboxyméthyl-cellulose sodique",
                    "Dextrines, amidon torréfié",
                    "Amidon traité aux acides",
                    "Amidon traité aux alcalis",
                    "Amidon blanchi",
                    "Amidon oxydé",
                    "Amidons traités aux enzymes",
                    "Phosphate de monoamidon",
                    "Phosphate de diamidon",
                    "Phosphate de diamidon phosphate",
                    "Phosphate de diamidon acétyle",
                    "Acétate d’amidon",
                    "Adipate de diamidon acétyle",
                    "Amidon hydroxypropylique",
                    "Phosphate de diamidon hydroxy"
                ]
            },
            "Nom du produit": [
                "Le nom du produit doit être 'Cottage Cheese' et doit être conforme aux normes d'étiquetage."
            ]
        }

    elif dairy_product == '274 coulommiers':
        return {
            "Matières premières": [
                "Lait de vache ou de bufflonne, ou leurs mélanges",
                "Produits obtenus à partir de ces laits"
            ],
            "Composition": [
                "Matière grasse laitière dans l'extrait sec : teneur minimale 40% (m/m), sans restriction pour la teneur maximale, niveau de référence 40% à 50% (m/m)",
                "Teneur en matière grasse dans l'extrait sec égale ou supérieure à 40% mais inférieure à 50% : teneur minimale en matière sèche correspondante 42% (m/m)"
            ],
            "Additifs alimentaires": {
                "Colorants": [
                    "Béta-carotène, synthétique",
                    "Béta-carotène, Blakeslea trispora",
                    "Béta-apo-8’-caroténal",
                    "Acide béta-apo-8’-caroténique, ester méthylique",
                    "Béta-carotène",
                    "Extraits de rocou – base de norbixine"
                ],
                "Régulateurs de l’acidité": [
                    "Glucono-delta-lactone"
                ]
            },
            "Nom du produit": [
                "Le nom du produit doit être 'Coulommiers' et doit être conforme aux normes d'étiquetage."
            ]
        }
    
    elif dairy_product == '276 camembert':
        return {
            "Matières premières": [
                "Lait de vache ou de bufflonne",
                "Produits obtenus à partir de ces laits"
            ],
            "Composition": [
                "Matière grasse laitière dans l'extrait sec : minimum 30% (m/m)",
                "Teneur en matière sèche minimale : 38% si la matière grasse dans l'extrait sec est entre 30% et 40%",
                "41% si la matière grasse dans l'extrait sec est entre 40% et 45%",
                "43% si la matière grasse dans l'extrait sec est entre 45% et 55%",
                "48% si la matière grasse dans l'extrait sec est supérieure à 55%"
            ],
            "Additifs alimentaires": {
                "Colorants": [
                    "X (masse du fromage), traitement de la surface/croûte (–)"
                ],
                "Agents blanchissants": [
                    "Masse du fromage (–), traitement de la surface/croûte (–)"
                ],
                "Régulateurs de l’acidité": [
                    "X (masse du fromage), traitement de la surface/croûte (–)"
                ],
                "Stabilisants": [
                    "Masse du fromage (–), traitement de la surface/croûte (–)"
                ],
                "Épaississants": [
                    "Masse du fromage (–), traitement de la surface/croûte (–)"
                ],
                "Émulsifiants": [
                    "Masse du fromage (–), traitement de la surface/croûte (–)"
                ],
                "Antioxydants": [
                    "Masse du fromage (–), traitement de la surface/croûte (–)"
                ],
                "Conservateurs": [
                    "Masse du fromage (–), traitement de la surface/croûte (–)"
                ],
                "Agents moussants": [
                    "Masse du fromage (–), traitement de la surface/croûte (–)"
                ],
                "Antiagglomérants": [
                    "Masse du fromage (–), traitement de la surface/croûte (–)"
                ]
            },
            "Nom du produit": [
                "Le nom du produit doit être 'Camembert' et doit être conforme aux normes d'étiquetage."
            ]
        }
    elif dairy_product == '277 brie':
        return {
            "Matières premières": [
                "Lait de vache ou de bufflonne, ou leurs mélanges",
                "Produits obtenus à partir de ces laits"
            ],
            "Composition": [
                "Matière grasse laitière dans l'extrait sec : minimum 40% (m/m)",
                "Teneur en matière sèche minimale : 42% si la matière grasse dans l'extrait sec est comprise entre 40% et 45%",
                "43% si la matière grasse dans l'extrait sec est comprise entre 45% et 55%",
                "48% si la matière grasse dans l'extrait sec est comprise entre 55% et 60%",
                "51% si la matière grasse dans l'extrait sec est supérieure à 60%"
            ],
            "Additifs alimentaires": {
                "Colorants": [
                    "Béta-carotène",
                    "Béta-apo-8’-caroténal",
                    "Acide béta-apo-8’-caroténique, ester méthylique",
                    "Extraits de rocou – base de norbixine"
                ],
                "Régulateurs de l’acidité": [
                    "Glucono-delta-lactone"
                ]
            },
            "Nom du produit": [
                "Le nom du produit doit être 'Brie' et doit être conforme aux normes d'étiquetage."
            ]
        }
    elif dairy_product == '288 crème et crèmes préparées':
        return {
            "Matières premières": [
                "Lait",
                "Beurre",
                "Laits en poudre",
                "Crèmes",
                "Babeurre"
            ],
            "Additifs alimentaires": {
                "Régulateurs de l’acidité": [
                    "Acide lactique (L, D et DL)",
                    "Lactate de sodium",
                    "Lactate de potassium",
                    "Lactate de calcium",
                    "Acide citrique",
                    "Citrates de calcium",
                    "Carbonate de sodium",
                    "Carbonate acide de sodium",
                    "Sesquicarbonate de sodium",
                    "Carbonate de potassium",
                    "Carbonate acide de potassium"
                ],
                "Épaississants et Stabilisants": [
                    "Carbonate de calcium",
                    "Citrate de sodium dihydrogène",
                    "Citrate trisodique",
                    "Citrate monopotassique",
                    "Citrate tripotassique",
                    "Orthophosphate monosodique",
                    "Orthophosphate disodique",
                    "Orthophosphate trisodique",
                    "Orthophosphate monopotassique",
                    "Orthophosphate dipotassique",
                    "Orthophosphate tripotassique",
                    "Orthophosphate monocalcique",
                    "Orthophosphate dicalcique",
                    "Orthophosphate tricalcique",
                    "Diphosphate disodique",
                    "Diphosphate trisodique",
                    "Diphosphate tétrasodique",
                    "Diphosphate tétrapostassique",
                    "Diphosphate dicalcique",
                    "Diphosphate biacide de calcium",
                    "Triphosphate pentasodique",
                    "Triphosphate pentapotassique",
                    "Polyphosphate sodique",
                    "Polyphosphate potassique",
                    "Polyphosphate calcio-sodique",
                    "Polyphosphate calcique",
                    "Polyphosphate d’ammonium",
                    "Acide alginique",
                    "Alginate de sodium",
                    "Alginate de potassium",
                    "Alginate d’ammonium",
                    "Alginate de calcium",
                    "Alginate de propylène-glycol",
                    "Agar-agar",
                    "Carraghénane",
                    "Algues euchema transformées",
                    "Gomme de caroube",
                    "Gomme de guar",
                    "Gomme arabique",
                    "Gomme de xanthane",
                    "Gomme gellane",
                    "Pectines",
                    "Cellulose microcristalline",
                    "Cellulose en poudre",
                    "Méthylcellulose",
                    "Hydroxypropylcellulose",
                    "Hydroxypropylméthylcellulose",
                    "Méthyléthylcellulose",
                    "Carboxyméthylcellulose sodique",
                    "Esters glycéroliques de l’acide diacétyltartarique et d’acides gras",
                    "Chlorure de potassium",
                    "Chlorure de sodium",
                    "Phosphate de mono-amidon",
                    "Phosphate de diamidon phosphaté",
                    "Phosphate de diamidon acétylé",
                    "Acétate d’amidon estérifié à l’anhydride acétique",
                    "Adipate de diamidon acétylé",
                    "Amidon hydroxypropyle",
                    "Phosphate de diamidon hydroxypropyle",
                    "Octényle succinate d’amidon sodique"
                ],
                "Émulsifiants": [
                    "Lécithine",
                    "Monolaurate de polyoxyéthylène (20) sorbitane",
                    "Monooléate de polyoxyéthylène (20) sorbitane",
                    "Monopalmitate de polyoxyéthylène (20) sorbitane",
                    "Monostéarate de polyoxyéthylène (20) sorbitane",
                    "Tristéarate de polyoxyéthylène (20) sorbitane",
                    "Mono- et diglycérides d’acides gras",
                    "Esters d’acides acétiques et d’acides gras de glycérol",
                    "Esters d’acides lactiques et d’acides gras de glycérol",
                    "Esters d’acides citriques et d’acides gras de glycérol",
                    "Esters de saccharose d’acides gras",
                    "Esters polyglycéroliques d’acides gras",
                    "Monostéarate de sorbitane",
                    "Tristéarate de sorbitane",
                    "Monolaurate de sorbitane",
                    "Monooléate de sorbitane",
                    "Monopalmitate de sorbitane"
                ],
                "Gaz de conditionnement": [
                    "Dioxyde de carbone",
                    "Azote"
                ],
                "Propulseurs": [
                    "Oxyde nitreux"
                ]
            },
            "Nom du produit": [
                "Le nom du produit doit être 'Crème' ou 'Crèmes préparées' et doit être conforme aux normes d'étiquetage."
            ]
        }

    elif dairy_product == '208 fromage en saumure':
        return {
            "Matières premières": [
                "Lait et/ou produits dérivés du lait"
            ],
            "Substances nutritives autorisées": [
                "Les vitamines et minéraux ajoutés respectent-ils la législation nationale ?"
            ],
            "Composition": [
                "Teneur minimale en matière grasse dans l'extrait sec : 40% pour la pâte molle, 40% pour la pâte ferme",
                "Teneur en extrait sec : 40% pour la pâte molle, 52% pour la pâte ferme"
            ],
            "Additifs alimentaires": {
                "Régulateurs de l’acidité": [
                    "Acide lactique",
                    "Glucono-delta-lactone"
                ]
            },
            "Nom du produit": [
                "Le nom du produit doit être 'Fromage en saumure' et doit être conforme aux normes d'étiquetage."
            ]
        }

    elif dairy_product == '221 fromage non affiné, y compris les fromages frais':
        return {
            "Matières premières": [
                "Lait et/ou produits obtenus à partir du lait"
            ],
            "Substances nutritives autorisées": [
                "Les vitamines et minéraux ajoutés respectent-ils la législation nationale ?"
            ],
            "Composition": [
                "Respecte les exigences en matière de composition pour les fromages non affinés"
            ],
            "Additifs alimentaires": {
                "Régulateurs de l’acidité": [
                    "Carbonates de calcium",
                    "Acide lactique glacial",
                    "Acide lactique (L-, D- et DL)",
                    "Acide malique (DL)",
                    "Acide citrique",
                    "Acide orthophosphorique",
                    "Carbonates de sodium",
                    "Carbonates de potassium",
                    "Acide chlorhydrique",
                    "Glucono delta-lactone"
                ],
                "Stabilisants/Épaississants": [
                    "Citrates de sodium",
                    "Citrates de potassium",
                    "Citrates de calcium",
                    "Phosphates de sodium",
                    "Phosphates de potassium",
                    "Phosphates de calcium",
                    "Diphosphate disodique",
                    "Diphosphate trisodique",
                    "Lactose",
                    "Acide alginique",
                    "Alginate de sodium",
                    "Alginate de potassium",
                    "Alginate d’ammonium",
                    "Alginate de calcium",
                    "Alginate de glycol propylène",
                    "Agar-agar",
                    "Carragénine",
                    "Gomme de caroube",
                    "Gomme de guar",
                    "Gomme de tragacanthe",
                    "Gomme de xanthane",
                    "Gomme de karaya",
                    "Gomme de tara",
                    "Pectines",
                    "Cellulose",
                    "Cellulose carboxyméthylique de sodium",
                    "Gluconate de sodium"
                ],
                "Amidons modifiés": [
                    "Dextrines, amidon torréfié blanc et jaune",
                    "Amidon traité à l’acide",
                    "Amidon traité aux alcalis",
                    "Amidon blanchi",
                    "Amidon oxydé",
                    "Amidons traités aux enzymes",
                    "Phosphate de mono-amidon",
                    "Phosphate de di-amidon phosphaté",
                    "Phosphate de di-amidon acétylé",
                    "Acétate d’amidon estérifié à l’anhydride acétique",
                    "Adipate de di-amidon acétylé",
                    "Amidon hydroxypropyle",
                    "Phosphate de di-amidon hydroxypropyle"
                ],
                "Colorants": [
                    "Curcumin",
                    "Riboflavine",
                    "Chlorophylle",
                    "Chlorophylles cupriques",
                    "Béta-carotène",
                    "Extraits de rocou – base de norbixine",
                    "Oléorésines de paprika",
                    "Béta-apo-8’-caroténal",
                    "Acide béta-apo-8’-caroténique, ester méthylique ou éthylique",
                    "Rouge de betterave",
                    "Dioxyde de titanium"
                ],
                "Agents de conservation": [
                    "Acide sorbique",
                    "Sorbate de potassium",
                    "Sorbate de calcium",
                    "Nisine",
                    "Acide propionique",
                    "Propionate de sodium",
                    "Propionate de calcium",
                    "Propionate de potassium",
                    "Pimaricine (natamycine) - pour le traitement de surface uniquement, absente à 5 mm de profondeur"
                ],
                "Agents moussants (pour les produits fouettés seulement)": [
                    "Dioxyde de carbone",
                    "Azote"
                ],
                "Antiagglomérants (produits coupés, en tranches, râpés et râpés finement - traitement de surface)": [
                    "Cellulose",
                    "Dioxyde de silicone amorphe",
                    "Silicate de calcium",
                    "Silicates de magnésium",
                    "Silicate de potassium"
                ],
                "Agents de conservation (produits coupés, en tranches, râpés et râpés finement - traitement de surface)": [
                    "Acide sorbique",
                    "Sorbate",
                    "Sorbate de calcium",
                    "Acide propionique",
                    "Propionate de sodium",
                    "Propionate de calcium",
                    "Propionate de potassium",
                    "Pimaricine (natamycine)"
                ]
            },
            "Nom du produit": [
                "Le nom du produit doit être 'Fromage non affiné, y compris les fromages frais' et doit être conforme aux normes d'étiquetage."
            ]
        }
    elif dairy_product == '275 fromage crémeux':
        return {
            "Matières premières": [
                "Lait et/ou produits dérivés du lait"
            ],
            "Substances nutritives autorisées": [
                "Les vitamines et minéraux ajoutés respectent-ils la législation nationale ?"
            ],
            "Composition": [
                "Matière grasse laitière dans l'extrait sec : teneur minimale 25%, sans restriction pour la teneur maximale, niveau de référence 60-70% (m/m)",
                "Humidité du produit dégraissé : teneur minimale 67%",
                "Matière sèche : teneur minimale 22%, limitée par le HPD"
            ],
            "Additifs alimentaires": {
                "Agents de conservation": [
                    "Acide sorbique",
                    "Sorbate de sodium",
                    "Sorbate de potassium",
                    "Sorbate de calcium",
                    "Nisine",
                    "Acide propionique",
                    "Propionate de sodium",
                    "Propionate de calcium",
                    "Propionate de potassium"
                ],
                "Régulateurs de l’acidité": [
                    "Carbonate de calcium",
                    "Acide acétique",
                    "Acétate de potassium",
                    "Diacétate de potassium",
                    "Acétate de sodium",
                    "Acétate de calcium",
                    "Acide lactique (L-, D- et DL)",
                    "Acide malique (DL)",
                    "Lactate de sodium",
                    "Lactate de potassium",
                    "Lactate de calcium",
                    "Acide citrique",
                    "Citrate biacide de sodium",
                    "Citrate biacide de potassium",
                    "Citrates de calcium",
                    "Acide tartrique L(+)",
                    "Tartrate monosodique",
                    "Tartrate disodique",
                    "Tartrate monopotassique",
                    "Tartrate dipotassique",
                    "Tartrate de potassium-sodium",
                    "Acide orthophosphorique",
                    "Malate acide de sodium",
                    "Malate de sodium",
                    "Malate acide de potassium",
                    "Malate de potassium",
                    "Malate de calcium (D, L)",
                    "Carbonate de sodium",
                    "Carbonate acide de sodium",
                    "Sesquicarbonate de sodium",
                    "Carbonate de potassium",
                    "Carbonate de magnésium",
                    "Carbonate acide de magnésium",
                    "Acide chlorhydrique",
                    "Glucono-delta-lactone",
                    "Gluconate de potassium",
                    "Gluconate de calcium"
                ],
                "Stabilisants": [
                    "Orthophosphate monosodique",
                    "Orthophosphate disodique",
                    "Orthophosphate trisodique",
                    "Orthophosphate monopotassique",
                    "Orthophosphate dipotassique",
                    "Orthophosphate tripotassique",
                    "Orthophosphate monocalcique",
                    "Orthophosphate dicalcique",
                    "Orthophosphate tricalcique",
                    "Orthophosphate monoammonié",
                    "Orthophosphate diammonié",
                    "Orthophosphate dimagnésien",
                    "Orthophosphate trimagnésien",
                    "Diphosphate disodique",
                    "Diphosphate tétrasodique",
                    "Diphosphate tétrapotassique",
                    "Diphosphate dicalcique",
                    "Triphosphate pentasodique",
                    "Triphosphate pentapotassique",
                    "Polyphosphate de sodium",
                    "Polyphosphate de potassium",
                    "Polyphosphate de calcium",
                    "Polyphosphate d’ammonium",
                    "Acide alginique",
                    "Alginate de sodium",
                    "Alginate de potassium",
                    "Alginate d’ammonium",
                    "Alginate de calcium",
                    "Alginate de propylène glycol",
                    "Agar-agar",
                    "Carragenane",
                    "Algue euchema transformée",
                    "Gomme de caroube",
                    "Gomme guar",
                    "Gomme adragante",
                    "Gomme xanthane",
                    "Gomme karaya",
                    "Gomme tara",
                    "Gomme gellane",
                    "Carboxyméthyl-cellulose",
                    "Dextrines, amidon torréfié",
                    "Amidon traité aux acides",
                    "Amidon traité aux alcalis",
                    "Amidon blanchi",
                    "Amidon oxydé",
                    "Amidons traités aux enzymes",
                    "Phosphate de monoamidon",
                    "Phosphate de diamidon",
                    "Phosphate de diamidon phosphate",
                    "Phosphate de diamidon acétylé",
                    "Acétate d’amidon",
                    "Adipate de diamidon acétylé",
                    "Amidon hydroxypropylique",
                    "Phosphate de diamidon hydroxy - propylique"
                ],
                "Émulsifiants": [
                    "Lécithines",
                    "Sels d’acides myristique, palmitique et stéarique avec ammoniaque, calcium, potassium et sodium",
                    "Sels d’acides oléique avec calcium, potassium et sodium",
                    "Mono- et diglycérides d’acides gras",
                    "Esters glycéroliques de l’acide acétique et d’acides gras",
                    "Esters glycéroliques de l’acide lactique et d’acides gras",
                    "Esters glycéroliques de l’acide citrique et d’acides gras",
                    "Esters glycéroliques de l’acide diacetyltartrique et d’acides gras"
                ],
                "Antioxygènes": [
                    "Acide ascorbique (L)",
                    "Ascorbate de sodium",
                    "Ascorbate de calcium",
                    "Palmitate d’ascorbyle",
                    "Mélangé concentré de tocophérols",
                    "alpha-Tocophérol dl"
                ],
                "Colorants": [
                    "Béta-carotène, synthétique",
                    "Béta-carotène, Blakeslea trispora",
                    "Béta-apo-8’-caroténal",
                    "Acide béta-apo-8’-caroténique, ester méthylique ou éthylique",
                    "Béta-carotène",
                    "Extraits de rocou – base de norbixine",
                    "Bioxyde de titane"
                ],
                "Agents moussants": [
                    "Anhydride carbonique",
                    "Nitrogène"
                ]
            },
            "Nom du produit": [
                "Le nom du produit doit être 'Fromage crémeux' et doit être conforme aux normes d'étiquetage."
            ]
        }
    elif dairy_product == '279 beurre':
        return {
            "Matières premières": [
                "Lait et/ou produits obtenus à partir du lait"
            ],
            "Substances nutritives autorisées": [
                "Les vitamines et minéraux ajoutés respectent-ils la législation nationale ?"
            ],
            "Composition": [
                "Teneur minimale en matière grasse laitière : 80% (m/m)",
                "Teneur maximale en eau : 16% (m/m)",
                "Teneur maximale en extrait sec non gras : 2% (m/m)"
            ],
            "Additifs alimentaires": [
                "Liste des additifs autorisés à vérifier selon la réglementation locale"
            ],
            "Nom du produit": [
                "Le nom du produit doit être 'Beurre' et doit être conforme aux normes d'étiquetage."
            ]
        }
    elif dairy_product == '243 lait fermenté':
        return {
            "Matières premières": [
                "Lait et/ou produits dérivés du lait",
                "Eau potable utilisée lors de la reconstitution ou de la recombinaison"
            ],
            "Substances nutritives autorisées": [
                "Les vitamines et minéraux ajoutés respectent-ils la législation nationale ?"
            ],
            "Composition": [
                "Protéine du lait : minimum 2,7% (m/m)",
                "Acidité titrable, exprimée en % d’acide lactique : minimum 0,3% (m/m)",
                "Somme des micro-organismes : minimum 10^7 (ufc/g, total), étiquetés(b) : minimum 10^6"
            ],
            "Additifs alimentaires": {
                "Régulateurs de l’acidité": [
                    "Acide tartrique",
                    "Tartrate monosodique",
                    "Tartrate de sodium",
                    "Tartrate monopotassique",
                    "Tartrate dipotassique",
                    "Tartrate de potassium-sodium",
                    "Acide adipique",
                    "Adipates de sodium",
                    "Adipates de potassium",
                    "Adipates d’ammonium"
                ],
                "Agents de carbonation": [
                    "Anhydride carbonique"
                ],
                "Colorants": [
                    "Curcumine",
                    "Riboflavine",
                    "Phosphate sodique",
                    "Tartrazine",
                    "Jaune de quinoléine",
                    "Jaune soleil",
                    "Carmins",
                    "Azorubine",
                    "Ponceau 4R",
                    "Rouge allura AC",
                    "Indigotine",
                    "Bleu brillant",
                    "Chlorophylles, complexes cupriques",
                    "Chlorophyllines, complexes cupriques, sels de sodium et de potassium",
                    "Vert solide",
                    "Caramel II",
                    "Caramel III",
                    "Caramel IV",
                    "Noir brillant",
                    "Brun",
                    "Béta-carotène, synthétique",
                    "Béta-apo-8’-caroténal",
                    "Acide béta-apo-8’-caroténique, ester méthylique ou éthylique",
                    "Béta-carotène, Blakeslea trispora",
                    "Béta-carotène, légume",
                    "Extraits de rocou – base de bixine",
                    "Extraits de rocou – base de norbixine",
                    "Lycopènes",
                    "Lutéines de Tagetes erecta",
                    "Zéaxanthine, de synthèse",
                    "Extrait de peau de raisin",
                    "Oxyde de fer, noir",
                    "Oxyde de fer, rouge",
                    "Oxyde de fer, jaune"
                ],
                "Émulsifiants": [
                    "Polyoxyéthylène (20), monolaurate de sorbitane",
                    "Polyoxyéthylène (20), monooléate de sorbitane",
                    "Polyoxyéthylène (20), monopalmitate de sorbitane",
                    "Polyoxyéthylène (20), monostéarate de sorbitane",
                    "Polyoxyéthylène (20), tristéarate de sorbitane",
                    "Esters glycéroliques de l’acide diacetyltartrique et d’acides gras",
                    "Esters de saccharose d’acides gras",
                    "Sucroglycérides",
                    "Esters polyglycéroliques d’acides gras",
                    "Esters de propylène glycol d’acides gras",
                    "Stéaryl de sodium lactylé",
                    "Stéaryl de calcium lactylé",
                    "Monostéarate de sorbitane",
                    "Tristéarate de sorbitane",
                    "Monolaurate de sorbitane",
                    "Monooléate de sorbitane",
                    "Monopalmitate de sorbitane",
                    "Polydiméthylsiloxane"
                ],
                "Exaltateurs d’arôme": [
                    "Gluconate de magnésium",
                    "Acide glutamique",
                    "Glutamate monosodique",
                    "Glutamate monopotassique",
                    "Glutamate de calcium",
                    "Glutamate monoammonique",
                    "Glutamate de magnésium",
                    "Acide guanylique",
                    "Guanylate disodique",
                    "Guanylate dipotassique",
                    "Guanylate de calcium",
                    "Acide 5’-inosinique",
                    "Inosinate disodique",
                    "Inosinate de potassium",
                    "Inosinate de calcium",
                    "Ribonucléotides calciques",
                    "Ribonucléotides disodiques",
                    "Maltol",
                    "Ethyl-maltol"
                ],
                "Conservateurs": [
                    "Acide sorbique",
                    "Sorbate de sodium",
                    "Sorbate de potassium",
                    "Sorbate de calcium",
                    "Acide benzoïque",
                    "Benzoate de sodium",
                    "Benzoate de potassium",
                    "Benzoate de calcium",
                    "Nisine"
                ],
                "Stabilisants et épaississants": [
                    "Carbonate de calcium",
                    "Citrate trisodique",
                    "Acide phosphorique",
                    "Phosphate de sodium dihydrogène",
                    "Phosphate disodique d’hydrogène",
                    "Phosphate trisodique",
                    "Phosphate de potassium dihydrogène",
                    "Phosphate dipotassique d’hydrogène",
                    "Phosphate tripotassique",
                    "Phosphate de calcium dihydrogène",
                    "Phosphate de calcium d’hydrogène",
                    "Phosphate tricalcique",
                    "Phosphate d’ammonium dihydrogène"
                ]
            },
            "Nom du produit": [
                "Le nom du produit doit être 'Lait fermenté' et doit être conforme aux normes d'étiquetage."
            ]
        }
    elif dairy_product == '283 fromage':
        return {
            "Matières premières": [
                "Lait et/ou produits obtenus à partir du lait"
            ],
            "Substances nutritives autorisées": [
                "Les vitamines et minéraux ajoutés respectent-ils la législation nationale ?"
            ],
            "Composition": [
                "Respecte les exigences en matière de composition pour le fromage"
            ],
            "Additifs alimentaires": {
                "Colorants": [
                    "Curcumine",
                    "Riboflavines",
                    "Carmins",
                    "Chlorophylle",
                    "Chlorophylles, complexes cupriques",
                    "Béta-carotène, synthétique",
                    "Béta-carotène, légume",
                    "Extraits de rocou – base de norbixine",
                    "Oléorésines de paprika",
                    "Béta-apo-8’-caroténal",
                    "Acide caroténoïque beta-apo-8', ester méthylique ou éthylique",
                    "Rouge de betterave",
                    "Dioxyde de titanium"
                ],
                "Régulateurs d’acidité": [
                    "Carbonate de calcium",
                    "Carbonate de magnésium",
                    "Glucono-delta-lactone"
                ],
                "Agents de conservation": [
                    "Acide sorbique",
                    "Sorbate de sodium",
                    "Sorbate de potassium",
                    "Sorbate de calcium",
                    "Nisine",
                    "Hexaméthylène-tétramine (exprimés en tant que formaldéhyde)",
                    "Nitrate de sodium",
                    "Nitrate de potassium",
                    "Acide propionique",
                    "Propionate de sodium",
                    "Propionate de calcium",
                    "Lysozyme"
                ],
                "Pour le traitement en surface/croûte seulement": [
                    "Acide sorbique",
                    "Sorbate de potassium",
                    "Sorbate de calcium",
                    "Pimaricine"
                ],
                "Additifs divers": [
                    "Chlorure de potassium"
                ],
                "Antiagglomérants": [
                    "Celluloses",
                    "Dioxyde de silice amorphe",
                    "Silicate de calcium",
                    "Silicate de magnésium",
                    "Silicate de potassium"
                ],
                "Agents conservateurs (produits coupés, en tranches, râpés et râpés finement seulement - traitement de surface)": [
                    "Acide sorbique",
                    "Sorbate de potassium",
                    "Sorbate de calcium"
                ]
            },
            "Nom du produit": [
                "Le nom du produit doit être 'Fromage' et doit être conforme aux normes d'étiquetage."
            ]
        }
    else:
        return {}

# Interface Streamlit
def audit_form():
    st.title('Audit de Conformité des Produits Laitiers')

    # Sélection du produit laitier
    dairy_product = st.selectbox("Sélectionner le produit laitier", dairy_products)

    # Générer les sous-questionnaires pour le produit choisi
    sub_questions = generate_sub_questionnaire(dairy_product)
    responses = {}

    # Affichage des sous-questionnaires en fonction du produit choisi
    if sub_questions:
        st.subheader(f"Sous-questionnaire pour {dairy_product}")

        for category, questions in sub_questions.items():
            st.markdown(f"### {category}")
            responses[category] = {}
            for idx, question in enumerate(questions):
                # Ajout d'une clé unique en combinant la catégorie et l'index de la question
                responses[category][question] = st.checkbox(question, key=f"{category}_{idx}")

        # Bouton de soumission
        if st.button("Soumettre l'audit"):
            # Sauvegarder les réponses dans un fichier Excel
            save_to_excel(dairy_product, responses)
            st.success("Audit soumis avec succès! Les résultats ont été sauvegardés dans un fichier Excel.")

# Fonction pour sauvegarder les réponses dans un fichier Excel
def save_to_excel(dairy_product, responses):
    # Transformer les réponses en DataFrame
    data = []
    for category, questions in responses.items():
        for question, answer in questions.items():
            data.append([dairy_product, category, question, answer])
    
    df = pd.DataFrame(data, columns=["Produit Laitier", "Catégorie", "Question", "Réponse"])
    df.to_excel("audit_resultats.xlsx", index=False)

# Exécuter l'application Streamlit
if __name__ == "__main__":
    audit_form()
