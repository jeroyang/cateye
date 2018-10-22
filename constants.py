#!/usr/bin/env python
# -*- coding: utf-8 -*-

import string

SITE_TITLE = 'Cateye'
SITE_SUBTITLE = 'A hint enabled search engine'

TOKEN_FOLDER = 'data/token'
SNIPPET_FOLDER = 'data/snippet'
HINT_FOLDER = 'data/hint'

SPELLING_FILE = 'data/spelling.txt' # The formal spelling of tokens
ABBREVIATION_FILE = 'data/abbrevation.txt'

MAX_HINT_SMAPLING_SIZE = 100 # smaller size, faster system, less accurate hint

STOPCHARS = '之或及的型在與和併於，、,'

STOPWORDS =  list(string.punctuation) + [ '',  ' ', 'and', 'at', 'as', 'by',
            'for', 'due', 'from', 'in', 'into', 'of', 'or', 'other',
            'specified', 'the', 'to', 'unspecified', 'using', 'via', 'with',
            '伴有']

HINT_STOPWORDS =  STOPWORDS + [ 'cause', 'diseases', 'disorders', 'due',
            'encounter', 'except', 'identified', 'induced', 'manifestations',
            'no', 'not', 'notlevel', 'on', 'region', 'side', 'site', 'sites',
            'specific', 'type', 'underlying', 'unidentified', 'without', 'with',
            'approach', 'part', 'syndrome', 'disease', 'lesion', 'disorder',
            'dependence', 'elsewhere', 'other', 'involvement', 'forms']

FORMAL_SURFACE = {'A', 'AB', 'ABL', 'ABO', 'ACTH', 'ADA', 'ADEM', 'ALK', 'ALL',
            'ALPS', 'ALTE', 'ASC', 'Achilles', 'African', 'Aldrich',
            'Alzheimer', 'American', 'Anderson', 'Arnold', 'Asian', 'Asperger',
            'Australian', 'B', 'B. f', 'B12', 'B6', 'BCR', 'BMI', 'Baker',
            'Balo', 'Barr', 'Barre', 'Barrett', 'Bartholin', 'Barton',
            'Bartter', 'Beau', 'Beck', 'Behcet', 'Bell', 'Bennett', 'Besnier',
            'Biotin', 'Bitot', 'Bockhart', 'Bordetella', 'Boston', 'Bouchard',
            'Bowman', 'Brill', 'Brown', 'Brucella', 'Brugia', 'Budd', 'Buerger',
            'Burkitt', 'Buzzi', 'C', 'C. p', 'C0', 'C1', 'C2', 'C3', 'C4', 'C5',
            'C6', 'C7', 'C8', 'CA', 'CD30', 'CEA', 'CKD', 'CR', 'CRP', 'CRPS',
            'Calve', 'Cesarean', 'Chagas', 'Chalcosis', 'Charcot', 'Chediak',
            'Chiari', 'Chilblains', 'Christian', 'Churg', 'Civatte', 'Clutton',
            'CoA', 'Colles', 'Congo', 'Conn', 'Creutzfeldt', 'Crigler',
            'Crimean', 'Crohn', 'Crosti', 'Cushing', 'D', 'DMAC', 'DNA', 'DSAP',
            'Danlos', 'Devic', 'Dressler', 'Duane', 'Dupuytren', 'E', 'E. c',
            'ECG', 'ECMO', 'EEG', 'EFA', 'EIN', 'EKG', 'EMG', 'EMT', 'EOG',
            'ER', 'ERG', 'ESBL', 'Ebstein', 'Ehlers', 'Ehrlichia', 'Epstein',
            'Erb', 'Escherichia', 'European', 'Eustachian', 'Fallot', 'Feil',
            'Felty', 'Forestier', 'Foster', 'Friderichsen', 'Fuchs', 'G',
            'G6PD', 'GM2', 'Galeazzi', 'Gastaut', 'George', 'German',
            'Gerstmann', 'Gianotti', 'Gierke', 'Glasgow', 'Gliding',
            'Glucocorticoid', 'Goniosynechiae', 'Gottron', 'Grover', 'Guillain',
            'H', 'H. i', 'H. p', 'H2', 'HCPS', 'HGSIL', 'HIE', 'HIV', 'HPFH',
            'HPS', 'HPV', 'HTLV', 'Hallervorden', 'Hansen', 'Harada', 'Harris',
            'Hartnup', 'Hb', 'Heberden', 'Hermansky', 'Higashi', 'Hirschsprung',
            'Hodgkin', 'Hoffman', 'Horner', 'Huntington', 'Hurler', 'Hurst',
            'Hutchinson', 'I', 'IBM', 'IED', 'II', 'IIA', 'IIB', 'III', 'IIIA',
            'IIIB', 'IIIC', 'ISD', 'IV', 'IX', 'IgA', 'IgE', 'IgG', 'IgM',
            'Jaccoud', 'Jadassohn', 'Jakob', 'Johnson', 'Jones', 'K', 'K. p',
            'Kaposi', 'Kaschin', 'Kawasaki', 'Kayser', 'Kearns', 'Kennedy',
            'Kienbock', 'Klebsiella', 'Klippel', 'Klumpke', 'Koyanagi', 'L1',
            'L2', 'L3', 'L4', 'L5', 'LDH', 'LFA', 'LGSIL', 'LSD', 'Lambert',
            'Langerhans', 'Legg', 'Legionnaires', 'Leigh', 'Leishmaniasis',
            'Lemli', 'Lennox', 'Lequesne', 'Lesch', 'Leucocoria', 'Lewy',
            'Louis', 'Lowe', 'Luschka', 'Lyell', 'Lyme', 'M', 'M. p', 'MALT',
            'MEN', 'MacLeod', 'Magendie', 'Maisonneuve', 'Marchiafava',
            'Marfan', 'Mauclaire', 'Meckel', 'Melkersson', 'Meniere',
            'Meningitis', 'Meningococcemia', 'Merkel', 'Micheli', 'Mikity',
            'Mollaret', 'Monteggia', 'Mooren', 'Myhre', 'NASH', 'NDPH', 'NEC',
            'NK', 'NKHHC', 'NOS', 'NSAID', 'NSTEMI', 'Najjar', 'Nelson',
            'Nezelof', 'Niemann', 'Nile', 'Norwalk', 'Nyhan', 'O', 'O157',
            'Oddi', 'Olszewski', 'Opitz', 'PNP', 'PSA', 'PTLD', 'PTO', 'PTSD',
            'PUPPP', 'Paget', 'Parkinson', 'Pasini', 'Pellegrini', 'Pellizzari',
            'Perthes', 'Pierini', 'Pontiac', 'Portugese', 'Potter', 'Pudlak',
            'Pylorospasm', 'QT', 'Quervain', 'Raynaud', 'Refsum', 'Reiter',
            'Rett', 'Reye', 'Rh', 'Richardson', 'Rickettsia', 'Rieger', 'Rifle',
            'Riley', 'Robertson', 'Rolando', 'Russian', 'Ruvalcaba', 'SARS',
            'SCID', 'SERMs', 'SIRS', 'SLE', 'SS', 'ST', 'STEC', 'STEMI',
            'SUNCT', 'Sachs', 'Salter', 'Sayre', 'Scheie', 'Scheinker',
            'Schistosoma', 'Schmorl', 'Schweninger', 'Sequard', 'Serratia',
            'Shiga', 'Shigella', 'Sickle', 'Sjogren', 'Soemmering', 'Spatz',
            'Steele', 'Stevens', 'Stieda', 'Strauss', 'Straussler', 'Sylvius',
            'T', 'T1', 'T10', 'T11', 'T12', 'T2', 'T3', 'T4', 'T5', 'T6', 'T7',
            'T8', 'T9', 'TAC', 'TIA', 'TRALI', 'Takayasu', 'Tay', 'Tietze',
            'Todd', 'Tourette', 'Turner', 'US', 'USA', 'V', 'VEP', 'VIII',
            'Vater', 'Velo', 'Vertebro', 'Vesicoureteral', 'Vibrio', 'Vincent',
            'Vogt', 'Vomiting', 'WMD', 'Waldeyer', 'Waterhouse', 'Weber',
            'Wegener', 'Wells', 'Werdnig', 'Wernicke', 'Whipple', 'Willebrand',
            'Wilson', 'Wiskott', 'Wuchereria', 'X', 'XI', 'XX', 'XXX', 'XXY',
            'XY', 'XYY', 'Xq', 'Yersinia', 'Zellweger', 'Zygomycosis', 'hCG',
            'rtPA', 'tPA'}
