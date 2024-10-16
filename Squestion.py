#!/usr/bin/env python
# coding: utf-8

# In[11]:


import streamlit as st

# Liste des dérivées du lait
dairy_products = ['282 lait concentré sucré', '250 mélange de lait concentré', '251 mélange de lait écrémé', 'Mélange de lait écrémé et graisses végétales']

# Fonction pour générer un sous-questionnaire structuré selon les rubriques
def generate_sub_questionnaire(dairy_product):
    if dairy_product == '282 lait concentré sucré':
        return {
            "Matières premières": [
                "lait et laits en poudre",
                "crèmes et crème en poudre",
                "produit à base de matière grasses laitières",
                "Rétentat du lait",
                "Perméat du lait",
                "Lactose"
            ],
            "Ingrédients autorisés": [
                "eau potable",
                "sucre et chlorure de sodium",
                
            ],
            "Substances nutritives autorisées": [
                "Les vitamines et minéraux ajoutés respectent-ils la législation nationale ?"
            ],
            "Composition": [
                "protéines du lait dans l'extrait sec degraissé (34% m/m)",

                "Lait concentré sucré écrémé",
                "teneur maximale en matière grasse laitière (1% m/m).",
                "teneur minimale en extrait sec du lait (24% m/m)",
                "teneur minimale en protéines du lait dans l'extrait sec degraissé (34% m/m)",

                "lait concentré sucré partiellement écrémé",
                "*teneur en matière grasse laitière (comprise entre 1 et 8 % m/m).",
                "*teneur minimale en extrait sec degraissé (20% m/m).",
                "*teneur minimale en extrait sec du lait (24% m/m)",
                "*teneur minimale en protéines du lait dans l'extrait sec degraissé (34% m/m).",

                "lait concentré sucré riche en matière grasse",
                "teneur minimale en matière grasse laitière (16% m/m)",
                "teneur minimale en extrait sec degraissé (14% m/m)",
                "teneur minimale en protéines du lait dans l'extrait sec degraissé (34% m/m)."
            ],
            "Additifs alimentaires": [
                "Agents raffermissants",

                "508 chlorure de potassium (2000 mg/kg seuls ou 3000 mg/kg en combinaison, exprimés en tant substances anhydres).",
                "509 chlorure de calcium (2000 mg/kg seuls ou 3000 mg/kg en combinaison, exprimés en tant substances anhydres).",

                "Stabilisants",
                
                "331 citrates de sodium (2000 mg/kg seuls ou 3000 mg/kg en combinaison, exprimés en tant substances anhydres).",
                "332 citrates de potassium (2000 mg/kg seuls ou 3000 mg/kg en combinaison, exprimés en tant substances anhydres).",
                "333 citrates de calcium (2000 mg/kg seuls ou 3000 mg/kg en combinaison, exprimés en tant substances anhydres)."
            ],
            "Nom du produit": [
                "Le nom du produit doit être:",
                "Lait concentré sucré, Lait concentré écrémé sucré, Lait concentré sucré partiellement écrémé sucré, Lait concentré sucré riche en matière grasse. ?",
                "Le nom du produit est-il conforme aux normes d'étiquetage ?"
            ],
            "Pays d'origine": [
                "Le pays d'origine du lait est-il indiqué sur l'étiquette ?"
            ],
            "Déclaration de la teneur en matière grasse laitière": [
                "Déclaration de la teneur en matière grasse laitière est t'elle déclarée?"
            ],
            "Étiquetage des récipients non destinés à la vente au détail": [
                "Les renseignements requis à la Section 7 de la présente norme et aux Sections 4.1 à  4.8 de la Norme générale pour l’étiquetage des denrées alimentaires préemballées figurent-elle sur l'ambalage?"
            ],
            "Déclaration de la teneur en protéines du lait": [
                "Déclaration de la teneur en protéines du lait est-elle déclarée?"
            ],
            "Marquage et étiquetage": [
                "L'étiquetage est-il conforme aux règles de marquage et d'étiquetage ?"
            ]
        }
    elif dairy_product == '250 mélange de lait concentré':
        return {
            "Matières premières": [
                "Rétentat du lait",
                "lait écrémé et lait écrémé en poudre",
                "autres extraits secs du lait écrémé et graisses/huiles végétales comestibles.",
                "*Rétentat du lait",
                "*Perméat du lait", 
                "*Lactose"
            ],
            "Ingrédients autorisés": [
                "eau potable",
                "chlorure de sodium et/ou chlorure de potassium en tant que succédanés du sel."
            ],
            "Substances nutritives autorisées": [
                "lorsque les Principes généraux régissant l’adjonction d’éléments nutritifs aux aliments (CAC/GL 9-1987) le permettent, les teneurs maximales et minimales en vitamines A, D et autres substances nutritives, le cas échéant, devraient être prescrites par la législation nationale en fonction des besoins de chaque pays y compris, s’il y a lieu, l’interdiction d’utiliser certaines substances nutritives."
            ],
            "Composition": [
                "mélange de lait concentré écrémé et de graisses végétales"

                "*Teneur minimale en matière grasse (7,5 % m/m).",
                "*Teneur minimale en extrait sec dégraissé du lait (17,5 % m/m).",
                "*Teneur minimale en protéines du lait dans l’extrait sec dégraissé du lait (34 % m/m).",
                
                "Mélange à faible teneur en matière grasse de lait concentré écrémé et de graisse végétale",
                
                "*Teneur minimale en matière grasse (> 1 % et < 7,5 % m/m).",
                "*Teneur minimale en extrait sec dégraissé du lait (19 % m/m).",
                "*Teneur minimale en protéines du lait dans l’extrait sec dégraissé du lait (34 % m/m)"

            ],
            "Additifs alimentaires": [
                "Emulsifiants",

                "322 Lécithines (Limitée par les BPF).",
                
                "Stabilisants",
                
                "331(i) Citrate biacide de sodium (Limitée par les BPF)",
                "331(iii) Citrate trisodique (Limitée par les BPF)",
                "332(i) Citrate biacide de potassium (Limitée par les BPF)",
                "332(ii) Citrate tripotassique (Limitée par les BPF)",
                "333 Citrate de calcium (Limitée par les BPF)",
                "508 Chlorure de potassium (Limitée par les BPF)",
                "509 Chlorure de calcium (Limitée par les BPF)",
                
                "Régulateur d'acidité",
                
                "170(i) Carbonate de calcium (Limitée par les BPF)",
                "339(i) Orthophosphate monosodique",
                "339(ii) Orthophosphate disodique",
                "339(iii) Orthophosphate trisodique",
                "340(i) Orthophosphate monopotassique",
                "340(ii) Orthophosphate dipotassique",
                "340(iii) Orthophosphate tripotassique",
                "341(i) Orthophosphate monocalcique",
                "341(ii) Orthophosphate dicalcique",
                "341(iii) Orthophosphate tricalcique",
                "450(i) Diphosphate disodique",
                "450(ii) Diphosphate trisodique",
                "450(iii) Diphosphate tétrasodique",
                "450(v) Diphosphate tétrapotassique",
                "450(vi) Diphosphate dicalcique", 
                "450(vii) Diphosphate biacide de calcium (4 400 mg/kg, seul ou en combinaison, en tant que phosphore)",
                "451(i) Triphosphate pentasodique (4 400 mg/kg, seul ou en combinaison, en tant que phosphore)",
                "451(ii) Triphosphate pentasodique (4 400 mg/kg, seul ou en combinaison, en tant que phosphore)",
                "452(i) Polyphosphate de sodium (4 400 mg/kg, seul ou en combinaison, en tant que phosphore)",
                "452(ii) Polyphosphate de potassium (4 400 mg/kg, seul ou en combinaison, en tant que phosphore)",
                "452(iii) Polyphosphate de sodium-calcium (4 400 mg/kg, seul ou en combinaison, en tant que phosphore)",
                "452(iv) Polyphosphate de calcium (4 400 mg/kg, seul ou en combinaison, en tant que phosphore)",
                "452(v) Polyphosphate d’ammonium (4 400 mg/kg, seul ou en combinaison, en tant que phosphore)",
                "500(i) Carbonate de sodium (Limitée par les BPF)", 
                "500(ii) Carbonate acide de sodium (Limitée par les BPF)", 
                "500(iii) Sesquicarbonate de sodium (Limitée par les BPF)", 
                "501(i) Carbonate de potassium (Limitée par les BPF)", 
                "501(ii) Carbonate acide de potassium (Limitée par les BPF)"

                "Epaississant",
                
                "407 Carragenane (Limitée par les BPF)",
                "407a Algue eucheuma transformée (Limitée par les BPF)",
            ],
            "Nom du produit": [
                "Le nom du produit est-il clairement indiqué ?",
                "Le nom du produit est-il conforme aux spécifications ?"
            ],
            "Pays d'origine": [
                "Le pays d'origine du yaourt est-il mentionné sur l'étiquette ?"
            ],
            "Déclaration de la teneur en matière grasse laitière": [
                "La teneur en matière grasse est-elle correctement mentionnée ?"
            ],
            "Étiquetage des récipients non destinés à la vente au détail": [
                "Les récipients non destinés à la vente au détail sont-ils étiquetés correctement ?"
            ],
            "Déclaration de la teneur en protéines du lait": [
                "La teneur en protéines du lait est-elle indiquée sur l'étiquette ?"
            ],
            "Marquage et étiquetage": [
                "L'étiquetage est-il conforme aux règles locales de marquage ?"
            ]
        }
    elif dairy_product == '251 mélange de lait écrémé':
        return {
            "Matières premières": [
                "lait écrémé et lait écrémé en poudre",
                "autres extraits secs du lait écrémé et graisses/huiles végétales comestibles"
            ],
            "Ingrédients autorisés": [
                "Tous les ingrédients dans la fabrication du fromage sont-ils autorisés ?"
            ],
            "Substances nutritives autorisées": [
                "Les vitamines et minéraux sont-ils conformes aux normes locales ?"
            ],
            "Composition": [
                "La composition du fromage respecte-t-elle les normes en matière de matière grasse et de protéines ?"
            ],
            "Additifs alimentaires": [
                "Les additifs alimentaires utilisés dans le fromage sont-ils conformes aux limites autorisées ?"
            ],
            "Nom du produit": [
                "Le nom du fromage est-il correctement indiqué ?",
                "Le nom est-il conforme aux exigences locales ?"
            ],
            "Pays d'origine": [
                "Le pays d'origine du fromage est-il indiqué ?"
            ],
            "Déclaration de la teneur en matière grasse laitière": [
                "La teneur en matière grasse du fromage est-elle clairement indiquée ?"
            ],
            "Étiquetage des récipients non destinés à la vente au détail": [
                "Les récipients non destinés à la vente au détail sont-ils correctement étiquetés ?"
            ],
            "Déclaration de la teneur en protéines du lait": [
                "La teneur en protéines du lait est-elle indiquée sur l'étiquette ?"
            ],
            "Marquage et étiquetage": [
                "Le marquage et l'étiquetage respectent-ils les normes locales ?"
            ]
        }
    elif dairy_product == 'Mélange de lait écrémé et graisses végétales':
        return {
            "Matières premières": [
                "Les ingrédients utilisés sont conformes (lait écrémé, lait écrémé en poudre, graisses végétales comestibles) ?",
                "Les matières premières sont-elles certifiées conformes aux normes locales ?"
            ],
            "Ingrédients autorisés": [
                "Les ingrédients sont-ils autorisés pour ce type de produit ?"
            ],
            "Substances nutritives autorisées": [
                "Les vitamines et minéraux ajoutés respectent-ils la législation en vigueur ?"
            ],
            "Composition": [
                "La teneur en matière grasse est-elle correcte (26% m/m) ?",
                "La teneur en eau ne dépasse-t-elle pas 5% m/m ?",
                "La teneur en protéines du lait dans l'extrait sec dégraissé est-elle conforme (34% m/m) ?"
            ],
            "Additifs alimentaires": [
                "Les additifs alimentaires respectent-ils les limites autorisées ?"
            ],
            "Nom du produit": [
                "Le nom du produit est-il correctement mentionné ?",
                "Le produit porte-t-il la mention « NE CONVIENT PAS AUX NOURRISSONS » ?"
            ],
            "Pays d'origine": [
                "Le pays d'origine du produit est-il indiqué ?"
            ],
            "Déclaration de la teneur en matière grasse laitière": [
                "La teneur en matière grasse est-elle clairement indiquée ?"
            ],
            "Étiquetage des récipients non destinés à la vente au détail": [
                "Les récipients non destinés à la vente au détail sont-ils étiquetés correctement ?"
            ],
            "Déclaration de la teneur en protéines du lait": [
                "La teneur en protéines du lait est-elle clairement indiquée ?"
            ],
            "Marquage et étiquetage": [
                "L'étiquetage du produit respecte-t-il les règles locales de marquage ?"
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

    # Affichage des sous-questionnaires en fonction du produit choisi
    if sub_questions:
        st.subheader(f"Sous-questionnaire pour {dairy_product}")

        for category, questions in sub_questions.items():
            st.markdown(f"### {category}")
            for idx, question in enumerate(questions):
                # Ajout d'une clé unique en combinant la catégorie et l'index de la question
                st.checkbox(question, key=f"{category}_{idx}")

        # Bouton de soumission
        if st.button("Soumettre l'audit"):
            st.success("Audit soumis avec succès!")

# Exécuter l'application Streamlit
if __name__ == "__main__":
    audit_form()


# In[ ]:




